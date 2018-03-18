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

    def setInput0(self, value):
        self.Input0 = value

    def setInput1(self, value):
        self.Input1 = value

class OrGate:                               #Klassendefinition
    def __init__(self):                     #Attribute definieren
        self.Input0 = False
        self.Input1 = False
        self.Output = False
        self.Name = "YaOrGate"

    def execute(self):
        self.Output = self.Input0 or self.Input1

    def show(self):
        print("Output = " + str(self.Output))

    def __str__(self):
        return "OrGate Name = " + str(self.Name)

    def setInput0(self, value):
        self.Input0 = value

    def setInput1(self, value):
        self.Input1 = value

#Erstellung einer Instanz
myAndGate = AndGate()
myOrGate = OrGate()

#Aufruf der Methoden
myAndGate.execute()
myAndGate.show()
myOrGate.execute()
myOrGate.show
print(str(myAndGate))
print(str(myOrGate))