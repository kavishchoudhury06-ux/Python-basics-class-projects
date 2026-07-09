class fruits:
    taste = 'sweet'
    
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
        
    def sentence(self):
        print('fruits are very healthy')

obfruits = fruits('apple', 'red')

obfruits.sentence()

print(obfruits.name)
print(obfruits.colour)
print(obfruits.colour)
print(obfruits.name)


