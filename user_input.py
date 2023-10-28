from DataHandler import DataHandler


    # UserInputDataClass inheriting from DataHandler
class UserInputDataClass(DataHandler):
        """
        Concrete class responsible for collecting and validating user input data.
        """

        # Public Constructor
        def __init__(self):
            self.user_input = None  # Example attribute

        # Public Method (Overriding abstract method)
        def get_data(self):

            while True:
                self.user_input = input("Please enter your name: ")
                if len(self.user_input) > 20:
                    print("Invalid input. The input should not exceed 20 characters.")
                #elif self.user_input.isnumeric():
                 #   print("Invalid input. Numbers are not allowed.")
                #elif not all(char.isalpha() for char in self.user_input):
                 #   print("Invalid input. Symbols are not allowed.")
                else:
                    break

            return self.user_input

        # Public Method (Overriding abstract method)
        def validate_data(self, data):
            return bool(data)  # Example validation: checks if the data is non-empty