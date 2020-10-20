# Dictionary is nothing but it is key value pairs

d1 ={}
# print(d1)

d2 = {"Shazzy":"Biryani", "Jabbar":"Fiverr", "Touqeer":"car", "Miraj":"bike"}
# print(d2["Shazzy"])

d2 ["Sohail"] = "car"
print(d2)

del d2 ["Sohail"]
print(d2)

d2.update({"Shazzy":"Tea"})
print(d2)

# d3 - d2.copy()
# del d3["Jabbar"]

print(d2.keys())

print(d2.items())