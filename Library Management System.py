print('\n\t\t<-------Welcome to Online Library Management System------->\n')
print('Enter 1 for Display Books: ')
print('Enter 2 for Issue Books: ')
print('Enter 3 for Add Books: ')
print('Enter 4 for Return Books: ')
print('Enter 0 for Exit Program: \n')

choose = int(input("Enter Your Choice: "))

# if choose == str:
#     print('Please Choose a Valid Input!!')


while choose == True:
    if choose == 1:
        print("\nWelcome to Display Books: ")
        break
    elif choose == 2:
        print("\nWelcome to Issue Book: ")
        break
    elif choose == 3:
        print("\nWelcome to Add Book: ")
        break
    elif choose == 4:
        print("\nWelcome to Return Book: ")
        continue
    elif choose == 0:
        exit()
    else:
        print("\nInvalid Input! Please Enter Valid Input..")
    # continue


class Library:

    def __init__(self, java, math, data, python, ruby):
            self.java = java
            self.math = math
            self.data = data
            self.python = python
            self.ruby = ruby

    def print_details(self):
         return f'\n {self.java} \n {self.math} \n {self.data} \n {self.python} \n {self.ruby}'

    def issue_book(self, first, last, dept, batch, roll_no):
            self.first = first
            self.last = last
            self.dept = dept
            self.batch = batch
            self.roll_no = roll_no

    def add_book(self, bookid, book_name, book_author):
        self.bookid = bookid
        self.book_name = book_name
        self.book_author = book_author


shazzy = Library('Id 4 Java', 'Id 5 Math', 'Id 6 Data Structure', 'Id 7 Python', 'Id 8 Ruby')
print(shazzy.print_details())
