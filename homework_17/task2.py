def total_price(*item_prices, tax_rate = 0.1):
    subtotal = 0
    for price in item_prices:
        subtotal += price
    total_price = subtotal * (tax_rate + 1)
    return total_price


print(total_price(10,20,5))
