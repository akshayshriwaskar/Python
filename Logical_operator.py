"""Operator     Description             Example
    and         Returns True if both    x<5 and x<10
                statements are true

    or          Returns True if one      x<5 or x<4
                of the satements is
                true

    not         Reverse the result,     not(x<5 and x<10)
                returs False if the
                result is true
"""

x=10
y=20

print(x==10 and x<y and x==y) #and
print(x==10 or x<y or x==y)   #or
print(not x!=10)              #not
