from NoteManager import NoteManager
from Note import Note
from unittest.mock import call
import pytest

DUMMY_NOTES = [{"title": "someTitle", "content": "someContent", "date": "2021-10-07"}]

@pytest.fixture
def json_load(mocker):
    json_mock = mocker.patch("NoteManager.json.load")
    json_mock.return_value = DUMMY_NOTES
    return json_mock


@pytest.fixture
def open(mocker):
    open = mocker.patch("NoteManager.open")
    return open


@pytest.fixture
def input_note_manager(mocker):
    input_mock = mocker.patch("NoteManager.input")
    return input_mock


@pytest.fixture
def exit(mocker):
    exit_mock = mocker.patch("NoteManager.exit")
    return exit_mock


@pytest.fixture
def note(mocker):
    note_mock = mocker.patch("NoteManager.Note")
    return note_mock


@pytest.fixture
def json_dump(mocker):
    dump_mock = mocker.patch("NoteManager.json.dump")
    return dump_mock


@pytest.fixture
def input_note(mocker):
    input_mock = mocker.patch("Note.input")
    return input_mock


class TestNoteManager:

    def test_create_noteManager_object(self, open, json_load):
        NoteManager()

    def test_exit_from_main_menu(self, open, json_load, input_note_manager, exit):
        input_note_manager.return_value = "3"

        noteManager = NoteManager()
        noteManager.main_menu()

        assert exit.call_count == 1
    
    def test_add_note_from_main_menu(self, open, json_load, json_dump, input_note_manager, note, exit):
        input_note_manager.side_effect = ["1", "title", "content", "3"]
        
        noteManager = NoteManager()
        noteManager.main_menu()
        args, kwargs = json_dump.call_args

        assert len(args[0]) == 2
        note.assert_has_calls([
            call("someTitle", "someContent", "2021-10-07"), call("title", "content")])
        assert input_note_manager.call_count == 4
        assert exit.call_count == 1
    
    def test_change_title_from_show_all_notes(self, open, json_load, input_note_manager, note, json_dump, exit):
        input_note_manager.side_effect = ["2", "a", "1", "1", "3"]

        noteManager = NoteManager()
        noteManager.main_menu()

        note.assert_has_calls([call("someTitle", "someContent", "2021-10-07")])
        note.change_title.assert_called_once       
        
    def test_change_content_from_show_all_notes(self, open, json_load, note, input_note_manager, json_dump, exit):
        input_note_manager.side_effect = ["2", "a", "1", "2", "3"]

        noteManager = NoteManager()
        noteManager.main_menu()

        note.assert_has_calls([call("someTitle", "someContent", "2021-10-07")])
        note.change_content.assert_called_once 
        
    def test_delete_note_from_show_notes_list_menu(self, open, json_load, input_note_manager, json_dump, exit):
        input_note_manager.side_effect = ["2", "s", "1", "3"]

        noteManager = NoteManager()
        noteManager.main_menu()

        assert input_note_manager.call_count == 4
        args, kwargs = json_dump.call_args
        assert args[0] == []
        assert exit.call_count == 1

    def test_back_to_main_menu_from_show_notes_list_menu(self, open, json_load, input_note_manager, exit):
        input_note_manager.side_effect = ["2", "d", "3"]

        noteManager = NoteManager()
        noteManager.main_menu()

        assert input_note_manager.call_count == 3
        assert exit.call_count == 1
    
    def test_exit_from_show_notes_list_menu(self, open, json_load, input_note_manager, exit):
        input_note_manager.side_effect = ["2", "f"]

        noteManager = NoteManager()
        noteManager.main_menu()

        assert input_note_manager.call_count == 2
        assert exit.call_count == 1

    def test_back_to_menu_from_show_note_menu(self, mocker, open, json_load, input_note_manager, exit):
        input_note_manager.side_effect = ["2", "a", "1" "3", "3"]

        noteManager = NoteManager()
        noteManager.main_menu()

        assert input_note_manager.call_count == 5
        assert exit.call_count == 1


class TestNote:

    def test_set_title(self, input_note):
        input_note.return_value = "newTitle"
        note = Note()
        note.set_title()
        assert note.title == "newTitle"
    
    def test_set_content(self, input_note):
        input_note.return_value = "newContent"
        note = Note()
        note.set_content()
        assert note.content == "newContent"
        