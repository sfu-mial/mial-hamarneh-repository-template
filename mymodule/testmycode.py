import unittest
from mymodule.mycode import myfunction

class MyTest(unittest.TestCase):
    def testMyFunction(self):
        self.assertEqual(myfunction([0]), [0])

    # Create a new function per testcase


if __name__=="__main__":
    print("Running")
    unittest.main()
