from WebAppImplementation import WebAppImplementation

# These are the concrete implementations that implement the themes.

class LightImplementation(WebAppImplementation):
    def create_blog(self):
        print("Creating light blog")

    def create_store(self):
        print("Creating light store")

    def create_news(self):
        print("Creating light news")


class DarkImplementation(WebAppImplementation):
    def create_blog(self):
        print("Creating dark blog")

    def create_store(self):
        print("Creating dark store")

    def create_news(self):
        print("Creating dark news")
