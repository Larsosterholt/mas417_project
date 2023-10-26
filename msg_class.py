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
