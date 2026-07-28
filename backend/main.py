from fastapi import FastAPI
# from database.status import router as status_router

app = FastAPI()

# app.include_router(status_router)

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/hello")
def hello():
    return {
        "message": "Olá do FastAPI"
    }