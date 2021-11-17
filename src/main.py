from fastapi import FastAPI

import json
from typing import Optional
from SPARQLWrapper import SPARQLWrapper, JSON
from fastapi.encoders import jsonable_encoder

app = FastAPI()

# From all study room, get name, road_name, number, postal_code, neighborhood and district. 
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

# From all study room, get name, schedule, description, content-url, telephone1, telephone2, telephone3.
# Description, telephone2 and telephone3 can be blank 
@app.get("/studies_room_query2")
def read_study_rooms_query2():

    sparql = SPARQLWrapper("http://localhost:9000/sparql")
    sparql.setQuery("""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX sr: <http://www.studyroomsmadrid.es/ns#>
        SELECT ?name ?schedule ?description ?contentUrl ?telephone1 ?telephone2 ?telephone3 WHERE {
            ?x a sr:StudyRoom .
            ?x sr:hasName ?name .
            ?x sr:hasSchedule ?schedule .
            OPTIONAL {?x sr:hasDescription ?description} .
            ?x sr:hasContentUrl ?contentUrl .
            ?x sr:hasTelephone1 ?telephone1 .
            OPTIONAL {?x sr:hasTelephone2 ?telephone2} .
            OPTIONAL {?x sr:hasTelephone3 ?telephone3} .
        }
    """)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    return results

# From all study room, get name, latitude, longitude. 
@app.get("/studies_room_query3")
def read_study_rooms_query3():

    sparql = SPARQLWrapper("http://localhost:9000/sparql")
    sparql.setQuery("""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX sr: <http://www.studyroomsmadrid.es/ns#>
        PREFIX wgs84_pos: <http://www.w3.org/2003/01/geo/wgs84_pos#>
        SELECT ?name ?lat ?lon WHERE {
            ?x a sr:StudyRoom .
            ?x sr:hasName ?name .
            ?x sr:isLocated ?z .
            ?z wgs84_pos:lat ?lat .
            ?z wgs84_pos:long ?lon .
        }
    """)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    return results

# Get name, schedule, description, content-url, telephone1, telephone2, telephone3 from study rooms with an specific postal code.
# Description, telephone2 and telephone3 can be blank 
@app.get("/studies_room_query4")
def read_study_rooms_query4():
    postal_code = "28024"
    sparql = SPARQLWrapper("http://localhost:9000/sparql")
    sparql.setQuery("""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX sr: <http://www.studyroomsmadrid.es/ns#>
        SELECT ?name ?schedule ?description ?contentUrl ?telephone1 ?telephone2    ?telephone3 WHERE {
            ?x a sr:StudyRoom .
            ?x sr:hasName ?name .
            ?x sr:hasSchedule ?schedule .
            OPTIONAL {?x sr:hasDescription ?description} .
            ?x sr:hasContentUrl ?contentUrl .
            ?x sr:hasTelephone1 ?telephone1 .
            OPTIONAL {?x sr:hasTelephone2 ?telephone2} .
            OPTIONAL {?x sr:hasTelephone3 ?telephone3} .
            ?x sr:hasAddress ?y .
            ?y sr:hasPostalCode '"""+postal_code+"""' .
        }
    """)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    return results

# From all study room, get name, wikidata road_type, wikidata neighborhood and wikidata district. 
@app.get("/studies_room_query5")
def read_study_rooms_query5():

    sparql = SPARQLWrapper("http://localhost:9000/sparql")
    sparql.setQuery("""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX sr: <http://www.studyroomsmadrid.es/ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        SELECT ?name ?wikidataRoadType ?wikidataNeighborhood ?wikidataDistrict WHERE {
            ?x a sr:StudyRoom .
            ?x sr:hasName ?name .
            ?x sr:hasAddress ?y .
            ?y sr:hasRoadType ?z1 .
            ?z1 owl:sameAs ?wikidataRoadType .
            ?y sr:hasNeighborhood ?z2 .
            ?z2 owl:sameAs ?wikidataNeighborhood .
            ?y sr:hasDistrict ?z3 .
            ?z3 owl:sameAs ?wikidataDistrict .
        }
    """)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    return results

