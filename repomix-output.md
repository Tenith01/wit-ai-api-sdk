This file is a merged representation of the entire codebase, combined into a single document by Repomix.

# File Summary

## Purpose
This file contains a packed representation of the entire repository's contents.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Files are sorted by Git change count (files with more changes are at the bottom)

## Additional Info

# Directory Structure
```
dataset/
  dataset-v1.json
  dataset-v2.json
sdk/
  sample.py
  witai_sdk.py
.gitignore
.repomixignore
fine_tune_witai.py
main.py
README.md
repomix.config.json
requirements.txt
```

# Files

## File: dataset/dataset-v1.json
````json
[
  {"text": "Open my profile now.", "entities": [{"entity": "intent", "value": "NAVIGATE_PROFILE"}]},
  {"text": "Go straight to the home screen.", "entities": [{"entity": "intent", "value": "NAVIGATE_HOME"}]},
  {"text": "Pull up my memories quickly.", "entities": [{"entity": "intent", "value": "NAVIGATE_MEMORIES"}]},
  {"text": "Open the community page fast.", "entities": [{"entity": "intent", "value": "NAVIGATE_COMMUNITY"}]},
  {"text": "Jump to my wanderlist now.", "entities": [{"entity": "intent", "value": "NAVIGATE_WANDERLIST"}]}
]
````

## File: dataset/dataset-v2.json
````json
[
  {"text": "Play my favorite playlist.", "entities": [{"entity": "intent", "value": "PLAY_PLAYLIST"}]},
  {"text": "Skip to the next song.", "entities": [{"entity": "intent", "value": "SKIP_TRACK"}]},
  {"text": "Pause the music now.", "entities": [{"entity": "intent", "value": "PAUSE_MUSIC"}]},
  {"text": "Turn up the volume a bit.", "entities": [{"entity": "intent", "value": "INCREASE_VOLUME"}]},
  {"text": "Mute everything instantly.", "entities": [{"entity": "intent", "value": "MUTE_AUDIO"}]}
]
````

## File: sdk/sample.py
````python
# sample.py
import os
import time

import requests
from dotenv import load_dotenv

from witai_sdk import WitAI

# Load environment variables from .env file
load_dotenv()

# Replace with your actual server access token from environment variable
TOKEN = os.getenv("WITAI_ACCESS_TOKEN")

# Initialize WitAI client
wit = WitAI(TOKEN)


