garments = ["Shirt", "Jeans", "Burkha", "Ferakh", "Suit"]

print(garments)

price = [200, 300, 400, 500, 600]

# print(price)
price.append(12)
print("After Append: ", price)

price.insert(2, 890)
print("After Insert: ", price)

price.reverse()
print("After Reverse: ", price)

price.pop(2)
print("After Pop: ", price)

price.remove(890)
print("After Remove: ", price)

price.clear()
print("After Clear: ", price)

price.insert(0,12)
print("After Insert: ", price)