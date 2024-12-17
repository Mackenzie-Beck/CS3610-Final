from themeImplementation import ThemeImplementation
# These are the concrete implementations that implement the themes.

class LightTheme(ThemeImplementation):
    def create_post(self, title : str, content : str):
        print(f"Creating light post with title: {title} and content: {content}")

    def create_product(self, name : str, price : float):
        print(f"Creating light product with name: {name} and price: {price}")

    def create_article(self, title : str, content : str):
        print(f"Creating light article with title: {title} and content: {content}")

    def post_message(self, message : str):
        print(f"Creating light message with message: {message}")

class DarkTheme(ThemeImplementation):
    def create_post(self, title : str, content : str):
        print(f"Creating dark post with title: {title} and content: {content}")

    def create_product(self, name : str, price : float):
        print(f"Creating dark product with name: {name} and price: {price}")

    def create_article(self, title : str, content : str):
        print(f"Creating dark article with title: {title} and content: {content}")

    def post_message(self, message : str):
        print(f"Creating dark message with message: {message}")
