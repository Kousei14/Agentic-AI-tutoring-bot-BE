import os
from dotenv import load_dotenv
load_dotenv()

from google.genai.types import SafetySetting
from google.genai.types import GenerateContentConfig

# API KEYS
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# PROJECT DETAILS
PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("LOCATION")

# AGENTS
# --- QueryProcessorAgent (uses API keys)
QUERY_PROCESSOR_MODE = "gemini"
QUERY_PROCESSOR_MODEL = "gemini-2.5-flash"

# --- AnswerGeneratorAgent (uses API keys)
ANSWER_GENERATOR_MODE = "gemini"
ANSWER_GENERATOR_MODEL = "gemini-2.5-flash"
ANSWER_GENERATOR_CONFIG = GenerateContentConfig(
    safety_settings = [
    SafetySetting(
        category = "HARM_CATEGORY_HATE_SPEECH", 
        threshold = "OFF"
        ),
    SafetySetting(
        category = "HARM_CATEGORY_DANGEROUS_CONTENT", 
        threshold = "OFF"
        ),
    SafetySetting(
        category = "HARM_CATEGORY_SEXUALLY_EXPLICIT", 
        threshold = "OFF"
        ),
    SafetySetting(
        category = "HARM_CATEGORY_HARASSMENT", 
        threshold = "OFF"
        ),
],
    response_mime_type = "application/json",
    response_json_schema = {
    "type": "object",
    "properties": {
        "summary": {
            "type": "array",
            "items": {"type": "string"},
            "minItems": 2,
            "maxItems": 2
        },
        "narration_lines": {
            "type": "array",
            "items": {"type": "string"}
        },
        "math_lines": {
            "type": "array",
            "items": {"type": "string"}
        }
    },
    "required": ["summary", "narration_lines", "math_lines"],
    "additionalProperties": False
}
)

# --- IllustrationUtilsGeneratorAgent (uses API keys)
ILLUSTRATION_UTILS_GENERATOR_MODE = "openai"
ILLUSTRATION_UTILS_GENERATION_MODEL = "gpt-4o-mini"
ILLUSTRATION_UTILS_GENERATOR_CONFIG = GenerateContentConfig(
    safety_settings = [
    SafetySetting(
        category = "HARM_CATEGORY_HATE_SPEECH", 
        threshold = "OFF"
        ),
    SafetySetting(
        category = "HARM_CATEGORY_DANGEROUS_CONTENT", 
        threshold = "OFF"
        ),
    SafetySetting(
        category = "HARM_CATEGORY_SEXUALLY_EXPLICIT", 
        threshold = "OFF"
        ),
    SafetySetting(
        category = "HARM_CATEGORY_HARASSMENT", 
        threshold = "OFF"
        ),
],
    response_mime_type = "application/json",
    response_json_schema = {
    "type": "object",
    "properties": {
        "illustration_prompt": {
            "type": "string"
        },
        "illustration_narration": {
            "type": "string",
        },
        "animation_prompt": {
            "type": "string"
        }
    },
    "required": [
        "illustration_prompt",
        "illustration_narration",
        "animation_prompt"
    ],
    "additionalProperties": False
}
)

# --- IllustrationGeneratorAgent (uses vertexai project through google.genai)
ILLUSTRATION_GENERATOR_MODEL = "imagen-4.0-generate-preview-06-06"

# --- AnimationGeneratorAgent (uses vertexai project through google.genai)
ANIMATION_GENERATOR_MODEL = "veo-3.0-generate-001"

# --- AudioGeneratorAgent (uses API keys)
AUDIO_GENERATOR_MODEL = "gemini-2.5-flash-preview-tts"
NARRATION_MODE = "default_tts"
SUMMARY_MODE = "gemini_tts"
ILLUSTRATION_NARRATION_MODE = "gemini_tts"
