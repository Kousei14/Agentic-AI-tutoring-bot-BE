from PIL import Image as PilIlmage
import io
import numpy as np

from google.genai.types import Image as GoogleGenaiImage

def save_bytes_as_image(bytes,
                        filename: str = "illustration.jpg"):

    pil_image = PilIlmage.open(
                fp = io.BytesIO(bytes)
                )

    image = pil_image.convert("RGB")
    image.save(
        fp = "tutorbot/assets/{filename}".format(filename = f"images/{filename}"), 
        format = "JPEG"
        )
    
def bytes_to_array(bytes):

    pil_image = PilIlmage.open(
        fp = io.BytesIO(bytes)
        )
    
    return np.array(pil_image)

def bytes_to_GoogleGenaiImage(image_path: str):

    with open(image_path, "rb") as f:
        image_bytes = f.read()

    reference_image = GoogleGenaiImage(
        image_bytes = image_bytes,
        mime_type = "image/png"
    )

    return reference_image