import json
import json
json.dumps({'a': 1, 'b': 2})
'{"b": 2, "a": 1}'
json.dumps({'a': 1, 'b': 2}, sort_keys=True)
'{"a": 1, "b": 2}'


# data = '{"var1":"Shahzaib", "var2":67}'
# # print(data)
# #
# # parsed = json.loads(data)
# # print(parsed['var1'])
#
#
# data2 = {
#  "Channel name": "ShahzaibRind",
#  "Accounts": ['Fiverr', "Upwork", "Frelancer"],
#  "fride": ('Meet', 540),
#  "isbad": False
# }
#
# jscompitable = json.dumps(data2)
# print(jscompitable)