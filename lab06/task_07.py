from fastapi import FastAPI

app = FastAPI()


@app.get("/api/status")
def status():
    return {"status": "ok", "laboratory": 6, "variant": 2}
