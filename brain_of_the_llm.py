
from dotenv import load_dotenv
load_dotenv()
#convert immage to text
import base64

imange_path = "acne.jpg"
image = open(imange_path, "rb")
image_base64 = base64.b64encode(image.read()).decode('utf-8')

def encode_image_to_base64(image_path):
   
    image = open(imange_path, "rb")
    return   base64.b64encode(image.read()).decode('utf-8')

    """
    Encode an image file to a base64 string.
    
    :param image_path: Path to the image file.
    :return: Base64 encoded string of the image.
    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

from groq import Groq

query="Is there something wrong with my face? and give some advice to cure it"
#model = "meta-llama/llama-4-maverick-17b-128e-instruct"
model="meta-llama/llama-4-scout-17b-16e-instruct"

def anayze_image(image_base64, query, model):
    client = Groq()
    response = client.chat.completions.create(
        model=model,
        messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{image_base64}",
                    },
                },
            ],
        }]
    )
    return response.choices[0].message.content
  

