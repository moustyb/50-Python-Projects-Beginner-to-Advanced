# Project 4: Word Counter
# Description: Count words and characters in a given text or file

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    return len(text)

def word_counter():
    print("📖 Welcome to the Word Counter!")
    choice = input("Do you want to enter text manually or read from a file? (text/file): ").lower()

    if choice == "text":
        text = input("Enter your text: ")
    elif choice == "file":
        filename = input("Enter the filename: ")
        try:
            with open(filename, "r") as f:
                text = f.read()
        except FileNotFoundError:
            print("Error: File not found.")
            return
    else:
        print("Invalid choice.")
        return

    print(f"Word count: {count_words(text)}")
    print(f"Character count: {count_characters(text)}")

if __name__ == "__main__":
    word_counter()
