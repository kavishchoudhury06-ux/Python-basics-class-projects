class fruits:
    
    
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
        
    def sentence(self):
        print("my favourite fruit is", self.name, 'and it is', self.colour, 'in colour')

obfruits = fruits('apple', 'red')

obfruits.sentence()

print(obfruits.name)
print(obfruits.colour)