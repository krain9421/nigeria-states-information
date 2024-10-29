#!/usr/bin/python3
from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()
    

class State(BaseModel):
    name: str
    capital: str
    population: int
    nickname: str
    governor: str
    deputy: str
    LGA: list

my_states = [
            {
         "name": "Lagos",
         "id": 1,
         "capital": "Ikeja",
         "population": 35000000,
         "nickname": "Centre of Excellence",
         "governor": "Babajide Sanwo-Olu",
         "deputy": "Femi Hamzat"
    },
    {    "name": "Ogun",
         "id": 2,
         "capital": "Abeokuta",
         "population": 6379500,
         "nickname": "Gateway State",
         "governor": "Dapo Abiodun",
         "deputy": "Noimot Salako-Oyedele"
    },
    {
        "name": "Kano",
        "id": 3,
        "capital": "Kano",
        "population": 13740000,
        "nickname": "Center of Commerce",
        "governor": "Abdullahi Umar Ganduje",
        "deputy": "Nasiru Yusuf Gawuna"
    },
    {
        "name": "Kaduna",
        "id": 4,
        "capital": "Kaduna",
        "population": 8272000,
        "nickname": "Centre of Learning",
        "governor": "Nasir Ahmad el-Rufai",
        "deputy": "Hadiza Sabuwa Balarabe"
    },
    {
        "name": "Oyo",
        "id": 5,
        "capital": "Ibadan",
        "population": 7810000,
        "nickname": "Pace Setter State",
        "governor": "Seyi Makinde",
        "deputy": "Rauf Olaniyan"
    },
    {
        "name": "Rivers",
        "id": 6,
        "capital": "Port Harcourt",
        "population": 7395000,
        "nickname": "Treasure Base of the Nation",
        "governor": "Nyesom Wike",
        "deputy": "Ipalibo Banigo"
    },
    {
        "name": "Katsina",
        "id": 7,
        "capital": "Katsina",
        "population": 6611000,
        "nickname": "Home of Hospitality",
        "governor": "Aminu Bello Masari",
        "deputy": "Mannir Yakubu"
    },
    {
        "name": "Bauchi",
        "id": 8,
        "capital": "Bauchi",
        "population": 6537000,
        "nickname": "Pearl of Tourism",
        "governor": "Bala Mohammed",
        "deputy": "Baba Tela"
    },
    {
        "name": "Anambra",
        "id": 9,
        "capital": "Awka",
        "population": 5612000,
        "nickname": "Light of the Nation",
        "governor": "Willie Obiano",
        "deputy": "Nkem Okeke"
    },
    {
        "name": "Jigawa",
        "id": 10,
        "capital": "Dutse",
        "population": 5442000,
        "nickname": "The New World",
        "governor": "Muhammad Badaru Abubakar",
        "deputy": "Umar Namadi"
    },
    {
        "name": "Benue",
        "id": 11,
        "capital": "Makurdi",
        "population": 5316000,
        "nickname": "Food Basket of the Nation",
        "governor": "Samuel Ortom",
        "deputy": "Benson Abounu"
    }
    ]

def find_state(id):
    for state in my_states:
        if str(state["id"]) == id:
            return state

@app.get("/")
def read_root():
    return "Welcome to Nigeria States Information API!"

@app.get("/states")
def get_states():
    """
    Get the list of all states in the API
    """
    return {"data": my_states}

@app.get("/states/{id}")
def get_state(id):
    """
    Get a state based on the id
    """
    state = find_state(id)
    return {"state": state}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
