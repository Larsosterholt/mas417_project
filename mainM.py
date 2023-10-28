from msg_class import UserData
from model_generator import STLGenerator
from user_input import UserInputDataClass
from geo_location import GeoLocationAPI_Class



# Main program
if __name__ == "__main__":
    user_data = UserData()


    user_input = UserInputDataClass()
    name = user_input.get_data()
    isInputValid = user_input.validate_data(name)  # Store the return value of validate_data in is_valid
    print("User input valid: ", isInputValid)

    user_data.set_name(name)

    geo_location = GeoLocationAPI_Class("https://ipgeolocation.abstractapi.com/v1/?api_key=6c96de49e97f467b8cc6a446e5c4bdf1")
    location = geo_location.get_data()
    isLocationValid = geo_location.validate_data(location)
    print("Location input valid: ", isLocationValid)

    user_data.set_geolocation(location)





    stl_generator = STLGenerator()
    stl_generator.generate_stl(user_data)
