import json 
from fastapi import FastAPI #henter Fastapi fra bibloteket
from fastapi import Request


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

#lurt å sjekke om det jeg har komentert er riktig.
@app.post("/todos") # lager en ny post på todos men noe annet
async def vreat_todo(request: Request): #henter data fra bruker 
    data = await reqest.json() #leser data fra bruker

    todos = loas_todos()
    new_id = 1 if not todos else todos[-1]["id"] + 1

    new_dodo = {
        "id": nww_id,
        "title": data["title"],
        "tasks": data["tasks"] 
    }