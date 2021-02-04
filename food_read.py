""" Program that reads a file"""

f = open("food.txt", "r")  # Opens the file in read mode

# Iterating over lines
for line in f:
    print(line)

# Alternative approach - read full contents
#data = f.read()  # Reads the contents of the file into a variable called data
#print(data)

f.close()
# Leaving files open can cause data loss and can also prevent access when files are used by multiple concurrent users


### Option 2 - Using with
with open("food.txt") as f:
    data = f.read()
    print(data)