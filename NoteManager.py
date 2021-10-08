from Note import Note
import json


class NoteManager:
    def __init__(self, notes_list=[]):
        self.notes_list = notes_list
        with open("jsonFile.json") as json_file:
            data = json.load(json_file)
        
        self.notes_list = [Note(d["title"], d["content"], d["date"]) for d in data]

    def main_menu(self):
        print(
            "Welcome in Notebook\n"
            "What do you want to do:\n"
            "\t1 - Add note\n"
            "\t2 - View the note list\n"
            "\t3 - Exit")
        response = input()
        try:
            dictMainMenu = {
                "1": self.add_note,
                "2": self.show_all_notes,
            }
            dictMainMenu[response]()
        except:
            exit()

    def add_note(self):
        print("Add title of note")
        title = input()
        print("Here write the content")
        content = input()

        self.notes_list.append(Note(title, content))
        self.__save_notes_list()
        self.main_menu()

    def show_all_notes(self):
        i = 1
        for note in self.notes_list:
            print(f"  {i} - {note}")
            i += 1
        self.show_notes_list_menu()

    def show_notes_list_menu(self):
        print(
            "a - Choose and open note\n"
            "s - Delete the note\n"
            "d - Back to the main menu\n"
            "f - Exit")
        response = input()
        try:
            dictMenu = {
                "a": self.show_note,
                "s": self.delete_note,
                "d": self.main_menu
            }
            dictMenu[response]()
        except:
            exit()

    def show_note(self):
        print("Enter the number of the note you want to show")
        noteIndex = input()

        if self.__is_index_valid(noteIndex):
            noteToShow = self.notes_list[int(noteIndex) - 1]
            print(noteToShow)
            self.show_note_menu(int(noteIndex) - 1)
        else:
            self.show_note()

    def show_note_menu(self, noteIndex):
        print(
            "What do you want to do:\n"
            "\t1 - Change title\n"
            "\t2 - Change content\n"
            "\t3 - Back to main menu")
        answer = input()

        dict = {
            "1": self.notes_list[noteIndex].set_title,
            "2": self.notes_list[noteIndex].set_content,
            "3": self.main_menu
            }
        dict[answer]()
        self.__save_notes_list()
        self.main_menu()

    def delete_note(self):
        print("Choose the note you want to delete")
        noteIndex = input()

        if self.__is_index_valid(noteIndex):
            del self.notes_list[int(noteIndex) - 1]
            self.__save_notes_list()
            self.main_menu()
        else:
            self.delete_note()

    def __is_index_valid(self, x):
        try:
            if int(x) not in range(1, len(self.notes_list) + 1):
                print("You entered the wrong number. Please select the number from given in list")
                return False
            else:
                return True
        except:
            print("You have to use only numbers")
            return False

    def __save_notes_list(self):
        with open("jsonFile.json", "w", encoding="utf-8") as outfile:
            json.dump([obj.__dict__ for obj in self.notes_list], outfile, ensure_ascii=False, indent=4)
