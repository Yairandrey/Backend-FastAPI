from fastapi import FastAPI
# Inicio el servidor uvicorn main:app --reload
app = FastAPI()

@app.get("/root")
async def root():
    return "Estoy aprendiendo FastAPI"

@app.get("/saludo")
async def saludo():
    return f'Hola, bienvenido'