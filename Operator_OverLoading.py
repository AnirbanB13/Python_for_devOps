# m = 0

# This code creates a special type of number that knows how to add itself to other numbers
# Think of it like a box that holds a number inside it
class Number:
    # When we make a new Number box, we put a number inside it
    def __init__(self, n):
        self.n = n

    # This tells the Number box what to do when we use the + sign
    # It takes the number from this box and adds it to the number from another box
    def __add__(self, m):
        return self.n + m.n

# Here we make two Number boxes - one with 1 inside and one with 2 inside
n = Number(1)
m = Number(2)

# When we add the two boxes together, it adds 1 + 2 and prints 3
print( n + m )
