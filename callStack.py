# the call stack (pseudocode).

# simple function.
def greet(name):
    print ("hello," +  name + "!")

    greet2(name)
    print ("getting ready to say bye...")
    bye()

# function greets you and calls two other functions.
def greet2(name):
    print ("how are you," + name + "?")

def bye():
    print ("ok bye!")

