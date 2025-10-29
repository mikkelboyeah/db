import requests
from pyjstat import pyjstat
import pandas as pd

class SsbApi:
    def __init__(self, ssb_url):
        self.ssb_url = ssb_url
        self._meta = None

    def get_metadata(self):
        if self._meta is None:
            response = requests.get(self.ssb_url)
            response.raise_for_status()
            self._meta = response.json()
        return self._meta

    def get_variable_codes(self):
        meta = self.get_metadata()
        return [var["code"] for var in meta["variables"]]

    def get_variable_values(self, variable_code):
        meta = self.get_metadata()
        for var in meta["variables"]:
            if var["code"] == variable_code:
                return var["values"]
        return []

def fetch_game_data():
    url = "https://data.ssb.no/api/v0/no/table/14380"
    api = SsbApi(url)
    # Example: get all variable codes and values for 'Region'
    variable_codes = api.get_variable_codes()
    region_values = api.get_variable_values("Region")
    # Use all values for each variable in the query
    query = {
        "query": [
            {"code": code, "selection": {"filter": "all", "values": ["*"]}} for code in variable_codes
        ],
        "response": {"format": "json-stat2"}
    }
    response = requests.post(url, json=query)
    response.raise_for_status()
    df = pyjstat.from_json_stat(response.json())[0]
    return df

# Standalone execution - save to CSV for dbt to consume
if __name__ == "__main__":
    df = fetch_game_data()
    df.to_csv("game_data.csv", index=False)
    print(f"Data saved to game_data.csv with {len(df)} rows")