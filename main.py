from fastapi  import FastAPI

app = FastAPI()


@app.get("/greet")
def greet():
    return "Welcome to My app"

@app.get("/health")
def health():
    return "Good health"