# src/hnh/main.py

import random
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.templating import Jinja2Templates
from transformers import pipeline
from PIL import Image
import numpy as np
import io

from src.hnh.util import summary

app = FastAPI()
model_name = "julien-c/hotdog-not-hotdog"
#html = Jinja2Templates(directory="pbulic")

@app.get("/hello")
def read_root():
    return { "Hello": "World!" }

@app.post("/predict/")
async def hotdog(file: UploadFile):
    try:
        img = await file.read()
        model = pipeline("image-classification", model=model_name)
        img = Image.open(io.BytesIO(img))

        pred = model(img)
        return summary(file.filename, pred)
        #return { "filename": file.filename, "This seems to be...": pred }

    except Exception as e:
        return { "error": str(e) }

