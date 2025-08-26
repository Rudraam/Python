import cv2
import os

# Create datasets directory if it doesn't exist
if not os.path.exists('datasets'):
    os.makedirs('datasets')

# Try different camera indices (0, 1, 2)
camera_index = 0
video = None

for i in range(3):
    video = cv2.VideoCapture(i)
    if video.isOpened():
        camera_index = i
        print(f"Camera found at index {i}")
        break
    else:
        video.release()

if not video or not video.isOpened():
    print("Error: Could not open any camera")
    print("Please check your camera connection and permissions")
    exit()

# Use OpenCV's built-in face detector
facedetect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

if facedetect.empty():
    print("Error: Could not load face detector")
    video.release()
    exit()

print("Face detector loaded successfully")
print("Press 'q' to quit or wait until 100 images are captured")

id = input("Enter Your ID: ")
count = 0

while True:
    ret, frame = video.read()
    
    if not ret:
        print("Error: Failed to capture frame")
        break
        
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)
    
    if len(faces) > 0:
        for (x, y, w, h) in faces:
            count += 1
            # Save the face region
            face_region = gray[y:y+h, x:x+w]
            
            # Resize to consistent size for better training
            face_region = cv2.resize(face_region, (100, 100))
            
            filename = f'datasets/User.{id}.{count}.jpg'
            cv2.imwrite(filename, face_region)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 2)
            print(f"Saved: {filename} - Faces detected: {len(faces)}")
    else:
        print("No faces detected - looking for faces...")

    cv2.imshow("Frame", frame)

    k = cv2.waitKey(1) & 0xFF
    
    if k == ord('q'):
        break
    if count >= 100:
        break

video.release()
cv2.destroyAllWindows()
print(f"Dataset Collection Done! Collected {count} images for User {id}")
