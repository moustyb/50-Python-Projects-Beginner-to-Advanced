# Project 10: Calendar Reminder
# Description: Lets users set and view reminders. Builds skills in working with dates, lists, and user interaction.

from datetime import datetime

# Store reminders in a list of dictionaries
reminders = []

def add_reminder():
    """Add a new reminder with title, date, and time."""
    title = input("Enter reminder title: ")
    date_str = input("Enter date (YYYY-MM-DD): ")
    time_str = input("Enter time (HH:MM in 24-hour format): ")

    try:
        reminder_datetime = datetime.strptime(date_str + " " + time_str, "%Y-%m-%d %H:%M")
        reminders.append({"title": title, "datetime": reminder_datetime})
        print("✅ Reminder added successfully!\n")
    except ValueError:
        print("❌ Invalid date or time format. Please try again.\n")

def view_reminders():
    """View all reminders sorted by date and time."""
    if not reminders:
        print("📭 No reminders set.\n")
        return

    print("📅 Your Reminders:")
    for r in sorted(reminders, key=lambda x: x["datetime"]):
        print(f"- {r['title']} at {r['datetime'].strftime('%Y-%m-%d %H:%M')}")
    print()

def calendar_reminder():
    """Main menu loop for Calendar Reminder."""
    while True:
        print("🔔 Calendar Reminder")
        print("1. Add Reminder")
        print("2. View Reminders")
        print("3. Quit")

        choice = input("Enter choice (1-3): ")

        if choice == "1":
            add_reminder()
        elif choice == "2":
            view_reminders()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    calendar_reminder()

