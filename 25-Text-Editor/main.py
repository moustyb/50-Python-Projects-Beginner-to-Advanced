# main.py

def create_document():
    print("\nStart typing your text. Type ':save' on a new line to finish.\n")
    lines = []
    while True:
        line = input()
        if line == ":save":
            break
        lines.append(line)
    return "\n".join(lines)

def save_document(text):
    filename = input("Enter filename to save (example: notes.txt): ")
    with open(filename, "w") as f:
        f.write(text)
    print(f"✅ Saved as {filename}")

def load_document():
    filename = input("Enter filename to load: ")
    try:
        with open(filename, "r") as f:
            content = f.read()
        print("\n📄 File Content:\n")
        print(content)
    except FileNotFoundError:
        print("❌ File not found.")

def main():
    while True:
        print("\n🖊️ Text Editor")
        print("1. Create new document")
        print("2. Load existing document")
        print("3. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            text = create_document()
            save_document(text)

        elif choice == "2":
            load_document()

        elif choice == "3":
            print("Goodbye.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
