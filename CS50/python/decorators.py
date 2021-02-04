def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done witht the function.")
    return wrapper

@announce
def hello():
    print("Hello, I am voight")

hello()
