def greeting(name="User", location="Mutare"):
    name = name[0].upper() + name[1:].lower()
    location = location[0].upper() + location[1:].lower()
    print(f"Hello, {name}!")
    print(f"How's the weather like in {location}?")

greeting('joshua', "harare")