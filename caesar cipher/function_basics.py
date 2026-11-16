# defination of parameters and arguments
# default arguments protect the app from crashing
def greeting(name="User", location="Mutare"):
    # capitalises a word and i actually discover that there is a string method .capitalize() to do the job
    name = name[0].upper() + name[1:].lower()
    location = location[0].upper() + location[1:].lower()
    print(f"Hello, {name}!")
    print(f"How's the weather like in {location}?")

greeting('joshua', "harare")
