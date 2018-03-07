__version__ = "1.0"                         #Verwaltungsinfos
__author__ = "Oliver Kümmerle"

class AndGate:                              #Klassendefinition
    def __init__(self):                     #Attribute definieren
        self.Input0 = False
        self.Input1 = False
        self.Output = False
        self.Name = "YaAndGate"
    def execute(self):
        self.Output = self.Input0 and self.Input1
    def show(self):
        print("Output = " + str(self.Output))
    def __str__(self):
        return "AndGate Name = " + str(self.Name)

#Erstellung einer Instant
myAndGate = AndGate()

#Aufruf der Methoden
myAndGate.execute()
myAndGate.show()
print(str(myAndGate))
