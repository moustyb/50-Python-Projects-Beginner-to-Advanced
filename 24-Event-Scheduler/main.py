# main.py

import json
from datetime import datetime

DATA_FILE = "events.json"

def load_events():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_events(events):
    with open(DATA_FILE, "w") as f:
        json.dump(events, f, indent=4)

def add_event():
    title = input("Event title: ")
    date_str = input("Date (YYYY-MM-DD): ")
    time_str = input("Time (HH:MM): ")

    try:
        datetime.strptime(date_str + " " + time_str, "%Y-%m-%d %H:%M")
    except ValueError:
        print("Invalid date or time format.")
        return

    events = load_events()
    events.append({"title": title, "date": date_str, "time": time_str})
    save_events(events)
    print("✅ Event added.")

def view_events():
    events = load_events()
    if not events:
        print("No events scheduled.")
        return

    print("\n🗓️ Upcoming Events:")
    for e in events:
        print(f"- {e['date']} {e['time']} — {e['title']}")

def delete_event():
    events = load_events()
    if not events:
        print("No events to delete.")
        return

    view_events()
    index = int(input("Enter event number to delete (1-N): ")) - 1

    if 0 <= index < len(events):
        removed = events.pop(index)
        save_events(events)
        print(f"✅ Deleted: {removed['title']}")
    else:
        print("Invalid selection.")

def main():
    while True:
        print("\n🗓️ Event Scheduler")
        print("1. Add event")
        print("2. View events")
        print("3. Delete event")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_event()
        elif choice == "2":
            view_events()
        elif choice == "3":
            delete_event()
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
