from WebAppImplementation import WebAppImplementation


# This is the framework class which in our pattern is the abstraction.
# It is the class that the client uses to create the web application.

class Framework:
    def __init__(self, implementation: WebAppImplementation):
        self._implementation = implementation

    def set_implementation(self, implementation: WebAppImplementation):
        self._implementation = implementation

    def create_blog(self):
        return self._implementation.create_blog()

    def create_store(self):
        return self._implementation.create_store()

    def create_news(self):
        return self._implementation.create_news()
