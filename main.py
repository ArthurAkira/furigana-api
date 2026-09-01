from fastapi import FastAPI, middleware
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import pykakasi

app = FastAPI(title="Japanese Text Converter", description="Convert Japanese kanji to furigana.", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

kks = pykakasi.kakasi()

class TextRequest(BaseModel):
    text: str

def generate_furigana(text: str) -> str:
    result = kks.convert(text)
    furigana_text = ""
    html_text = []

    for item in result:
        if item['orig'] != item['hira']:
            furigana_text += f"{item['orig']}({item['hira']})"
            html_text.append(f"<ruby>{item['orig']}<rt>{item['hira']}</rt></ruby>")
        else:
            furigana_text += item['orig']
            html_text.append(item['orig'])
    return furigana_text, ''.join(html_text)

@app.post("/furigana", summary="Convert Japanese text to furigana")
@app.post("/convert", summary="Convert Japanese text to furigana")
def convert_to_furigana(payload: TextRequest):
    furigana_text, html_text = generate_furigana(payload.text)
    return {"furigana": furigana_text, "html": html_text}