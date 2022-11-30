from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.description import Description
from hamcrest.core.helpers.hasmethod import hasmethod


class checkFigures(BaseMatcher):

    def __init__(self, a, b=[]):
        self.a = a
        self.b = b

    def result(self):
        return 3 * self.a

    def listLength(self):
        return len(self.b)

    def _matches(self, item):
        if not hasmethod(item, "result"):
            return False
        return item.result() == self.result

    def describe_to(self, description: Description) -> None:
        description.append_text(self.result)


def checkCalculation():
    return checkFigures(2, ["", "", "", "", "", ""]).result()


def checkLsistLengths():
    return checkFigures(2, ["", "", "", "", "", ""]).listLength()
