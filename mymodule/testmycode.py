import unittest
from mymodule.mycode import myfunction

class TreeTest(unittest.TestCase):
    def testMyFunction(self):
        self.assertEqual(myfunction([0]), [0])


if __name__=="__main__":
    print("Running")
    unittest.main()
