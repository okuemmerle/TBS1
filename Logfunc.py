__version__ = "1.1"                         #Verwaltungsinfos
__author__ = "Oliver Kümmerle"

class LogFunc:                              #Klassendefinition
    def __init__(self):                     #Attribute definieren
        self.__Input0 = False
        self.__Input1 = False
        self._Output = False
        self._Name = ""

    def show(self):
        print("Output = " + str(self._Output))

    def __str__(self):
        return "Name = " + str(self._Name)

    def setInput0(self, value):
        self.__Input0 = value

    def setInput1(self, value):
        self.__Input1 = value

    def getInput0(self):
        return self.__Input0

    def getInput1(self):
        return self.__Input1

class AndGate(LogFunc):                              #Klassendefinition
    def __init__(self):                             #Attribute definieren
        self._Name = "YaAndGate"
    def execute(self):
        self._Output = self.getInput0() and self.getInput1()

class OrGate(LogFunc):                               #Klassendefinition
    def __init__(self):                             #Attribute definieren
        self._Name = "YaOrGate"

    def execute(self):
        self._Output = self.getInput0() or self.getInput1()

class XOrGate(LogFunc):                               #Klassendefinition
    def __init__(self):                             #Attribute definieren
        self._Name = "YaXOrGate"

    def execute(self):
        self._Output = self.getInput0() != self.getInput1()

class NAndGate(AndGate):                               #Klassendefinition
    def __init__(self):                             #Attribute definieren
        self._Name = "YaNAndGate"

    def execute(self):
        self._Output = not(self.getInput0() and self.getInput1())


#Erstellung jeweils einer Instanz
myAndGate = AndGate()
myOrGate = OrGate()
myXOrGate = XOrGate()
myNAndGate = NAndGate()

#Aufruf der Methoden
myAndGate.setInput0(True)
myAndGate.setInput1(True)
myAndGate.execute()
myAndGate.show()

myOrGate.setInput0(True)
myOrGate.setInput1(True)
myOrGate.execute()
myOrGate.show()

myXOrGate.setInput0(True)
myXOrGate.setInput1(True)
myXOrGate.execute()
myXOrGate.show()

myNAndGate.setInput0(True)
myNAndGate.setInput1(False)
myNAndGate.execute()
myNAndGate.show()
