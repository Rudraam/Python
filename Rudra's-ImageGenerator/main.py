import base64
from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from openai import OpenAI, PermissionDeniedError
from config import key

app = FastAPI()
client = OpenAI(api_key=key)

templates = Jinja2Templates(directory="templates")

# Serve HTML page
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Generate multiple images
@app.get("/generateimages")
async def generate(prompt: str = Query(...), n: int = 3):
    try:
        response = client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size="1024x1024",
            n=n
        )
        images_base64 = [img.b64_json for img in response.data]

    except PermissionDeniedError:
        # Fallback to text if image generation fails
        response = client.responses.create(
            model="gpt-5",
            input=f"Describe in detail: {prompt}"
        )
        images_base64 = [response.output[0].content[0].text]

    return {"images": images_base64}
