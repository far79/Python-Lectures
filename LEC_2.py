#STRINGS
# ~ str1="This is a string. It is in python"
# ~ str2="This is a string.\nIt is in python" #\n makes the next words in next line, if space is given then there will be one character space left in result
# ~ str3="This is a string.\tIt is in python"#\leaves tab space I think
# ~ print(str1)
# ~ print(str2)
# ~ print(str3)


           #BASIC OPERATIONS
#CONCATENATION
# ~ a="hello"
# ~ b="world"
# ~ c=a+b #a+b is concatenation, it prints helloworld
# ~ print(c)


#LENGTH OF STRING
# ~ str1="Ice"
# ~ len1=len(str1)
# ~ print(len1)

# ~ str2="Fire"
# ~ len2=len(str2)
# ~ print(len2)  

# ~ final_str=str1+str2
# ~ print(final_str)
# ~ final_str2=str1+" "+str2
# ~ print(final_str2)


#INDEXING
#(((Index means position
#str1=Ice_Fire
#     01234567)))
#str1[0]=I
#we can access charactres in a string, but can't modify it


#SLICING

#(used to access part of string)
# ~ str1="Ice Fire"
# ~ slc1=str1[0:5]#note that the last index letter is not included
# ~ print(slc1)
# ~ slc2=str1[0:9] #indexing gives 8 at e of fire, but keep 0:9 to get full word
# ~ print(slc2)
# ~ slc3=str1[0:3]
# ~ print(slc3)
# ~ print(len(str1))
# ~ slc4=str1[0:len(str1)]#can be used for full word
# ~ print(slc4)
# ~ slc5=str1[:len(str1)]#same as [0:len(str1)]
# ~ slc6=str1[2:]#same as [2:len(str1)]
# ~ print(slc5,slc6,sep="\n")

#backward indexing
# A   P   P   L   E
#-5  -4  -3  -2  -1
# ~ str2="APPLE"
# ~ print(str2[-3:-1])#letter having -1 index is not printed
# ~ print(str2[-5:len(str2)])#prints full word
# ~ print(str2[-5:5])#prints full word




#STRING FUNCNTIONS(str="JKLJKL.")
# str1="ice is cold"


#str.endswith("KL.")  #prints true if string ends with matter inside of "...", or else false
# ~ print(str1.endswith("old"))
# ~ print(str1.endswith("dl")) 


#str.capitalize()   #capitalize first character
# ~ print(str1.capitalize()) # this function doesn't replace old string(str1) but creates new string
# ~ print(str1)
 
# ~ str1=str1.capitalize() #this way the old string is replaced by new string
# ~ print(str1)

#str.replace("K","I") #replaces K with I
# ~ print(str1.replace("s","u"))
# ~ print(str1.replace("cold","hot"))


#str.find("K") #finds the index position of first K
# ~ print(str1.find("l"))
# ~ print(str1.find("U")) # U isnt there in str1, prints -1
# ~ print(str1.find("is")) #is starts from i, i index is 4


#str.count("J") #counts number of J
# ~ print(str1.count("i"))
# ~ print(str1.count("s"))
# ~ print(str1.count("cold")) 




###PRACTICE PROBLEMS###
#Users first name input and calculate length
# ~ fname=input("Enter your first name:")
# ~ print("length of your name is",len(fname))
#note:write length of your name is in print fn to make it more explanatory


#Program to count occurence of $
# ~ str1=input("Enter your line:")
# ~ a=str1.count("$")
# ~ print("number of $ is:", a) 

###***###


#CONDITIONAL STATEMENTS
# ~ age=18 

# ~ if(age>=18): #if(true), statement is written then the below statements are executed
	# ~ print("can apply for license") 
	# ~ print("can open a account")
# ~ if (age<18):
	# ~ print("can't apply for license")
	# ~ print("can't open a account")


# ~ l="red"
# ~ print(l=="red")
# ~ print(l=="G")


#elif=else if

# ~ light="green" #input("enter the colour of light in small characters:") ----> can be used 


# ~ if (light=="red"):
	# ~ print("stop")
