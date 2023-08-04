import streamlit as st  # pip install streamlit
from deta import Deta  # pip install deta
DETA_KEY = "d0nyjdvcqqz_J6TaRbJyX2ocsLCPfzZqKAgdAB1toFez"
# Initialize with a project key
deta = Deta(DETA_KEY)
# This is how to create/connect a database
db = deta.Base("koshish")
def insert_period(period, modules):
    """Returns the report on a successful creation, otherwise raises an error"""
    return db.put({"key": period, "modules": modules})

def fetch_all_periods():
    """Returns a dict of all periods"""
    res = db.fetch()
    return res.items

def get_period(period):
    """If not found, the function will return None"""
    return db.get(period)


