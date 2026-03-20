from fastapi import FastAPI #henter Fastapi fra bibloteket

app = FastAPI() # lager navn på surveren

json = {
id: 1,
"title": "Handleliste",
"tasks": [
    {"text": "Kjøpe melk", "done": False}, 
    {"text": "Kjøpe brød", "done": True},
    {"text": "Kjøpe ost", "done": True}
        ]
}

@app.get("/")
def home():
    return {"message": "Hello, Theo!"}