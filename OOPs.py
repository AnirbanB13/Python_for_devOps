# Objective oriented Programming #

# class is a blueprint of objects
# object is an instance of a class

class Employee:
    name = "harry"
    language = "python"   #class attribute
    salary = 5000  

    def getInfo(self):
        print(f"the language is {self.language} and salary is {self.salary}")

harry = Employee()
# harry.lastname = "singh"  #instance attribute
# print(harry.name, harry.language)

#instance attribute takes precedence over class attribute duing assignment and retrieval
Employee.getInfo(harry)
