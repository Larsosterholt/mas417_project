import requests
import json


response = requests.get("https://ipgeolocation.abstractapi.com/v1/?api_key=6c96de49e97f467b8cc6a446e5c4bdf1")
#print(response.status_code)
#print(response.content) #byteData

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

print("country: ", country)
print("region: ", region)
print("city: ", city)
print("postal_code: ", postal_code )
print("longitude: ", longitude)
print("latitude: ", latitude)



