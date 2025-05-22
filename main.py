from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Person(BaseModel):
    name: str
    age: int
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
def person(prs: Person):
    return prs
