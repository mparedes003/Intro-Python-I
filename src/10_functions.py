# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(num):
  if num % 2 == 0:
    return True
  else:
    return False
print(is_even(44))
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

print('You entered number:', num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def even_or_odd(num):
  if num % 2 == 0:
    return "Even!"
  else:
    return "Odd"

print(even_or_odd(23444227))
print(even_or_odd(1232426))

