from fastapi import FastAPI
from app.routers import auth

app = FastAPI()
app.include_router(auth.router)
@app.get("/")
def roo():
  return {"message": "Hello"}

