from fastapi import FastAPI

import json
from typing import Optional
from SPARQLWrapper import SPARQLWrapper, JSON
from fastapi.encoders import jsonable_encoder

app = FastAPI()

# From all study room, get name, road_name, number, postal_code. 
@app.get("/studies_room")
def read_study_rooms():

    sparql = SPARQLWrapper("http://localhost:9000/sparql")
    sparql.setQuery("""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX sr: <http://www.studyroomsmadrid.es/ns#>
        SELECT ?name ?roadType ?roadName ?number ?postalCode ?neighborhood ?district WHERE {
            ?x a sr:StudyRoom .
            ?x sr:hasName ?name .
            ?x sr:hasAddress ?y .
            ?y sr:hasRoadType ?roadType .
            ?y sr:hasRoadName ?roadName .
            ?y sr:hasNumber ?number .
            ?y sr:hasPostalCode ?postalCode .
            ?y sr:hasNeighborhood ?neighborhood .
            ?y sr:hasDistrict ?district
        }
    """)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    return results


