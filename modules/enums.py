from enum import Enum


class ChordType(Enum):
    BIG_MAJOR = "maj"
    MAJOR = ""
    MINOR = "m"

    @classmethod
    def parse(cls, value):
        value = value[:3]
        vals = [cls(e.value) for e in cls if e.value == value]
        if not vals:
            return cls.MAJOR
        val, *_ = vals
        return val

    def __str__(self) -> str:
        return self.value


class AdditionType(Enum):
    NONE = "/"
    SUSPENDED = "sus"
    DIMINISHED = "dim"
    AUGMENTED = "aug"
    ADDITION = "add"
    WITHOUT = "no"
    UPPER = "#"
    LOWER = "b"

    def __str__(self) -> str:
        return self.value


class Interval(Enum):
    NONE = -1
    SECOND = 2
    THIRD = 3
    FOURTH = 4
    FIFTH = 5
    SIXTH = 6
    SEVENTH = 7
    NINTH = 9
    ELEVENTH = 11
    THIRTEENTH = 13

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def parse(cls, value):
        parsed_grade = ""
        for char in value:
            if not char.isdigit():
                break
            parsed_grade += char
        if parsed_grade:
            parsed_grade = int(parsed_grade)
            return cls(parsed_grade)
        else:
            return
