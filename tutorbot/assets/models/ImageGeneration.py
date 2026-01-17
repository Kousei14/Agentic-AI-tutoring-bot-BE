from google import genai
from google.genai.types import GenerateImagesConfig

from tutorbot.app import settings

from dotenv import load_dotenv
load_dotenv()

class ImageGenerationModels:
    def __init__(self,
                 model: str = "imagen-4.0-generate-preview-06-06"):

        self.model = model

        self.client = genai.Client(
            vertexai = True, 
            project = settings.PROJECT_ID, 
            location = settings.LOCATION
            )

    def generate(self, 
                 prompt: str, 
                 number_of_outputs: int = 1, 
                 aspect_ratio: str = "16:9"):
        
        config = GenerateImagesConfig(
            number_of_images = number_of_outputs,
            aspect_ratio = aspect_ratio,
            person_generation = "allow_all",
            safety_filter_level = "block_few"
        )
        images = self.client.models.generate_images(
            model = self.model,
            prompt = prompt,
            config = config
        )

        return images.generated_images[0].image.image_bytes
