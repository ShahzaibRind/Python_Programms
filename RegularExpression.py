import re
mystr = """We are the most accurate financial data API out there.
To make it simple we are a free stock 
API | historical data API | financial statements API Rind
We update our financial statements in real time, 
every statements is audited, standardized, and up to date.
We cover NYSE, NASAQ, AMEX, EURONEX, TSX, INDEXES, ETFs, MUTUAL FUNDS, FOREX and CRYPTO.
We have real time stock price, we cover the fundamental data part of 
the stocks via providing income statement, 41202-5979625-5 
balance sheet statement and cashflow statement quaterly and annually 41202-59796255.
We have 1 minute, 15 minutes, 30 minutes, 1 hour and daily historical stock prices"""

# findall, search, split, sub, finditer

# Meta Characters
# pattern = re.compile(r'via')
# pattern = re.compile(r'.an') # . Any Character
# pattern = re.compile(r'^We')   # ^ Starts With
# pattern = re.compile(r'prices$')   # ^ Ends With
# pattern = re.compile(r'a*i*')   # * Zero or More Occurances
# pattern = re.compile(r'ai+')   # + One or More Occurances
# pattern = re.compile(r'ai{1}')   # {} Extactly the specified number of occurences
# pattern = re.compile(r'(We){1}')   # () Capture and Group
# pattern = re.compile(r'ai{1} | f')   # | Either Or

# Special Characters

# pattern = re.compile(r'\AWe')   # \A Returns a Match if the specified characters are not beginning of the String
# pattern = re.compile(r'Rind\b')   # \b Returns a Match Where the specified characters are not beginning or at the end of word
pattern = re.compile(r'\d{5}-\d{7}')   # \d Returns a Match Where the Stings contains the digits(numbers 0 - 9)

matches = pattern.finditer(mystr)
for match in matches:
    print(match)












