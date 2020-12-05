class Kettle(object):
    # similar to static in C# and Java
    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch(self, is_on):
        self.on = is_on

    
kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

# pass in object like so:
print("Models: {0.make} - {0.price}".format(kenwood))

kenwood.switch(True)

print(kenwood.on)

# not sure why you'd want to do this but you can dynamically add properties
kenwood.power = 1.5
print(kenwood.power)

# get all items as object
print(kenwood.__dict__)

# iterate over a objects properties
for attr, value in kenwood.__dict__.items():
        print(attr, value)

# you can access class attributes as so:
print(Kettle.power_source)
print(kenwood.power_source)

# you can also change class atrributes:
Kettle.power_source = "atomic"

print(Kettle.power_source)
print(kenwood.power_source)

# you can change a specific instance class attributes as such: 
kenwood.power_source = "gas"

print(Kettle.power_source)
print(kenwood.power_source)