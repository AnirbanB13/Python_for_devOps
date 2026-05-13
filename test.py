#print ( 2 < 4 )

#min_score = 13
#score = 13

#print(score > min_score)
#print(score <= min_score)

#'python'>'Python'

#x = -10
#if x < 0:
#    print("The negative number ",  x, " is not valid here.")
#print("This is always printed")

#if 4 + 5 == 10:
#    print("TRUE")
#else:
#    print("FALSE")
#print("TRUE")


# 1st if statement
#if True: print('hello')

# 2nd if statement
#if (5,10):
#    print('hello')

# 3rd if statement
#if (yes):
#    print('hello')

# 4th if statement
#if (5,10): print('hello')

# x = 0
# a = 6
# b = 6
# if a > 0:
#     if b < 0: 
#         x = x + 6 
#     elif a > 6:
#         x = x + 5
#     else:
#         x = x + 4
# else:
#     x = x + 3

# print(x)

# num_1 = int(input("enter first number = "))
# num_2 = int(input("Enter second number = "))

# total = num_1 + num_2

# print("the total is = ", total)

# for letter in "python":
#     print(letter)

# import pyjokes

# jokes = pyjokes.get_joke()

# print(jokes)

# import math

# for i in range(1, 11):
#     i = i * 5
#     print(i)

# import pyttsx3
# engine = pyttsx3.init()

# engine.say("""
# I met an old woman at the bus stop today.
# She talked to me, but I didn’t know what to say.
# ‘Your little brother looks smart,’ she said.
# But I didn’t know what to say.

# ‘I’m from Romania,’
# ‘I’ve been here six years,’
# ‘I sleep in the shelters.”
# I held my brother’s hand tighter.""")
# engine.runAndWait()


# import os

# print(os.listdir('.'))

# print(os.getcwd())

# print(os.open('test.py', os.O_RDONLY))


# directory_path = "/"

# contents = os.listdir(directory_path)

# for item in contents:
#     print(item)

# a = "This is the first line \nthis is the second line"
# print(a)

# name = input("Enter your name: ")

# print(f"Good Afternoon {name}")

# letter = """Dear <|Name|>,
#         You are selected!
#         <|Date|>"""

# print(letter.replace("<|Name|>", "Anirban").replace("<|Date|>", '13th sept, 1996'))

# name = "harry  isagoodboyandagreatabuddy"

# if (name.find("goo")):
#     print(name.index("goo"))

# name = "harry  is a good boy and a great buddy"
 
# print(name.replace("  ", " "))

# letter = "Dear Harry, \n\tThis is Python course. \nThanks!"
# print(letter)

#friends = ["Anirban", "Satyarth", "Orange", 1, 345.6 , False, "Rohit", "Satyarth"]
# print(friends[1:5])

# friends[0] = "Anirban Das"    #Unlike strings, lists are mutable, which means we can change their content without changing their identity.
# print(friends)

# friends.append("Harry")
# print(friends)

# friends.insert(1, "Satyarth")
# print(friends)

# friends.remove("Satyarth")
# print(friends)

# friends.pop(1)
# print(friends)

# l1 = [1, 5, 3, 9, 2]

# l1.sort()
# print(l1)

# l1.reverse()
# print(l1)

# l1.insert(3, 333333)
# print(l1)

# marks = []
# m1 = input("Enter the marks of 5 students separated by space: ").split()
# marks = [int(i) for i in m1]
# print(marks)

# a = (1, 2, 3, 4, 5, 5, 5, 5, 5, 5)

# n = a.count(5)
# print(n)

# marks = {
#     "Anirban": 95,
#     "Satyarth": 90,
#     "Rohit": 85,
#     "Harry": 80
# }

# # # print(marks, type(marks))

# # print(marks["Anirban"])

# marks.update({"Anirban": 99})

# print(marks.get("Anirban"))

# print(marks.keys())

# print(marks.values())

# print(marks.items())

# empty_set = set() #This is an empty set, also no values can be repeated

# s = {1, 2, 3, 4, 5, 5, 5, 5}

# s.add(6)

# print(s)

# s1 = {1, 2, 3, 4, 5}
# s2 = {4, 5, 6, 7, 8}

# print(s1.union(s2)) #union of two sets₹

# print(s1.intersection(s2)) #intersection of two sets

