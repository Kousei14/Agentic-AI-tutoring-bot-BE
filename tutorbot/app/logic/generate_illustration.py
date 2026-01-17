from tutorbot.assets.models.ImageGeneration import ImageGenerationModels

class IllustrationGeneratorAgent:
    def __init__(self,
                 model: str = "imagen-4.0-generate-preview-06-06"):
        
        self.model = model

    def generate(self,
                 prompt: str, 
                 number_of_outputs: int = 1, 
                 aspect_ratio: str = "16:9"):
        
        images = ImageGenerationModels(
            model = self.model
        ).generate(
            prompt = prompt,
            number_of_outputs = number_of_outputs,
            aspect_ratio = aspect_ratio
        )

        return images
