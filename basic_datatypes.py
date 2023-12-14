## Operators

#    + , - , * , / have their regular meaning

#    ** is used for exponentiation
print(3**2)   # prints 9

#    % operator  == return remainder after division

#   // operator  == floor division rounds quotient to smaller integer
print(9//4)   # 9/4 = 2.25 normal calculation ----  // returns 2
print (23//8)    # 23/8 = 2.87 normal calculation  ----  // returns 2 




## Variable Declaration

# num = 4
# x,y,z = 4,5,8

# variable  name start with letter or underscore, name cannot be same as built as in identifiers or reserved words
# try descriptive variable names
# pythonic way to name variables is to use all lowercase letters and underscores to separate thewords (called snake_case)
new_var =78

## Assignment Operators

#  += , -= , *= , /= , %= , //= have their usual meanings

# scientific notation eg.
print(4.445e8)    # here  4.445e8 = 4.445*10**8



#############################################################################################################################################

## Practice Question

# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
rainfall*=0.9
# add the rainfall variable to the reservoir_volume variable
reservoir_volume+= rainfall
# increase reservoir_volume by 5% to account for stormwater that flows
# into the resevoir in the days following storm
reservoir_volume*=1.05
# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume*=0.95
# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume-=2.5e5
# print the new value of the reservoir_volume variable
print(reservoir_volume)

# answer = 447627500.0

#################################################################################################################################################


### Integers And Floats
 
# Declaration 
intnum =4
floatnum=4.78
# keywords ( are not used to declare/define the data type)
# int -- 387
# float --38 7. , 393.13 -- with decimal 
print ( type (387.7) )

# operation involving int and float gives float 
print( 3 + 2.5)

# convert data type to int  -- int() function
print ( int(4.78) ) # directly remove digits after decimal

# convert data type to float -- float() function
print ( float(4) )  # add .0 at end

# float approximates fractional numbers eg.
num1 =1/3
print (num1) #1/3

# this may result in diff answers when operations are performed on float numbers
print( 0.1 + 0.1 + 0.1)   # gives 0.30000000000000004

# divide by zero gives ZeroDivisionError
# print (4/0)

## Best Practices In Python

# snake_case

# pythonic way to name variables is to use all lowercase letters and underscores to separate the words (called snake_case)
new_var_num = 78

# add spaces
# to lower priority operations multiple operations
# print(3*7 - 1+2)  # here space 3*7 is higher priority


## Booleans, Comparison & Logical Operators

# bool -- abbreviation for boolean value -- True/False

x = 42>48
print(x)
# > , < , >= , <=, == , != Comparison operators have their same meaning

# and , or , not Logical Operators have their same meaning

print( 4>3 and 9>5)
print ( not True )
print ( 4>7 or 8<75 )

age =14
is_teen = age>12 and age<20
print(is_teen)

not_teen = not(age>12 and age<20)


## Strings

# they are immutable ordered sequence of characters

# str keyword ( not used to declare/define string)

# single and double quotes acceptable

print("Hello")
print("hello")

welcome_message= "Hello everyone"

# define string which itself contains double quotes inside it, use the single quote eg.

pet_halibut = 'Why should I be tarred with the epithet "loony" merely because I have a pet halibut'
print(pet_halibut)

# define string which itself contains single quote inside it like in the word you're, use \'   ....eg.
salesman = ' I think you\'re an encyclopedia salesman '
print(salesman)

#or
salesman = "I think you're an encyclopedia salesman"
print(salesman)

# + sign used to combine strings
str1 = "Hello"
str2 = "World"
print(str1 + " " + str2)

# * sign used to repeat strings
str3 = "## "
print(str3 *5)

# len() function -- returns length of string
udacity_length = len("Udacity")
print(udacity_length)

# It is acceptable to index strings
first_word = "Hello"
print(first_word[0]) 


#####################################################################################################################################################

#Practice Question

coconut_count = "34"
mango_count="15"
tropical_fruit_count=coconut_count + mango_count
print(tropical_fruit_count)
print(type(tropical_fruit_count))


## STRINGS

# strings are always written in single quotes


# they are immutable ordered sequence of characters

# str keyword (not used to declare / define string)

# single and double quotes acceptable

print("Hello")
print('hello')

welcome_message = "Hello Everyone"

# define string which  itself contains double quotes inside it , use the single quote eg.

pet_halibut = 'Why should I be tarred with the epithet "loony" merely because I have a pet halibut'
print(pet_halibut) 

# define string which itself contains single quote inside it like in the word you're, use \'    .... eg.

salesman = ' I think you\'re an encyclopedia salesman'
print(salesman)

# + sign used to combine strings

str1 = "Hello"
str2 = "World"
print(str1 + " " + str2)

# * sign used to repeat strings
str3 = "##"

print(str3 * 5)

# len() function is used to return length of string
udacity_length = len ("udacity")
print(udacity_length)

# It is acceptable to index strings
first_word = "Hello"
print(first_word[0])



##############################################################################################################################################################################

# PRACTICE QUESTION

coconut_count="34"
mango_count="15"
tropical_fruit_count = coconut_count + mango_count
print(tropical_fruit_count)
print(type(tropical_fruit_count))

# We've just used the len function to find the length of strings. What does the len function return when we give it the integer 835 instead of a string?

# answer= Error

##############################################################################################################################################################################

## TYPE &TYPE CONVERSION

# Conversion Functions
# int(number_here)
# float(number_here)
# str(number_here)

count = int(4.7)
print(count)

grams = "35.0"
grams = float(grams)
print(type(grams))

# print("0" +5)    gives error as "0" is string and 5 an integer

print(type("hippo"*12))    # gives string as "hippo"*12 repeats the string 12 times


## STRING METHODS

# methods are special types of functions but unlike functions, methods are associated with specific types of objects like strings, integer etc.

# there are different methods depending on type of data

print("sebastian thrun".title()) 

# .title() method belong to object string
# converts first letter to uppercase

full_name = "sebastian thrun"
print(full_name.islower())

# .islower() method -- belong to object string and returns True if no character in uppercase

print("one fish, two fish , red fish, blue fish".count('fish'))

# .count('sub_string_here')  -- counts number of occurences of the sub_string -- belong to object string

# print() is also a method

# .format() method

print("Mohammed has {} balloons".format(27))
# prints -- Mohammed has 27 ballons

animal = "dog"
action = "bite"
print("Does your {} {}?".format(animal,action))

# prints -- "Does your dog bite?"

book1 = "Harry Potter"
book2 = "Helen Keller"
price1 = 45
price2 = 50
print("The books and prices are as follows {}:{},{}:{} ".format(book1,price1,book2,price2))

book_dictionary={
    'book1': 'Harry Potter',
    "book2": "Helen Keller",
    'price1': 45,
    'price2' : 50
}

print("\n The books and prices are as follows {book1},{price1},{book2}:{price2} ".format(**book_dictionary))
# **book_list is used to put list as parameter in .format() method

# .split() method

new_str = "The cow jumped over the moon" 

print( new_str.split())
# splits acc to spaces

print( new_str.split( ' ' , 3) )

# here separator is space i.e ' '
# maximum splits set to 3

print ( new_str.split(None,3) )
# None -- means no separator, thus by default,space is used as separator

##############################################################################################################################################################################

# PRACTICE QUESTION

# 1. What is the length of the string varaible verse?
# 2. What is the index of the first occurrence of the word 'and' in verse?
# 3. What is the index of the last occurrence of the word 'you' in verse?
# 4. What is the count of occurrences of the word 'you' in the verse?

verse = "If you can keep your head when all about you\n Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you, \n But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)
print("\n")
print(len(verse))
print( verse.index('and'))   # finds the first occurrence of the word
print( verse.rfind('you'))   # finds the last occurrence of the word
print( verse.count('you'))
answers={
    "A":len (verse),
    "B":verse.index('and'),
    "C":verse.rfind('you'),
    "D":verse.count('you') 
}

print("Answers to question: \n {A},\n{B},\n{C},\n{D}".format(**answers))

# Answers are 362,65,186,8


