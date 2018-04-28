'''
Created on Apr 7, 2018

@author: johnny
'''
import unittest


class Test(unittest.TestCase):


    def setUp(self):
        self.a = 1

    def tearDown(self):
        del self.a

    def test_basic1(self):
        "Basic with setup"

        self.assertNotEqual(self.a, 2)

    def test_basic2(self):
        "Basic2 with setup"
        assert self.a != 2

    def test_fail(self):
        "This test should fail"
        assert self.a == 2



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()