import os
print(dir(os))
print(os.getcwd())
os.chdir("C://") #Show the current Directory
print(os.getcwd())
print(os.listdir()) #Show the list of files or folders in current Directory

os.mkdir("New file")
os.makedirs("Python/Flask/Django") #Make folder within folder

os.rename("Shazzy.txt", "Shahzaib.txt") #Rename the File,,
print(os.environ.get('Path')) #Use to Read Environment Variables

# Join the two paths with optical way \\Function
print(os.path.join("C://", "Shahzaib.txt"))

print(os.path.exists("C://fdssd"))