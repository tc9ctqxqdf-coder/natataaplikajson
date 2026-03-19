import json 
from fastapi import FastAPI #henter Fastapi fra bibloteket


app = FastAPI() # lager navn på surveren

@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}

def load_todos():
    with open("todos.json", "r") as file:
        return json.load(file) # gjøt file om til pyton data

def save_todos(todos):#jeg gir denne funksjonen navn og samt hentet data todos froa funksjonen over
    with open("todos.json", "w") as file:
        json.dump(todos, file, indent=4)

#forsto ikke denne koden?
@app.get("/todos")
def get_todos():
    return load_todos()