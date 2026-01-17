import ast
import json
from typing import Literal

from tutorbot.app.logic.generate_prompt import PromptFormatter
from tutorbot.assets.models.TextGeneration import TextGenerationModels
from tutorbot.utils.TextUtils import strip_code_block_fence

from tutorbot.app import settings

class QueryProcessorAgent:
    def __init__(self,
                 mode: Literal["gemini", "openai"] = "gemini",
                 model: Literal["gemini-2.5-flash", "gpt-4o-mini"] = "gemini-2.5-flash"):
        
        self.mode = mode
        self.model = model

        self.prompt_generator = PromptFormatter()

    def generate(self,
                 prompt: str):
        
        query_processor_prompt = self.prompt_generator.read_prompt(
            user_problem = prompt,
            mode = "query_processor"
        )
        response = TextGenerationModels(
            mode = self.mode,
            model = self.model,
        ).generate(
            prompt = query_processor_prompt
            )
        
        return response
    
class AnswerGeneratorAgent:
    def __init__(self,
                 mode: Literal["gemini", "openai"] = "gemini",
                 model: Literal["gemini-2.5-flash", "gpt-4o-mini"] = "gemini-2.5-flash"):

        self.mode = mode
        self.model = model

        self.prompt_generator = PromptFormatter()

    def generate(self, 
                 prompt: str):
        
        answer_generator_prompt = self.prompt_generator.read_prompt(
            user_problem = prompt,
            mode = "answer_generator"
            ) 
        response = TextGenerationModels(
            mode = self.mode,
            model = self.model
        ).generate(
            prompt = answer_generator_prompt, 
            )
        response = strip_code_block_fence(
            response
            )
        response = ast.literal_eval(
            response
            )
        print(response)
        return response
    
    def _generate(self,
                  prompt: str):
        
        answer_generator_prompt = self.prompt_generator.read_prompt(
            user_problem = prompt,
            mode = "answer_generator"
            ) 
        response = TextGenerationModels(
            mode = "gemini",
            model = "gemini-2.5-flash"
        )._generate(
            prompt = answer_generator_prompt,
            generation_config = settings.ANSWER_GENERATOR_CONFIG 
            )
        response = json.loads(s = response)

        return response
    
class IllustrationUtilsGeneratorAgent:
    def __init__(self,
                 mode: Literal["gemini", "openai"] = "gemini",
                 model: Literal["gemini-2.5-flash", "gpt-4o-mini"] = "gemini-2.5-flash"):
        
        self.mode = mode
        self.model = model

        self.prompt_generator = PromptFormatter()

    def generate(self,
                 prompt: str):
        
        illustration_generator_prompt = self.prompt_generator.read_prompt(
            user_problem = prompt,
            mode = "illustration_utils_generator_v2"
            )
        response = TextGenerationModels(
            mode = self.mode,
            model = self.model
        ).generate(
            prompt = illustration_generator_prompt
            )
        response = strip_code_block_fence(
            response
            )
        response = ast.literal_eval(
            response
            )
        print(response)
        return response
    
    def _generate(self,
                  prompt: str):
        
        answer_generator_prompt = self.prompt_generator.read_prompt(
            user_problem = prompt,
            mode = "answer_generator"
            ) 
        response = TextGenerationModels(
            mode = "gemini",
            model = "gemini-2.5-flash"
        )._generate(
            prompt = answer_generator_prompt, 
            generation_config = settings.ILLUSTRATION_UTILS_GENERATOR_CONFIG
            )
        response = json.loads(s = response)

        return response

