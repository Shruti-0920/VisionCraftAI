def build_prompt(vision_description, user_notes=""):
    """
    Convert the vision analysis into a detailed prompt
    for image generation.
    """

    prompt = f"""
Create a high-quality professional image based on the following description.

Sketch Analysis:
{vision_description}

Additional User Instructions:
{user_notes}

Requirements:
- Preserve the original idea.
- Make it clean and professional.
- High resolution.
- Detailed.
- Realistic lighting.
"""

    return prompt