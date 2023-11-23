from nameTagLib.DataHandler import DataHandler
import requests
import json



class GeoLocationAPI_Class(DataHandler): #KLASSENAVN KONVENSJON????
    def __init__(self, endpoint_url: str):
        if not endpoint_url.startswith('https://'):
            raise ValueError("The endpoint URL must start with 'https://'")

        self.endpoint_url = endpoint_url




    def get_data(self):
        try:
            response = requests.get(self.endpoint_url)      # byte data to string
            response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code
            byte2str = response.content.decode('utf-8')     # Parse the JSON string to a Python dictionary
            self.json_object = json.loads(byte2str)
            #print(self.json_object)
            city = self.json_object["city"]
        except requests.RequestException as e:
            print(f"An error occurred while fetching data: {e}")
            return None
        return city

    def validate_data(self, get_data):
        if not get_data:
            print("Invalid input. The name must not be empty.")
            return False
        if not isinstance(get_data, str):
            print("Invalid input. The city name must be a string.")
            return False
        if len(get_data) < 1 or len(get_data) > 50:
            print("Invalid input. The city name must be between 1 and 50 characters.")
            return False
        return True
