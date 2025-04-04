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

