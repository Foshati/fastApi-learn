from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root():
    return {"message": "hello world"}



@app.get("/home/{name}/{age}")
def info(name: str, age :int):
    return {"message" : f"{name} is {age} old" }