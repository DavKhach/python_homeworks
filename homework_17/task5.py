def display_products(**product_details):
    details = []
    for key, value in product_details.items():
        details.append(f"{key.capitalize()}: {value}")
    return "\n".join(details)

product = {
    'name': 'Laptop',
    'brand': 'Acer',
    'price': 399.99,
    'stock': 20
}

product_info = display_products(**product)
print(product_info)
