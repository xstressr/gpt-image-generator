import os
import base64
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def generate_image(prompt):
    """
    Generate images from a text prompt
    """
    # Retrieve API base and token from environment variables
    base_url = os.getenv("OPENAI_API_BASE")
    api_key = os.getenv("OPENAI_API_KEY")

    if not base_url or not api_key:
        print("Error: OPENAI_API_BASE and OPENAI_API_KEY must be set in environment variables.")
        return []

    # Initialize client with credentials from environment variables
    client = OpenAI(api_key=api_key, base_url=base_url)

    try:
        result = client.images.generate(
            model="gpt-image-1",
            prompt=prompt
        )
        image_base64 = result.data[0].b64_json
        image_bytes = base64.b64decode(image_base64)

        # Save the image to a file
        output_filename = "generated_image.png"
        with open(output_filename, "wb") as f:
            f.write(image_bytes)
        print(f"Image saved as {output_filename}")
    except Exception as e:
        print(f"Error generating image: {e}")

if __name__ == "__main__":
    sample_prompt = "A children's book drawing of a veterinarian using a stethoscope to listen to the heartbeat of a baby otter."
    print(f"Generating image for prompt: {sample_prompt}")
    generate_image(sample_prompt)
