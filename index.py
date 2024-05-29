from fastapi import FastAPI
from routes.editora import editoraRouter
from routes.autor import autorRouter
from routes.livro import livroRouter
import uvicorn

app = FastAPI(openapi_tags=[{"name": "livro"},{"name": "autor"},{"name":"editora"}])
app.include_router(editoraRouter,prefix="/editora",tags=["editora"])
app.include_router(autorRouter,prefix="/autor",tags=["autor"])
app.include_router(livroRouter,prefix="/livro", tags=["livro"])

@app.get("/")
def hello():
    return {"msg": "Hello", "docs": "http://localhost:8080/docs"}


uvicorn.run(app,port=8080)