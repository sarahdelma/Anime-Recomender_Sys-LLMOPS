import os
from dotenv import load_dotenv

load_dotenv()

# Make sure your .env file contains:
# GROQ_API_KEY=your_key_here
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Groq model name
MODEL_NAME = "llama-3.1-8b-instant"
