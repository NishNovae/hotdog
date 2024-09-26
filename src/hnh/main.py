# src/hnh/main.py

import random
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/")
def read_root():
    return { "Hello": "World!" }

@app.post("/hotdog")
def is_hotdog():
    # dummy!
    hotdog = random.choice(["True", "False"])
    return { "dummy": "code", "hotdog": hotdog }
