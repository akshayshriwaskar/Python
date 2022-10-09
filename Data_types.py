"""Data types in python
Data Types List:
-Numeric
Integers
Float
Complex Numbers

-Sequence Type
String
List
Tuple

-Dictionary
-Set

"Mutable and Immutable Data Types
-Mutable object can change its state or contents and immutable objects cannot.

Mutable Data Types:
-List
-Dictionary
-byte array

Immutable Data Types:
-Int
-Float
-Complex
-String
-Tuple
-Set
"""

#Numbers
#integers
#float
#complex numbers
a=5
print(a,"is of type",type(a))
a=2.0
print(a,"is of type",type(a))
a=1+2j
print(a,"is of type",type(a))
a=5
print(a, type (a))

#String
#A string is a collection of one or more characters put in a
# single quote, double-quote or triple quote.
#- Multi-line strings can be denoted using triple quotes,""  or"""

s= "This is string"
print(s)
s="""A multiline string"""
print(s)

s='Hello@123'
print(s,type(s))

s='''
        Hello
        Welcome to Aklinkworld
'''
print(s)

s='10'
print(s,type(s))


#List-Mutable type(able for modify, update, delete)
#List is an ordered sequence of items.
#It is one of the most used datatype in Python and is very flexible.
#[]
#eg.a=[1,2.2,'ws']

l=[1,2.2, 'akshay']
print(l, type(l))
l[2]=10
print(l,type(l))

#Tuple- Immutable data type( not able for change data, modify and delete)
#Tuple is an ordered sequence of items same as a list.
# It is defined withn parentheses () where items are seperated by commas.
#t=(5,'progra,',1+3j)
t=(10,20,'hello')
print(t,type(t))
#t=(10)  'tuple' object does not support item assignment
print(t,type(t))
t=(10,20,'hello')
#t[1]=30
print(t,type(t))

#Dictionary- Mutable data type

#Dictionary is an unordered collection of key-value pairs.
#In python, dictionaries are defined within braces{} with each item being a
#pair  in the form key: value
# eg. d={1:'value','key':2}
# print(type(d))
#class 'dict'>

d={
    'course_name':'python',
    'course_duration':'2 month'
}
print(d['course_name'])
print(d, type(d))

#Set
#A set is an unordered collection of items.
#Every set element is unique (no duplicates) and must be immutable
# (cannot be changed)
#{}
#eg my_set={1,2,3}
#print(my_set)

s={10,20,30,10} #remove the same no.
print(s,type(s))

