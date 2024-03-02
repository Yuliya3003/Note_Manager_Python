from datetime import datetime


class View:

    def __init__(self, note_manager):
        self.note_manager = note_manager

    @staticmethod
    def get_user_choice():
        print("Выберите действие:")
        print("1. Создать заметку")
        print("2. Просмотреть заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Сохранить заметки")
        print("6. Загрузить заметки")
        print("7. Просмотреть заметку по id")
        print("8. Отфильтровать по дате")
        print("9. Выйти")

        choice = input("Введите номер действия: ")
        return choice

    @staticmethod
    def get_note_details():
        title = input("Введите заголовок заметки: ")
        body = input("Введите текст заметки: ")
        return title, body

    @staticmethod
    def get_note_id():
        return input("Введите ID заметки: ")

    @staticmethod
    def get_start_time():
        start_time_str = input("Введите начальное время в формате ГГГГ-ММ-ДД ЧЧ:ММ:СС: ")
        try:
            start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S")
            return start_time
        except ValueError:
            print("Неправильный формат времени. Пожалуйста, введите время в формате ГГГГ-ММ-ДД ЧЧ:ММ:СС.")
            return None

    @staticmethod
    def get_end_time():
        end_time_str = input("Введите конечное время в формате ГГГГ-ММ-ДД ЧЧ:ММ:СС: ")
        try:
            end_time = datetime.strptime(end_time_str, "%Y-%m-%d %H:%M:%S")
            return end_time
        except ValueError:
            print("Неправильный формат времени. Пожалуйста, введите время в формате ГГГГ-ММ-ДД ЧЧ:ММ:СС.")
            return None

    def run(self):
        while True:
            choice = self.get_user_choice()

            if choice == "1":
                title, body = self.get_note_details()
                while not title:
                    print('Нельзя создать заметку с пустым названием.')
                    title = input('Введите заголовок заметки: ')
                self.note_manager.create_note(title, body)
                self.note_manager.save_to_json('notes.json')
                print(f"Создана заметка с заголовком '{title}' и текстом '{body}'.")
            elif choice == "2":
                self.note_manager.read_notes()
                print("Просмотр заметок:")
            elif choice == "3":
                note_id = self.get_note_id()
                if note_id:
                    title, body = self.get_note_details()
                    if not title:
                        title = self.note_manager.notes[note_id].title
                    if not body:
                        body = self.note_manager.notes[note_id].body
                    self.note_manager.edit_note(note_id, title, body)
                    self.note_manager.save_to_json('notes.json')
                    print(f"Заметка с ID '{note_id}' изменена на заголовок '{title}' и текст '{body}'.")
            elif choice == "4":
                note_id = self.get_note_id()
                if self.note_manager.delete_note(note_id):
                    print(f"Заметка с ID '{note_id}' удалена.")
                    self.note_manager.save_to_json('notes.json')
            elif choice == "5":
                self.note_manager.save_to_json('notes.json')
                print('Все заметки успешно сохранены.')
            elif choice == "6":
                self.note_manager.load_from_json('notes.json')
                print('Заметки загружены из файла')
            elif choice == "7":
                note_id = self.get_note_id()
                self.note_manager.read_note(note_id)
            elif choice == "8":
                start_time = self.get_start_time()
                while not start_time:
                    start_time = self.get_start_time()
                end_time = self.get_end_time()
                while not end_time:
                    end_time = self.get_end_time()
                filtered_note = self.note_manager.filter_notes_by_date(start_time, end_time)
                if filtered_note:
                    for note in filtered_note:
                        print(note)
                else:
                    print("За выбранный период времени нет заметок")
            elif choice == "9":
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор. Пожалуйста, введите число от 1 до 7.")
