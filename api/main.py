from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def Test():
    return "Test Deploy Vercel"