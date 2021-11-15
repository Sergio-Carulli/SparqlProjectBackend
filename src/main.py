from fastapi import FastAPI

import json
from typing import Optional
from SPARQLWrapper import SPARQLWrapper, JSON

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Sparql"}


# From all study room, get name, road_name, number, postal_code. 
@app.get("/studies_room")
def read_study_rooms():

    sparql = SPARQLWrapper("http://localhost:9000/sparql")
    sparql.setQuery("""
        PREFIX rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
        PREFIX rdfs: http://www.w3.org/2000/01/rdf-schema#
        SELECT * WHERE {
            ?sub ?pred ?obj .
        } 
        limit 10
        """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    results_json = json.dumps(results, indent = 4)

    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print(results_json)

    return results_json


