from fastapi import FastAPI
from routes.editora import editoraRouter
import uvicorn

app = FastAPI()

app.include_router(editoraRouter,prefix="/editora")

@app.get("/")
def hello():
    return {"msg": "Hello", "docs": "http://localhost:8080/docs"}


uvicorn.run(app,port=8080)