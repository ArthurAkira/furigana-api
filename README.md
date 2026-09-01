# Furigana Inserter API

A small web project that converts Japanese text into Furigana using FastAPI and `pykakasi`.

## Features

- Accepts Japanese text via API or browser form
- Converts kanji into Ruby annotation HTML
- Returns both plain furigana text and HTML output
- Simple frontend built with HTML, CSS, and JavaScript

## Project structure

- `main.py` — FastAPI backend
- `index.html` — frontend interface
- `style.css` — frontend styling
- `README.md` — project documentation

## Requirements

- Python 3.9+
- pip
- Modern browser

## Installation

1. Open a terminal in the project folder.
2. Install the dependencies:

```bash
pip install fastapi uvicorn pykakasi
```

## Run the API

Start the server:

```bash
uvicorn main:app --reload
```

The app will be available at:

- http://127.0.0.1:8000

## API endpoints

### POST /furigana

Request body:

```json
{
  "text": "日本語を勉強しています。"
}
```

Example request:

```bash
curl -X POST "http://127.0.0.1:8000/furigana" \
  -H "Content-Type: application/json" \
  -d '{"text":"日本語を勉強しています。"}'
```

Example response:

```json
{
  "furigana": "日(に)本(ほん)語(ご)を勉(べん)強(きょう)しています。",
  "html": "<ruby>日<rt>に</rt></ruby><ruby>本<rt>ほん</rt></ruby><ruby>語<rt>ご</rt></ruby>を<ruby>勉<rt>べん</rt></ruby><ruby>強<rt>きょう</rt></ruby>しています。"
}
```

There is also a second route available:

- `POST /convert`

Both routes behave the same way.

## Frontend usage

Open the browser page for the frontend and enter a Japanese sentence, then click the button to generate the Furigana output.

The frontend currently sends requests to `/furigana` and expects the API to be available on the same origin. If needed, update the `fetch` URL in `index.html` to match your local API address.

## Notes

This project is a simple demonstration of converting Japanese text into furigana annotations for learning and testing purposes.