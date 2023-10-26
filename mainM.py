class UserData:
    def __init__(self, name=None, geolocation=None):
        self.name = name
        self.geolocation = geolocation

    def set_name(self, name):
        self.name = name

    def set_geolocation(self, geolocation):
        self.geolocation = geolocation

    def get_name(self):
        return self.name

    def get_geolocation(self):
        return self.geolocation

    def __repr__(self):
        return f"UserData(name={self.name}, geolocation={self.geolocation})"


# Class to take user input
class UserInput:
    def get_name(self):
        name = input("Please enter your name: ")
        return name


# Class to get geolocation (mock implementation)
class GeoLocation:
    def get_location(self):
        # Simulating an API call to get geolocation data
        return 'Grimstad'


# Class to generate STL file (mock implementation)
class STLGenerator:
    def generate_stl(self, user_data):
        print(f"Generating STL file for {user_data.name} based at {user_data.geolocation}")


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
