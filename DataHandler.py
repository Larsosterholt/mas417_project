from abc import ABC, abstractmethod

class DataHandler(ABC):
    """
    Abstract class that serves as a blueprint for classes that handle data fetching and validation.
    """

    # Constructor: None (Since this is an abstract class, it's not mandatory to have a constructor)

    # Public Abstract Method
    @abstractmethod
    def get_data(self):
        """
        Abstract method to be overridden by subclasses for fetching data.

        Returns:
            data (Any): The fetched data. Type may vary depending on the implementation.
        """
        pass

    # Public Abstract Method
    @abstractmethod
    def validate_data(self, data):
        """
        Abstract method to be overridden by subclasses for validating fetched data.

        Parameters:
            data (Any): The data to validate. Type may vary depending on the implementation.

        Returns:
            bool: True if data is valid, False otherwise.
        """
        pass
