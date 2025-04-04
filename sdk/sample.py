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
