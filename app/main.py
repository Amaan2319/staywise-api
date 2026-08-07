from fastapi import FastAPI
from app.routers.auth import router

app = FastAPI()

@app.get("/")
def roo():
  return {"message": "Hello"}

