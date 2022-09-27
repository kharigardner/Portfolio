# this is a sample API built with FastAPI, performing crud operations on a sample sqllite database representing the star wars universe

from fastapi import FastAPI
from db import db_session
from models import Character
from crud import *

app = FastAPI(
    title="Star Wars API",
    description="This is a sample API built with FastAPI, performing crud operations on a sample sqllite database representing the star wars universe",
    version="0.1.0",
)
#TODO: add more description and settings to the API initialization


@app.get("/")
async def root():
    return {"message": "Hello! This is a sample API built with FastAPI, performing crud operations on a sample sqllite database representing the star wars universe"}

@app.get("/health")
async def health():
    return {"status": "ok"}

# endpoint with path parameters
@app.post("/character", response_model=Character)
async def create_character(character: Character):
    try:
        db_session.add(character)
        return "{message: 'character created'}"
    except:
        return "{message: 'character creation failed'}"
#TODO: define the exception and return more standardized json response
