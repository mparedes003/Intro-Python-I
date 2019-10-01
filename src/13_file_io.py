"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
f = open('foo.txt', 'r')  # opens file "foo.txt" for reading

for contents in f:  # print all the contents of the file
    print(contents)

f.close()  # close the file

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
f = open('bar.txt', 'w')  # open up a file called "bar.txt" for writing

f.write('''Arbitrary Line 1  
Arbitrary Line 2
Arbitrary Line 3''')  # write three lines of arbitrary content to the file

f.close()  # close the file
