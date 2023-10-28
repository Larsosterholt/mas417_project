from DataHandler import DataHandler
import requests
import json

class GeoLocationAPI_Class(DataHandler):

    def __init__(self, endpoint_url: str):

        self.endpoint_url = endpoint_url

    def get_data(self):
        response = requests.get(self.endpoint_url)      # byte data to string
        byte2str = response.content.decode('utf-8')     # Parse the JSON string to a Python dictionary
        self.json_object = json.loads(byte2str)
        #print(self.json_object)
        city = self.json_object["city"]
        #print(city)
        return city

    def validate_data(self, get_data):
        if not get_data:
            print("Invalid input. The name must not be empty.")
            return False
        if not isinstance(get_data, str):
            print("Invalid input. The city name must be a string.")
            return False
        if len(get_data) < 1 or len(get_data) > 50:
            print("Invalid input. The city name must be between 2 and 100 characters.")
            return False
        return True

