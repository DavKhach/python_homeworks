class ShoppingCart:
    class Item:
        def __init__(self, name, price):
            self.name = name
            self.price = price

    def __init__(self):
        self.__items = []

    def add_item(self, name, price):
        if price >= 0:
            item = self.Item(name, price)
            self.__items.append(item)
            print(f"Added {name} to the cart")
        else:
            print("Price can't be negative. Item not added")

    def remove_item(self, name):
        for item in self.__items:
            if item.name == name:
                self.__items.remove(item)
                print(f"Removed {name} from the cart")
                return
        print(f"Item {name} not found in the cart")


    def total_items(self):
        return len(self.__items)

    def display_cart(self):
        if not self.__items:
            print("Your cart is empty")
        else:
            print("Items in your cart:")
            for item in self.__items:
                print(f"- {item.name}: ${item.price:.2f}")
            print(f"Total number of items: {self.total_items()}")


cart = ShoppingCart()
cart.add_item("Laptop", 1299.99)
cart.add_item("Mouse", 39.99)
cart.add_item("Keyboard", 89.99)
cart.display_cart()


cart.remove_item("Mouse")
cart.display_cart()


cart.remove_item("Tablet")