# translations = {
#     "hello": "hola",
#     "goodbye": "adios",
#     "thank you": "gracias",
#     "please": "por favor"
# }

# # print(translations.get("hello"))

# word = input("Enter a word to translate: ")
# print(translations.get(word, "Translation not found."))

# numbers = int(input("Enter 8 numbers separated by space: "))
# print(numbers)

# s = set()
# s.add(20)
# s.add('10')
# s.add(20.0)
# print(len(s))

# dic = {}

# n1 = input("Enter the name of the student: ")
# m1 = int(input("Enter the marks of the student: ")) 

# dic.update({n1: m1})
# print(dic)

# age = int(input("Enter your age: "))
# if age < 18:
#     print("You are a minor.")
# elif age >= 18 and age < 65:
#     print("You are an adult.")
# else:
#     print("You are a senior citizen.")

#****SPAM FILTER****

# m1 = "buy now"
# m2 = "limited time offer"
# m3 = "click this"

# message = input("Enter your message: ")

# if (m1 in message) or (m2 in message) or (m3 in message):
#     print(f"This message is spam, In contains {message}" )  
# else:    
#     print("This message is not spam.")

#loops in python#

# for i in range(1, 11, 2):
#     print(i)

# i = 1

# while i <= 10:
#     print(i)
#     i += 1

# for i in "harry":
#     print(i)

# i = 0

# while i < 5:
#     i = i + 1
#     print("harry")

# list = [1, "hello", 3.14, True]

# i = 0

# while (i < len(list)):
#     print(list[i])
#     i += 1

# for i in range(4):
#     print(i)


# l = [1, 2, 3, 4, 5]

# for item in l:
#     print(item)
# else:
#     print("This is end...")

# for i in range(100):
#     if i == 34:
#         break #exirt the loop right now
#     print(i)


# for i in range(100):
#     if i == 34:
#         continue #skip the current iteration and move to the next one
#     print(i)

# table = int(input("Enter the number to print its multiplication table: "))
# for i in range(1, 11):
#     print(f"{table} x {i} = {table * i}")


# l = ["harry", "Soham", "Sachin", "rohit"]

# for name in l:
#     if(name.startswith("S")):
#         print(f"Hello, {name}!")


# i = 1

# while i < 11:
#     print(f"{table} x {i} = {table * i}")
#     i += 1

# n = int(input("Enter a number: "))
# i = 1
# sum = 0
# while i <= n:
#     sum += i 
#     i += 1

# print(sum)

# n = int(input("Enter a number: "))
# i = 1
# factorial = 1
# while i <= num:
#     factorial *= i
#     i += 1
# print(factorial)

# for i in range(1, n+1):
#     print(" " * (n-i), end="")
#     print("*" * (2*i-1), end="")
#     print("")

# def input_number(num):
#     return int(input("Enter a number : ")) * num

# print(input_number(num = 10))

# a = 0
# def add_three(a):
# 	return a+3

# result = add_three(3)
# print(result)

# def add_func(num1,num2):
#         return num1 + num2
# print ( add_func(5 , 5) )

# def my_function(*friends):
#   print("The tallest student is " + friends[0])

# my_function("john", "Ella", "mark")


# def fullname_func(fname):
#   print(fname + " Mark")

# fullname_func("John")

# def fullname_func(fname, lname):
#   print(fname + " " + lname)

# fullname_func("John", "Mark")

# def print_sum (num1, num2):
#     sum = num1 + num2
#     if(sum==0):
#         return True
#     print("The sum is: " + str(sum))
# print_sum(-1, 1)

# def square(i):
#     j = i * i
#     return j

# print(square(3))

# def is_true(a): 
#   return bool(a)
# result = is_true(3<6) 
# print("The result is", result)

# def square(i):
#     j = i * i
#     return j

# num = 2
# result = square(num)
# print("The result of ", num, " is ", result)

# def return_greeting():
#   return "Hello, World"

# print(return_greeting())

# def my_function(x):
#   return 5 + x

# print(my_function(3))

# def add(x, y):
#   return x+y

# def my_function(x):
#   return 10 - x

# print(my_function(4))

# def my_function(x):
#   return 10 / x
# print(my_function(2))

# def is_true(a): 
#   return bool(a) 

# result = is_true(6<3) 
# print("The result is", result)

