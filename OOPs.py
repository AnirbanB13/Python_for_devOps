# # Objective oriented Programming #

# # class is a blueprint of objects
# # object is an instance of a class

class Employee:
    name = "harry"
    language = "python"   #class attribute
    salary = 5000  

    def __init__(self, name, language, salary):  #dunder method which is automatically called
        print("I am creating an object")
        self.name = name
        self.language = language
        self.salary = salary

#   def getInfo(self):
#       print(f"the language is {self.language} and salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("hello world")

# harry = Employee()
# harry.lastname = "singh"  #instance attribute
# print(harry.name, harry.language)

# #instance attribute takes precedence over class attribute duing assignment and retrieval
# Employee.getInfo(harry)

# self is neccessary to provide in methods within class

harry = Employee("harry", "javascript", 10000)
harry.greet()
print(harry.name, harry.language, harry.salary)

