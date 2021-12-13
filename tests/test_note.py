import pytest

from modules.note import Note, Alteration

class TestNote:

    def test_note_serialized_correctly(self):
        assert "E" == str(Note(key="E"))
        assert "F#" == str(Note(key="F", alteration=Alteration.SHARP))
        assert "Gb" == str(Note(key="G", alteration=Alteration.FLAT))

    def test_note_aliases(self):
        assert Note(key="B") == Note(key="H", alias=True)
    
    def test_note_failed(self):
        with pytest.raises(ValueError):
            assert Note(key="J")
            assert Note(key="E", alteration=Alteration.SHARP)
            assert Note(key="F", alteration=Alteration.FLAT)


class TestNoteParse:
    
    def test_simple_note(self):
        assert str(Note.parse("C")) == "C"
    
    def test_note_with_alteration(self):
        assert str(Note.parse("F#")) == "F#"
        assert str(Note.parse("Gb")) == "Gb"
    
    def test_failed_note(self):
        with pytest.raises(ValueError):
            assert str(Note.parse("J#"))
            assert str(Note.parse("LOREM"))
            assert str(Note.parse(333))

