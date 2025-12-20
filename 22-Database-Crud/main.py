# main.py

import sqlite3

DB_NAME = "app.db"

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_user(name, age):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()
    print("✅ User added.")

def view_users():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    conn.close()

    if not rows:
        print("No users found.")
        return

    print("\n🗃️ Users:")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")

def update_user(user_id, name, age):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("UPDATE users SET name = ?, age = ? WHERE id = ?", (name, age, user_id))
    conn.commit()
    conn.close()
    print("✅ User updated.")

def delete_user(user_id):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    print("✅ User deleted.")

def main():
    create_table()

    while True:
        print("\n🗃️ Database CRUD App")
        print("1. Add user")
        print("2. View users")
        print("3. Update user")
        print("4. Delete user")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Name: ")
            age = int(input("Age: "))
            add_user(name, age)

        elif choice == "2":
            view_users()

        elif choice == "3":
            user_id = int(input("User ID to update: "))
            name = input("New name: ")
            age = int(input("New age: "))
            update_user(user_id, name, age)

        elif choice == "4":
            user_id = int(input("User ID to delete: "))
            delete_user(user_id)

        elif choice == "5":
            print("Goodbye.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
