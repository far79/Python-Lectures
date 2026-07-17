# LOOPS IN PYTHON
# loops are used to repeat instructions

# while loops
#  while condition
#    #some work:
# count=1
# while count<=5 :
#     print("hello")
#     count+=1

# print(count)

# iteration: the process of going through loop
# iterator: it makes the code go in loop


# i=1
# while i<=100:
#     print("IceFire",i)
#     i+=1
# print(i)

# print("loop ended")

# i=5
# while i>=1 :
#     print(i)
#     i-=1
 
# print("loop ended")


# PRACTICE
# print numbers from 1 to 100
# i=1
# while i<=100 :
#     print(i)
#     i+=1


# print numbers from 100 to 1
# i=100
# while i>=1 :
#     print(i)
#     i-=1

# print the multiplication table of a number n

# i=1

# while (3*i)<=30 :
#     print(3*i)
#     i+=1


# print the elements of the following list using a loop:
# [1,4,9,16,25,36,49,64,81,100]

# ~ i=1

# ~ while i<=10 :
#     ~ print(i**2)
#     ~ i+=1
 
# search for a number x in this tuple using loop:
# [1,4,9,16,25,36,49,64,81,100]


# print table of number
# i=1
# while i<=10:
#     print(3*i)
#     i+=1
# OR
# n=int(input("enter number:"))
# i=1
# while i<=10:
#     print(n*i)
#     i+=1


# print the elements of the following list using a loop:
# [1,4,9,16,25,...,100]
# i=1
# while i<=10:
#     print(i**2)
#     i+=1

# OR

# nums=[1,4,9,16,25,36,49,64,81,100]
# i=0
# while i<=9:
#     print(nums[i])
#     i+=1

# list1=["a","b","c","d"]
# idx=0
# while idx<len(list1):
#     print(list1[idx])
#     idx+=1


# search for a number x in this tuple using loop:
# (1,4,9,16,25,36,49,64,81,100)
# tup1=(1,4,9,16,25,36,49,64,81,100)
# x=int(input("Enter number:"))
# idx=0
# while idx<len(tup1):
#     if x==tup1[idx]:
#         print("Given number's position is:", idx+1)
#     idx+=1
# In the above method, suppose x=36, even after finding 36, it stills check further index

# tup1=(1,4,9,16,25,36,49,64,81,100)
# x=int(input("Enter number:"))
# idx=0
# while idx<len(tup1):
#     if x==tup1[idx]:
#         print("Given number's position is:", idx+1)
#     else:
#          print("finding...")
#     idx+=1


# BREAK & CONTINUE
# break:used to terminate the loop when encountered
# continue:terminates execution in the current iteration & continues execution of the loop with the next iteration

# i=1
# while i<=5:
#     print(i)
#     if(i==3):
#         break
#     i+=1

# print("end of loop")

#example of search 
# tup1=(1,4,9,16,25,36,49,64,81,100)
# x=int(input("Enter number:"))
# idx=0
# while idx<len(tup1):
#     if x==tup1[idx]:
#         print("Given number's position is:", idx+1)
#         break #break added
#     else:
#          print("finding...")
#     idx+=1
    

# CONTINUE:terminates execution in the current iteration & continues execution of the loop with the next iteration. 


# i=0
# while i<=5:
#     if(i==3):
#         i+=1
#         continue #skip
#     print(i)
#     i+=1

# i=1
# while i<=10:
# 	if(i%2==0): #replace '=' with '!' for printing even numbers
# 		i+=1
# 		continue
# 	print(i)
# 	i+=1


#Loops are used for sequential traversal. For traversing list, string, etc.
#for loops
#example:
# list=[1,2,3]
# for el in list:
#     print(el)

# nums=[1,2,3,4,5]
# for val in nums:
#     print(val)


# veggies=["potato","brinjal","ladyfinger","cucumber"]

# for veg in veggies:
#     print(veg)


# tup=(1,2,3,4,2,8,9)

# for num in tup:
#     print(num)

# str="apnacollege"

# for char in str:
#     print(char)



#for loop with else
# str="apnacollege"

# for char in str:
#     print(char)
# else:
#     print("End ") # but if only print("End")was given then it would work, why else? check below


# str="apnacllege" #add "o" to check different result

# for char in str:
#     if(char == "o"):
#         print("o found")
#         break
#     print(char)
# else:
#     print("End")


#PRACTICE
#print the elements of the following list using a loop:
#[1,4,9,16,25,36,49,64,81,100]

# nums=(1,4,9,16,25,36,49,64,81,100)

# for el in nums:
#     print(el)

# for el in nums:
#     print(nums)

# for nums in nums:
#     print(nums)

#Search for a number x in this tuple using loop:
#[1,4,9,16,25,36,49,64,81,100]

# nums=[1,4,9,16,25,36,49,64,81,100]
# x=49

# idx=0
# for y in nums:
#     if(x==y):
#         print("number found at idx", idx)
#         break
#     idx+=1


#range() function
#range functions returns a sequence of numbers, starting from 0 by default, and increments by 1(by defualt), and stops before a specified number.
#range(start?,stop,step?)

# print(range(5))

# seq=range(5)

# for i in seq:
#     print(i)

#OR

# j=0
# while j<=4:
#     print(seq[j])
#     j+=1

#OR

# for i in range(10):
#     print(i)

#start?, (?-means optional)
#stop
#step?
# for i in range(10):#range(stop)
#     print(i)

# for i in range(2,10): #range(start, stop)
#     print(i)

# for i in range(2,10,2): #range(start, stop, step)
#     print(i) # step incrased next number by two

# for i in range(2,101,2): #prints even number
#     print(i)

# for i in range(1,100,2): # prints odd number
#     print(i)

#PRACTICE
#Solve using for & and range()


#print numbers from 1 to 100
# for i in range(1,101):
#     print(i)

#print numbers from 100 to 1

# for i in range(100,0,-1):
#     print(i)
    

#print the multiplication table of n

# n=7
# for i in range(1,11):
#     print(n,"x",i,"=",n*i)

#pass statement
#pass is a null statement that does nothing. It is used as a placeholder for future code.

# for i in range(5):
#     #empty

# print("some useful work")#error because ntg inside loop

# for i in range(5):
#     pass

# if i>5:
#     pass

# print("some useful work")


#WAP to find the sum of first n numbers.(using while)
# n=7

# sum=0
# for i in range(n+1):
#     sum+=i


# print("total sum=",sum)

#OR using while looop
# n=7
# sum=0
# i=1
# while i<=n:
#     sum+=i
#     i+=1

# print("total sum=",sum)

#WAP to find the factorial of first n numbers.(using for)

# n=5
# fac=1
# for i in range(1,n+1):
#     fac*=i

# print("factorial of",n,"=",fac)
#OR

# n=5
# fac=1
# i=1
# while i<=n:
#     fac*=i
#     i+=1

# print(fac)

























