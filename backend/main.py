from fastapi import FastAPI
from routers import auth, entradas

app = FastAPI(title="Diario Emocional")

app.include_router(auth.router)
app.include_router(entradas.router)


@app.get("/")
def raiz():
    return {"mensaje": "El diario emocional esta vivo"}