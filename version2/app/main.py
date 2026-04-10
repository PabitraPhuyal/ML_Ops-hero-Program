from fastapi import FastAPI, UploadFile, File, HTTPException, Response
import pandas as pd
from io import BytesIO
from .cleaning import clean_df

app = FastAPI(title="Data Cleaner")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/clean")
async def clean(file: UploadFile = File(...)):
    if not file.filename or not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Please upload a CSV file.")
    contents = await file.read()
    try:
        df = pd.read_csv(BytesIO(contents))
        cleaned = clean_df(df)
        # Return CSV
        csv_bytes = cleaned.to_csv(index=False).encode("utf-8")
        return Response(content=csv_bytes, media_type="text/csv")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to clean CSV: {e}")
