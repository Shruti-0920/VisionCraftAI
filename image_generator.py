from openai import OpenAI
from config import OPENAI_API_KEY

import base64
import os

client = OpenAI(api_key=OPENAI_API_KEY)


def generate_image(prompt):

    try:

        response = client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size="1024x1024"
        )

        image_bytes = base64.b64decode(response.data[0].b64_json)

        os.makedirs("output", exist_ok=True)

        image_path = "output/generated_image.png"

        with open(image_path, "wb") as f:
            f.write(image_bytes)

        return image_path

    except Exception as e:
        return str(e)