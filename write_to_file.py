""" Program that asks the user for their name and saves to a file"""

f = open("names.txt", "a")
# "w" - file should be opened in write mode
# "a" - file is appended

name = input("Hello, what is your name? ")

print("Hello " + name)

f.write(name + "\n")  # Writes the contents of the variable name to the file f using the write method
# Write - handles all of the tasks needed to write data to a file

f.close()  # Closing ensures contents are saved correctly and reduces the risk of data loss