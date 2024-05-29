from fastapi import FastAPI
from routes.editora import editoraRouter
from routes.autor import autorRouter
import uvicorn

app = FastAPI()

app.include_router(editoraRouter,prefix="/editora")
app.include_router(autorRouter,prefix="/autor")

@app.get("/")
def hello():
    return {"msg": "Hello", "docs": "http://localhost:8080/docs"}


uvicorn.run(app,port=8080)