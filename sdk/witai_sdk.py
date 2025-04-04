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