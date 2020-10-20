import time
def Searcher():
    print('Wait for 4 seconds to start......')
    # Some 4 seconds time consuming task
    book = 'THis is book of Shahzaib rind and it 500k up to words'
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Your word is Found, and word is: ", text)
        else:
            print(text, " Word Not Found!!!")


search = Searcher()
next(search)
search.send("Shahzaib")
input('Press Enter key')
search.send("Shqa")
input('Press Enter key')
search.send("rind")
search.close()
input('Press Enter key')
search.send("rind")


# def Search():
#     print('Please Wait for 2 Seconds...')
#     book = open('Shazzy2.txt')
#     time.sleep(2)
#
#     while True:
#         text = (yield)
#         if text in book:
#             print("Word Found Successfully... and your word is: ", text)
#         else:
#             print(text, "Word is Not Found!!!")
#
#
# search = Search()
# next(search)
# search.send('good')
# input('Press Enter Key')