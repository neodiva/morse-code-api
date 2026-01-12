
# Text ↔ Morse Code Converter API

## Documentation

This API converts:
- Normal text → Morse code
- Morse code → Normal text

It is built using **FastAPI** and accepts **JSON input**.

---

## 1. Endpoint Description

### 1.1 Home Page (UI)

- **Endpoint:** `/`
- **Method:** `GET`
- **Purpose:**  
  Displays a simple web page where users can enter text or Morse code and convert it using buttons.
- **Response Type:** HTML page  
- **Source:** `index.html`

---

### 1.2 Convert Text to Morse Code

- **Endpoint:** `/text-to-morse`
- **Method:** `POST`
- **Purpose:**  
  Converts English text (A–Z, 0–9, space) into Morse code.

**Spacing Rules:**
- Letters are separated by spaces  
- Words are separated by `/`

- **Source:** `main.py`

---

### 1.3 Convert Morse Code to Text

- **Endpoint:** `/morse-to-text`
- **Method:** `POST`
- **Purpose:**  
  Converts Morse code back into readable text.

**Spacing Rule:**
- Morse symbols must be separated by **single spaces**

- **Source:** `main.py`

---

## 2. Input and Output Formats

### 2.1 Common Input Format (JSON)

Both endpoints use the same input format:

```json
{
  "message": "string"
}
````

**message field:**

* For text-to-morse: normal text
* For morse-to-text: Morse symbols separated by spaces

---

### 2.2 Output Format — Text to Morse

**Success Response**

```json
{
  "morse": "... --- ..."
}
```

**Error Response (400 Bad Request)**

```json
{
  "detail": "Unsupported character: @"
}
```

Occurs if the text contains characters not supported by the Morse dictionary.

---

### 2.3 Output Format — Morse to Text

**Success Response**

```json
{
  "text": "SOS"
}
```

**Error Response (400 Bad Request)**

```json
{
  "detail": "Invalid Morse code: ....-.-"
}
```

Occurs if the Morse pattern is not recognized.

---

## 3. Example Requests and Responses

### 3.1 Example: Text to Morse

**Request**

```http
POST /text-to-morse
Content-Type: application/json
```

```json
{
  "message": "HELLO WORLD"
}
```

**Response**

```json
{
  "morse": ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
}
```

---

### 3.2 Example: Morse to Text

**Request**

```http
POST /morse-to-text
Content-Type: application/json
```

```json
{
  "message": ".... . .-.. .-.. ---"
}
```

**Response**

```json
{
  "text": "HELLO"
}
```

---
Created By: **Electronauts**
