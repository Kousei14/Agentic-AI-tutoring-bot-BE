from google import genai
from google.genai.types import GenerateVideosConfig

from tutorbot.app import settings
from tutorbot.utils.ImageUtils import bytes_to_GoogleGenaiImage

import time
import os
from dotenv import load_dotenv
load_dotenv()

class VideoGenerationModels:
    def __init__(self,
                 model: str = "veo-3.0-generate-001"):
        
        self.model = model

        self.client = genai.Client(
            vertexai = True,
            project = settings.PROJECT_ID,
            location = settings.LOCATION
        )

    def generate(self,
                 prompt: str,
                 image_path: str,
                 number_of_videos: int = 1,
                 aspect_ratio: str = "16:9"):
        
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file not found at {image_path}")

        reference_image = bytes_to_GoogleGenaiImage(
            image_path = image_path
        )

        operation = self.client.models.generate_videos(
            model = self.model,
            prompt = prompt,
            image = reference_image,
            config = GenerateVideosConfig(
                number_of_videos = number_of_videos,
                aspect_ratio = aspect_ratio,
                person_generation = "allow_all",
                generate_audio = True
            ),
        )

        while not operation.done:
            time.sleep(20)
            operation = self.client.operations.get(operation)

        return [generated_video.video.video_bytes for generated_video in operation.response.generated_videos]