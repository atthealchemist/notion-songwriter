from modules.chord import Chord, ChordAddition, AdditionType, ChordType, Interval, PowerChord
from modules.note import Alteration, Note


class TestChordSerialization:

    def test_basic_chords(self):
        assert "Am" == str(
            Chord(key=Note(key="A"), chord_type=ChordType.MINOR)
        )
        assert "D" == str(
            Chord(key=Note(key="D"), chord_type=ChordType.MAJOR)
        )
        assert "Hm" == str(
            Chord(key=Note("H", alias=True), chord_type=ChordType.MINOR)
        )
    
    def test_basic_chords_with_alterations(self):
        assert "C#5" == str(
            Chord(
                key=Note(key="C", alteration=Alteration.SHARP), 
                chord_type=ChordType.MAJOR,
                interval=Interval.FIFTH
            ),
        )
        assert "E5" == str(
            PowerChord(
                key=Note("E")
            )
        )
    
    def test_basic_chords_with_additions(self):
        assert "Bsus4" == str(
            Chord(
                key=Note("B"), 
                chord_type=ChordType.MAJOR, 
                additions=[
                    ChordAddition(
                        addition_type=AdditionType.SUSPENDED, 
                        interval=Interval.FOURTH
                    )
                ]
            )
        )
        assert "Edim" == str(
            Chord(
                key=Note("E"), 
                chord_type=ChordType.MAJOR,
                additions=[
                    ChordAddition(addition_type=AdditionType.DIMINISHED)
                ]
            )
        )
        assert "Cadd9" == str(
            Chord(
                key=Note("C"),
                additions=[
                    ChordAddition(
                        addition_type=AdditionType.ADDITION,
                        interval=Interval.NINTH
                    )
                ]
            )
        )
        assert "Em7no5" == str(
            Chord(
                key=Note("E"),
                chord_type=ChordType.MINOR,
                interval=Interval.SEVENTH,
                additions=[
                    ChordAddition(
                        addition_type=AdditionType.WITHOUT,
                        interval=Interval.FIFTH
                    )
                ]
            )
        )
    
    def test_two_non_altered_grades_chords(self):
        assert "C6/9" == str(
            Chord(
                key=Note("C"),
                chord_type=ChordType.MAJOR,
                interval=Interval.SIXTH,
                additions=[
                    ChordAddition(
                        interval=Interval.NINTH
                    )
                ]
            )
        )

    def test_more_than_one_addition_chords(self):
        assert "D7#5b9" == str(
            Chord(
                key=Note("D"),
                chord_type=ChordType.MAJOR,
                interval=Interval.SEVENTH,
                additions=[
                    ChordAddition(
                        addition_type=AdditionType.UPPER,
                        interval=Interval.FIFTH
                    ),
                    ChordAddition(
                        addition_type=AdditionType.LOWER,
                        interval=Interval.NINTH
                    )
                ]
            )
        )

        assert "Amaj9#11" == str(
            Chord(
                key=Note("A"),
                chord_type=ChordType.BIG_MAJOR,
                interval=Interval.NINTH,
                additions=[
                    ChordAddition(
                        addition_type=AdditionType.UPPER,
                        interval=Interval.ELEVENTH
                    )
                ]
            )
        )
    

    def test_bass_note_chords(self):
        assert "C/F#" == str(
            Chord(key=Note(key="C"), bass=Note(key="F", alteration=Alteration.SHARP))
        )
        assert "Db/E" == str(
            Chord(key=Note(key="D", alteration=Alteration.FLAT), bass=Note(key="E"))
        )

        assert "Gmaj13#11/B" == str(
            Chord(
                key=Note("G"),
                chord_type=ChordType.BIG_MAJOR,
                interval=Interval.THIRTEENTH,
                bass=Note("B"),
                additions=[
                    ChordAddition(
                        addition_type=AdditionType.UPPER,
                        interval=Interval.ELEVENTH
                    )
                ]
            )
        )


class TestChordParsing:

    def test_simple_chords(self):
        assert str(Chord.parse("Cm")) == "Cm"

    def test_chords_with_additions(self):
        assert str(Chord.parse("Dsus2")) == "Dsus2"
        assert str(Chord.parse("Edim")) == "Edim"
        assert str(Chord.parse("Fmaj13")) == "Fmaj13"
        assert str(Chord.parse("Cmaj9#11")) == "Cmaj9#11"
