from WebApp import *
from concreteImplementations import *



# this is the client code which uses the WebApp class to create the web applications.

# we create a blog with the light theme.
blog = Blog(LightTheme())
blog.create_post("Hello", "This is a post")
blog.post_message("This is a message")

# we change the theme of the blog to dark.
blog.set_implementation(DarkTheme())
blog.create_post("Hello", "This is a post")
blog.post_message("This is a message")

print("\n")

# we create a store with the dark theme.
store = Store(DarkTheme())
store.create_product("Apple", 1.99)
store.post_message("This is a message")

# we change the theme of the store to light.
store.set_implementation(LightTheme())
store.create_product("Apple", 1.99)
store.post_message("This is a message")


print("\n")

# we create a news with the light theme.
news = News(LightTheme())
news.create_article("Hello", "This is a article")
news.post_message("This is a message")

# we change the theme of the news to dark.
news.set_implementation(DarkTheme())
news.create_article("Hello", "This is a article")
news.post_message("This is a message")
