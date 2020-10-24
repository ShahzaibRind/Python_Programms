lists = [1,2,3,4,5,6,7,8,9]

def is_greaterthan_5(num):
    return num > 5

gr_than_5 = list(filter(is_greaterthan_5, lists))
print(gr_than_5)