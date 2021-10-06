from Note import Note

class NoteManager:
    def __init__(self, notes_list=[]):
        self.notes_list = notes_list

    def main_menu(self):
        print("Welcome in Notebook\n"
            "What do you want to do:\n"
            "\t1 - Add note\n"
            "\t2 - View the note list")
                
        response = input()
        if response == "1":
            self.add_note()
        elif response == "2":
            self.view_the_note()
        else:
            exit()

    def add_note(self):
        print("Add title of note")
        title = input()
        print("Here write the contents")
        contents = input()
        
        self.notes_list.append(Note(title, contents))
        self.main_menu()

    def view_the_note(self):
        i = 1
        for note in self.notes_list:
            print(f"  {i} - {note}")
            i += 1
        print("a - Choose and open note\n"
            "s - Delete the note\n"
            "d - Back to the main menu\n"
            "f - Exit")
        answer = input()
        
        if answer == "a":
            self.choose_note()
        elif answer == "s":
            self.delete_note()
        elif answer == "d":
            self.main_menu()
        else:
            exit()

    def choose_note(self):
        pass
            #here user will choose the note and the program opens it
      
    def delete_note(self):
        print("Choose the note which you want to delete")
            #here will be the number of the note, which the user wants to delete
