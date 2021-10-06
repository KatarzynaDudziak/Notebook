import json
from datetime import date


class Note:
    def __init__(self, title="", contents=""):
        self.title = title
        self.date = date.today()
        self.contents = contents
    
    def __repr__(self) -> str:
        return f"{self.title}, {self.date}"
