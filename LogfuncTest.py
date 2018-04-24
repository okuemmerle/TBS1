import unittest
from Logfunc import AndGate
from Logfunc import OrGate
from Logfunc import XOrGate
from Logfunc import NAndGate

class AndGateTest(unittest.TestCase):
    def testcase_01(self):
        a = AndGate()
        a.setInput0(False)
        a.setInput1(False)
        a.execute()
        self.assertFalse(a._Output, "Class AndGate: TestCase01 failed")

    def testcase_02(self):
        a = AndGate()
        a.setInput0(True)
        a.setInput1(False)
        a.execute()
        self.assertFalse(a._Output, "Class AndGate: TestCase02 failed")

    def testcase_03(self):
        a = AndGate()
        a.setInput0(False)
        a.setInput1(True)
        a.execute()
        self.assertFalse(a._Output, "Class AndGate: TestCase03 failed")

    def testcase_04(self):
        a = AndGate()
        a.setInput0(True)
        a.setInput1(True)
        a.execute()
        self.assertTrue(a._Output, "Class AndGate: TestCase04 failed")

class OrGateTest(unittest.TestCase):
    def testcase_01(self):
        a = OrGate()
        a.setInput0(False)
        a.setInput1(False)
        a.execute()
        self.assertFalse(a._Output, "Class OrGate: TestCase01 failed")

    def testcase_02(self):
        a = OrGate()
        a.setInput0(True)
        a.setInput1(False)
        a.execute()
        self.assertTrue(a._Output, "Class OrGate: TestCase02 failed")

    def testcase_03(self):
        a = OrGate()
        a.setInput0(False)
        a.setInput1(True)
        a.execute()
        self.assertTrue(a._Output, "Class OrGate: TestCase03 failed")

    def testcase_04(self):
        a = OrGate()
        a.setInput0(True)
        a.setInput1(True)
        a.execute()
        self.assertTrue(a._Output, "Class OrGate: TestCase04 failed")

class XOrGateTest(unittest.TestCase):
    def testcase_01(self):
        a = XOrGate()
        a.setInput0(False)
        a.setInput1(False)
        a.execute()
        self.assertFalse(a._Output, "Class XOrGate: TestCase01 failed")

    def testcase_02(self):
        a = XOrGate()
        a.setInput0(True)
        a.setInput1(False)
        a.execute()
        self.assertTrue(a._Output, "Class XOrGate: TestCase02 failed")

    def testcase_03(self):
        a = XOrGate()
        a.setInput0(False)
        a.setInput1(True)
        a.execute()
        self.assertTrue(a._Output, "Class XOrGate: TestCase03 failed")

    def testcase_04(self):
        a = XOrGate()
        a.setInput0(True)
        a.setInput1(True)
        a.execute()
        self.assertFalse(a._Output, "Class XOrGate: TestCase04 failed")

class NAndGateTest(unittest.TestCase):
    def testcase_01(self):
        a = NAndGate()
        a.setInput0(False)
        a.setInput1(False)
        a.execute()
        self.assertTrue(a._Output, "Class NAndGate: TestCase01 failed")

    def testcase_02(self):
        a = NAndGate()
        a.setInput0(True)
        a.setInput1(False)
        a.execute()
        self.assertTrue(a._Output, "Class NAndGate: TestCase02 failed")

    def testcase_03(self):
        a = NAndGate()
        a.setInput0(False)
        a.setInput1(True)
        a.execute()
        self.assertTrue(a._Output, "Class NAndGate: TestCase03 failed")

    def testcase_04(self):
        a = NAndGate()
        a.setInput0(True)
        a.setInput1(True)
        a.execute()
        self.assertFalse(a._Output, "Class NAndGate: TestCase04 failed")
if __name__ == "__main__":
    unittest.main()                 #Führt automatisch alle Methoden aus, die mit testcase_ beginnen.
