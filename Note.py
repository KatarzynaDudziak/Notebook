from datetime import date


class Note:
    def __init__(self, title="", content="", pDate=str(date.today())):
        self.title = title
        self.date = pDate
        self.content = content
    
    def __repr__(self) -> str:
        return f"{self.title}, {self.content}, {self.date}"

    def set_title(self):
        print("Enter new title")
        newTitle = input()
        self.title = newTitle
        
    def set_content(self):
        print("Enter new content")
        newContent = input()
        self.content = newContent
