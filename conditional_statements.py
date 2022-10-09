#key points:
# 1. if statement
# 2. if else statement
# 3. if elif else statement

"""
if [conditional expression]:
        [statement(s) to execute]

Example:-

a=10
if a%2==0
print("Even Number");
"""
# a=int(input("Enter the value:-"))
# if a%2==0:
#     print(a,"Even Number")

"""If else statement"""
# a=int(input("Enter the value:-"))
# if a%2==0:
#     print(a,"Even Number")
# else:
#         print(a,"Odd Number")

"""if elif else statement
eg.if[condition #1]:
        [statement #1]
 elif[condition #2]:
        [statement #2]
 elif[condition #3]:
        [statement #3]
else:
        [statement when if and elif(s) are False]
Example:-                
per = 55
if per>=60:
        print("First Div")
elif per>=48:
        print("Second Div")
elif per>35:
        print("Third Div")
else:
        print("Fail")
         
"""

per=int(input("Enter the value:-"))
if per>=60:
    print("First Div")
elif per>=48:
    print("Second Div")
elif per>=35:
    print("Third Div")
else:
    print("Fail")