# def multiply_values(list):
#     multiplied_values = []
    
#     for item in list:
#         multiplied_values.append(item * 2)
    
#     return multiplied_values

# numbers = [1, 2, 3, 4, 5]
# print(multiply_values(numbers))

# def get_odd_func(numbers):
#     odd_numbers = [num for num in numbers if num % 2]
#     return odd_numbers

# print(get_odd_func([1, 2, 3, 4, 5, 6]))

# def get_even_func(numbers):
#     even_numbers = [num for num in numbers if not num % 2]
#     return even_numbers

# print(get_even_func([1, 2, 3, 4, 5, 6]))


# def mean_func(list1):
#     return sum(list1) / len(list1)

# print(mean_func([5, 2, 2, 4]))

# def my_function(numbers):
#   for i in numbers:
#     print(i+1, end=' ')

# numbers = [1, 2, 3] 
# my_function(numbers)

# def my_function(numbers):
#   for i in numbers:
#     print(i*2+10, end=' ')

# numbers = [1, 2, 3]
# my_function(numbers)

# def my_function(names):
#   for i in names:
#     print(i, end=' ')

# names = ["john", "mark", "emmy"]
# my_function(names)

# def double_list(numbers):
#   return 2 * numbers

# numbers = [1, 2, 3]
# print(double_list(numbers))

# def mean_func(list1):
#     return sum(list1) / len(list1)

# print(mean_func([5, 6, 7, 8]))

# def my_function():
#   def my_inner_function():
#     x = 20
#   print(x)
#   my_inner_function()

# my_function()


# x = 30
# def my_function():
#   global x
#   x = 20

# my_function()
# print(x)

# x = 20
# def my_function():
#   print(x, end=' ')

# my_function()
# print(x, end=' ')

# def my_function():
#   def my_inner_function():
#     x = 20
#     print(x)
#   my_inner_function()

# my_function()


# x = 20
# def my_function():
#   x = 30
#   print(x, end=' ')

# my_function()
# print(x, end=' ')

# def myfunc():
#   a = 20
#   print(a)

# myfunc()

# def myfunc():
#   a = 20

# myfunc()
# print(a)

# def my_function():
#   global x
#   x = 30

# my_function()
# print(x)


# def my_function():
#   x = 20
#   def my_inner_function():
#     print(x)
#   my_inner_function()
# my_function()

# x = 20
# def my_function():
#   x = 30
#   print(x, end=' ')

# my_function()


# def sum(*args):
#     for arg in args:
#         result += arg
#     return result 

# print(sum(2,3,1))

# def my_function(*argv):
#   print(argv[0])

# my_function('Hello', 'World!')

# def division(a,b):
#     return a/b

# print(division(8,2))

# def sum(a,b):
#     return a+b

# print(sum(2,3))

# def my_function(*ages):
#   print("The older friend is " + ages[0] + " years")

# my_function("13", "12", "11")


# def my_function(*argv):  
#     for arg in argv:  
#         print(arg) 

# my_function('Hello', 'World!')


# def my_function(*argv):
#   print(argv)

# my_function('Hello', 'World!')

# def my_function(arg1, *argv): 
#     print ("First argument:", arg1) 
#     for arg in argv: 
#         print("Next argument:", arg) 

# my_function('Welcome', 'to', 'Python!')

# tuple1 = (0, 1, 2, 3, 4, 5)

# print(tuple1[0:4])

# x = tuple(3)
# print(x)

# a = (10, [20, 30], 40, 50)

# print(a.index(30))

# a = (10, 20, 30, 40, 50)
# a = a[::-1]
# print(a)

# testdict = {
#   "brand": "apple",
#   "ram": "3",
#   "year": 2020,
#   "year": 2021
# }

# print(testdict)


# testdict = {
#   "brand": "Samsung",
#   "ram": "3",
#   "Os": "Android",
#   "year": 2020
# }

# testdict.update({'brand':'oppo' })
# print(testdict)


# testdict = {
#   "brand": "Samsung",
#   "ram": "3",
#   "Os": "Android",
#   "year": 2020
# }

# print(testdict.keys())

# testdict = {
#   "brand": "Samsung",
#   "ram": "3",
#   "Os": "Android",
#   "year": 2020
# }

# print(testdict.items())

