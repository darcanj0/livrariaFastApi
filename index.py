from fastapi import FastAPI
from routes.editora import editoraRouter
import uvicorn

app = FastAPI()

@app.get("/")
def hello():
    return {"msg": "Hello", "docs": "http://localhost:8080/docs"}

app.include_router(editoraRouter)

uvicorn.run(app,port=8080)