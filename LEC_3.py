#LISTS IN PYTHON
# ~ marks=[94.4, 87.5, 95.2, 66.4, 45,1]
# ~ print(marks)
# ~ print(type(marks))
# ~ print(marks[0])
# ~ print(marks[1])
# ~ #data of different type can be stored
# ~ k=[85,"J","Hyderabad",None]
# ~ print(k)

#REPLACEMENT
#strings are immutable(strings can not be replaced)<\, but list is mutable
# ~ k[0]=8.5
# ~ print(k)

#MAKING A LIST OF A GIVEN WORD
# ~ a=input("Enter the word: ")
# ~ a=list(a)
# ~ print(a)

#LIST SLICING
# ~ marks=[87,64,33,95,76]
# ~ print(marks[0:3])#ending index not included
# ~ print(marks[:len(marks)])
#indexing and negative indexing position is similar in Strings and Lists


#LIST METHODS
list=[2,1,3]
list1=["banana", "litchi", "apple"]
#list.append(4)#adds one element at end
# ~ list.append(4)
# ~ print(list)#list mutated


#list.sort #sorts in ascending order
#list.sort(reverse=True)#sorts in descending order
# ~ list.sort()
# ~ print(list)
# ~ list.sort(reverse=True)
# ~ print(list)
# ~ list1.sort()#replaces list1 in assecending
# ~ print(list1)
# ~ print(list1.sort())#prints None


#list.reverse #reverses the list
# ~ list.reverse()
# ~ print(list)
# ~ list1.reverse()
# ~ print(list1)


#list.insert(index, element) #element is inserted at that index, and the other element at that index is pushed forward
# ~ list.insert(1,5)
# ~ print(list)
# ~ list1.insert(2,"Mango")
# ~ print(list1)


#list.remove(1)#removes first occurence of 1(1 is element not index)
# ~ list2=[1,2,3,1]

#list.pop(index)
# ~ list2.pop(2)
# ~ print(list2)



#TUPLES IN PYTHON, enclosed in (...)
#Tuples aren't mutable
tup=(2,1,3,1)
# ~ print(tup[0])                  
# ~ tup[1]=7
# ~ print(tup)#tupple isn't mutable, error

# ~ tup1=()#empty tuple
# ~ print(tup1)

#for single value tuple, use comma
# ~ tup2=(2,)
# ~ print(type(tup2))
# ~ tup3=(2)#it is considered as a integer
# ~ print(tup3)
# ~ print(type(tup3))


#SLICING IN TUPLES
# ~ print(tup[0:len(tup)])
# ~ print(len(tup))

#TUPLE METHODS
#tup.index(element)#returns index of first occurence of element
# ~ print(tup.index(1))

#tup.count(element)#returns total occurences
# ~ print(tup.count(1))


###PRACTICE

#Ask name of three movies and store them in a list
# ~ mov1=input("Enter your first favourite movie:")
# ~ mov2=input("Enter your second favourite movie:")
# ~ mov3=input("Enter your third favourite movie:")

# ~ list1=[mov1,mov2,mov3]
# ~ print(list1)
#OR
# ~ list2=[]
# ~ list2.append(mov1)
# ~ list2.append(mov2)
# ~ list2.append(mov3)
# ~ print(list2)
#OR
# ~ list3=[input("1st movie:"),input("2nd movie:"), input("3rd movie:")]
# ~ print(list3)


#check if  a list contains a palindrome of elements.(Hint:use copy()method)
#Palindrome example: MAM, spelled backwards MAM, 121 backwards is 121

# ~ a=input("Enter the word: ")
# ~ a=list(a)
# ~ # print(a)
# ~ c=a.copy()
# ~ a.reverse()
# ~ print(c)
# ~ print(a)
# ~ print(a==c)



#WAP to count the number  of students with grade "A" in following tuple
grades = ("A", "B", "C", "A", "D", "A", "B")
# ~ count=grades.count("A")
# ~ print("Number of students with grade A:", count)

res=input("Enter the results:")
res=tuple(res)
print(res.count("A"))

#store the above values in a list and sort them from "A to D"
# ~ grades_list=list(grades)
# ~ grades_list.sort()
# ~ print(grades_list)
#doesnt work in this file in geany, but works fine in vs code
# ~ res_list=list(res)
# ~ res_list.sort()
# ~ print(res_list)

