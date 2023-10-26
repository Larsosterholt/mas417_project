from msg_class import UserData
from model_generator import STLGenerator
from user_imput import UserInput
from geo_location import GeoLocation

# Class to take user input








# Main program
if __name__ == "__main__":
    user_data = UserData()

    user_input = UserInput()
    name = user_input.get_name()
    user_data.set_name(name)

    geo_location = GeoLocation()
    location = geo_location.get_location()
    user_data.set_geolocation(location)

    stl_generator = STLGenerator()
    stl_generator.generate_stl(user_data)
