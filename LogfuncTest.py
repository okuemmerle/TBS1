import unittest
from Logfunc import AndGate
from Logfunc import OrGate

class AndGateTest(unittest.TestCase):
    def testcase_01(self):
        a = AndGate()
        a.Input0 = False
        a.Input1 = False
        a.execute()
        self.assertFalse(a.Output, "Class AndGate: TestCase01 failed")

    def testcase_02(self):
        a = AndGate()
        a.Input0 = True
        a.Input1 = False
        a.execute()
        self.assertFalse(a.Output, "Class AndGate: TestCase02 failed")

    def testcase_03(self):
        a = AndGate()
        a.Input0 = False
        a.Input1 = True
        a.execute()
        self.assertFalse(a.Output, "Class AndGate: TestCase03 failed")

    def testcase_04(self):
        a = AndGate()
        a.Input0 = True
        a.Input1 = True
        a.execute()
        self.assertTrue(a.Output, "Class AndGate: TestCase04 failed")

class OrGateTest(unittest.TestCase):
    def testcase_01(self):
        a = OrGate()
        a.Input0 = False
        a.Input1 = False
        a.execute()
        self.assertFalse(a.Output, "Class OrGate: TestCase01 failed")

    def testcase_02(self):
        a = OrGate()
        a.Input0 = True
        a.Input1 = False
        a.execute()
        self.assertTrue(a.Output, "Class OrGate: TestCase02 failed")

    def testcase_03(self):
        a = OrGate()
        a.Input0 = False
        a.Input1 = True
        a.execute()
        self.assertTrue(a.Output, "Class OrGate: TestCase03 failed")

    def testcase_04(self):
        a = OrGate()
        a.Input0 = True
        a.Input1 = True
        a.execute()
        self.assertTrue(a.Output, "Class OrGate: TestCase04 failed")

if __name__ == "__main__":
    unittest.main()                 #Führt automatisch alle Methoden aus, die mit testcase_ beginnen.