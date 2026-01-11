from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI(title="Text ↔ Morse Code Converter API")


templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Morse code dictionary
MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',
    ' ': '/'
}

REVERSE_MORSE = {v: k for k, v in MORSE_CODE.items()}

class InputText(BaseModel):
    message: str

@app.post("/text-to-morse")
def text_to_morse(data: InputText):
    result = []
    for char in data.message.upper():
        if char not in MORSE_CODE:
            raise HTTPException(
                status_code=400,
                detail=f"Unsupported character: {char}"
            )
        result.append(MORSE_CODE[char])
    return {"morse": " ".join(result)}

@app.post("/morse-to-text")
def morse_to_text(data: InputText):
    result = []
    codes = data.message.split(" ")
    for code in codes:
        if code not in REVERSE_MORSE:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid Morse code: {code}"
            )
        result.append(REVERSE_MORSE[code])
    return {"text": "".join(result)}
