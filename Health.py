def Health():
    x = '1'
    while x in ['1', '2', '3']:
        print('1 for Environment')
        print('1 for Food')
        print('1 for Healt')
        print("0 for Quit")
        x = input('Enter the Number: ')
        if x == 1:
            print("Good Environment")
        elif x == 2:
            print("Fast Food!!!")
        elif x == 3:
            print("Always be Healthy")
        elif x == 0:
            print('Quitting...')
        else:
            print('Invalid Input!!!')