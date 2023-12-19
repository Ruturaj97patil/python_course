# DATA STRUCTURES

# -- are containers of data, contains different data types and even other data structures/containers

# LISTS AND MEMBERSHIP OPERATORS

# Lists

# A data type for mutable ordered sequences of elements 

# Lists can contain any mix and match of the data types you have seen so far

# declared with square brackets []

random_list = [147,34.25,'a string', True ]

print(random_list[2]) # inside [2] here 2 denotes the index and only prints the value which is present at 2 index.


months = ['January','February','March','April','May','June','July','August','September','October','November','December']

print(months[0])  # first element has index 0 
print(months[1])

# can retrieve last element of list by following method
print( months [ len(months)-1 ] )

# OR

print(months[-1])  #last element has index -1
print(months[-2])  # second last element has index -2
print(months[-12])

# print(months[18])
# gives error as Index out of range

# Slicing Lists

# using indexes

quarter_3 = months[6:9]  # index 6 to 9 i.e [6,9] including lower bound [6] and excluding upper bound [9] -- months[6] = July
print(quarter_3)

# slicing at beginning
print(months[:4])   # prints until month[3] = April,months[4] is excluded

# slicing at end
print(months[9:])  # months[9]= October

# negative indexes work in slicing
print(months[-10:-8])
print(months[:-4])
print(months[-4:])

# sting & lists both suppport len(), indexing and slicing , & membership operators
greeting="Hello World"
print( len(greeting) ) # len()
print(greeting[0] ) # indexing
print(greeting[2:10] ) # slicing [2,10]



# Membership Operators

# two operators:
# in -- evaluates whether object on left is noot included in object on right side

greeting = "Hello There"
print( 'her' in greeting , 'her' not in greeting)
print('Sunday' in months, ' Sunday' not in months)

# lists contain other data types while strings contain characters


# MUTABILITY AND ORDER


# Mutability

# is a term for whether an object can be modified after its creation.

# lists -- mutable , strings -- immutable

my_list = [1,2,3,4,5]
my_list[0]='one'
print(my_list)

greeting = "Hello"
print(greeting)

# Important feature of Mutability

# Mutable objects when assigned to another object, and then value of the mutable object is changed, the value of the other object also changes

# eg. (as lists are mutable)
scores=['A','B','C','D','E']
grades=scores
print(scores)
print(grades)

scores[2]='F'
print(scores)
print(grades) # grades[2] value is also changed automatically to 'F'

# eg. (strings are immutable)
name="Jim"
student=name
print(name)
print(student)

name = "Not Jim"
print(name)
print(student)

# Order 

# term for whether the order of elements in an object matters, and whether this can be used to access elements

# both lists and strings are ordered