def main():
    # --- Message Endpoints ---
    print("1. Getting message meaning:")
    meaning = wit.get_message_meaning("What's the weather like today?")
    print(meaning)

    # --- Speech Endpoints ---
    print("\n2. Transcribing audio (assuming 'sample.wav' exists):")
    try:
        transcription = wit.transcribe_audio("sample.wav", "audio/wav")
        print(transcription)
    except FileNotFoundError:
        print("Sample audio file not found.")
    except requests.exceptions.RequestException as e:
        print(f"Error transcribing audio: {e}")

    print("\n3. Getting speech meaning (assuming 'sample.wav' exists):")
    try:
        speech_meaning = wit.get_speech_meaning("sample.wav", "audio/wav")
        print(speech_meaning)
    except FileNotFoundError:
        print("Sample audio file not found.")
    except requests.exceptions.RequestException as e:
        print(f"Error getting speech meaning: {e}")

    # --- Synthesize Endpoint ---
    print("\n4. Synthesizing speech:")
    try:
        audio_data = wit.synthesize_speech("Hello, this is a test!", "wit$Rebecca")
        with open("../output.raw", "wb") as f:
            f.write(audio_data)
        print("Audio saved to 'output.raw'")
    except requests.exceptions.RequestException as e:
        print(f"Error synthesizing speech: {e}")

    # --- Language Detection ---
    print("\n5. Detecting language:")
    lang = wit.detect_language("Bonjour mes amis")
    print(lang)

    # --- Intent Management ---
    print("\n6. Getting all intents:")
    intents = wit.get_intents()
    print(intents)

    print("\n7. Creating a new intent:")
    new_intent = wit.create_intent("test_intent")
    print(new_intent)

    print("\n8. Getting intent info:")
    intent_info = wit.get_intent_info("test_intent")
    print(intent_info)

    # print("\n9. Deleting an intent:")
    # deleted_intent = wit.delete_intent("test_intent")
    # print(deleted_intent)
    #
    # print("\n10. Deleting all intents:")
    # intents = wit.get_intents()
    # for intent in intents:
    #     try:
    #         wit.delete_intent(intent['name'])
    #         print(f"Deleted intent: {intent['name']}")
    #         time.sleep(0.5)  # Delay to respect rate limits
    #     except requests.exceptions.HTTPError as e:
    #         print(f"Failed to delete intent {intent['name']}: {e}")
    # print("Finished deleting all intents.")

    # --- Entity Management ---
    print("\n11. Getting all entities:")
    entities = wit.get_entities()
    print(entities)

    print("\n12. Creating a new entity:")
    new_entity = wit.create_entity("test_entity", roles=["primary"])
    print(new_entity)

    print("\n13. Getting entity info:")
    entity_info = wit.get_entity_info("test_entity")
    print(entity_info)

    print("\n14. Updating an entity:")
    updated_entity = wit.update_entity("test_entity", "test_entity", roles=["primary"],
                                       keywords=[{"keyword": "test", "synonyms": ["trial"]}])
    print(updated_entity)

    print("\n15. Adding a keyword to entity:")
    keyword_added = wit.add_keyword("test_entity", "example", ["sample"])
    print(keyword_added)

    # print("\n16. Deleting a keyword from entity:")
    # keyword_deleted = wit.delete_keyword("test_entity", "example")
    # print(keyword_deleted)
    #
    # print("\n17. Deleting an entity:")
    # deleted_entity = wit.delete_entity("test_entity")
    # print(deleted_entity)

    # --- App Management ---
    print("\n18. Getting all apps:")
    apps = wit.get_apps(limit=10)
    print(apps)

    # print("\n19. Creating a new app:")
    # new_app = wit.create_app("TestApp", "en", False)
    # print(new_app)
    #
    # print("\n20. Getting app info:")
    # app_info = wit.get_app_info(new_app["app_id"])
    # print(app_info)
    #
    # print("\n21. Updating an app:")
    # updated_app = wit.update_app(new_app["app_id"], name="UpdatedTestApp")
    # print(updated_app)
    #
    # print("\n22. Deleting an app:")
    # deleted_app = wit.delete_app(new_app["app_id"])
    # print(deleted_app)

    # --- Training Endpoint ---
    # print("\n23. Uploading utterances:")
    # sample_utterances = [
    #     {
    #         "text": "I want to test this",
    #         "intent": "test_intent",
    #         "entities": [],
    #         "traits": []
    #     }
    # ]
    # wit.create_intent("test_intent")  # Ensure intent exists
    # uploaded = wit.upload_utterances(sample_utterances)
    # print(uploaded)
    # time.sleep(2)  # Wait for processing
    #
    # print("\n24. Deleting all utterances:")
    # deleted_utterances = wit.delete_all_utterances()
    # print(deleted_utterances)

if __name__ == "__main__":
    main()
````

## File: sdk/witai_sdk.py
````python
# witai_sdk.py
import os

import requests
import json
from typing import Dict, List, Optional, Union, Any

from dotenv import load_dotenv


