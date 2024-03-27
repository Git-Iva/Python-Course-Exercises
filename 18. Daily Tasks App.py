# Command line app for users to enter notes of the day
# Once done, notes saved in a "today".txt file

import datetime


def tasks_today():
    # Get today's date and time
    today = datetime.date.today()
    filename = f"{today}.txt"

    # User enters notes; program exits when user types exit
    print("Enter your notes from today. Type exit to save and exit.")
    notes = []
    while True:
        updated_notes = input()
        if updated_notes == "exit":
            break
        notes.append(updated_notes)

    # Join all notes into a single string
    content = "\n".join(notes)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    print("Your notes have been savade to {filename}")


if __name__ == "__main__":
    tasks_today()