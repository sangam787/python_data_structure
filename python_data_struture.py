# _______________________________________________________________________________________________________________________________
# 1- Discuss string slicing and provide examples
"""
answer-1
If we need a substring of a particular string, then we simply use "string slicing".
We can return a range of characters by using the slice syntax. 
We need to specify the start index and the end index, separated by a colon, to return a part of the string.
For Example
"""
# str = "Hello, World!"
# print(str[1:5])

"slicing from the start"
"If we leave out the start index, the range will start at the first character."

# str = "Hello, World!"
# print(str[:5])

"slicing to the end"
"If we leave out the end index, the range will go to the end"

# str = "Hello, World!"
# print(str[1:])

"slicing by negative indexing"
"We can use negative indexes to start the slice from the end of the string"

# b = "Hello, World!"
# print(b[-5:-2])


# _________________________________________________________________________________________________________________________________
# 2- Explain the key features of lists in Python

"Python lists are changeable (mutable), which means they can have their elements changed after they are created." 
"for example"
# list = ["banana", "mango", "apple"]
# list[1] = "papaya"
# print(list)


"A list can also have values of different data types."
"for example"
# list = ["mango", 2, (4+5j), 7.5]
# print(list)



"The elements in the list are separated by using commas (,) and are surrounded by square brackets []."
"for example"
# list = ["bat", "ball", "gloves"]
# print(type(list))




# _____________________________________________________________________________________________________________________________________________
# 3- Describe how to access, modify, and delete elements in a list with examples

"""
(1) List Access Items:-
List items are indexed and we can access them by referring to the index number.
for example
"""
# listA = ["book", "pen", "box"]
# print(listA[1])

"""
Negative Indexing
Negative indexing means start from the end

-1 refers to the last item, -2 refers to the second last item etc.
for example
"""
# listA = ["book", "pen", "box"]
# print(listA[-1])

"""
Range of Indexes
We can specify a range of indexes by specifying where to start and where to end the range.
When specifying a range, the return value will be a new list with the specified items.
"""
# listB = ["lemon", "banana", "papaya", "orange", "kiwi", "melon", "mango"]
# print(listB[2:5])

"""
This will return the items from position 2 to 5.
Remember that the first item is position 0,
and note that the item in position 5 is NOT included

"""

"By leaving out the start value, the range will start at the first item"

# listB = ["lemon", "banana", "papaya", "orange", "kiwi", "melon", "mango"]
# print(listB[:5])

"By leaving out the end value, the range will go on to the end of the list"

# listB = ["lemon", "banana", "papaya", "orange", "kiwi", "melon", "mango"]
# print(listB[2:])

"To determine if a specified item is present in a list we use the in keyword"

# listB = ["lemon", "banana", "papaya", "orange", "kiwi", "melon", "mango"]
# if "orange" in listB:
#     print("Yes, 'orange is present in listB")

"""
(2) Modification of list:-
Change Item Value
"""
# listB = ["lemon", "banana", "papaya", "orange", "kiwi", "melon", "mango"]
# listB[1] = "potato"
# print(listB)
" We can also change a Range of Item Values."
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)
"""
Insert Items
To insert a new list item, without replacing any of the existing values, we can use the insert() method.

The insert() method inserts an item at the specified index:
"""
# listA = ["apple", "mango", "orange", "cherry"]
# listA.insert(1, "watermelon")
# print(listA)
"""
Append Items
To add an item to the end of the list, we use the append() method:
for example
"""
# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)
"""
Extend List
To append elements from another list to the current list, use the extend() method.
"""
# listA = ["apple", "banana", "cherry"]
# listB = ["mango", "pineapple", "papaya"]
# listA.extend(listB)
# print(listA)
"""
(3) Delete Elements:-
Remove Specified Item
The remove() method removes the specified item.
for example
"""
# listA = ["apple", "banana", "cherry"]
# listA.remove("banana")
# print(listA)
"""
Remove Specified Index
The pop() method removes the specified index.
for example
"""
# listA = ["apple", "banana", "cherry"]
# listA.pop(1)
# print(listA)

"""
The del keyword also removes the specified index 
for example
"""
# listA = ["apple", "banana", "cherry"]
# del listA[1]
# print(listA)        #>>"del keyword can also delete entire list."

#example
# listA = ["apple", "banana", "cherry"]
# del listA    

#  #>> print(listA) this will cause an error because we have succsesfully deleted "listA".
"""
Clear the List
The clear() method empties the list.

The list still remains, but it has no content.
for example
"""
# listA = ["apple", "banana", "cherry"]
# listA.clear()
# print(listA)


