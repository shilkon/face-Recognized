from enum import Enum

class Condition(Enum):
    UNKNOWN = 1
    RECOGNIZED = 2

class InfoRecognize():

    condition = Condition.UNKNOWN
    name = ''

    def __init__(self, condition, name):
        self.condition = condition
        self.name = name
