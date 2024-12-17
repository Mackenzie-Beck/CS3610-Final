from framework import Framework
from concreteImplementations import LightImplementation, DarkImplementation


# This is the client which uses the framework to create the web application.



framework = Framework(LightImplementation())
framework.create_blog()
framework.create_store()
framework.create_news()


print("\n")

framework.set_implementation(DarkImplementation())
framework.create_blog()
framework.create_store()
framework.create_news()