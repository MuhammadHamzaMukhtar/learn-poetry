# Hello World with fastapi
1. `poetry new fastapi_helloworld_online`
2. `cd fastapi_helloworld_online`
3. Select your project with VSCode
4. open file `pyproject.toml`
```
[tool.poetry]
name = "project-1"
version = "0.1.0"
description = ""
authors = ["sumra <sumrakhalidev@gmail.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.12"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```
5. install new packages in poetry project
    `poetry add fastapi "uvicorn[standard]"`

```
[tool.poetry.dependencies]
python = "^3.12"
fastapi = "^0.111.0"
uvicorn = {extras = ["standard"], version = "^0.290"}
```
6. create `main.py` location `project_1\main.py`

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello, World!"}

@app.get("/piaic/")
def piaic():
    return {"organization": "Welcome to PIAIC!"}
```

7. run server
`poetry run uvicorn project_1_fastapi_helloworld.main:app --reload`
