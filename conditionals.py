day_of_week = input("Enter the day of week: ").lower() #convert to lower-case
print(day_of_week)

if day_of_week == "saturday" or day_of_week == "sunday": #true
    print("I'll learn devOps")
else: #false
    print("I will practice devops")

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: " ))

choice = input("Enter the operation: (Options + , - , * , / , %) ")

if choice == "+":
    sum_of_num = num1 + num2
    print("addtion", sum_of_num)
elif choice == "-":
    diff_of_num = num1 - num2
    print("substraction", diff_of_num)
elif choice == "*":
    product_of_num = num1 * num2
    print("product", product_of_num)
elif choice == "/":
    division_of_num = num1 / num2
    print("division", division_of_num)
elif choice == "%":
    remainder_of_num = num1 % num2
    print("modulus", remainder_of_num)
else:
    print("Invalid input")

