#A Python Decorator Function wraps a function and gives it additional functionality

def decorator_function(function):
    def wrapper_function():
        function()
    return wrapper_function 

#example, we want to set a delay for each function
import time
def say_hello():
    #time.sleep() would be an option, but too repetitive
    print('Hello')
    
def say_bye():
    print('Bye')


def delayed_function(function):
    def wrapper_function():
        #do something before the function
        time.sleep(3)
        function()
        #do something after the function
        print('Said he')
    return wrapper_function

@delayed_function
def guten_Tag():
    print('Guten Tag')

guten_Tag()