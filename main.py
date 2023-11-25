import json
import datetime


class Note:
    def __init__(self, id, title, body, date):
        self.id = id
        self.title = title
        self.body = body
        self.date = date


class NoteApp:
    def __init__(self):
        self.notes = []

    def add_note(self, title, body):
        new_id = len(self.notes) + 1
        new_note = Note(new_id, title, body, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.notes.append(new_note)
        self.save_notes()

    def read_notes(self, filter_date=None):
        if filter_date:
            filtered_notes = [note for note in self.notes if note.date[:10] == filter_date]
            for note in filtered_notes:
                print(f"ID: {note.id}, Title: {note.title}, Body: {note.body}, Date: {note.date}")
        else:
            for note in self.notes:
                print(f"ID: {note.id}, Title: {note.title}, Body: {note.body}, Date: {note.date}")

    def edit_note(self, id, title, body):
        for note in self.notes:
            if note.id == id:
                note.title = title
                note.body = body
                note.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_notes()
                print("Заметка успешно отредактирована.")
                return
        print("Заметка не найдена.")

    def delete_note(self, id):
        for note in self.notes:
            if note.id == id:
                self.notes.remove(note)
                self.save_notes()
                print("Заметка успешно удалена.")
                return
        print("Заметка не найдена.")

    def save_notes(self):
        data = []
        for note in self.notes:
            data.append({"id": note.id, "title": note.title, "body": note.body, "date": note.date})
        with open('notes.json', 'w') as file:
            json.dump(data, file)
            print('Заметка успешно сохранена')

    def load_notes(self):
        try:
            with open('notes.json', 'r') as file:
                data = json.load(file)
                for item in data:
                    new_note = Note(item["id"], item["title"], item["body"], item["date"])
                    self.notes.append(new_note)
        except FileNotFoundError:
            pass



app = NoteApp()
app.load_notes()

while True:
    command = input("Enter command (add, read, edit, delete, exit): ")

    if command == "add":
        title = input("Enter note title: ")
        body = input("Enter note body: ")
        app.add_note(title, body)
    elif command == "read":
        filter_date = input("Enter filter date (YYYY-MM-DD) or leave empty: ")
        app.read_notes(filter_date)
    elif command == "edit":
        id = int(input("Введите ID заметки для редактирования: "))
        title = input("Введите новое название: ")
        body = input("Введите изиенения в заметке : ")
        app.edit_note(id, title, body)
    elif command == "delete":
        id = int(input("Введите ID заметки для удаления: "))
        app.delete_note(id)
    elif command == "exit":
        break
    else:
        print("Invalid command.")
