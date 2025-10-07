# backend/service.py
import spacy
from typing import List, Dict
from .utils import clean_text
import os
from pathlib import Path

# Load spaCy model once at startup
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = os.getenv("MODEL_PATH")

if not MODEL_PATH:
    print("using base dir one \n")
    MODEL_PATH = BASE_DIR / "entity_extractor_model"

print(f"🔹 Using model path: {MODEL_PATH}")


nlp = spacy.load(MODEL_PATH)

def extract_entities(text: str) -> List[Dict[str, str]]:
    """
    Given raw text, returns a list of extracted entities
    as dicts: [{"label": "...", "text": "..."}, ...]
    """
    cleaned = clean_text(text)
    doc = nlp(cleaned)
    entities = [{"label": ent.label_, "text": ent.text} for ent in doc.ents]
    return entities
