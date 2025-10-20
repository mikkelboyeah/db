import requests
from pyjstat import pyjstat
import pandas as pd

def model(dbt, session):
    dbt.config(
        materialized="table"
    )

    url = "https://data.ssb.no/api/v0/no/table/11342"
    query = {
        "query": [
            {
                "code": "Region",
                "selection": {"filter": "item", "values": ["0301"]}
            },
            {
                "code": "ContentsCode",
                "selection": {"filter": "item", "values": ["Folkemengde"]}
            }
        ],
        "response": {"format": "json-stat2"}
    }

    response = requests.post(url, json=query)
    response.raise_for_status()

    # Use pyjstat.from_json_stat for a dict
    df = pyjstat.from_json_stat(response.json())[0]  # returns a list of DataFrames

    return df