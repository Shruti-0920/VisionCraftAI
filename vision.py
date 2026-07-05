from openai import OpenAI
from config import OPENAI_API_KEY
import base64

client = OpenAI(api_key=OPENAI_API_KEY)


def analyze_sketch(image_path):

    try:

        with open(image_path, "rb") as image_file:
            image_base64 = base64.b64encode(image_file.read()).decode("utf-8")

        response = client.responses.create(
            model="gpt-4.1-mini",
            input=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": """
Analyze this sketch.

Describe:
1. Main subject
2. Style
3. Colors
4. Objects present
5. Suggested improvements

Return a clear paragraph.
"""
                        },
                        {
                            "type": "input_image",
                            "image_url": f"data:image/png;base64,{image_base64}"
                        }
                    ]
                }
            ]
        )

        return response.output_text

    except Exception as e:
        return str(e)