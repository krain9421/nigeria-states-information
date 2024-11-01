# Nigerian States Information API
##Overview
The Nigerian States Information API is a RESTful service designed to provide detailed information about the 36 states in Nigeria. This API provides information about state capitals, populations, nicknames, governors, deputies, and local government areas (LGAs). The purpose is to create an accessible way to retrieve data on Nigerian states for educational and informational use.

##Table of Contents
Features
Technologies
Project Structure
Installation
Usage
API Endpoints
Future Improvements
Contributors
##Features
Get All States: Retrieve a list of all 36 Nigerian states and their details.
Get State by ID: Retrieve specific state information by using a unique ID.
HTML Home Page: A static HTML page provides information about the API.
Database Integration: Connects to a MongoDB database for data storage and retrieval.
Scalability: Designed for handling multiple requests and scaling efficiently.
##Technologies
Python: Core language for development.
FastAPI: Framework for creating and managing API routes.
MongoDB: Database to store Nigerian state information.
HTML/CSS: Basic static page for API information.
NGINX: Web server used for production deployment.
##Project Structure
The project directory is organized as follows:


nigeria-states-information/
├── app/
│   ├── __init__.py
│   ├── main.py                # Main entry point
│   ├── models/
│   │   └── state.py           # MongoDB schema for states
│   ├── routes/
│   │   └── states.py          # Route handling for states
│   └── controllers/
│       └── stateController.py # Logic for state operations
├── static/
│   └── styles.css             # HTML page styles
├── templates/
│   └── index.html             # Home page template
├── README.md                  # Project documentation
└── .venv/                     # Python virtual environment
##Installation
Prerequisites
Python 3.8 or above
MongoDB
Git
Steps
Clone the Repository:

bash
git clone https://github.com/krain9421/nigeria-states-information.git
cd nigeria-states-information
Set Up a Virtual Environment:

bash
python3 -m venv .venv
source .venv/bin/activate
Install Required Packages:

bash
pip install -r requirements.txt
Configure Database Connection: Make sure MongoDB is running and update connection settings in app/main.py.

Run the Application:

bash
uvicorn app.main:app --reload
Access the API: Open http://127.0.0.1:8000 in your browser or API client.

##Usage
With the server running, use Postman or curl to interact with the API. Access the static HTML page at http://127.0.0.1:8000/ for available endpoints.

##API Endpoints
Get All States
Endpoint: /states
Method: GET
Description: Lists all 36 Nigerian states and their details.
Get State by ID
Endpoint: /states/{id}
Method: GET
##Parameters:
id (integer): ID of the state to retrieve.
Description: Fetches specific state information based on ID.
Example JSON Response
json
{
  "id": 1,
  "name": "Lagos",
  "capital": "Ikeja",
  "population": 13900000,
  "nickname": "Centre of Excellence",
  "governor": "Babajide Sanwo-Olu",
  "deputy": "Femi Hamzat",
  "LGA": ["Agege", "Ajeromi-Ifelodun", "Alimosho", "Amuwo-Odofin", "Apapa"]
}
##Future Improvements
Database Expansion: Add more data sources to enrich state information.
Frontend Interface: Develop a more interactive and responsive frontend.
API Documentation: Use Swagger or ReDoc for documentation.
Caching: Integrate Redis caching for improved performance.
##Contributors
@krain9421 - CHIDUBEM NWIGWE
@Ipinsokansunday - Sunday Ipinsokan
   git clone https://github.com/krain9421/nigeria-states-information.git
   cd naijastates-api
