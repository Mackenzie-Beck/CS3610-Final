from themeImplementation import ThemeImplementation


# This is the WebApp class which is the abstraction in our pattern.
class WebApp():
    def __init__(self, implementation: ThemeImplementation):
        self._implementation = implementation

    def set_implementation(self, implementation: ThemeImplementation):
        self._implementation = implementation

    def post_message(self, message : str):
        self._implementation.post_message(message)


# this is a refined abstraction which is a specific type of web app.
class Blog(WebApp):
    def __init__(self, implementation: ThemeImplementation):
        super().__init__(implementation)

    def post_message(self, message : str):
        self._implementation.post_message(message)

    def create_post(self, title : str, content : str):
        self._implementation.create_post(title, content)

class Store(WebApp):
    def __init__(self, implementation: ThemeImplementation):
        super().__init__(implementation)

    def post_message(self, message : str):
        self._implementation.post_message(message)

    def create_product(self, name : str, price : float):
        self._implementation.create_product(name, price)

class News(WebApp):
    def __init__(self, implementation: ThemeImplementation):
        super().__init__(implementation)

    def post_message(self, message : str):
        self._implementation.post_message(message)

    def create_article(self, title : str, content : str):
        self._implementation.create_article(title, content)

