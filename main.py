from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/do_thing")
async def do_thing():
    await asyncio.sleep(5)
    return {"message": "A thing was done! Back at ya..."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
