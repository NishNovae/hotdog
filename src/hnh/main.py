# src/hnh/main.py

import random
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.get("/")
def read_root():
    return { "Hello": "World!" }

@app.get("/hotdog")
def is_hotdog():
    # dummy!
    hotdog = random.choice(["True", "False"])

    return { "is_dummy_code": "True", "hotdog?": hotdog }
