#FUNCTIONS IN PYTHON
#block of statement that perform a specific task

# def calc_sum(a,b):#function defition, a and b are function parameters
# 	sum1=a+b
# 	print(sum1)
# 	return sum1
	
# calc_sum(3,5)#
# calc_sum(222,333)
# #OR
# def calc_add(a,b):
# 	return a+b

# sum=calc_add(1,2)
# print(sum)

# def print_hello():
# 	print("hello")

# print_hello()
# output=print_hello()# None because function doesn't return hello in variable
# print(output)



#average of 3 numbers

# def calc_avg(a,b,c):
# 	avg=(a+b+c)/3
# 	print(avg)
# 	return avg

# calc_avg(1,2,3) 
# print(type(calc_avg(1,2,3)))


#Built in and user functions

#sep and end are function defined inside print function
# print("Ice", "Fire") #sep=' '

# print("Ice")#end="\n"
# print("Fire")

# print("Ice","Fire",sep='')

# print("Ice",end="\n\n\n\n\n")
# print("Fire")


# def cal_prod(a=1,b=1):# assumes a=1 and b=1 only when cal_prod() is written as it is, ntg inside, it is  fine if a or b, any single one is alloted value, the other can be provided with value in function use
# 	print(a*b)
# 	return(a*b)

# cal_prod()


#PRACTICE
#WAF to print the length of a list.(list is the parameter)

cities=["delhi","gurgaon","noida","pune","mumbai","chennai"]
components=["cpu","gpu","memory","storage","cooling system"]
# def length_list(a):
# 	print(len(a))
# 	return len(a)

# length_list(cities)
# b=length_list(cities)# because return was there in function, it can be stored
# print(type(b))

# length_list(components)


#WAF to print the elements of a list in a single line.(list is the parameter)
# i=0
# while i<=4:
# 	print(components[i],end=" ")
# 	i+=1

# def print_list(c):#better because it can process for any length of list
# 	for item in c:
# 		print(item, end=" ")

# print_list(components)
# print_list(cities)


#WAF to find the factorial of n.(n is the parameter)

# def fac(n):
# 	i=1
# 	fac=1
# 	while i<=n:
# 		fac*=i
# 		i+=1
# 	print(fac)
# 	return fac


#WAF to convert USD to INR
# def converter(usd_val):
# 	print(usd_val,"usd","=",usd_val*95,"inr")

# converter(73)

#WAF to identify odd or even 
# def num_type(n):
# 	if(n%2==0):
# 		print("even")
		
# 	elif(n%2!=0):
# 		print("odd")
		
# num_type(2)
# num_type(57)



#RECURSION
#when a function calls itself repeatedly
# def show(n):
# 	if(n==0):
# 		return
# 	print(n)
# 	show(n-1)

# show(5)
#show(100)


# def show1(n):
# 	if(n==0):
# 		return
# 	print(n)
# 	show1(n-1)
# 	print("end")

# show1(5)

# def show2(n):
# 	if(n==0):
# 		return
# 	print(n)
# 	print("end")
# 	show2(n-1)

# show2(5)



#Factorial

# def fac(n):
# 	if(n==0 or n==1):
# 		return 1
# 	else:
# 		return n*fac(n-1)
	
# print(fac(4))
# print(fac(5))


#PRACTICE
#Write a recursive function to calculate the sum of first n natural numbers.

# def calc_sum(n):
# 	if(n==0):
# 		return 0
# 	return calc_sum(n-1)+n


# print(calc_sum(10))


#Write a recursive function to print all elements in a list.
#Hint: use list & index as parameters

# def print_list(list,idx=0):
# 	if(idx==len(list)):
# 		return
# 	print(list[idx])
# 	print_list(list,idx+1)


# fruits=["mango","litchi","apple","banana"]
# print_list(fruits,)






