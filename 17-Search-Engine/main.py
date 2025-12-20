# main.py
import os
import string

def index_files(folder):
    index = {}  # word -> set of filenames

    if not os.path.exists(folder):
        print("Folder does not exist.")
        return index

    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            filepath = os.path.join(folder, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    text = f.read().lower()

                    # Remove punctuation
                    for p in string.punctuation:
                        text = text.replace(p, " ")

                    words = text.split()

                    for word in words:
                        if word not in index:
                            index[word] = set()
                        index[word].add(filename)

            except Exception as e:
                print(f"Error reading {filename}: {e}")

    return index


def search(index, keyword):
    keyword = keyword.lower()
    if keyword in index:
        return index[keyword]
    return set()


def main():
    print("🔍 Mini Search Engine")
    folder = input("Enter folder path containing .txt files: ").strip()

    print("\nIndexing files...")
    index = index_files(folder)
    print("Indexing complete!")

    while True:
        keyword = input("\nEnter keyword to search (or 'quit' to exit): ").strip()
        if keyword.lower() == "quit":
            print("Goodbye!")
            break

        results = search(index, keyword)
        if results:
            print(f"\nKeyword '{keyword}' found in:")
            for file in results:
                print(" -", file)
        else:
            print(f"\nNo results for '{keyword}'.")


if __name__ == "__main__":
    main()