#___________________________________________________________________________________________________________________________
# 4- Compare and contrast tuples and lists with examples
"""
Answer-4

Tuples amd Lists both are built in data type in Python and other two Dictionary, Sets.

Tuples are immutable, unchangeable, ordered while Lists are muatable, changeable, ordered.
Both allows duplicates values.
Tuples are created by using "()" while List by "[]"

<class 'list'>  is the data type of Lists
<class 'tuple'> is the data type of Tuples

Example of immutability
"""
# ListA = ["Ram", "Shyam", "Gopal"] # if we want to change "shyam" with "Krishna" we can.
# ListA[1] = "Krishna"
# print(ListA)

# TupA = ("Ram", "Shyam", "Gopal") # while in tuple we will get an error.
# TupA[1] = "Krishna"
# print(TupA)





#______________________________________________________________________________________________________________________________
# 5- Describe the key features of sets and provide examples of their use
"""
Answer-5
Set:-

Sets are used to store multiple items in a single variable.
A set is a collection which is unordered, unchangeable(but we can remove items and add new items.), and unindexed.
Sets are written with curly brackets.
for example-
"""
# setA = {"apple", "banana", "mango"}
# print(setA)
"""
Set Items:-
Set items are unordered, unchangeable, and do not allow duplicate values.
for example
"""
# setA = {1,3,2,2,3,4,4,5}
# print(setA)

"The values True and 1, False and 0 are considered the same value in sets, and are treated as duplicates:"
"for example"
# setA = {1,True, "mango", 0, "banana", 1, False}
# print(setA)

"""
Length of a Set:-
To determine how many items a set has, use the len() function.
for example
"""
# setA = {"apple", "banana", "mango"}
# print(len(setA))


#____________________________________________________________________________________________________________________________
# 6- Discuss the use cases of tuples and sets in Python programming
"""
Tuples and Sets are built in data type funtions(in Python used to store collections of data) and 
other two are Dictionary, List.

Tuples are immutable while Sets are mutable objects.
In Sets we can add, modify, change the items while, in Tuples we can not add, change the items.

The Python sets are highly useful to efficiently remove duplicate values from a collection 
like a list and to perform common math operations like unions and intersections.

Tuples can have duplicates values but Sets can not have duplicate values.
Tuples are ordered while Sets are unordered.

"""




#_______________________________________________________________________________________________________________________________
# 7- Describe how to add, modify, and delete items in a dictionary with examples
"""
Dictionary:-

Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered, changeable and do not allow duplicates.
Dictionaries are written with curly brackets, and have keys and values:
for example
"""
# dictA = {
#     "name":"sangam",
#     "age": 25,
#     "course": "data analytics"
# }
# print(dictA)
"""
Adding Items
Adding an item to the dictionary is done by using a new index key and assigning a value to it:
for example
"""
# dictA = {
#     "name":"sangam",
#     "age": 25,
#     "course": "data analytics"
# }
# dictA["gender"] = "male"
# print(dictA)

"""
Update Dictionary
The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
The argument must be a dictionary, or an iterable object with key:value pairs.

Example
"""
# dictA = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# dictA.update({"color": "red"})
# print(dictA)

"""
Removing Items
There are several methods to remove items from a dictionary:

Example
The pop() method removes the item with the specified key name:
"""

# dictA = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# dictA.pop("model")
# print(dictA)

"The popitem() method removes the last inserted item"

# dictA = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# dictA.popitem()
# print(dictA)

"The del keyword removes the item with the specified key name:"

# dictA = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del dictA["model"]
# print(dictA)

"The del keyword can also delete the dictionary completely:"

# dictA = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del dictA
# print(dictA) #this will cause an error because "dictA" no longer exists.

"The clear() method empties the dictionary:"

# dictA = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# dictA.clear()
# print(dictA)



#_________________________________________________________________________________________________________________________________
# 8- Discuss the importance of dictionary keys being immutable and provide example
"""
It is very important that a dictionary Keys should be imutable because we assign a value to the Keys.
If Keys is not well defined the it will be confusing where we are assigning the values.
Immutability is essential for keys because it ensures that the dictionary can efficiently look up values based on their keys. 
If a key was mutable, its hash value could change, making it impossible to find the associated value in the dictionary. 
for example
"""
# dictA = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(dictA)

"""
In above example if we want to change the value then it is neccessary that key should be fixed otherwise how will change the value 
for a perticular key. That's why keys are immutable.
for example
"""
# dictA = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# dictA["year"] = 2024
# print(dictA)

"end of assignment"
