# backend/utils.py
import re

def clean_text(text: str) -> str:
    """Remove extra whitespace and clean up text."""
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def read_text_from_txt(file_bytes: bytes) -> str:
    """Read text content from uploaded .txt file."""
    return file_bytes.decode("utf-8", errors="ignore")
