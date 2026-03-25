from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
app = FastAPI()

# Til Theo: Ignorer kodesnutten under. Den er utenfor pensum. 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)
# Ignorer kodesnutten over. Den er utenfor pensum. 

todos = {}
with open('todos.json', 'r', encoding='utf-8') as file:
        # Use json.load() to parse the file content into a Python object (usually a dictionary or list)
        todos = json.load(file) 

@app.get("/")
def home():
    return {"message": "Hello, API!"}

#Returnerer alle todos
@app.get("/todos")
def get_todos():
    return todos

#Returnerer 1 todo basert på /id
@app.get("/todos/{id}")
def get_todos(id: int):
    #print(todos["tasks"][0])
    return todos["tasks"][id]