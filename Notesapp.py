FILE = "notes.txt"


def add_note():
    title = input("Title: ")
    content = input("Note: ")

    with open(FILE, "a") as file:
        file.write(f"{title}|{content}\n")

    print("Note added.")


def view_notes():
    try:
        with open(FILE, "r") as file:
            notes = file.readlines()
    except FileNotFoundError:
        print("No notes found.")
        return

    if not notes:
        print("No notes found.")
        return

    for index, note in enumerate(notes, 1):
        title, content = note.strip().split("|", 1)

        print(f"\n{index}. {title}")
        print(content)


def delete_note():
    try:
        with open(FILE, "r") as file:
            notes = file.readlines()
    except FileNotFoundError:
        print("No notes found.")
        return

    if not notes:
        print("No notes found.")
        return

    view_notes()

    try:
        number = int(input("Enter note number to delete: "))

        if number < 1 or number > len(notes):
            print("Invalid note number.")
            return

        notes.pop(number - 1)

        with open(FILE, "w") as file:
            file.writelines(notes)

        print("Note deleted.")

    except ValueError:
        print("Enter a valid number.")


def main():
    while True:
        print("\nNotes App")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_note()

        elif choice == "2":
            view_notes()

        elif choice == "3":
            delete_note()

        elif choice == "4":
            break

        else:
            print("Invalid choice.")


main()