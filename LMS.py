class Library:
    def __init__(self, list, name):
        self.booksList = list
        self.name = name
        self.lendDict = {}

    def displaybooks(self):
        print(f'We Have Following Books in Our Library: {self.name}\n')
        for book in self.booksList:
            print(book)

    def lendBooks(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print('Lander-Book Has been Updated. You Can take the book now.\n')
        else:
            print(f'Book is already being used by {self.lendDict[book]}')
 
    def addBooks(self, book):
        self.booksList.append(book)
        print('Book Has been added Successfully...\n')

    def returnBook(self, book):
        self.lendDict.pop(book)


if __name__ == '__main__':
    shazzy = Library(['Python', 'Java', 'Data Structure', 'C++', 'Pak Study'], "Shahzaib RInd")

    while(True):
        print(f'\t\tWelcome to the {shazzy.name} Library. Enter your Choice to Continue: \n')
        print('1. Display Books: ')
        print('2. Lend a Book: ')
        print('3. Add a Book: ')
        print('4. Return a Book: \n')

        choice = input('Enter Your Choice: ')
        if choice not in ['1', '2', '3', '4']:
            print('\nPlease Enter A valid Option.\n')
            continue
        else:
            choice = int(choice)
        if choice == 1:
            shazzy.displaybooks()

        elif choice == 2:
            book = input("Enter the Name of the book you want to lend: ")
            user = input('Enter your Name: ')
            shazzy.lendBooks(user, book)

        elif choice == 3:
            book = input('Enter the Name of the book you want to Add: ')
            shazzy.addBooks(book)

        elif choice == 4:
            book = input('Enter the Name of the book you want to Return: \n')
            shazzy.returnBook(book)
            print("Book has been Returned Successfully...\n")

        else:
            print('Not a Valid Option!!!\n')

        print('Press q to Quit and c to Continue: ')
        choice2 = ''
        while(choice2 != 'c' and choice2 != 'q'):
            choice2 = input()
            if choice2 == 'q':
                exit()
                if choice2 == 'c':
                    continue