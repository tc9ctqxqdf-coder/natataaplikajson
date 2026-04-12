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
notes = {}#dette er en tom liste for den andre todos tabelen

with open('todos.json', 'r', encoding='utf-8') as file: # vi åpner filen (todos.json) leser av den("r") ((Støtter norsk bokstav)) gir filen et navn som er "file"
        todos = json.load(file)#så første vi ser er at todos er variablen og vi har puttet noe i den. lenger opp er todos en tom liste nå putter vi noe i den. Så gjør vi filen om til payton data slik at payton kan lese va den.(filen er det navnet vi ga (todos.json))

with open('notes.json', 'r', encoding='utf-8') as file:
        notes = json.load(file)

@app.get("/")#Når noen besøker dene netsiden av URL og skriver samtidig / gjøres denne funksjonen.
def home():#funksjone som heter "home".
    return {"message": "Hello, API!"}#retunerer en meldingn når siden er besøkt

#Returnerer alle todos
@app.get("/todos")##så er det ny URL vis noen besøker netsiden og dereter skrier "/todos" så kjøres denne funksjonen
def get_todos(): #funksjone med et navn "get_todos"
    return todos #retunerer(tilbake) todos (todos er listen lenger opp og den har fått en file som heter "file")

#Returnerer alle todos fra notes file
@app.get("/notes")##så er det ny URL vis noen besøker netsiden og dereter skrier "/todos" så kjøres denne funksjonen
def get_todos(): #funksjone med et navn "get_todos"
    return notes #retunerer(tilbake) todos (todos er listen lenger opp og den har fått en file som heter "file")

#Returnerer 1 todo basert på /id
@app.get("/todos/{id}") # når noen skriver URL pluss "/todos/" også et tall bak som er "id" så vil den kjøre dette
def get_todos(id: int):# funksjon som heter "get_todos" sier den at når "id" må være et tall (int)
    #print(todos["tasks"][0]) # et eksempel her er bestemt at den pronter noe fra todos som er tasks rad 0.
    return todos["tasks"][id] # retunerer lista (todos av oppgvae(tasks)) fra "id" du valkte

#Returnerer 1 todo basert på /id fra notes file
@app.get("/notes/{id}") # når noen skriver URL pluss "/todos/" også et tall bak som er "id" så vil den kjøre dette
def get_todos(id: int):# funksjon som heter "get_todos" sier den at når "id" må være et tall (int)
    return notes["notes"][id] # retunerer lista (todos av oppgvae(tasks)) fra "id" du valkte

class Item(BaseModel):
    todo: str

#dette er prosesen når oppgaver blir lakt til i databasen i todos.json
@app.post("/newtodo") # i denne URL så når noen skriver så kjer dette.
async def create_item(item: Item): # lager en funksjon som tar imot data fra brukeren
    with open("todos.json", "r") as file: #åpner filen "todos.json" og leser den
        data = json.load(file) # oversetter filen til ikk  (json)

    new_task = { #legger til ny oppgave
        "text": item.todo, # henter teksten fra brukeren (item: Item)
        "done": False #sett oppgaven til (False)
    }

    data["tasks"].append(new_task) #går inn i listen og legger den til en ny task og 

    with open("todos.json", "w", encoding="utf-8") as file: # åpner  filen (todos.json) og leser den oversetter.  
        json.dump(data, file, indent=4, ensure_ascii=False) 

    return {"message": "Task lagt til!", "task": new_task} # retunerer tasken inn i new_task som brukeren la til 


@app.post("/newnote") # i denne URL så når noen skriver så kjer dette.
async def create_item(item: Item): # lager en funksjon som tar imot data fra brukeren
    with open("notes.json", "r") as file: #åpner filen "todos.json" og leser den
        data = json.load(file) # oversetter filen til ikk  (json)

    new_note = { #legger til ny oppgave
        "title": item.todo, # henter teksten fra brukeren (item: Item)
        "content": "Dette er en test" #sett oppgaven til (False)
    }

    data["notes"].append(new_note) #går inn i listen og legger den til en ny task  

    with open("notes.json", "w", encoding="utf-8") as file: # åpner  filen (todos.json) og leser den oversetter. og 
        json.dump(data, file, indent=4, ensure_ascii=False)

    return {"message": "Task lagt til!", "task": new_note} # retunerer tasken inn i new_task som brukeren la til 




@app.delete("/delete/{id}") # en URL som venter til delite kommer inn
async def slett_element ( id: int ): # funksjon som tar inn heltall
     with open("todos.json", "r") as file: # åpner to (todos.json) filen 
        todos = json.load(file) #leser filen
        del todos["tasks"][id] #(del betyr å seltte) sletter elemtentet i task basert på id plassering

     with open("todos.json", "w", encoding="utf-8") as file: # åpner filen for skrivering "w" 
          json.dump(todos, file, indent=2) # oppdaterer daaen(todos) i filen 
          
    
