from abc import ABC, abstractmethod


class MenuItem:
    __slots__ = ['name', 'price', 'ingredients']

    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def __str__(self):
        return f"{self.name}: ${self.price} (Ingredients: {', '.join(self.ingredients)})"


class Appetizer(MenuItem):
    __slots__ = []


class Entree(MenuItem):
    __slots__ = []


class Dessert(MenuItem):
    __slots__ = []


class Customer:
    __slots__ = ['name', 'contact_info', 'order_history']

    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.order_history = []

    def place_order(self, order):
        self.order_history.append(order)
        print(f"{self.name} placed an order.")

    def view_order_history(self):
        if self.order_history:
            print(f"Order history for {self.name}:")
            for order in self.order_history:
                print(order)
        else:
            print(f"{self.name} has no order history.")


class Order(ABC):
    __slots__ = ['customer', 'menu_items', 'total_price']

    def __init__(self, customer):
        self.customer = customer
        self.menu_items = []
        self.total_price = 0.0

    def add_menu_item(self, item):
        self.menu_items.append(item)
        self.total_price += item.price

    def calculate_total(self):
        self.total_price = sum(item.price for item in self.menu_items)
        return self.total_price

    @abstractmethod
    def __str__(self):
        pass


class DineInOrder(Order):
    __slots__ = []

    def __str__(self):
        items = '\n'.join([str(item) for item in self.menu_items])
        return f"Dine-in Order by {self.customer.name}:\n{items}\nTotal: ${self.total_price}"


class TakeawayOrder(Order):
    __slots__ = []

    def __str__(self):
        items = '\n'.join([str(item) for item in self.menu_items])
        return f"Takeaway Order by {self.customer.name}:\n{items}\nTotal: ${self.total_price}"


class DeliveryOrder(Order):
    __slots__ = ['delivery_address']

    def __init__(self, customer, delivery_address):
        super().__init__(customer)
        self.delivery_address = delivery_address

    def __str__(self):
        items = '\n'.join([str(item) for item in self.menu_items])
        return f"Delivery Order by {self.customer.name} to {self.delivery_address}:\n{items}\nTotal: ${self.total_price}"


class Review:
    __slots__ = ['customer_name', 'order', 'rating', 'comments']

    def __init__(self, customer_name, order, rating, comments):
        self.customer_name = customer_name
        self.order = order
        self.rating = rating
        self.comments = comments

    def __str__(self):
        return f"Review by {self.customer_name}:\nRating: {self.rating}\nComments: {self.comments}\n"


if __name__ == "__main__":
    appetizer = Appetizer("Cheese Fries", 7.99, ["potato", "cheese"])
    entree = Entree("Spaghetti", 12.99, ["pasta", "meat sauce"])
    dessert = Dessert("Tiramisu", 6.99, ["coffee", "cream", "cocoa"])

    customer1 = Customer("John Doe", "093-43-89-82")

    order1 = DineInOrder(customer1)
    order1.add_menu_item(appetizer)
    order1.add_menu_item(entree)
    order1.calculate_total()
    customer1.place_order(order1)

    review1 = Review(customer1.name, order1, 5, "The food was amazing")

    customer1.view_order_history()
    print(review1)

    # try:
    #     customer1.address = "Wrong address"
    # except AttributeError as e:
    #     print(e)
