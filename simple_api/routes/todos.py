from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/todos", tags=["todos"])


# List of ToDos
todos = [
    {"id": 0, "description": "Get better at python"},
    {"id": 1, "description": "Develop 2 flutter apps"},
    {"id": 2, "description": "Updated dart package "},
]

# List all todos
@router.get("/")
async def index() -> dict:
    return {"data": todos}


# Create a new todo
@router.post("/", status_code=201)
async def create(data: dict) -> dict:

    if data is not None:
        todo = {
            "id": len(todos),
            "description": data["description"],
        }

        todos.append(todo)

        return {"data": todo}

    raise HTTPException(
        422,
        detail="A description is required",
    )


# Get a single todo item
@router.get("/{id}")
async def todo(id: int):

    for todo in todos:
        if todo["id"] == id:
            return {"todo": todo}

    raise HTTPException(
        404,
        detail=f"Task not found. Invalid id {id}",
    )


# Update a todo
@router.patch("/{id}")
async def update(id: int, data: dict):

    for todo in todos:
        if todo["id"] == id:
            todo["description"] = data["description"]

            return {"todo": todo}

    raise HTTPException(
        404,
        detail=f"Task not found. Invalid id {id}",
    )

# Delete a todo
@router.delete('/{id}')
async def destroy(id: int):
    for todo in todos:
        if todo["id"] == id:
            todos.remove(todo)

            return {"message": "Deleted successfully"}

    raise HTTPException(
        404,
        detail=f"Task not found. Invalid id {id}",
    )