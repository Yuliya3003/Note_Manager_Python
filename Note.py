from datetime import datetime
import uuid

class Note:
    def __init__(self, title, body):
        self.note_id = str(uuid.uuid4())
        self.title = title
        self.body = body
        self.creation_time = datetime.now()

    def __str__(self):
        return (f"Note ID: {self.note_id}\n"
                f"Title: {self.title}\n"
                f"Body: {self.body}\n"
                f"Created: {self.creation_time}\n"
                )

    def update_body(self, new_body):
        self.body = new_body
        self.creation_time = datetime.now()

    def update_title(self, new_title):
        self.title = new_title
        self.creation_time = datetime.now()

    def to_json(self):
        return {
            "note_id": self.note_id,
            "title": self.title,
            "body": self.body,
            "creation_time": self.creation_time.strftime("%Y-%m-%d %H:%M:%S"),
        }

    @staticmethod
    def from_json(json_data):
        note = Note("", "")
        note.note_id = json_data["note_id"]
        note.title = json_data["title"]
        note.body = json_data["body"]
        note.creation_time = datetime.strptime(json_data["creation_time"], "%Y-%m-%d %H:%M:%S")
        return note