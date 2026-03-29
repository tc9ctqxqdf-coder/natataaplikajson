#app er Fast appi vi har byttet fast apien som vi henter fra from fastapi og legger den i en variabel. slik kan vi bruke den

from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
import json #henter (json) som brukes til å lese data fra filer
from pydantic import BaseModel

app = FastAPI()

# Til Theo: Ignorer kodesnutten under. Den er utenfor pensum. 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)
# Ignorer kodesnutten over. Den er utenfor pensum. 

todos = {}#todos er tom liste akurat nå

with open('todos.json', 'r', encoding='utf-8') as file: # vi åpner filen (todos.json) leser av den("r") ((Støtter norsk bokstav)) gir filen et navn som er "file"
        # Use json.load() to parse the file content into a Python object (usually a dictionary or list)
        todos = json.load(file)#så første vi ser er at todos er variablen og vi har puttet noe i den. lenger opp er todos en tom liste nå putter vi noe i den. Så gjør vi filen om til payton data slik at payton kan lese va den.(filen er det navnet vi ga (todos.json))

@app.get("/")#Når noen besøker dene netsiden av URL og skriver samtidig / gjøres denne funksjonen.
def home():#funksjone som heter "home".
    return {"message": "Hello, API!"}#retunerer en meldingn når siden er besøkt

#Returnerer alle todos
@app.get("/todos")##så er det ny URL vis noen besøker netsiden og dereter skrier "/todos" så kjøres denne funksjonen
def get_todos(): #funksjone med et navn "get_todos"
    return todos #retunerer(tilbake) todos (todos er listen lenger opp og den har fått en file som heter "file")

#Returnerer 1 todo basert på /id
@app.get("/todos/{id}") # når noen skriver URL pluss "/todos/" også et tall bak som er "id" så vil den kjøre dette
def get_todos(id: int):# funksjon som heter "get_todos" sier den at når "id" må være et tall (int)
    #print(todos["tasks"][0]) # et eksempel her er bestemt at den pronter noe fra todos som er tasks rad 0.
    return todos["tasks"][id] # retunerer lista (todos av oppgvae(tasks)) fra "id" du valkte

class Item(BaseModel):
    todo: str


@app.post("/newtodo/")
async def create_item(item: Item):
    # Les eksisterende data
    with open("todos.json", "r") as file:
        data = json.load(file)

    # Lag ny task
    new_task = {
        "text": item.todo,
        "done": False
    }

    # Legg til i tasks-lista
    data["tasks"].append(new_task)

    # Skriv tilbake til fila
    with open("todos.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    return {"message": "Task lagt til!", "task": new_task}



