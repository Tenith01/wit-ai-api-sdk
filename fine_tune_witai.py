# fine_tune_witai.py
import json
import os
import time
import requests
from dotenv import load_dotenv

from sdk.witai_sdk import WitAI

# Load environment variables from .env file
load_dotenv()

# Server Access Token from environment variable
ACCESS_TOKEN = os.getenv("WITAI_ACCESS_TOKEN")

# Initialize WitAI client
wit = WitAI(ACCESS_TOKEN)

# Function to clean up existing data
def cleanup():
    print("Deleting all utterances...")
    try:
        result = wit.delete_all_utterances()
        print(f"Deleted utterances: {result['n']}")
    except requests.exceptions.HTTPError as e:
        print(f"Error deleting utterances: {e.response.status_code} - {e.response.text}")

    print("Deleting all intents...")
    try:
        intents = wit.get_intents()
        for intent in intents:
            wit.delete_intent(intent['name'])
            print(f"Deleted: {intent['name']}")
            time.sleep(1)  # Respect rate limits
    except requests.exceptions.HTTPError as e:
        print(f"Error deleting intents: {e.response.status_code} - {e.response.text}")

# Read dataset
with open('dataset/dataset-v1.json', 'r') as f:
    samples = json.load(f)

# Get unique intents (lowercase)
intents = list(set(sample['entities'][0]['value'].lower() for sample in samples))

# Convert samples to utterances format
utterances = [
    {
        'text': sample['text'],
        'intent': sample['entities'][0]['value'].lower(),
        'entities': [],
        'traits': []
    }
    for sample in samples
]

# Clean up before fine-tuning
cleanup()

# Create intents
print('Creating intents...')
for intent in intents:
    try:
        wit.create_intent(intent)
        print(f"Created: {intent}")
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 400 and "already exists" in e.response.text:
            print(f"Exists: {intent}")
        else:
            print(f"Error creating {intent}: {e.response.status_code} - {e.response.text}")
    time.sleep(1)  # Respect rate limits

# Upload utterances in batches
print(f"Training with {len(utterances)} utterances...")
batch_size = 10
for i in range(0, len(utterances), batch_size):
    batch = utterances[i:i + batch_size]
    try:
        wit.upload_utterances(batch)
        print(f"Uploaded batch {i // batch_size + 1} ({len(batch)} utterances)")
        time.sleep(2)  # Reduced delay
    except requests.exceptions.HTTPError as e:
        print(f"Batch {i // batch_size + 1} failed: {e.response.status_code} - {e.response.text}")
        exit(1)

print("Training completed!")