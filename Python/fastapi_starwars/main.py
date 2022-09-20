# this is a sample API built with FastAPI, performing crud operations on a sample sqllite database representing the star wars universe

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health")
async def health():
    return {"status": "ok"}

# endpoint with path parameters
@app.get("/characters/{character_id}")
async def get_character(character_id: int):
    return {"character_id": character_id}

@app.get("/characters/{character_id}/movies")