# info={
#     "key": "value",
#     "name": "IceFire",
#     "learning": "coding",
#     "age":35,
#     "is_adult": True,
#     "subjects": ["Python", "JavaScript", "C++"],
#     12.99: 94.4
# }

# print(info)
# print(type(info))
# print(info["key"])
# print(info["name"])
# print(info["learning"])
# print(info["surname"]) #error because there is no key named "surname" in the dictionary 
# info["name"]="FireIce"
# print(info)



# null_dict={}
# null_dict["name"]="IceFire"
# print(null_dict)



# NESTED DICTIONARY
# student={
#     "name": "JJJ",
#     "subjects":{
#         "physics": 95,
#         "chemistry": 98,
#         "maths": 95
#     }
# }

# print(student["subjects"]["chemistry"])


# DICTIONARY METHODS

# 1)mydict.keys() #returns all key
# print(student.keys()) #nested keys are not returned by this method
# print(student["subjects"].keys())
# print(list(student.keys()))
# print(len(student))#prints no of key in dictionary
# print(len(list(student.keys())))
# print(len(student["subjects"]))


# 2)mydict.values() #returns all values
# print(student.values())
# print(list(student.values()))

# 3)mydict.items() #returns all (key,val) pairs as tuples
# print(student.items())
# print(student["subjects"].items())
# pairs=list(student.items())
# print(pairs[0])
# print(pairs[1])

# 4)mydict.get("key") #returns the value according to key
# print(student["name2"]) # Give error
# print(student.get("name2")) # gives none(so this lets below code run)


# 5)mydict.update(newdict) #inserts the specified items to the dictionary
# student.update({"city":"Delhi"})
# print(student)
# or
# new_dict={"District":"Delhi", "age"=28, "name":"KKK"}#name will be replaced, no new key will be created
# # student.update(new_dict)
# print(student)



# SETS IN PYTHON
# set is the collection of the unordered items(no value).
# each element in the set must be unique and immutable
# sets is mutable but elements is not mutable
# boolean,int,float,str, tuple is storable in sets and list, dictionary is not storable as they are mutable
# collection={1,2,3,4,5}#set is not ordered, not necesarry the order is printed
# collection1={1,3,5,2, "hello", "world","world"}
# print(collection)
# print(type(collection))
# print(collection1)
# collection3={} #empty dictionary
# print(type(collection3))
# collection4=set()#empty set
# print(type(collection4))



# SET METHODS

# 1)set.add(el)#adds and element
# immutable(hash values) can be added,but mutbale(unhashable)can'tbe added
# collection5=set()
# collection5.add(1)
# collection5.add(2)
# collection5.add(2)
# collection5.add([1,2,3])#error because lsit can't be added in sets 
# print(collection5)

# 2)set.remove(el)
# collection5.remove(1)
# print(collection5)
# collection5.remove(6) #error
# print(collection5)

# 3)set.clear()#empties the set
# print(len(collection5))
# collection5.clear()
# print(len(collection5))


# 4)set.pop() #a random value
# collection6={"hello", "apnacollege", "world", "coding", "python"}
# print(collection6)
# print(collection6.pop())#gives a random value


# 5)set.union(set2)#combines both set values and returns new
# set1={1,2,3}
# set2={3,4,5}
# print(set1.union(set2))

# 6)set.intersection(set2)#combines common values and returns new
# print(set1.intersection(set2))


# Practice Questions


# 1)store the foolowing word meaning in a python dictionary:
# table:"a  piece of furniture", "list of facts and figures"
# cat:"a small animal"
# dict={
#     "table":["a  piece of furniture", "list of facts and figures"],
#     "cat":"a small animal"
# }
# print(dict)


# 2)you are given a list of subjects for students, Assume one classroom is required for subject. How many classrooms are needed by all students
# "python", "java", "C++", "python", "javascript", "java","python", "java", "C++", "C"
# set1={"python", "java", "C++", "python", "javascript", "java","python", "java", "C++", "C"}
# print("No.of classrooms required:", len(set1))
# print(set1)

# 3)Enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value
# dict={
# }
# x=float(input("Enter your physcis marks:"))
# dict1={"physics":x}
# dict.update(dict1)

# y=float(input("Enter your maths marks:"))
# dict2={"maths":y}
# dict.update(dict2)
 
# z=float(input("Enter your chemistry marks:")) 
# dict3={"chemistry":z}
# dict.update(dict3)

# print(dict)


#Figure out a way ot store 9 & and 9.0 as separate values in the set.(You can take help of built in data types)
# val1={9,"9.0"}
# print(val1)
#or
# val1={
#     ("float", 9.0),
#     ("int",9)
# }
# print(val1)


























