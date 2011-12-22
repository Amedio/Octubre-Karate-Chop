'''
Created on 22/12/2011

@author: ruben
'''
import unittest
from KataKarateChop import KarateChopper


class Test(unittest.TestCase):

    def testNoElementsGivesError(self):
        chopper = KarateChopper()
        actual = chopper.chop(3, [])
        expected = -1
        self.assertEquals(actual, expected, "Not correctly chopped. {0} != {1}".format(actual, expected))
        
    def testOneElementGivesErrorIfNumberIsNotEquals(self):
        chopper = KarateChopper()
        actual = chopper.chop(3, [1])
        expected = -1
        self.assertEquals(actual, expected, "Not correctly chopped. {0} != {1}".format(actual, expected))
        
    def testOneElementGivesOkIfNumberIsEquals(self):
        chopper = KarateChopper()
        actual = chopper.chop(1, [1])
        expected = 0
        self.assertEquals(actual, expected, "Not correctly chopped. {0} != {1}".format(actual, expected))

    def testTwoElementsGivesOkWithExistingNumber(self):
        chopper = KarateChopper()
        actual = chopper.chop(1, [1, 3])
        expected = 0
        self.assertEquals(actual, expected, "Not correctly chopped. {0} != {1}".format(actual, expected))
        
        actual = chopper.chop(3, [1, 3])
        expected = 1
        self.assertEquals(actual, expected, "Not correctly chopped. {0} != {1}".format(actual, expected))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testNoElementsGivesError']
    unittest.main()