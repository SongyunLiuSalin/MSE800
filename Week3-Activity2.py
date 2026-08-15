'''data = open("junk.txt") # Default is open for reading 
for line in data: # Processes file line by line
    print(line[0:1]) # Print the line without its final \n char 
data.close()# Do not need the file any more'''

with open("junk.txt", "a") as file:
    file.write("text file nanalyssis.\n") # Add a new line to the end of the file

with open("junk.txt", "r") as file:
    text = file.read()
text = text.lower()
with open("junk.txt", "w") as file:
    file.write(text)

data = open("junk.txt")
lines = data.readlines() # Get a list of all the lines in the file 
for line in lines:
# Processes file line by line
    print(line[0:-1]) # Print the line without its final \n char 
data.close()

print(len(lines)) # Print the number of lines in the file