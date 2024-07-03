# class MyClass:
#     """A simple class"""
#     i = 12345

#     def f(self):
#         return 'hello world'

# x = MyClass()
# print(x.f())

# y= MyClass()
# y.i = 100
# print(y.i)

#the first argument of a method is called self. This is nothing more than a convention: the name self has absolutely no special meaning to Python

# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart

# x = Complex(3.0, -4.5)
# print(x.r, x.i)



# destructor
# class Employee:
# 	# Initializing
# 	def __init__(self):
# 		print('Employee created.')

# 	# Deleting (Calling destructor)
# 	def __del__(self):
# 		print('Destructor called, Employee deleted.')

# obj = Employee()
#del obj


#Self parameter can be change with some other name
# class GFG:
#     def __init__(somename, name, company):
#         somename.name = name
#         somename.company = company

#     def show(somename):
#         print("Hello my name is " + somename.name +
#               " and I work in "+somename.company+".")


# obj = GFG("John", "Best Company")
# obj.show()


# str method
# class GFG:
#     def __init__(self, name, company):
#         self.name = name
#         self.company = company

#     def __str__(self):
#         return f"My name is {self.name} and I work in {self.company}."


# my_obj = GFG("John", "GeeksForGeeks")
# print(my_obj)

#Getter Setter
# class Dog:

#     # Class Variable
#     animal = 'dog'
#     color = 'red'

#     # The init method or constructor
#     def __init__(self, breed):

#         # Instance Variable
#         self.breed = breed

#     # Adds an instance variable
#     def setColor(self, color):
#         self.color = color

#     # Retrieves instance variable
#     def getColor(self):
#         return self.color


# # Driver Code
# Rodger = Dog("pug")
# Rodger.setColor("brown")
# print(Rodger.getColor())



#Inheritance
# Base or Super class. Note object in bracket. (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is equivalent to "class Person(object)"


# class Person(object):
# 	# Constructor
# 	def __init__(self, name):
# 		self.name = name

# 	# To get name
# 	def getName(self):
# 		return self.name

# 	# To check if this person is an employee
# 	def isEmployee(self):
# 		return False


# # Inherited or Subclass (Note Person in bracket)
# class Employee(Person):

# 	# Here we return true
# 	def isEmployee(self):
# 		return True
	
# 	def setName(self,newname):
# 		self.name = newname


# Driver code
# emp = Person("Good") # An Object of Person
# print(emp.getName(), emp.isEmployee())

# emp = Employee("Bad") # An Object of Employee
# print(emp.getName(), emp.isEmployee())
# emp.setName("Tahir")
# print(emp.getName(), emp.isEmployee())



#Encapsulation
#Protected Member

#Protected members (in C++ and JAVA) are those members of the class that cannot be accessed outside the class but can be accessed from within the class and its subclasses. 

# Creating a base class 
# class Base: 
# 	def __init__(self): 
# 		# Protected member 
# 		self._a = 2

# #Creating a derived class 
# class Derived(Base): 
# 	def __init__(self): 
# 		# Calling constructor of Base class 
# 		Base.__init__(self) 
# 		print("Calling protected member of base class: ", self._a) 

# 		# Modify the protected variable: 
# 		self._a = 3
# 		print("Calling modified protected member outside class: ",self._a) 

# obj1 = Derived() 
# obj2 = Base() 

# Calling protected member 
# Can be accessed but should not be done due to convention 
#print("Accessing protected member of obj1: ", obj1._a) 

# Accessing the protected variable outside 
#print("Accessing protected member of obj2: ", obj2._a) 

#Private members
#Private members are similar to protected members, the difference is that the class members declared private should neither be accessed outside the class nor by any base class. 


# Creating a Base class 

# class Base: 
# 	def __init__(self): 
# 		self.a = "Good"
# 		self.__c = "Bad"

# # Creating a derived class 
# class Derived(Base): 
# 	def __init__(self): 
# 		# Calling constructor of Base class 
# 		Base.__init__(self) 
# 		print("Calling private member of base class: ") 
# 		print(self.__c) 


# Driver code 
# obj1 = Base() 
# print(obj1.__c) 


# Uncommenting print(obj1.c) will raise an AttributeError 

# Uncommenting obj2 = Derived() will also raise an AttributeError as private member of base class is called inside derived class 
#obj2 = Derived()


#polymorphism means the same function name (but different signatures) being used for different types. The key difference is the data types and number of arguments used in function.

#Python program to demonstrate in-built poly-morphic functions
 
# # len() being used for a string
# print(len("geeks"))
 
# # len() being used for a list
# print(len([10, 20, 30]))


#polymorphism in Python using inheritance and method overriding
# class Animal:
# 	def speak(self):
# 		raise NotImplementedError("Subclass must implement this method")

# class Dog(Animal):
# 	def speak(self):
# 		return "Woof!"

# class Cat(Animal):
# 	def speak(self):
# 		return "Meow!"

# # Create a list of Animal objects
# animals = [Dog(), Cat()]

# # Call the speak method on each object
# for animal in animals:
# 	print(animal.speak())


# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1
    def g(self):
        return 'hello world'

chk= C()
print(chk.f(4,7))