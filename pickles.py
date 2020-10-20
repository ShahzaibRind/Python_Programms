# import pickle
#
# cars = ['Audi', 'BMA', 'Ferrari', 'Honda']
#
# # #  pickling a python Object
# # file = ('my_car.pkl')
# # fileobj =  open(file, 'wb')
# # pickle.dump(cars, fileobj)
# # fileobj.close()
#
# file = "my_car.pkl"
# myfile = open(file, 'rb')
# mycar = pickle.load(myfile)
# # mycar = pickle.loads(file)
# print(mycar)
import pickle

# take user input to take the amount of data
number_of_data = int(input('Enter the number of data : '))
data = []

# take input of the data
for i in range(number_of_data):
    raw = input('Enter data '+str(i)+' : ')
    data.append(raw)

# open a file, where you ant to store the data
file = open('important', 'wb')

# dump information to that file
pickle.dump(data, file)

# close the file
file.close()
