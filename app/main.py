from fastapi import FastAPI
from app.routers import auth
from app.routers import pg

app = FastAPI()
app.include_router(auth.router)
app.include_router(pg.router)


@app.get("/")
def roo():
  return {"message": "Hello"}

