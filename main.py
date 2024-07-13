from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello world"}


@app.get("/blog/{slug}")
async def blog(slug: int):
    return {"message": slug}


