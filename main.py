# list (its mutable, means we can change the values of list)
number = [ 1 , 2 , 9 , 4 , 5]

# tuple ( its immutable, means we can't change the values of tuple and if we try to change the values it will return new object)
floor = ( 1 , 3 , 4)

# set (this will remove the duplicate values) 
my_set = { 1 , 2 , 2 , 3 , 1 , 4 ,"arisha" , 5 ,"karim" }

# frozenset (its immutable version of sets )
frozen_set = frozenset({ 1 , 2 , 2 , 3 , 1 , 4 ,"arisha" , 5 ,"karim" })

# integer (whole number)
Age = 19

# String (text wriiten in single & double quotes)
Name = "Arisha Karim"

# Multi line string (this will print the string as it is formatted )
intro = """I'm student of GIAIC \n Currently in Q3 and learning Python and Generated AI."""

# Float (numbers with decimal points)
Q2_Percentage = 82.57

# Boolean (True or False)
is_Q3_passed = True

# Range (this will generate a sequence of numbers)
my_range = range(5)

# None (absence of value)
Bank_Account = None

# Distionary (key value pair)
student = {
    "Name" : "Arisha Karim",
    "Age" : "19" ,
    "is_student" : True
}

print(f"List: {number}")
print(f"Tuple: {floor}")
print(f"Set: {my_set}")
print(f"Frozen set: {frozen_set}")
print(f"Integer: {Age}")
print(f"String: {Name}")
print(f"Multi-line string: {intro}")
print(f"Float: {Q2_Percentage}")
print(f"Boolean: {is_Q3_passed}")
print(f"Range: {list(my_range)}")
print(f"None: {Bank_Account}")
print(f"Dictionary: {student}")