# ~ elif(light=="green"):
	# ~ print("go")
# ~ elif(light=="yellow"):
	# ~ print("look")
#

# ~ print("end of code")

#difference between if and elif

# ~ num=5

# ~ if(num>3):
	# ~ print("greater than 3")
# ~ if(num>2):
	# ~ print("greater than 2")
# ~ #checks for both

# ~ if(num>3):
	# ~ print("greater than 3")
# ~ elif(num>2):
	# ~ print("greater than 2")
#



# ~ light="black" #input("enter the colour of light in small characters:") ----> can be used 


# ~ if (light=="red"):
	# ~ print("stop")
# ~ elif(light=="green"):
	# ~ print("go")
# ~ elif(light=="yellow"):
	# ~ print("look")
# ~ else:
	# ~ print("light is broken")
#

# ~ age1=2

# ~ if(age1>=18):
	# ~ print("can vote")#indentation
# ~ else:
	# ~ print("can't vote")
# ~ #
 
#Students marks and grades

# ~ marks=float(input("Enter student's marks:"))

# ~ if(marks>=90):
	# ~ print("Grade A")
# ~ elif(marks<90 and marks>=80):
	# ~ print("Grade B")
# ~ elif(marks<80 and marks>=70):
	# ~ print("Grade C")
# ~ else:
	# ~ print("Grade D")
#



#NESTING
# ~ age=85

# ~ if(age>=18):
	# ~ if(age>=80):#considering age 80 and above can't drive
		# ~ print("cannot drive")
	# ~ else:
		# ~ print("can drive")

# ~ else:
	# ~ print("can't drive")
#	
	

##PRACTICE
#Check number entered by user is even or odd
# ~ a=float((input("Enter a number:")))
# ~ if(a-int(a)!=0):
	# ~ print("given number is not even or odd")
# ~ else:
	# ~ b=a/2
	# ~ c=b-int(b)
	# ~ if(c==0):
		# ~ print("given number is even")
	# ~ elif(c!=0):
		# ~ print("given number is odd")
#
  
	
# ~ a=float((input("Enter a number:")))

# ~ if (a%1!=0):
	# ~ print("Given number is not even or negative")
# ~ else:
	# ~ a=int(a)
	# ~ if(a/2==0):
		# ~ print("Given number is even")
	# ~ else:
		# ~ print("Given number is odd")	
	
	   
#Find the biggest of 3 numbers given
# ~ a = float(input("Enter your first number: "))
# ~ b = float(input("Enter your second number: "))
# ~ c = float(input("Enter your third number: "))

# ~ # Check equality first
# ~ if a == b and b == c:
    # ~ print("Biggest number is", a)
# ~ elif a == b:
    # ~ if a > c:
        # ~ print("Biggest number is", a)
    # ~ else:
        # ~ print("Biggest number is", c)
# ~ elif a == c:
    # ~ if a > b:
        # ~ print("Biggest number is", a)
    # ~ else:
        # ~ print("Biggest number is", b)
# ~ elif b == c:
    # ~ if b > a:
        # ~ print("Biggest number is", b)
    # ~ else:
        # ~ print("Biggest number is", a)

# ~ # If all numbers are unique, handle them independently
# ~ else:
    # ~ if a > b and a > c:
        # ~ print("Biggest number is", a)
    # ~ elif b > a and b > c:
        # ~ print("Biggest number is", b)
    # ~ else:
        # ~ print("Biggest number is", c)
        
#from google ai
# ~ a = float(input("Enter your first number: "))
# ~ b = float(input("Enter your second number: "))
# ~ c = float(input("Enter your third number: "))

# ~ if a >= b and a >= c:
    # ~ print("Biggest number is", a)
# ~ elif b >= a and b >= c:
    # ~ print("Biggest number is", b)
# ~ else:
    # ~ print("Biggest number is", c)
    
     
#Check if number is multiple of 7 or not
# num=float(input("Enter number:"))
# if(num%1!=0):
# 	print("Decimals aren't multiples of 7")
# elif(num%7==0):
# 	print("Given numver is multiple of 7")
# else:
# 	print("Given number is not multiple of 7")



