#!/usr/bin/python3
from typing import Union, List
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")   

class State(BaseModel):
    name: str
    capital: str
    population: int
    nickname: str
    governor: str
    deputy: str
    id: int
    LGA: List[str] 
 
states_data = [
    State(id=1, name="Lagos", capital="Ikeja", population=14600000, nickname="Centre of Excellence", governor="Babajide Sanwo-Olu", deputy="Femi Hamzat", LGA=["Ikeja", "Alimosho", "Eti-Osa", "Surulere", "Mushin"]),
    State(id=2, name="Kano", capital="Kano", population=13400000, nickname="Centre of Commerce", governor="Abdullahi Ganduje", deputy="Nasiru Gawuna", LGA=["Fagge", "Dala", "Nasarawa", "Gwale", "Kumbotso"]),
    State(id=3, name="Kaduna", capital="Kaduna", population=9500000, nickname="Centre of Learning", governor="Nasir El-Rufai", deputy="Hadiza Balarabe", LGA=["Chikun", "Giwa", "Igabi", "Kaduna North", "Kaduna South"]),
    State(id=4, name="Rivers", capital="Port Harcourt", population=8000000, nickname="Treasure Base", governor="Nyesom Wike", deputy="Ipalibo Banigo", LGA=["Obio-Akpor", "Eleme", "Ikwerre", "Okrika", "Oyigbo"]),
    State(id=5, name="Oyo", capital="Ibadan", population=7800000, nickname="Pace Setter State", governor="Seyi Makinde", deputy="Rauf Olaniyan", LGA=["Ibadan North", "Ibadan South-West", "Oyo East", "Afijio", "Ogbomosho North"]),
    State(id=6, name="Katsina", capital="Katsina", population=7600000, nickname="Home of Hospitality", governor="Aminu Masari", deputy="Mannir Yakubu", LGA=["Bakori", "Batagarawa", "Batsari", "Danja", "Dutsin-Ma"]),
    State(id=7, name="Bauchi", capital="Bauchi", population=6900000, nickname="Pearl of Tourism", governor="Bala Mohammed", deputy="Baba Tela", LGA=["Bauchi", "Bogoro", "Darazo", "Dass", "Ganjuwa"]),
    State(id=8, name="Anambra", capital="Awka", population=6300000, nickname="Light of the Nation", governor="Willie Obiano", deputy="Nkem Okeke", LGA=["Awka North", "Awka South", "Anambra East", "Anambra West", "Anaocha"]),
    State(id=9, name="Jigawa", capital="Dutse", population=5800000, nickname="New World", governor="Muhammad Badaru", deputy="Umar Namadi", LGA=["Auyo", "Babura", "Biriniwa", "Birnin Kudu", "Buji"]),
    State(id=10, name="Benue", capital="Makurdi", population=5700000, nickname="Food Basket of the Nation", governor="Samuel Ortom", deputy="Benson Abounu", LGA=["Gboko", "Guma", "Gwer East", "Gwer West", "Katsina-Ala"]),
]

def find_state(id):
    for state in states_data:
        #if str(state["id"]) == id:
        if state.id == id:
            return state

def find_index_state(id):
    """
    Get the index of a state that corresponds to id
    """
    for i, p in enumerate(states_data):
        if p['id'] == id:
            return i

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    """
    Returns the index page for the API
    """
    # return "Welcome to Nigeria States Information API!"
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/states")
def get_states():
    """
    Get the list of all states in the API
    """
    return {"data": my_states}

@app.get("/states/{id}")
def get_state(id: int):
    """
    Get a state that corresponds to the index
    """
    state = find_state(id)
    if not state: # Raise 404 exception if state not found
        raise HTTPException(status_code=404, detail=f"state with id: {id} was not found")
    return {"state": state}

@app.delete("/states/{id}", status_code=204)
def delete_state(id: int):
    """
    Delete a state that corresponds to the index
    """
    index = find_index_state(id)

    if index == None:
        raise HTTPException(status_code=404, detail=f"state with id: {id} was not found")

    my_states.pop(index)
    return Response(status_code=204)

@app.put("/states/{id}")
def update_state(id: int, state: State):
    """
    Update a state that corresponds to the index
    """
    index = find_index_state(id)

    if index == None:
        raise HTTPException(status_code=404, detail=f"state with id: {id} was not found")
    state_dict = state.dict() # Store the state as a dict
    state_dict['id'] = id # Update the state id
    my_states[index] = state_dict # Overwrite the state
    return {'message': "updated state"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
