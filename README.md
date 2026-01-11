# Text ↔ Morse Code Converter API

## Description
This is a REST API that converts plain text to Morse code and Morse code back to plain text.
The API is built using FastAPI and supports bidirectional conversion with proper validation.

## Base URL
http://127.0.0.1:8000

## Endpoints

### 1. Text to Morse
POST /text-to-morse

Request Body:
{
  "message": "HELLO"
}

Response:
{
  "morse": ".... . .-.. .-.. ---"
}

### 2. Morse to Text
POST /morse-to-text

Request Body:
{
  "message": ".... . .-.. .-.. ---"
}

Response:
{
  "text": "HELLO"
}

## Error Handling
- Returns 400 error for unsupported characters
- Returns 400 error for invalid Morse code input

## How to Run Locally
1. Install dependencies:
   pip install -r requirements.txt

2. Start the server:
   python -m uvicorn main:app --reload

3. Open in browser:
   http://127.0.0.1:8000/docs
