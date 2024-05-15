from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello, World!"}

@app.get("/piaic/")
def piaic():
    return {"organization": "Welcome to PIAIC!"}