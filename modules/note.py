from enum import Enum
import attr

notes = {'C', 'D', 'E', 'F', 'G', 'A', 'B', 'H'}
aliases = {
    'H': "B"
}



class Alteration(Enum):
    NONE = ""
    SHARP = "#"
    FLAT = "b"

    def __str__(self) -> str:
        return self.value

@attr.s(frozen=True, auto_attribs=True, auto_detect=True)
class Note:
    key: str = attr.ib()
    alias: bool = False
    alteration: Alteration = attr.ib(default=Alteration.NONE)

    @classmethod
    def parse(cls, value):
        value = value[:2]
        key, alteration = value[:1], ""
        if any(letter for letter in value if letter in ('#', 'b')):
            key, alteration = list(value[:2])
        return cls(key=key, alteration=Alteration(alteration))

    @key.validator
    def validate_key(self, attribute, value):
        if all((value, value not in notes, not self.alias)):
            raise ValueError(f"{attribute} should be one of these: {notes}")
        return value
    
    @alteration.validator
    def validate_alteration(self, attribute, value):
        no_sharps, no_flats = (
            ('B', 'E'),
            ('C', 'F')
        )
        if self.key in no_sharps and value == Alteration.SHARP:
            raise ValueError(f"{self.key} can't have sharp alteration!")
        if self.key in no_flats and value == Alteration.FLAT:
            raise ValueError(f"{self.key} can't have flat alteration!")
        return value

    
    def __eq__(self, another: "Note") -> bool:
        conditions = [
            self.alteration == another.alteration
        ]
        another_key = aliases.get(another.key) if another.alias else another.key
        conditions.append(self.key == another_key)
        return all(conditions)
    
    def __str__(self) -> str:
        return f"{self.key}{self.alteration}"
