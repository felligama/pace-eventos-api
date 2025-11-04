from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI(title="Pace Eventos API")

# Permitir acesso de qualquer origem (para o app mobile funcionar)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Função para carregar o arquivo JSON
def load_events():
    with open("events_corridasbr.json", "r", encoding="utf-8") as f:
        return json.load(f)

# Rota principal (teste rápido)
@app.get("/")
def home():
    return {"message": "API Pace Eventos funcionando!"}

# Rota principal de eventos
@app.get("/api/events")
def get_events(city: str | None = Query(default=None)):
    events = load_events()
    if city:
        events = [e for e in events if city.lower() in e["city"].lower()]
    return events
