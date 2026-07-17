
#To map with real world scenarios, we started using objects in code.
#This is called object oriented programming.

#Class & Object in Python
#Class is a blueprint for creating objects.

#creating class
# class Student:#Student is class name
	# name="karan"

#creating object(instance)
# s1=Student()
# print(s1)
# print(s1.name)

# s2=Student()
# print(s2.name)



# class Car:
# 	color="blue"
# 	brand="mercedes"

# car1=Car()
# print(car1.color)
# print(car1.brand)


# _init_ function(Constructor)
#All classes have a function called _init_(), which is always executed when the object is being initiated


# class Student:
# 	name="karan"
# 	def __init__(self):#the self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# 		print(self)
# 		print("adding new student in Database ...")

# s1=Student()
# print(s1.name)
# print(s1)

# s2=Student()
# print(s2.name)




# class Student:
# 	#default constuctor
# 	def__init__(self):
# 	pass


# 	#parameterized constructors
# 	name="karan"
# 	def __init__(self, name, marks):
# 		self.name = name
# 		self.marks = marks
# 		print("adding new student in Database ...")


# s1=Student("Ice",99)
# print(s1.name, s1.marks)

# s2=Student("Fire",100)
# print(s2.name, s2.marks)




#CLASS & INSTANCE ATTRIBUTES (attribute-data)(instance attributes are attributes which are not same for different object)(class attribute is same for different objects)
#class attributes
#object attributes



# class Student:
# 	college_name="ABC College"

# 	def __init__(self,name,marks):
# 		self.name = name
# 		self.marks = marks
# 		print("adding new student in Database")

# s1=Student("ice",99)
# print(s1.name,s1.marks,s1.college_name)
# print(s1.name,s1.marks,Student.college_name)


#object attr vs class attr

# class Student:
# 	college_name="ABC College"
# 	name="anonymous"#class attr

# 	def __init__(self,name,marks):
# 		self.name = name #obj attr > class attr
# 		self.marks = marks
# 		print("adding new student in Database")



# s1=Student("ice", 97)
# print(s1.name, s1.marks, s1.college_name)
 
# s2=Student("fire", 98)
# print(s2.name, s2.marks, s2.college_name)



#METHODS
#Methods are functions that belong to objects
# class Student:
# 	college_name="ABC College"
# 	name="anonymous"#class attr

# 	def __init__(self,name,marks):
# 		self.name = name #obj attr > class attr
# 		self.marks = marks
# 		print("adding new student in Database")

# 	def welcome(self):
# 		print("welcome student", self.name)

# 	def get_marks(self):
# 		return self.marks



# s1=Student("ice",97)
# s1.welcome()
# print(s1.get_marks())

#Create student class that takes name & marks of 3 subjects as arguments in contructor. Then create a method to print the average

# class Student:
# 	def __init__(self,name,marks):
# 		self.name=name
# 		self.marks=marks

# 	def get_avg(self):
# 		sum=0
# 		for val in self.marks:
# 			sum+=val
# 		print("hi", self.name,"your avg score is", sum/3)




# s1=Student("ice fire", [99,98,97])
# s1.get_avg()

# s1.name="fire ice"
# s1.get_avg()




#STATIC METHODS
#Methods that don't use self parameters(work at class level)
# class Student:
# 	def __init__(self,name,marks):
# 		self.name=name
# 		self.marks=marks

# 	@staticmethod #decorator
# 	def hello():
# 		print("hello")

# 	def get_avg(self):
# 		sum=0
# 		for val in self.marks:
# 			sum+=val
# 		print("hi", self.name,"your avg score is", sum/3)


# s1=Student("icefire", [99,98,97])
# s1.get_avg()
# s1.hello()

#Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function without permanently modifying it
 
 


#IMPORTANT
#Abstraction
#Hiding the implementation details of a class and only showing the essential features to the user.

# class Car:
# 	def __init__(self):
# 		self.acc = False
# 		self.brk = False
# 		self.clutch = False

# 	def start(self):
# 		self.clutch = True
# 		self.acc = True
# 		print("car started...")


# car1=Car()
# car1.start()


#Encapsulation
#Wrapping data and functions into a single unit(object)(data+function)



#PRACTICE
#Create Account class with 2 attributes-balance& account no.
#Create methods for debit, credit & printing the balance.


class Account:
	def __init__(self, bal, acc):
		self.balance = bal
		self.account_no = acc 

	def debit(self, amount):
		self.balance-=amount
		print("Rs", amount, "was debited")
		print("total balance =", self.get_balance())

	def credit(self, amount):
		self.balance+=amount
		print("Rs", amount, "was credited")
		print("total balance =", self.get_balance())

	def get_balance(self):
		return self.balance

acc1=Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit







