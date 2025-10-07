# 🧠 SpaCy Entity Extractor

A Python app for extracting entities from text using a pre-trained spaCy NER model.
Includes a **Streamlit frontend** and **FastAPI backend** for easy use.

---

## Features

* Extract entities like `Counterparty`, `Notional`, `ISIN`, `Maturity`, `Underlying`, `Bid`, `PaymentFrequency`, etc.
* Accepts **text input** or **.txt file upload**
* User-friendly interface via Streamlit
* Run backend and frontend with **one command** for non-technical users

---

## Project Structure

```
ChatDataApp/
├─ backend/
│  ├─ main.py
│  ├─ service.py
│  └─ utils.py
├─ frontend/
│  └─ streamlit_app.py
├─ requirements.txt
```

---

## Installation

```bash
git clone <repo-url>
cd entity_extractor_app
pip install -r requirements.txt
```

---

## Running the App

```bash
python run_app.py
```

* Streamlit UI opens automatically at `http://localhost:8501`
* FastAPI backend runs at `http://localhost:8000`

---

## Usage

* **Text Input:** Paste text → Extract Entities
* **File Upload:** Upload `.txt` → Extract Entities

---

## Notes

* Uses pre-trained spaCy model stored in `entity_extractor_model/`
* Training is not required for end users

---

## License

MIT License

---

If you want, I can also make an **even shorter 10–15 line version** that’s ultra-minimal for GitHub repos.
Do you want me to do that?
