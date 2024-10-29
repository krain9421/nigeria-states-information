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
            {
                "name": "Ogun",
                "id": 2,
                "capital": "Abeokuta",
                "population": 6379500,
                "nickname": "Gateway State",
                "governor": "Dapo Abiodun",
                "deputy": "Noimot Salako-Oyedele"
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
