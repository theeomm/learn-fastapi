import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "simple_api.app:app",
        reload=True,
    )
