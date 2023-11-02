from DataHandler import DataHandler


class UserInputDataClass(DataHandler):
    def __init__(self) -> None:
        """Public Constructor."""
        self.user_input: str = None

    def get_data(self) -> str:
        """Public Method for getting user data."""
        while True:
            self.user_input = input("Please enter your name: ")
            if self.validate_data(self.user_input):
                break
        return self.user_input

    def validate_data(self, user_input: str) -> bool:
        """Public Method for validating user data."""
        if not user_input:
            print("Invalid input. The name must not be empty.")
            return False
        if len(user_input) > 20:
            print("Invalid input. The name must not exceed 20 characters.")
            return False
        return True
