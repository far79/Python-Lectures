#del keyword
#Used to delete object properties or object itself

# class Student:
# 	def __init__(self,name):
# 		self.name = name

# s1=Student("ice")
# print(s1.name)#prints ice
# del s1.name
# print(s1.name)#error




#Private(like) attributes & methods
#Conceptual implementation in python
#Private attributes & methdos are meant to be used only within the class and are not accessible from outside the class.


# class Account:
# 	def __init__(self, acc_no, acc_pass):
# 		self.acc_no = acc_no
# 		self.acc_pass = acc_pass


# acc1 = Account("12345", "abcde")

# print(acc1.acc_no)
# print(acc1.acc_pass)




# class Account:
# 	def __init__(self, acc_no, acc_pass):
# 		self.acc_no = acc_no
# 		self.__acc_pass = acc_pass# add __ to make it private

# 	def reset_pass(self):
# 		return(self.__acc_pass)


# acc1 = Account("12345", "abcde")

# print(acc1.acc_no)
# # print(acc1.acc_pass)#error
# print(acc1.reset_pass())


# class Person:
# 	__name = "Anonymous"

# 	def __hello(self):
# 		print("hello person!")

# 	def welcome(self):
# 		self.__hello()

# p1=Person()
# # print(p1.__name)#error
# # print(p1.__hello())#error
# print(p1.welcome())


#Private(like) attributes



#Inheritance
#When once class(child/derived) derives the properties & methods of another class(parent/base)

# class Car:
# 	color="black"
# 	@staticmethod
# 	def start():
# 		return("car started...")

# 	@staticmethod
# 	def stop():
# 		return("car stopped...")


# class ToyotaCar(Car):
# 	def __init__(self,name):
# 		self.name = name

# car1 = ToyotaCar("Fortuner")
# car2 = ToyotaCar("prius")

# print(car1.start())
# print(car1.color)

# #Inheritance is of 3 types:
# #1) Single inheritance
# #2) Multi level inheritance
# #3) Multiple inheritance



# class Car:
# 	color="black"
# 	@staticmethod
# 	def start():
# 		return("car started...")

# 	@staticmethod
# 	def stop():
# 		return("car stopped...")


# class ToyotaCar(Car):
# 	def __init__(self,brand):
# 		self.name = brand

# car1 = ToyotaCar("Fortuner")
# car2 = ToyotaCar("prius")

# print(car1.start())
# print(car1.color)

# class Fortuner(ToyotaCar):
# 	def __init__(self, type):
# 		self.type = type

# car3 = Fortuner("diesel")
# print(car3.start())



#3) Multiple inheritance
#Multiple inheritance is when a class inherits from more than one parent class
# class A:
# 	varA="welcome to class A"

# class B:
# 	varB="welcome to class B"

# class C(A,B):
# 	varC="welcome to class C"

# c1=C()
# print(c1.varA)
# print(c1.varB)
# print(c1.varC)


#Super method
#Super method is used to call the parent class method

# class Car:
# 	def __init__(self, type):
# 		self.type = type 

# 	@staticmethod
# 	def start():
# 		return("car started...")

# 	@staticmethod
# 	def stop():
# 		return("car stopped...")


# class ToyotaCar(Car):
# 	def __init__(self,brand,type):
# 		self.name = brand
# 		# self.type = type #error
# 		super().__init__(type) #super method to call parent class constructor

# car1=ToyotaCar("prius", "electric") 
# print(car1.type)







#CLASS METHOD
#A class method is a method that is bound to the class and not the object of the class. It can modify a class state that applies across all instances of the class. It takes cls as the first parameter while a regular method takes self.
#Note-static method can't access or modify class state & generally for utiltity.
# class Person:
#     name = "Anonymous"

#     def changeName(self, name):
#         self.name = name

# p1=Person()
# p1.changeName("ice")
# print(p1.name)
# print(Person.name)# the change of name has occured in a function but not in the class variable. So the class variable remains unchanged.
#To make it change in the class variable:

# class Person:
#     name = "Anonymous"

#     def changeName(self, name):
#         Person.name = name #this changes the class variable

# p1=Person()
# p1.changeName("ice")
# print(p1.name)
# print(Person.name) #gives ice in both cases because the class variable has been changed.

#2nd method
# class Person:
#     name = "Anonymous"

#     def changeName(self, name):
#         self.__class__.name = name #any object whose class it to be changed, it will change the class variable of that class.

