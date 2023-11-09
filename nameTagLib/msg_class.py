class UserData:
    def __init__(self, name=None, geolocation=None):
        self._name = name
        self._geolocation = geolocation

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def geolocation(self):
        return self._geolocation

    @geolocation.setter
    def geolocation(self, value):
        self._geolocation = value

    def __repr__(self):
        return f"UserData(name={self.name}, geolocation={self.geolocation})"
