from abc import ABC, abstractmethod

# This is the theme implementation interface which defines the methods that the concrete implementations must implement.

class ThemeImplementation(ABC):
    @abstractmethod
    def create_post(self, title : str, content : str):
        pass

    @abstractmethod
    def create_product(self, name : str, price : float):
        pass

    @abstractmethod
    def create_article(self, title : str, content : str):
        pass

    @abstractmethod
    def post_message(self, message : str):
        pass
