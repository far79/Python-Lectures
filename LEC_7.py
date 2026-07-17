#FILE I/O in python
#python can be used to perform operations on a file.(read & write data)
#Types of all files
#1)Text Files: .txt, .docx, .log, etc.
#2)Binary Files: .mp4, .mov, .png, .jpeg etc.
#in memory, text and binary files, both are binary 

#Open, read & and close file
#We have to open a file before reading or writing.

# f=open("file_name","mode")
# example:
# file_name can be sample.txt or demo.docx
# mode=r:read mode,w:write mode

# f=open("/home/mint/Videos/geany/demo/demo.txt", "r")
# data=f.read()
# print(data)
# print(type(data))
# f.close()


#'r':open for reading(default)
#'w':open for writiing, truncating the file first
#'x':create a new file and open it for writing
#'a':open for writing, appending to the end of the file if it exists
#'b':binary mode
#'t':text mode(default)
#'+':open a disk file for updating(reading and writing)

#Reading a file
# f=open("/home/mint/Videos/geany/demo/demo.txt", "r")
# data=f.read(5)# prints 5 characters only
# print(data)


# line1=f.readline()#\n switches to next line in txt file, so python reads it and after first line leaves a blank line
# print(line1)

# line2=f.readline()
# print(line2)

# f.close()

#in above case there are some anomalies in result, discussed below

# f=open("/home/mint/Videos/geany/demo/demo.txt","r")

# data=f.read()
# print(data)

# line1=f.readline()
# print(line1)

# line2=f.readline()
# print(line2)

#once all data is read, the below line wise data is not read or printed


# line1=f.readline()
# print(line1)

# line2=f.readline()
# print(line2)


# data=f.read()
# print(data)
#another anomaly above

# f.close()


#Writing to a file
#f=open("demo.txt", "w")
# f.write("this is a new line")#overwrites the entire file

# f=open("/home/mint/Videos/geany/demo/demo1.txt","w")
# f.write("I want to learn JavaScript tomorrow. 123")
# f.close()

# f=open("demo.txt","a")
# f.write("this is a new line")#adds to the file

# f=open("/home/mint/Videos/geany/demo/demo1.txt","a")
# f.write("\nafter that node js")# \n for next line
# f.close()

#if a file which doesn't exist is opened, python creates it
# f=open("/home/mint/Videos/geany/demo/demo2.txt","a")#creates a new file


# f=open("/home/mint/Videos/geany/demo/demo3.txt","r+")
# f.write("abc")#replaces first three letter of line, with abc
# print(f.read())# pointer writes abc, pointer was before s so it reads from s onwards
# f.close()


# f=open("/home/mint/Videos/geany/demo/demo4.txt","w+")# w+ truncates the files and writes 
# f.write("abcd")
# print(f.read())#pointer after abcd, doesn't read anything
# f.close()


# with Syntax

with open("demo.txt","a") as f:
	data=f.read()

with open("/home/mint/Videos/geany/demo/demo5.txt","r") as f:#with closes the file automatically
	data=f.read()
	print(data)

with open("/home/mint/Videos/geany/demo/demo6.txt","w") as f:
	f.write("new data")



#Deleting the file
#using the os module
#module(like a code library)is a file written by another programmer that generally has a functions we can use.
#import os
#os.remove(filename)

# import os

# os.remove("/home/mint/Videos/geany/demo/demo7.txt")#deletes demo7

#PRACTICE
#Create a new file "practice.txt" using python. Add the following data in it:
# Hi everyone
# we are leanring file I/O
# using Java
# I like programming in Java

# with open("/home/mint/Videos/geany/demo/practice.txt","w") as f:
# 	f.write("Hi everyone\nwe are leanring file I/O\nusing Java\nI like programming in Java")


#WAF that replace all occurrences of "java" with "python" in above file.

# def rep(x,y):
# 	with open("/home/mint/Videos/geany/demo/practice.txt","r") as f: 
# 		data=f.read()

# 	# with open("/home/mint/Videos/geany/demo/practice.txt","w") as f:
# 	new_data=data.replace(x,y)

# 	with open("/home/mint/Videos/geany/demo/practice.txt","w") as f:
# 		f.write(new_data)
	
# rep("Java","python")


#WAF if the word "learning" exists in the file or not

# def find(n):
# 	with open("/home/mint/Videos/geany/demo/practice.txt","r") as f: 
# 		data=f.read()
# 		if(data.find(n)!=-1):
# 			print("Found")
# 		else:
# 			print("not found")


# find("learning")
# find("what")
# find("Java")
# find("java")
		



#WAF to find in which line of the file does the word "learning" occur first.
#print -1 if word not found

# def find_line(n):
# 	data=True
# 	line_no=1
# 	with open("/home/mint/Videos/geany/demo/practice.txt","r") as f: 
# 		while data:#data is being used as condition, first it is true and data=f.readline() provides value, but at end of file it becomes empty so loop ends
# 			data=f.readline()
# 			if(n in data):
# 				print(line_no)
# 				return
# 			line_no+=1
# 	print("-1")
# 	return -1

# find_line("hello")



#From a file containing numbers separated by comma, print the count of even numbers



#Below code lines prints numbers from file(exception: the last number should end with comma to be checked)
# with open("/home/mint/Videos/geany/demo/practice1.txt","r") as f:
# 	data=f.read()
	
# 	num=""
# 	for i in range(len(data)):
# 		if(data[i]==","):
# 			print(int(num))
# 			num=""
# 		else:
# 			num+=data[i]
	

#below code prints only even number(exception: the last number should end with comma to be checked)
# with open("/home/mint/Videos/geany/demo/practice1.txt","r") as f:
# 	data=f.read()
	
# 	num=""
# 	for i in range(len(data)):
# 		if(data[i]==","):
# 			if(int(num)%2 == 0):
# 				print(int(num))
# 			num=""
# 		else:
# 			num+=data[i]



#below code prints only even number	
# count=0
# with open("/home/mint/Videos/geany/demo/practice2.txt","r") as f:
# 	data=f.read()

# 	nums=data.split(",")
# 	for val in nums:
# 		if(int(val)%2==0):
# 			count+=1


# print(count)














