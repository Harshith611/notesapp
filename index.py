from fastapi import FastAPI
from routes.note import note
from fastapi.staticfiles import StaticFiles

app=FastAPI()
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(note)