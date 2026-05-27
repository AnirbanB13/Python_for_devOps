# # Objective oriented Programming #

# # class is a blueprint of objects
# # object is an instance of a class

# class Employee:
#     name = "harry"
#     language = "python"   #class attribute
#     salary = 5000  

#     def __init__(self, name, language, salary):  #dunder method which is automatically called
#         print("I am creating an object")
#         self.name = name
#         self.language = language
#         self.salary = salary

# #   def getInfo(self):
# #       print(f"the language is {self.language} and salary is {self.salary}")
    
#     @staticmethod
#     def greet():
#         print("hello world")

# # harry = Employee()
# # harry.lastname = "singh"  #instance attribute
# # print(harry.name, harry.language)

# # #instance attribute takes precedence over class attribute duing assignment and retrieval
# # Employee.getInfo(harry)

# # self is neccessary to provide in methods within class

# harry = Employee("harry", "javascript", 10000)
# harry.greet()
# print(harry.name, harry.language, harry.salary)

# class Programmer:
#     company = "Microsoft"

#     def __init__(self, name, salary, pin):
#         self.name = name
#         self.salary = salary
#         self.pin = pin
        
#     def getinfo(self):
#         print(f"The name of the programmer is {self.name}, salary is {self.salary} and pin is {self.pin}")


# p = Programmer("anirban", 100000, 797979)

# # print(p.name, p.salary, p.pin, p.company)

# p.getinfo()

class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is {self.n*self.n}")
    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")
    def squareRoot(self):
        print(f"The square root is {self.n**(1/2)}")
    

a = Calculator(4)
a.square()
a.cube()
a.squareRoot()
