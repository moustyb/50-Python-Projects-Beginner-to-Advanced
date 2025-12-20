# main.py

import json

DATA_FILE = "inventory.json"

def load_inventory():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_inventory(inventory):
    with open(DATA_FILE, "w") as f:
        json.dump(inventory, f, indent=4)

def add_item():
    name = input("Item name: ").strip()
    quantity = int(input("Quantity: "))
    inventory = load_inventory()

    if name in inventory:
        inventory[name] += quantity
    else:
        inventory[name] = quantity

    save_inventory(inventory)
    print(f"✅ Added {quantity} x {name}")

def view_inventory():
    inventory = load_inventory()
    if not inventory:
        print("Inventory is empty.")
        return

    print("\n📦 Current Inventory:")
    for item, qty in inventory.items():
        print(f"- {item}: {qty}")

def update_item():
    inventory = load_inventory()
    if not inventory:
        print("Inventory is empty.")
        return

    view_inventory()
    name = input("Item to update: ").strip()

    if name not in inventory:
        print("❌ Item not found.")
        return

    new_qty = int(input("New quantity: "))
    inventory[name] = new_qty
    save_inventory(inventory)
    print(f"✅ Updated {name} to {new_qty}")

def remove_item():
    inventory = load_inventory()
    if not inventory:
        print("Inventory is empty.")
        return

    view_inventory()
    name = input("Item to remove: ").strip()

    if name in inventory:
        del inventory[name]
        save_inventory(inventory)
        print(f"✅ Removed {name}")
    else:
        print("❌ Item not found.")

def main():
    while True:
        print("\n📦 Inventory Manager")
        print("1. Add item")
        print("2. View inventory")
        print("3. Update item")
        print("4. Remove item")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            view_inventory()
        elif choice == "3":
            update_item()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
