from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def roo():
  return {"message": "Hello"}