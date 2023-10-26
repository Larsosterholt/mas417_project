from msg_class import UserData
class STLGenerator:
    def generate_stl(self, user_data):
        print(f"Generating STL file for {user_data.name} based at {user_data.geolocation}")