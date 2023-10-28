from DataHandler import DataHandler
import requests
import json

class GeoLocation(DataHandler):

    def __init__(self, endpoint_url: str):

        self.endpoint_url = endpoint_url

    def get_data(self):
        response = requests.get(self.endpoint_url)
        # Step 1: Decode byte data to string
        byte2utf = response.content.decode('utf-8')
        # Step 2: Parse the JSON string to a Python dictionary
        json_object = json.loads(byte2utf)
        # Step 3: Extract the value for the " " key
        country = json_object["country"]
        region = json_object["region"]
        city = json_object["city"]
        postal_code = json_object["postal_code"]
        longitude = json_object["longitude"]
        latitude = json_object["latitude"]
        return city

    def validate_data(self):
        """
        Validate the fetched data (implementation needed).
        """
        pass

