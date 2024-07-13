from typing import Annotated
from fastapi import Body, Depends, FastAPI
from pydantic import BaseModel


app = FastAPI()


class createPostIn(BaseModel):
    title: str
    content: str
    rate: int


@app.get("/")
async def root():
    return {"message": "hello world"}


@app.get("/blog/{slug}")
async def blog(slug: int):
    return {"message": slug}


@app.get("/blog/{slug}")
async def blogPrivate(slug: int, is_private: bool = False):
    return {"message": slug}


@app.post("/blog/create")
async def blogCreate(post: createPostIn):
    return post


# Dependency Injection in fastAPI
# q: Union[str, None] = None
async def help_params(q: str | None = None, limit: int = 20):
    return {"query": q, "limitQuery": limit}


@app.get("/items")
async def reade_items(allItems: Annotated[dict, Depends(help_params)]):
    return allItems
