from WebApp import *
from concreteImplementations import *


blog = Blog(LightTheme())
blog.create_post("Hello", "This is a post")
blog.post_message("This is a message")

blog.set_implementation(DarkTheme())
blog.create_post("Hello", "This is a post")
blog.post_message("This is a message")

print("\n")



store = Store(DarkTheme())
store.create_product("Apple", 1.99)
store.post_message("This is a message")

store.set_implementation(LightTheme())
store.create_product("Apple", 1.99)
store.post_message("This is a message")


print("\n")

news = News(LightTheme())
news.create_article("Hello", "This is a article")
news.post_message("This is a message")

news.set_implementation(DarkTheme())
news.create_article("Hello", "This is a article")
news.post_message("This is a message")
    