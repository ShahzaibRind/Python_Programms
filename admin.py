# False Values:
# False
# None
# Zero of any Numeric Number
# Any Empty Sequence. for example, '', (), [].
# Any Empty mapping. for example, {}

# condition = 'Test'
# if condition:
#     print("Evaluated to True")
# else:
#     print("Evaluated to False")
#
# user = "admin"
# logged_in = False
#
# if user == "admin" or logged_in:
#     print("Admin Page")
# else:
#     print("Invalid!!!")

nums = [1,2,3,4,5]
for num in nums:
    if num == 3:
        print("Found!!!")
        continue
        print(num)