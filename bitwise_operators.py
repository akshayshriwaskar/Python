"""Operator         Name                Description
     &              AND                     x&y
    |               OR                      X|Y
    ^               XOR                     X^Y
TRUTH TABLE:
A       B       A&B     A|B     A^B
0       0        0      0       0
0       1       0       1       1
1       0       0       1       1
1       1       1       1       0
"""

x=10
y=8
print(bin(x))         #0b1010
print(bin(y))         #0b1000
print(bin(x&y),x&y)   #0b1000 8
print(bin(x|y),x|y)  #0b1010 10
print(bin(x^y),x^y)  #0b10 2    0010