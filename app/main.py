from fastapi import FastAPI, Query                  # Import FastAPI and Query
from random import randint                          # for random number generation
import json                                         # to read and create json
# import mysql.connector                            # mysql db connector - deprecated
import sqlite3                                      # sqlite db connector
from pydantic import BaseModel                      # base model for data validation
from fastapi.middleware.cors import CORSMiddleware  # CORS

# post class
class Circuit(BaseModel):
    name: str

# init app
app = FastAPI()

# CORS allow all origins
origins = ["https://rmetdep.github.io", "https://bacbat32.sinners.be"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# db setup - deprecated
# db = mysql.connector.connect(
#   host="sql-service",
#   user="apiaccess",
#   password="apidev1!"
# )
# cursor = db.cursor()

# SQLite db setup dict
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def rmv_json(file):
    file = file.replace("}", "").replace("{", "").replace("'", "")
    file = file.split(": ")
    return file[1]
# return link to docs if people are lazy and didn't read the docs
@app.get("/")
def read_root():
    return {"docs": "https://github.com/rmetdep/python-api"}

# test function - deprecated
@app.get("/test")
def test():
    return {"test": "no tests active"}

@app.get("/driver") # get a rondom driver back
async def get_driver():
    conn = sqlite3.connect('data.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    file = cur.execute("SELECT driverName FROM driver;").fetchall()
    conn.close()
    result = file[randint(1, len(file))-1]
    # result = str(result).replace("(", "").replace(")", "").replace(",", "").replace("'", "")
    return {"driver": rmv_json(str(result))}

@app.get("/team")   # get a random team back
async def get_team():
    conn = sqlite3.connect('data.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    file = cur.execute("SELECT teamName FROM team;").fetchall()
    conn.close()
    result = file[randint(1, len(file))-1]
    # result = str(result).replace("(", "").replace(")", "").replace(",", "").replace("'", "")
    return {"team": rmv_json(str(result))}

@app.post("/addciruit") # lookup a drivers stats by name
async def add_circuit(circuit: Circuit):
    conn = sqlite3.connect('data.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    file = cur.execute("SELECT circuitName FROM circuits;").fetchall()
    conn.close()
    for x in file:
        if rmv_json(str(x)) == circuit.name:
            return {"response": "circuit already exists"}
    conn = sqlite3.connect('data.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    cur.execute("INSERT INTO circuits (circuitName) VALUES ('" + circuit.name + "');")
    conn.commit()
    conn.close()
    return {"response": circuit.name + " added"}