from fastapi import FastAPI
from .routes import todos

app = FastAPI(title="Simple FastAPI App")

# App Routes

# index route
@app.get("/", tags=["base"])
async def index() -> dict:
    return {"hello": "world"}


# Register other routes
app.include_router(todos.router)