# p1=Person()
# p1.changeName("ice fire")
# print(p1.name)
# print(Person.name)


#3rd method
# class Person:
#     name = "Anonymous"
    
    
#     @classmethod
#     def changename(cls, name):
#         cls.name = name #this changes the class variable
    
# p1=Person()
# p1.changename("ice")
# print(p1.name)
# print(Person.name)

#All three methods are:
#1) static methods
#2) class methods(cls as argument)
#3) instance methods(self as argument)


#PROPERTY DECORATOR
#We use @property decorator on any method in the class to use the method as a property.

# class Student:
#     def __init__(self, phy, chem, maths):
#         self.phy = phy
#         self.chem = chem
#         self.maths = maths
#         self. percentage = str((self.phy+self.chem+self.maths)/3)+ "%"
    
#     def calcpercentage(self):
#         self.percentage = str((self.phy+self.chem+self.maths)/3)+ "%"

# s1=Student(98,97,99)
# print(s1.percentage)

# s1.phy = 86
# print(s1.percentage) #gives 98% because the percentage is calculated only once in the constructor. So we need to recalculate it after changing the marks.
# s1.calcpercentage()
# print(s1.percentage) #gives 94.33% because we have recalculated


# class Student:
#     def __init__(self, phy, chem, maths):
#         self.phy = phy
#         self.chem = chem
#         self.maths = maths
    
#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.maths) / 3) + "%"

# s1=Student(98,97,99)
# print(s1.percentage)

# s1.phy = 86
# print(s1.percentage)




#POLYMORPHISM
#Polymorphism : Operator Overloading
#When the same operator is allowed to have different meaning based on the context, it is called operator overloading. In python, we can overload operators by defining special methods in the class.

# Operators & Dunder functions
#a+b # addition  a.__add__(b)
#a-b # subtraction a.__sub__(b)
#a*b # multiplication a.__mul__(b)
#a/b # division a.__truediv__(b)
#a%b # modulus a.__mod__(b)


# print(1 + 2) #3
# print("apna" + "college") #concatenation
# print([1,2,3] + [4,5,6]) #merge
# # the operator '+' is overloaded to concatenate the string


# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img
    
#     def showNumber(self):
#         print(self.real, "i+", self.img, "j", sep="")


#     def add(self, num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return  Complex(newReal, newImg)




# num1 = Complex(1,3)
# num1.showNumber()

# num2 = Complex(4,6)
# num2.showNumber()

# num3 = num1.add(num2)
# num3.showNumber()

#making using of dunder functions

# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img
    
#     def showNumber(self):
#         print(self.real, "i+", self.img, "j", sep="")


#     def __add__(self, num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return  Complex(newReal, newImg)

#     def __sub__(self, num2):
#         newReal = self.real - num2.real
#         newImg = self.img - num2.img
#         return  Complex(newReal, newImg)



# num1 = Complex(1,3)
# num1.showNumber()

# num2 = Complex(4,6)
# num2.showNumber()

# num3 = num1+num2
# num3.showNumber()

# num4 = num1-num2
# num4.showNumber()

#PRACTICE
#1)Define a circle class to create a circle with radius r using the constructor.
#define an Area() method of the class which calculates the area of the circle.
#Define a perimeter() method of the class which allows you to calculate the perimeter of the circle.

# class Circle:
#     def __init__(self, r):
#         self.r = r

#     def Area(self):
#         return (22/7) * self.r **2
    
#     def perimeter(self):
#         return 2 * (22/7) * self.r


# c1= Circle(21) 
# print(c1.Area())
# print(c1.perimeter())


#2) Define a Employee class with attributes role, department & salary. This class also has a showDetails() method.
#Make an engineer class that inherits properties from the Employee class & has an additional attributes: name & age.

# class Employee:
#     def __init__(self, role, department, salary):
#         self.role = role
#         self.department = department
#         self.salary =salary

#     def showDetails(self):
#         print("Role :", self.role)
#         print("Department :", self.department)
#         print("Salary :", self.salary)

# e1=Employee("Accountant", "Accounts", 60000)
# e1.showDetails()

# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer", "IT", "75000")

# eng1=Engineer("ice", 25)
# eng1.showDetails()


#3) Create a class called Order which stores item & its price.
#Use dunder function __gt__() to convey that:
#   order1>order2 if price of order1 > price of order2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self,odr2):
        return self.price > odr2.price

odr1 = Order("chips", 20)
odr2 = Order("tea", 15)
print(odr1 > odr2) 
