from msg_class import UserData
from model_generator import STLGenerator
from user_input import UserInputDataClass
from geo_location import GeoLocation







# Main program
if __name__ == "__main__":
    user_data = UserData()

    user_input = UserInputDataClass()
    name = user_input.get_data()
    user_data.set_name(name)

    geo_location = GeoLocation()
    location = geo_location.get_location()
    user_data.set_geolocation(location)

    is_valid = user_input.validate_data(name)  # Store the return value of validate_data in is_valid

    print(f"Input length < 20: {is_valid}")  # Print the validation result



    stl_generator = STLGenerator()
    stl_generator.generate_stl(user_data)
