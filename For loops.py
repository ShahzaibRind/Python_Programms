# list1 = [ ["Shahzaib",1], ["Touqeer",3], ["Jabbar",4], ["Sohail",5] ]
#
# dic = dict(list1)
#
# for item, lollipop in dic.items():
#     print(item, lollipop)

items = [int, float, "Shazzy", 12, 45, 45, 86,22, 65, 34, 34,365]

for item in items:
    if str(item).isnumeric() and item>=6:
        print(item)