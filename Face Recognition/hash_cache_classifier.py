import cv2
import numpy as np
import os
import pickle
from datetime import datetime

class HashCacheClassifier:
    def __init__(self, cache_file='hash_cache.pkl'):
        self.cache_file = cache_file
        self.cache = self.load_cache()
        self.face_detector = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )
    
    def load_cache(self):
        """Load the hash cache from file"""
        if os.path.exists(self.cache_file):
            try:
                with open(self.cache_file, 'rb') as f:
                    return pickle.load(f)
            except:
                print("Cache file corrupted, creating new cache")
                return {}
        return {}
    
    def save_cache(self):
        """Save the hash cache to file"""
        with open(self.cache_file, 'wb') as f:
            pickle.dump(self.cache, f)
    
    def compute_image_hash(self, image):
        """Compute a perceptual hash for the image"""
        # Resize to 8x8 and convert to grayscale if needed
        if len(image.shape) == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Resize to consistent size for hashing
        image = cv2.resize(image, (8, 8))
        
        # Compute average pixel value
        avg = np.mean(image)
        
        # Create hash: 1 if pixel > average, 0 otherwise
        hash_value = 0
        for i in range(8):
            for j in range(8):
                if image[i, j] > avg:
                    hash_value |= 1 << (i * 8 + j)
        
        return hash_value
    
    def hamming_distance(self, hash1, hash2):
        """Compute Hamming distance between two hashes"""
        return bin(hash1 ^ hash2).count('1')
    
    def add_to_cache(self, image, label, metadata=None):
        """Add an image to the cache with its hash and label"""
        if metadata is None:
            metadata = {}
        
        hash_value = self.compute_image_hash(image)
        
        if hash_value not in self.cache:
            self.cache[hash_value] = []
        
        entry = {
            'label': label,
            'timestamp': datetime.now().isoformat(),
            'metadata': metadata
        }
        
        self.cache[hash_value].append(entry)
        self.save_cache()
        
        return hash_value
    
    def classify_image(self, image, threshold=5):
        """Classify an image based on hash similarity"""
        query_hash = self.compute_image_hash(image)
        best_match = None
        min_distance = float('inf')
        
        for stored_hash, entries in self.cache.items():
            distance = self.hamming_distance(query_hash, stored_hash)
            
            if distance < min_distance and distance <= threshold:
                min_distance = distance
                best_match = entries[0]  # Use the first entry for this hash
        
        if best_match:
            return {
                'label': best_match['label'],
                'confidence': 1 - (min_distance / 64),  # 64 bits in 8x8 hash
                'distance': min_distance
            }
        else:
            return None
    
    def detect_and_classify_faces(self, frame):
        """Detect faces in frame and classify them using hash cache"""
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_detector.detectMultiScale(gray, 1.3, 5)
        
        results = []
        
        for (x, y, w, h) in faces:
            face_region = gray[y:y+h, x:x+w]
            face_region = cv2.resize(face_region, (100, 100))
            
            classification = self.classify_image(face_region)
            
            if classification:
                label = classification['label']
                confidence = classification['confidence']
                color = (0, 255, 0)  # Green for recognized
                text = f"{label} ({confidence:.2f})"
            else:
                label = "Unknown"
                confidence = 0
                color = (0, 0, 255)  # Red for unknown
                text = "Unknown"
            
            # Draw rectangle and label
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
            cv2.putText(frame, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 
                       0.5, color, 2)
            
            results.append({
                'bbox': (x, y, w, h),
                'label': label,
                'confidence': confidence
            })
        
        return frame, results
    
    def train_from_dataset(self, dataset_path):
        """Train the classifier from a dataset directory"""
        if not os.path.exists(dataset_path):
            print(f"Dataset path {dataset_path} does not exist")
            return
        
        for filename in os.listdir(dataset_path):
            if filename.endswith('.jpg') or filename.endswith('.png'):
                # Extract label from filename (format: User.{id}.{count}.jpg)
                parts = filename.split('.')
                if len(parts) >= 3:
                    label = parts[1]  # The ID part
                    
                    image_path = os.path.join(dataset_path, filename)
                    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
                    
                    if image is not None:
                        self.add_to_cache(image, label, {'source_file': filename})
                        print(f"Trained on: {filename} -> Label: {label}")
    
    def get_cache_stats(self):
        """Get statistics about the cache"""
        total_entries = sum(len(entries) for entries in self.cache.values())
        unique_hashes = len(self.cache)
        unique_labels = set()
        
        for entries in self.cache.values():
            for entry in entries:
                unique_labels.add(entry['label'])
        
        return {
            'total_entries': total_entries,
            'unique_hashes': unique_hashes,
            'unique_labels': len(unique_labels),
            'labels': list(unique_labels)
        }


# Example usage and real-time classification
def real_time_classification():
    classifier = HashCacheClassifier()
    
    # Train from existing dataset if available
    if os.path.exists('datasets'):
        print("Training from existing dataset...")
        classifier.train_from_dataset('datasets')
        stats = classifier.get_cache_stats()
        print(f"Cache stats: {stats}")
    
    # Start real-time classification
    video = cv2.VideoCapture(0)
    
    if not video.isOpened():
        print("Error: Could not open camera")
        return
    
    print("Starting real-time classification. Press 'q' to quit, 'a' to add current face to cache")
    
    current_label = input("Enter your name for classification: ")
    
    while True:
        ret, frame = video.read()
        
        if not ret:
            break
        
        # Classify faces in the frame
        processed_frame, results = classifier.detect_and_classify_faces(frame)
        
        cv2.imshow("Face Recognition", processed_frame)
        
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord('q'):
            break
        elif key == ord('a') and results:
            # Add the first detected face to cache
            x, y, w, h = results[0]['bbox']
            face_region = cv2.cvtColor(frame[y:y+h, x:x+w], cv2.COLOR_BGR2GRAY)
            face_region = cv2.resize(face_region, (100, 100))
            
            hash_value = classifier.add_to_cache(face_region, current_label)
            print(f"Added face to cache with hash: {hash_value}")
    
    video.release()
    cv2.destroyAllWindows()
    print("Classification session ended")

if __name__ == "__main__":
    real_time_classification()
