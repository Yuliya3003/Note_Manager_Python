from NoteManager import NoteManager
from View import View

if __name__ == "__main__":
    note_manager = NoteManager()
    view = View(note_manager)
    view.run()
