# class = blueprint for creating a "mini import" (object)

class MyStuff(object): 

    def __init__(self):

        self.tangerine = "And now a thousand years between"

    def apple(self):
        print "I AM CLASSY APPLES!"


# calling the class

"""
instantiate operation (thing = MyStuff())
i)  python looks for MyStuff & sees = class
ii) python creates an empty object with all fns specified in MyStuff
iii) Looks for __init__ fn: calls it to initialise this new empty object
iv) __init__: extra self var used to create the obj. can set vars on it like mod, dict etc
v) python assings newly minted obj to "thing" variable

"""

thing = MyStuff()

# call apple part
thing.apple()

# print tangerine
print thing.tangerine
