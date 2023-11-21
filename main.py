from nameTagLib.msg_class import UserData
from nameTagLib.model_generator import modelGenerator
from nameTagLib.user_input import UserInputDataClass
from nameTagLib.geo_location import GeoLocationAPI_Class



# Main program
if __name__ == "__main__":
    user_data = UserData()



    user_input = UserInputDataClass()
    name = user_input.get_data()
    isInputValid = user_input.validate_data(name)  # Store the return value of validate_data in is_valid
    if isInputValid == True:
        print("Name: ", name)
        user_data.name = name
        pass


    geo_location = GeoLocationAPI_Class("https://ipgeolocation.abstractapi.com/v1/?api_key=6c96de49e97f467b8cc6a446e5c4bdf1")
    location = geo_location.get_data()
    isLocationValid = geo_location.validate_data(location)
    if isLocationValid == True:
        print("Location: ", location)
        user_data.geolocation = location
        pass


    model_generator = modelGenerator()
    model_generator.generate_3mf(user_data)
