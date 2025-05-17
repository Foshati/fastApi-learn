from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root():
    return {"message": "hello world"}



@app.get("/home/{name}/{age}")
def info(name, age):
    return {"message" : f "{name} is {age} old" }