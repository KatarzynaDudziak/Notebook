from NoteManager import NoteManager
from Note import Note
from unittest.mock import call

DUMMY_NOTES = [{"title": "someTitle", "content": "someContent", "date": "2021-10-07"}]

class TestNoteManager:

    def test_create_noteManager_object(self, mocker):
        mocker.patch("NoteManager.open")
        json_mock = mocker.patch("NoteManager.json.load")
        json_mock.return_value = DUMMY_NOTES
        
        NoteManager()

    def test_exit_from_main_menu(self, mocker):
        mocker.patch("NoteManager.open")
        json_mock = mocker.patch("NoteManager.json.load")
        json_mock.return_value = DUMMY_NOTES
        input_mock = mocker.patch("NoteManager.input")
        input_mock.return_value = "3"
        exit_mock = mocker.patch("NoteManager.exit")

        noteManager = NoteManager()
        noteManager.main_menu()

        assert exit_mock.call_count == 1
    
    def test_add_note_from_main_menu(self, mocker):
        mocker.patch("NoteManager.open")
        json_mock = mocker.patch("NoteManager.json.load")
        json_mock.return_value = DUMMY_NOTES
        note_mock = mocker.patch("NoteManager.Note")
        input_mock = mocker.patch("NoteManager.input")
        dump_mock = mocker.patch("NoteManager.json.dump")
        exit_mock = mocker.patch("NoteManager.exit")
        input_mock.side_effect = ["1", "title", "content", "3"]
        
        noteManager = NoteManager()
        noteManager.main_menu()
        args, kwargs = dump_mock.call_args

        assert len(args[0]) == 2
        note_mock.assert_has_calls([
            call("someTitle", "someContent", "2021-10-07"), call("title", "content")])
        assert input_mock.call_count == 4
        assert exit_mock.call_count == 1
    
    def test_change_title_from_show_all_notes(self, mocker):
        mocker.patch("NoteManager.open")
        json_mock = mocker.patch("NoteManager.json.load")
        note_mock = mocker.patch("NoteManager.Note")
        json_mock.return_value = DUMMY_NOTES
        input_mock = mocker.patch("NoteManager.input")
        input_mock.side_effect = ["2", "a", "1", "1", "3"]
        mocker.patch("NoteManager.json.dump")
        mocker.patch("NoteManager.exit")

        noteManager = NoteManager()
        noteManager.main_menu()

        note_mock.assert_has_calls([call("someTitle", "someContent", "2021-10-07")])
        note_mock.change_title.assert_called_once       
        
    def test_change_content_from_show_all_notes(self, mocker):
        mocker.patch("NoteManager.open")
        json_mock = mocker.patch("NoteManager.json.load")
        note_mock = mocker.patch("NoteManager.Note")
        json_mock.return_value = DUMMY_NOTES
        input_mock = mocker.patch("NoteManager.input")
        input_mock.side_effect = ["2", "a", "1", "2", "3"]
        mocker.patch("NoteManager.json.dump")
        mocker.patch("NoteManager.exit")

        noteManager = NoteManager()
        noteManager.main_menu()

        note_mock.assert_has_calls([call("someTitle", "someContent", "2021-10-07")])
        note_mock.change_content.assert_called_once 
        
    def test_delete_note_from_show_notes_list_menu(self, mocker):
        mocker.patch("NoteManager.open")
        json_mock = mocker.patch("NoteManager.json.load")
        json_mock.return_value = DUMMY_NOTES
        input_mock = mocker.patch("NoteManager.input")
        input_mock.side_effect = ["2", "s", "1", "3"]
        dump_mock = mocker.patch("NoteManager.json.dump")
        exit_mock = mocker.patch("NoteManager.exit")

        noteManager = NoteManager()
        noteManager.main_menu()

        assert input_mock.call_count == 4
        args, kwargs = dump_mock.call_args
        assert args[0] == []
        assert exit_mock.call_count == 1

    def test_back_to_main_menu_from_show_notes_list_menu(self, mocker):
        mocker.patch("NoteManager.open")
        json_mock = mocker.patch("NoteManager.json.load")
        json_mock.return_value = DUMMY_NOTES
        input_mock = mocker.patch("NoteManager.input")
        input_mock.side_effect = ["2", "d", "3"]
        exit_mock = mocker.patch("NoteManager.exit")

        noteManager = NoteManager()
        noteManager.main_menu()

        assert input_mock.call_count == 3
        assert exit_mock.call_count == 1
    
    def test_exit_from_show_notes_list_menu(self, mocker):
        mocker.patch("NoteManager.open")
        json_mock = mocker.patch("NoteManager.json.load")
        json_mock.return_value = DUMMY_NOTES
        input_mock = mocker.patch("NoteManager.input")
        input_mock.side_effect = ["2", "f"]
        exit_mock = mocker.patch("NoteManager.exit")

        noteManager = NoteManager()
        noteManager.main_menu()

        assert input_mock.call_count == 2
        assert exit_mock.call_count == 1

    def test_back_to_menu_from_show_note_menu(self, mocker):
        mocker.patch("NoteManager.open")
        json_mock = mocker.patch("NoteManager.json.load")
        json_mock.return_value = DUMMY_NOTES
        input_mock = mocker.patch("NoteManager.input")
        input_mock.side_effect = ["2", "a", "1" "3", "3"]
        exit_mock = mocker.patch("NoteManager.exit")

        noteManager = NoteManager()
        noteManager.main_menu()

        assert input_mock.call_count == 5
        assert exit_mock.call_count == 1


class TestNote:

    def test_set_title(self, mocker):
        input_mock = mocker.patch("Note.input")
        input_mock.return_value = "newTitle"
        note = Note()
        note.set_title()
        assert note.title == "newTitle"
    
    def test_set_content(self, mocker):
        input_mock = mocker.patch("Note.input")
        input_mock.return_value = "newContent"
        note = Note()
        note.set_content()
        assert note.content == "newContent"
        