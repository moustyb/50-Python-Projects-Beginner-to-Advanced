# main.py

class ShoppingCart:
    def __init__(self):
        self.items = {}  # item_name -> quantity

    def add_item(self, name, quantity):
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity
        print(f"Added {quantity} x {name}")

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
            print(f"Removed {name}")
        else:
            print("Item not found in cart.")

    def update_quantity(self, name, quantity):
        if name in self.items:
            self.items[name] = quantity
            print(f"Updated {name} to {quantity}")
        else:
            print("Item not found in cart.")

    def view_cart(self):
        if not self.items:
            print("Cart is empty.")
            return
        print("\n🛒 Your Cart:")
        for name, qty in self.items.items():
            print(f"- {name}: {qty}")

    def checkout(self):
        if not self.items:
            print("Cart is empty.")
            return
        print("\n✅ Checkout Summary:")
        for name, qty in self.items.items():
            print(f"- {name}: {qty}")
        print("Thank you for shopping!")


def main():
    cart = ShoppingCart()

    while True:
        print("\n🛒 Shopping Cart Menu")
        print("1. Add item")
        print("2. Remove item")
        print("3. Update quantity")
        print("4. View cart")
        print("5. Checkout")
        print("6. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Item name: ")
            qty = int(input("Quantity: "))
            cart.add_item(name, qty)

        elif choice == "2":
            name = input("Item name to remove: ")
            cart.remove_item(name)

        elif choice == "3":
            name = input("Item name: ")
            qty = int(input("New quantity: "))
            cart.update_quantity(name, qty)

        elif choice == "4":
            cart.view_cart()

        elif choice == "5":
            cart.checkout()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
