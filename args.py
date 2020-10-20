def funargs(normal, *args):
    print(normal)
    for item in args:
        print(item)

shah = ["Shah", "Umair", "touqeer", "Siraj", "Jabbar","The End"]
nor = "I am Normal Arguement and these are my frndz..."
funargs(nor,*shah)