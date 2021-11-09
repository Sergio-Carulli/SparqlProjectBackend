from fastapi import FastAPI

from typing import Optional

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Sparql"}


@app.get("/names")
def read_names():
    return [{"student1": "Gorka"},
        {"student2": "Celia"},
        {"student3": "Luis"},
        {"student4": "Sergio"}]

