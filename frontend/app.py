# frontend/streamlit_app.py
import streamlit as st
import requests

API_BASE = "http://localhost:8000/api"

st.set_page_config(page_title="Entity Extractor", layout="centered")
st.title("🧠 Entity Extractor (spaCy Model)")

tab1, tab2 = st.tabs(["Text Input", "File Upload"])

# --- Tab 1: Text ---
with tab1:
    st.header("Extract Entities from Text")
    text = st.text_area("Paste your text below", height=200)

    if st.button("Extract from Text"):
        if not text.strip():
            st.warning("Please enter some text.")
        else:
            with st.spinner("Extracting entities..."):
                resp = requests.post(f"{API_BASE}/extract-text", json={"text": text})
                if resp.ok:
                    data = resp.json()
                    st.success("Entities found:")
                    for ent in data["entities"]:
                        st.markdown(f"**{ent['label']}** → {ent['text']}")
                else:
                    st.error(f"Error: {resp.text}")

# --- Tab 2: File ---
with tab2:
    st.header("Extract Entities from File (.txt)")
    uploaded = st.file_uploader("Upload a .txt file", type=["txt"])
    if uploaded:
        if st.button("Extract from File"):
            with st.spinner("Processing file..."):
                files = {"file": (uploaded.name, uploaded.getvalue())}
                resp = requests.post(f"{API_BASE}/extract-file", files=files)
                if resp.ok:
                    data = resp.json()
                    st.success(f"Entities found in {uploaded.name}:")
                    for ent in data["entities"]:
                        st.markdown(f"**{ent['label']}** → {ent['text']}")
                else:
                    st.error(f"Error: {resp.text}")
