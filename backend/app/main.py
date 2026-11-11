from fastapi import FastAPI
from database.status import router as status_router

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Olá do FastAPI"
    }

app.include_router(status_router)