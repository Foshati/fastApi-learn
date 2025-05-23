from fastapi import FastAPI , Path,Query
from pydantic import BaseModel


app = FastAPI()


class Person(BaseModel):
    name: str
    age: int = Path(description="user age between 0 and 100", ge=0, le=20)
    height: int | None = 160


@app.get("/")
def root():
    return {"message": "hello world"}


@app.get("/home/{name}/{age}")
def info(name: str, age: int):
    return {"message": f"{name} is {age} years old"}


@app.get("/home/{name}")
def info_filter(name: str, age: int = 10):
    return {"message": f"{name} is {age} years old"}


@app.post("/home/person")
async def person(prs):
    return prs




@app.post("/home/car")
async def personCar(prs:Person, car:str=Query(default="nothing",min_length=2 ,max_length=20)):
    return prs, car