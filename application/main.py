import math
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return "Hello World"

@app.get("/twice/{number}")
def return_square_twice(number:int):
    return get_square(number) + get_square(number)

def get_square(number:int):
    return math.floor(math.pow(number, 2))