class Product:
    def __init__(self, product_id, product_name, quantity_in_stock):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__quantity_in_stock = quantity_in_stock


    def get_product_id(self):
        return self.__product_id

    def get_product_name(self):
        return self.__product_name

    def get_quantity_in_stock(self):
        return self.__quantity_in_stock

    
    def set_product_id(self, product_id):
        self.__product_id = product_id

    def set_product_name(self, product_name):
        self.__product_name = product_name

    def set_quantity_in_stock(self, quantity):
        if quantity >= 0:
            self.__quantity_in_stock = quantity
        else:
            print("Quantity cannot be negative")

    
    def add_stock(self, quantity):
        if quantity > 0:
            self.__quantity_in_stock += quantity
            print(f"Added {quantity} units to stock")
        else:
            print("Invalid quantity. Must be greater than 0")

    def reduce_stock(self, quantity):
        if 0 < quantity <= self.__quantity_in_stock:
            self.__quantity_in_stock -= quantity
            print(f"Reduced {quantity} units from stock")
        
        elif quantity > self.__quantity_in_stock:
            print("Cannot reduce more than available stock")
        
        else:
            print("Invalid quantity. Must be greater than 0")


    product_id = property(get_product_id, set_product_id)
    product_name = property(get_product_name, set_product_name)
    quantity_in_stock = property(get_quantity_in_stock, set_quantity_in_stock)


product = Product(1001, "Smartphone", 50)
print(product.product_id)
print(product.product_name)
print(product.quantity_in_stock)

product.add_stock(30)
print(product.quantity_in_stock)

product.reduce_stock(20)
print(product.quantity_in_stock)

product.reduce_stock(100)
