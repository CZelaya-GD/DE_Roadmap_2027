import os 
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()

@dataclass
class APIConfig: 
    api_key: str
    api_url: str

# testing_key = os.getenv("API") == False
testing_key = os.getenv("API_KEY")
testing_url = os.getenv("API_URL")

api_config = APIConfig(
    api_key=testing_key,
    api_url=testing_url
)

print("API configuration loaded successfully.")
print(f"API URL: {api_config.api_url}")
print(f"API key loaded: {bool(api_config.api_key)}")