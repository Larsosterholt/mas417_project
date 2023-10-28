from DataHandler import DataHandler


# UserInputDataClass inheriting from DataHandler
class UserInputDataClass(DataHandler):
    # Public Constructor
    def __init__(self):
        self.user_input: str = None  # Example attribute

    # Public Method (Overriding abstract method)
    def get_data(self) -> str:
        while True:
            self.user_input = input("Please enter your name: ")
            if self.validate_data(self.user_input):
                break
        return self.user_input

    # Public Method (Overriding abstract method)
    def validate_data(self, user_input: str):
        if not self.user_input:
            print("Invalid input. The name must not be empty.")
            return False
        if len(user_input) > 20:
            print("Invalid input. The name must not exceed 20 characters.")
            return False

        return True
