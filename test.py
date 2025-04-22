import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API key
openai_api_key = os.getenv("OPENAI_API_KEY")  # Alternative: os.environ['OPENAI_API_KEY']

print(f"Your OpenAI API Key is: {openai_api_key}")  # Avoid printing sensitive info in production

