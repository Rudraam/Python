from flask import Flask, request, Response, render_template
import json
from openai import OpenAI
from config import api_key
import os

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static"
client = OpenAI(api_key=api_key)



@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        language = request.form.get('language', '').strip()
        file = request.files.get('file')

        if file:
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            with open(filepath, "rb") as audio_file:
                transcription = client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file,
                    language=language if language else None  # use language if provided
                )

            # Always return JSON
            return Response(
                json.dumps({"text": transcription.text}, ensure_ascii=False),
                mimetype='application/json'
            )

        # Error if no file
        return Response(
            json.dumps({"error": "No file uploaded"}),
            mimetype="application/json",
            status=400
        )

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
