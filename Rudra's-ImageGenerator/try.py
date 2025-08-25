import base64
from openai import OpenAI
from openai import PermissionDeniedError
from config import key

client = OpenAI(api_key=key)

prompt = "gray tabby cat hugging an otter with an orange scarf"

try:
    # Try image generation first
    response = client.images.generate(
        model="gpt-image-1",
        prompt=prompt
    )
    image_base64 = response.data[0].b64_json
    with open("otter.png", "wb") as f:
        f.write(base64.b64decode(image_base64))
    print("✅ Image saved as otter.png")

except PermissionDeniedError:
    # Fall back to text response if not allowed
    print("⚠️ Image generation not available, falling back to text.")

    response = client.responses.create(
        model="gpt-5",
        input=f"Describe in detail: {prompt}"
    )
    print("💬 Text description:\n")
    print(response.output[0].content[0].text)