class WitAI:
    def __init__(self, token: str, api_version: str = "20240304"):
        """Initialize WitAI SDK with access token."""
        self.base_url = "https://api.wit.ai"
        self.token = token
        self.api_version = api_version
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    # Message Endpoints
    def get_message_meaning(self, query: str, tag: Optional[str] = None,
                            context: Optional[Dict] = None, n: Optional[int] = None,
                            entities: Optional[Dict] = None) -> Dict:
        """Return the meaning of a sentence."""
        params = {"v": self.api_version, "q": query}
        if tag: params["tag"] = tag
        if n: params["n"] = n
        if context: params["context"] = json.dumps(context)
        if entities: params["entities"] = json.dumps(entities)

        response = requests.get(f"{self.base_url}/message",
                                headers=self.headers,
                                params=params)
        response.raise_for_status()
        return response.json()

    # Speech Endpoints
    def transcribe_audio(self, audio_file: str, content_type: str) -> Dict:
        """Transcribe an audio wave."""
        headers = self.headers.copy()
        headers["Content-Type"] = content_type

        with open(audio_file, 'rb') as f:
            response = requests.post(
                f"{self.base_url}/speech?v={self.api_version}",
                headers=headers,
                data=f
            )
        response.raise_for_status()
        return response.json()

    def get_speech_meaning(self, audio_file: str, content_type: str,
                           context: Optional[Dict] = None) -> Dict:
        """Retrieve the meaning of an audio wave."""
        headers = self.headers.copy()
        headers["Content-Type"] = content_type

        params = {"v": self.api_version}
        if context: params["context"] = json.dumps(context)

        with open(audio_file, 'rb') as f:
            response = requests.post(
                f"{self.base_url}/speech",
                headers=headers,
                params=params,
                data=f
            )
        response.raise_for_status()
        return response.json()

    # Synthesize Endpoint
    def synthesize_speech(self, text: str, voice: str,
                          style: Optional[str] = None, speed: Optional[int] = None,
                          pitch: Optional[int] = None,
                          accept_format: str = "audio/raw") -> bytes:
        """Synthesize natural sounding speech."""
        headers = self.headers.copy()
        headers["Accept"] = accept_format

        data = {"q": text, "voice": voice}
        if style: data["style"] = style
        if speed: data["speed"] = speed
        if pitch: data["pitch"] = pitch

        response = requests.post(
            f"{self.base_url}/synthesize?v={self.api_version}",
            headers=headers,
            json=data
        )
        response.raise_for_status()
        return response.content

    # Language Detection
    def detect_language(self, text: str, n: Optional[int] = None) -> Dict:
        """Retrieve the language of a text message."""
        params = {"v": self.api_version, "q": text}
        if n: params["n"] = n

        response = requests.get(
            f"{self.base_url}/language",
            headers=self.headers,
            params=params
        )
        response.raise_for_status()
        return response.json()

    # Intent Management
    def get_intents(self) -> List[Dict]:
        """Retrieve all intents."""
        response = requests.get(
            f"{self.base_url}/intents?v={self.api_version}",
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def create_intent(self, name: str) -> Dict:
        """Create a new intent."""
        response = requests.post(
            f"{self.base_url}/intents?v={self.api_version}",
            headers=self.headers,
            json={"name": name}
        )
        response.raise_for_status()
        return response.json()

    def get_intent_info(self, intent: str) -> Dict:
        """Retrieve information about an intent."""
        response = requests.get(
            f"{self.base_url}/intents/{intent}?v={self.api_version}",
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def delete_intent(self, intent: str) -> Dict:
        """Delete an intent."""
        response = requests.delete(
            f"{self.base_url}/intents/{intent}?v={self.api_version}",
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def delete_all_intents(self) -> None:
        """Delete all intents in the app."""
        intents = self.get_intents()
        for intent in intents:
            self.delete_intent(intent['name'])

    # Entity Management
    def get_entities(self) -> List[Dict]:
        """Retrieve all entities."""
        response = requests.get(
            f"{self.base_url}/entities?v={self.api_version}",
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def create_entity(self, name: str, roles: List[str] = [],
                      lookups: Optional[List[str]] = None,
                      keywords: Optional[List[Dict]] = None) -> Dict:
        """Create a new entity."""
        data = {"name": name, "roles": roles}
        if lookups: data["lookups"] = lookups
        if keywords: data["keywords"] = keywords

        response = requests.post(
            f"{self.base_url}/entities?v={self.api_version}",
            headers=self.headers,
            json=data
        )
        response.raise_for_status()
        return response.json()

    def get_entity_info(self, entity: str) -> Dict:
        """Retrieve information about an entity."""
        response = requests.get(
            f"{self.base_url}/entities/{entity}?v={self.api_version}",
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def update_entity(self, entity: str, name: str, roles: List[str],
                      lookups: Optional[List[str]] = None,
                      keywords: Optional[List[Dict]] = None) -> Dict:
        """Update an entity."""
        data = {"name": name, "roles": roles}
        if lookups: data["lookups"] = lookups
        if keywords: data["keywords"] = keywords

        response = requests.put(
            f"{self.base_url}/entities/{entity}?v={self.api_version}",
            headers=self.headers,
            json=data
        )
        response.raise_for_status()
        return response.json()

    def delete_entity(self, entity: str) -> Dict:
        """Delete an entity."""
        response = requests.delete(
            f"{self.base_url}/entities/{entity}?v={self.api_version}",
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    # Keyword Management
    def add_keyword(self, entity: str, keyword: str,
                    synonyms: List[str]) -> Dict:
        """Add new values to a keywords entity."""
        response = requests.post(
            f"{self.base_url}/entities/{entity}/keywords?v={self.api_version}",
            headers=self.headers,
            json={"keyword": keyword, "synonyms": synonyms}
        )
        response.raise_for_status()
        return response.json()

    def delete_keyword(self, entity: str, keyword: str) -> Dict:
        """Remove a keyword from an entity."""
        response = requests.delete(
            f"{self.base_url}/entities/{entity}/keywords/{keyword}?v={self.api_version}",
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    # App Management
    def get_apps(self, limit: int, offset: int = 0) -> List[Dict]:
        """Get all apps."""
        params = {"v": self.api_version, "limit": limit, "offset": offset}
        response = requests.get(
            f"{self.base_url}/apps",
            headers=self.headers,
            params=params
        )
        response.raise_for_status()
        return response.json()

    def create_app(self, name: str, lang: str, private: bool,
                   timezone: Optional[str] = None) -> Dict:
        """Create a new app."""
        data = {"name": name, "lang": lang, "private": private}
        if timezone: data["timezone"] = timezone

        response = requests.post(
            f"{self.base_url}/apps?v={self.api_version}",
            headers=self.headers,
            json=data
        )
        response.raise_for_status()
        return response.json()

    def get_app_info(self, app_id: str) -> Dict:
        """Get information for a specific app."""
        response = requests.get(
            f"{self.base_url}/apps/{app_id}?v={self.api_version}",
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def update_app(self, app_id: str, name: Optional[str] = None,
                   lang: Optional[str] = None, private: Optional[bool] = None,
                   timezone: Optional[str] = None) -> Dict:
        """Update an existing app."""
        data = {}
        if name: data["name"] = name
        if lang: data["lang"] = lang
        if private is not None: data["private"] = private
        if timezone: data["timezone"] = timezone

        response = requests.put(
            f"{self.base_url}/apps/{app_id}?v={self.api_version}",
            headers=self.headers,
            json=data
        )
        response.raise_for_status()
        return response.json()

    def delete_app(self, app_id: str) -> Dict:
        """Delete an app."""
        response = requests.delete(
            f"{self.base_url}/apps/{app_id}?v={self.api_version}",
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    # Training Endpoint
    def upload_utterances(self, utterances: List[Dict]) -> Dict:
        """Upload multiple utterances for training."""
        response = requests.post(
            f"{self.base_url}/utterances?v={self.api_version}",
            headers=self.headers,
            json=utterances
        )
        response.raise_for_status()
        return response.json()

    def get_utterances(self, limit: int = 100, offset: int = 0) -> List[Dict]:
        """Retrieve utterances from the app."""
        params = {"v": self.api_version, "limit": limit, "offset": offset}
        response = requests.get(
            f"{self.base_url}/utterances",
            headers=self.headers,
            params=params
        )
        response.raise_for_status()
        return response.json()

    def delete_all_utterances(self) -> Dict:
        """Delete all utterances in the app."""
        # First get all utterances
        utterances = self.get_utterances(limit=10000)  # Max limit per API docs
        print("Utterances retrieved:", utterances)  # Debug output

        # Extract just the text fields for deletion
        utterances_to_delete = [{"text": u["text"]} for u in utterances]
        print("Utterances to delete:", utterances_to_delete)  # Debug output

        if not utterances_to_delete:
            return {"sent": True, "n": 0}

        # Delete in batches if needed (API has rate limits)
        response = requests.delete(
            f"{self.base_url}/utterances?v={self.api_version}",  # Fixed typo here
            headers=self.headers,
            json=utterances_to_delete
        )
        print("Request headers:", self.headers)  # Debug output
        print("Response status:", response.status_code)  # Debug output
        print("Response text:", response.text)  # Debug output
        response.raise_for_status()
        return response.json()

# Example usage:
if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()

    # Replace with your actual server access token from environment variable
    TOKEN = os.getenv("WITAI_ACCESS_TOKEN")

    # Initialize WitAI client
    wit = WitAI(TOKEN)

    # Example: Get intents
    intents = wit.get_intents()
    print(intents)
    # Example: Test message meaning
    meaning = wit.get_message_meaning("hello world")
    print(meaning)
````

## File: .gitignore
````
# Add patterns to ignore here, one per line
# Example:
# *.log
# tmp/
.env
````

## File: .repomixignore
````
# Add patterns to ignore here, one per line
# Example:
# *.log
# tmp/
# dataset
````

## File: fine_tune_witai.py
````python
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
````

## File: main.py
````python
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

# Create an entity
entity_response = wit.create_entity(
    name="favorite_color",
    roles=["color"],
    keywords=[{"keyword": "blue", "synonyms": ["navy", "azure"]}]
)
print(entity_response)

# Synthesize speech
audio_data = wit.synthesize_speech(
    text="Hello world",
    voice="wit$Rebecca",
    style="soft",
    speed=120
)
with open("hello.wav", "wb") as f:
    f.write(audio_data)
````

## File: README.md
````markdown
# Wit.ai SDK Project

## 📄 Introduction
Wit.ai is a powerful natural language processing (NLP) platform that enables developers to build applications capable of understanding human language. This project provides:

- **Python SDK** (`witai_sdk.py`) to interact with the Wit.ai API
- **Sample usage script** (`sample.py`)
- **Fine-tuning script** (`fine_tune_witai.py`) for custom training

## 🔄 Big Picture
This project simplifies the process of integrating Wit.ai with your applications by enabling you to:

- Analyze text and audio for meaning
- Synthesize speech from text
- Manage intents, entities, and apps programmatically
- Fine-tune your Wit.ai app using your own training data

## 📃 Wit.ai Terminology
| Term       | Description                                           |
|------------|-------------------------------------------------------|
| **Intent** | Purpose behind a user's input (e.g., `get_weather`)   |
| **Utterance** | A sample training sentence (e.g., "What's the weather?") |
| **Entity** | Extracted info (e.g., `location: New York`)           |
| **Trait**  | Input characteristic (e.g., `sentiment: positive`)    |
| **Context**| Additional data (e.g., `timezone`) to assist meaning  |
| **Keyword**| Words tied to entities with synonyms                  |

---

## ⚙️ Setup Instructions (Using Anaconda)

### Step 1: Install Anaconda
Download and install from [Anaconda Downloads](https://www.anaconda.com/products/distribution).

### Step 2: Create a New Environment
```bash
conda create -n witai_env python=3.9
conda activate witai_env
```

### Step 3: Install Dependencies
Navigate to your project directory and run:
```bash
pip install -r requirements.txt
```
Installs:
- `requests`
- `python-dotenv`

### Step 4: Set Up Environment Variables
Create a `.env` file in the project root and add:
```env
WITAI_ACCESS_TOKEN=your_server_access_token_here
```

### Step 5: Verify Setup
Run the sample script:
```bash
python sdk/sample.py
```

---

## 🚀 SDK Functions and Usage (`sample.py`)

Below is a technical breakdown of key SDK functions, demonstrated in `sample.py`:

### 🔵 Initialization
Initializes the Wit.ai client with an API token.
```python
wit = WitAI(TOKEN)
```

### 🔵 Message Processing
#### Get Meaning from Text
```python
wit.get_message_meaning("What's the weather like today?")
```
Calls the `/message` endpoint with a query to extract intents, entities, and traits.

### 🔵 Speech Processing
#### Transcribe Audio to Text
```python
wit.transcribe_audio("sample.wav", "audio/wav")
```
Sends audio to Wit.ai for transcription. Content-Type (e.g., `audio/wav`) must match file format.

#### Extract Meaning from Audio
```python
wit.get_speech_meaning("sample.wav", "audio/wav")
```
Combines transcription and intent/entity extraction in one step.

### 🔵 Text-to-Speech
#### Synthesize Text to Audio
```python
wit.synthesize_speech("Hello, this is a test!", "wit$Rebecca")
```
Uses a specified voice to generate audio from text input.

### 🔵 Language Detection
#### Detect Language from Input
```python
wit.detect_language("Bonjour mes amis")
```
Identifies the language of a given text using the language detection endpoint.

### 🔵 Intent Management
#### List Intents
```python
wit.get_intents()
```
#### Create Intent
```python
wit.create_intent("test_intent")
```
#### Get Intent Details
```python
wit.get_intent_info("test_intent")
```
#### Delete Intent
```python
wit.delete_intent("test_intent")
```

### 🔵 Entity Management
#### List Entities
```python
wit.get_entities()
```
#### Create Entity
```python
wit.create_entity("test_entity", roles=["primary"])
```
#### Add Keyword to Entity
```python
wit.add_keyword("test_entity", "example", ["sample"])
```

### 🔵 App Management
#### List Apps
```python
wit.get_apps(limit=10)
```

### 🔵 Training Endpoint
#### Upload Utterances
```python
utterances = [
{"text": "Open my profile.", "entities": [{"entity": "intent", "value": "NAVIGATE_PROFILE"}]},
{"text": "Show me the weather.", "entities": [{"entity": "intent", "value": "GET_WEATHER"}]}
]
wit.upload_utterances(utterances)
```
Sends custom training examples to the Wit.ai app.

See `sample.py` for comprehensive error handling and execution examples.

---

## 📂 Fine-Tuning with Custom Dataset

### Dataset Format (`dataset/dataset-v1.json`)
```json
[
  {"text": "Open my profile now.", "entities": [{"entity": "intent", "value": "NAVIGATE_PROFILE"}]},
  {"text": "Show me the weather.", "entities": [{"entity": "intent", "value": "GET_WEATHER"}]}
]
```

### Steps to Create:
1. Define your app's intents (e.g., `NAVIGATE_PROFILE`, `GET_WEATHER`)
2. Write sample utterances
3. Save as JSON in `dataset/` directory

---

## 📊 Training with `fine_tune_witai.py`

### Run Training
```bash
python fine_tune_witai.py
```

### What Happens:
- **Cleanup:** Deletes all existing utterances & intents
- **Intent Creation:** Extracts and creates new intents
- **Upload:** Sends utterances in batches (10 per request)

### Console Output
- Shows training progress
- Displays errors and completion status

---

## 📖 Summary
This SDK project makes it simple to use Wit.ai's NLP capabilities in Python, with tools to:
- Interact via text/audio
- Manage app components
- Train with custom utterances

> Happy building with Wit.ai! ✨
````

## File: repomix.config.json
````json
{
  "output": {
    "filePath": "repomix-output.md",
    "style": "markdown",
    "parsableStyle": false,
    "fileSummary": true,
    "directoryStructure": true,
    "removeComments": false,
    "removeEmptyLines": false,
    "compress": false,
    "topFilesLength": 5,
    "showLineNumbers": false,
    "copyToClipboard": false,
    "git": {
      "sortByChanges": true,
      "sortByChangesMaxCommits": 100
    }
  },
  "include": [],
  "ignore": {
    "useGitignore": true,
    "useDefaultPatterns": true,
    "customPatterns": []
  },
  "security": {
    "enableSecurityCheck": true
  },
  "tokenCount": {
    "encoding": "o200k_base"
  }
}
````

## File: requirements.txt
````
requests>=2.28.0
python-dotenv>=1.0.0
````
