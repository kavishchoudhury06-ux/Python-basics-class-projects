class enumarateion:
    
    def __init__(self, items):
        self.item = items
        
    def data(self):
        for i, fruits in enumerate(self.item, start = 10):
            print(i,'.', fruits)
            
obj = enumarateion(['apple', 'banana', 'mango'])

obj.data()