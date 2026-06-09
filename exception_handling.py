try:
    a = int(input("Hey, enter a number: "))
    print(a)

except ValueError:
    print("Invalid input. Please enter a valid integer.")

except Exception as e:
    print(e)


# raise error

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if b == 0:
    raise ValueError("The second number cannot be zero.")

print(a/b)

#finally

try:
    print("We are in try")
    i = int(input("Enter a number: "))
    print(i)
    
except ValueError:
    print("Invalid input. Please enter a valid integer.")

except Exception as e:
    print(e)

finally:
    print("We are in finally")