# main.py

import pandas as pd
import matplotlib.pyplot as plt

def load_file():
    filename = input("Enter CSV or Excel filename: ")

    try:
        if filename.lower().endswith(".csv"):
            df = pd.read_csv(filename)
        elif filename.lower().endswith((".xlsx", ".xls")):
            df = pd.read_excel(filename)
        else:
            print("Unsupported file type.")
            return None

        print("\n✅ File loaded successfully.")
        print("\n📊 Data Preview:")
        print(df.head())

        return df

    except FileNotFoundError:
        print("❌ File not found.")
        return None

def show_summary(df):
    print("\n📈 Summary Statistics:")
    print(df.describe(include="all"))

def plot_column(df):
    print("\nAvailable columns:")
    for col in df.columns:
        print(f"- {col}")

    column = input("\nEnter column name to plot: ")

    if column not in df.columns:
        print("❌ Column not found.")
        return

    try:
        plt.figure(figsize=(10, 5))
        plt.plot(df[column])
        plt.title(f"Plot of {column}")
        plt.xlabel("Index")
        plt.ylabel(column)
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print("❌ Unable to plot this column.")
        print(e)

def main():
    df = None

    while True:
        print("\n📊 Data Dashboard")
        print("1. Load CSV/Excel file")
        print("2. Show summary statistics")
        print("3. Plot a column")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            df = load_file()

        elif choice == "2":
            if df is not None:
                show_summary(df)
            else:
                print("Load a file first.")

        elif choice == "3":
            if df is not None:
                plot_column(df)
            else:
                print("Load a file first.")

        elif choice == "4":
            print("Goodbye.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
