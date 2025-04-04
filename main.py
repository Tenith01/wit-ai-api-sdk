import os

from dotenv import load_dotenv

from sdk.witai_sdk import WitAI

# Load environment variables from .env file
load_dotenv()

# Replace with your actual server access token from environment variable
TOKEN = os.getenv("WITAI_ACCESS_TOKEN")

# Initialize WitAI client
wit = WitAI(TOKEN)

# Use any function with dot notation
response = wit.get_message_meaning("What's the weather like?")
print(response)