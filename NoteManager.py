import json
import os
from datetime import datetime, timedelta

from Note import Note


class NoteManager:
    def __init__(self):
        self.notes = {}
        if os.path.exists('notes.json'):
            self.load_from_json('notes.json')

    def create_note(self, title, body):
        new_note = Note(title, body)
        self.notes[new_note.note_id] = new_note

    def read_note(self, note_id):
        if note_id not in self.notes:
            print(f"Note with ID {note_id} not found.")
            return
        print(self.notes[note_id])

    def read_notes(self):
        if not self.notes:
            print("No notes available.")
        else:
            sorted_notes = sorted(self.notes.items(), key=lambda x: x[1].creation_time)
            self.notes = {note_id: note for note_id, note in sorted_notes}
            for note in self.notes.values():
                print(note)


    def edit_note(self, note_id, new_title=None, new_body=None):
        if note_id not in self.notes:
            print(f"Note with ID {note_id} not found.")
            return
        note = self.notes[note_id]
        if new_title:
            note.update_title(new_title)
        if new_body:
            note.update_body(new_body)
        self.notes[note_id] = note
        sorted_notes = sorted(self.notes.items(), key=lambda x: x[1].creation_time)
        self.notes = {note_id: note for note_id, note in sorted_notes}

    def delete_note(self, note_id):
        if note_id not in self.notes:
            print(f"Note with ID {note_id} not found.")
            return
        else:
            del self.notes[note_id]
            return True

    def filter_notes_by_date(self, start_date=None, end_date=None):
        filtered_notes = []
        for note_id in self.notes:
            if start_date and self.notes[note_id].creation_time < start_date:
                continue
            if end_date and self.notes[note_id].creation_time > end_date + timedelta(days=1):
                break
            filtered_notes.append(self.notes[note_id])
        return filtered_notes

    def save_to_json(self, filename):
        with open(filename, "w") as file:
            json.dump([note.to_json() for note in self.notes.values()], file, indent=4)

    def load_from_json(self, filename):
        with open(filename, "r") as file:
            json_data = json.load(file)
            self.notes = {note_data["note_id"]: Note.from_json(note_data) for note_data in json_data}
