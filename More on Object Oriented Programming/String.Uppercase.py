class IOoperation:
    
    def __init__(self):
        self.word = ""
    def getinput(self):
        self.word = str(input("Enter a word to conver to usppercase letters"))
    def printstring(self):
        print(self.word.upper())
        




obj = IOoperation()


obj.getinput()
obj.printstring()