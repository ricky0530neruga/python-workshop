"""
def totalprice (a, b):
    return a * b

def discount(totalprice):
    if totalprice >= 1000:
        return totalprice * 0.8
    elif totalprice >= 500:
        return totalprice * 0.9
    else:
        return totalprice 

print(discount(totalprice(1200, 2)))
print(discount(totalprice(600, 1)))
print(discount(totalprice(300, 1)))
"""
def calculate_subtotal(price, quantity):
    return price * quantity 
def mindiscount(subtotal):
    if subtotal >= 1000:
        return min(300, subtotal * 0.2)
    else:
        return 0
def apply_discount(subtotal):
    return subtotal - mindiscount(subtotal)

     
result = apply_discount(calculate_subtotal(400, 3))
print(result)