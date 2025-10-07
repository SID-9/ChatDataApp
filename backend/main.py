from fastapi import FastAPI, UploadFile, File,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .utils import read_text_from_txt
from .service import extract_entities

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# to extract directly from text input
class TextRequest(BaseModel):
    text: str

@app.post("/api/extract-text")
async def extract_from_text(req: TextRequest):
    try:
        result = extract_entities(req.text)
        return {"entities": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# to extract from a txt file
@app.post("/api/extract-file")
async def chat_document(file: UploadFile = File(...)):
    try:
        if not file.filename.endswith(".txt"):
            raise HTTPException(status_code=400, detail="Only .txt files supported")
        
        contents = await file.read()
        text = read_text_from_txt(contents)
        if text:
            entities = extract_entities(text)
            return {"filename": file.filename, "entities": entities}
        else:
            raise HTTPException(status_code=400, detail="Empty file")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/healthz")
async def healthz():
    return {"status":"ok"}

    
