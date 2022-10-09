"""Python String Format() Method"
    The format() method formats the specified value(s)
and insert them inside the string's placeholder.
The placeholder is defined using curly brackets:{}.
Read more about the placeholders in the Placeholder 
section below.
Eg.
#named indexes:
txt1="welcome to {fname}{lname}".format(fname="aklink",
lname="world"
#numbered indexes:
txt 2="welcome to {0} {1}". format("aklink","world")
#empty placeholders:
txt3="welcome to {}{}". format("aklink", "world")
print(txt1)
print(txt2)
print(txt3)
"""
