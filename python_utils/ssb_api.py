import requests
import pandas as pd
from pyjstat import pyjstat

class SSBClient:
    """
    A client for interacting with the Statistics Norway (SSB) API.
    """
    BASE_URL = "https://data.ssb.no/api/v0/no/table/"

    def __init__(self, table_id):
        """
        Initializes the client for a specific SSB table.

        Args:
            table_id (str): The ID of the SSB table (e.g., '14380').
        """
        self.table_id = table_id
        self.table_url = f"{self.BASE_URL}{self.table_id}"
        self._meta = None

    def get_metadata(self):
        """
        Retrieves and caches metadata for the table.
        """
        if self._meta is None:
            response = requests.get(self.table_url)
            response.raise_for_status()
            self._meta = response.json()
        return self._meta

    def get_variable_codes(self):
        """
        Gets a list of all variable codes from the metadata.
        """
        meta = self.get_metadata()
        return [var["code"] for var in meta["variables"]]

    def get_variable_values(self, variable_code):
        """
        Gets a list of all possible values for a given variable code.
        """
        meta = self.get_metadata()
        for var in meta["variables"]:
            if var["code"] == variable_code:
                return var["values"]
        return []

    def get_dataframe(self, query):
        """
        Posts a query to the SSB API and returns the data as a pandas DataFrame.

        Args:
            query (dict): The query to send to the API.

        Returns:
            pd.DataFrame: A DataFrame containing the requested data.
        """
        response = requests.post(self.table_url, json=query)
        response.raise_for_status()
        dataset = pyjstat.from_json_stat(response.json())
        return dataset[0]

    def download_to_parquet(self, query, file_path):
        """
        Fetches data based on a query and saves it to a Parquet file.

        Args:
            query (dict): The query to send to the API.
            file_path (str): The path to save the Parquet file.
        """
        df = self.get_dataframe(query)
        df.to_parquet(file_path)
        print(f"Data for table {self.table_id} saved to {file_path}")