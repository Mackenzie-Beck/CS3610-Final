from abc import ABC, abstractmethod

# This is the implementation interface which defines the methods that the concrete implementations must implement.


class WebAppImplementation(ABC):
    @abstractmethod
    def create_blog(self):
        pass

    @abstractmethod
    def create_store(self):
        pass

    @abstractmethod
    def create_news(self):
        pass
