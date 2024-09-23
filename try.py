def say_hello():
    greeting = "Hello stranger!"
    return greeting

def say_louder(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

# Applying the decorator
@say_louder
def say_hello():
    greeting = "Hello stranger!"
    return greeting

# Calling the function
print(say_hello())  # Output will be "HELLO STRANGER!"

