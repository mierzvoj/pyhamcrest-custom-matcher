import string
import sys
import unittest

from hamcrest import assert_that, is_
from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.helpers.hasmethod import hasmethod

from CustomMatcher import checkCalculation, checkLsistLengths


class Calculator:
    def __init__(self, a, b=[]):
        self.a = a
        self.b = b

    def function(self):
        print(self.a + self.a + self.a)
        return self.a + self.a + self.a

    def listLengthChecker(self):
        return len(self.b)


calc = Calculator(2, ["john", "paul", "ann", ""])

print(calc.function())


class MathTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_check_Result(self):
        calc = Calculator(2, ["john", "paul", "ann", ""])
        assert_that(calc.function(), is_(checkCalculation()))

    def test_check_lists_lengths_equality(self):
        calc = Calculator(2, ["john", "paul", "ann", ""])
        assert_that(calc.function(), is_(checkLsistLengths()))