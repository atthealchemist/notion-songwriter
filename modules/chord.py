import attr

from typing import Optional, List

from modules.enums import Interval, ChordType, AdditionType
from modules.note import Note


@attr.s(frozen=True, auto_attribs=True)
class ChordAddition:
    addition_type: AdditionType = AdditionType.NONE
    interval: Optional[Interval] = Interval.NONE

    @classmethod
    def parse(cls, value):
        addition_types = [e.value for e in AdditionType]
        parsed_type = ""
        results = []
        value = list(value)
        for idx, char in enumerate(value):
            params = dict()
            parsed_type += str(char)
            if parsed_type in addition_types and idx + 1 <= len(value):
                params.update(dict(addition_type=AdditionType(parsed_type)))
                interval = ''.join(value[idx + 1:])
                if interval:
                    params.update(dict(interval=Interval(int(interval))))
                results.append(cls(**params))
        return results


    def __str__(self) -> str:
        interval = self.interval if self.interval.value > 0 else ""
        return f"{self.addition_type}{interval}"


@attr.s(frozen=True, auto_attribs=True)
class Chord:
    key: Note
    additions: List[ChordAddition] = []
    bass: Optional[Note] = None
    interval: Optional[Interval] = Interval.NONE
    chord_type: ChordType = ChordType.MAJOR

    @classmethod
    def parse(cls, source):
        key_part, bass_part = source, ""
        if '/' in source:
            key_part, bass_part = source.split("/")

        params = dict()
        
        key = Note.parse(key_part)
        key_rest = key_part[len(str(key)):]
        chord_type = ChordType.parse(key_rest)

        params.update(
            dict(key=key, chord_type=chord_type)
        )
        chord_has_interval = any(str(e.value) in key_rest for e in Interval)
        if chord_has_interval:
            grade_rest = key_part[sum(len(str(v)) for v in params.values()):]
            chord_interval = Interval.parse(grade_rest)
            if chord_interval:
                params.update(
                    dict(interval=chord_interval)
                )
        
        chord_has_additions = any(e.value in key_rest for e in AdditionType)
        if chord_has_additions:
            additions_rest = key_part[sum(len(str(v)) for v in params.values()):]
            chord_additions = ChordAddition.parse(additions_rest)
            if chord_additions:
                params.update(
                    dict(additions=chord_additions)
                )
        if bass_part:
            params.update({'bass': Note.parse(bass_part)})
        return cls(**params)

    def __str__(self) -> str:
        record = f"{self.key}{self.chord_type}"
        if self.interval and self.interval.value > 0:
            record += str(self.interval)
        record += "".join(str(a) for a in self.additions)
        if self.bass:
            record += f"/{self.bass}"
        return record

@attr.s(frozen=True, auto_attribs=True)
class PowerChord(Chord):
    key: Note = None
    interval: Interval = Interval.FIFTH
    chord_type: ChordType = ChordType.MAJOR


