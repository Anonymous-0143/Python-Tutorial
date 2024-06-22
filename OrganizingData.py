# Rather than creating a variable for each new piece of data, we can collect related data inside a 'list' using [ ]
Bro = ["Eat", "Sleep", "Code"]
print(Bro)
#Output:- ['Eat', 'Sleep', 'Code']

# Every element in a list has a numbered position called an index. They start with zero and increase with each further value.
Bro = [33, 66, 99]
print(Bro[1]) # Output:- 66

# To change a value in a list, access it and assign it a new value.
Bro = [33, 66, 99, 22]
Bro[3] = 777
print(Bro) # Output:- [33, 66, 99, 777]

# For updating element in a list we use 'append'.
bro = [22, 44, 66]
bro.append(88)
print(bro) # Output:- [22, 44, 66, 88]

# We add a value to a specific index with 'insert()'.
Bro = ["Eat", "Sleep", "Repeat"]
Bro.insert(2, "Code")
print(Bro) # Output:- ['Eat', 'Sleep', 'Code']
# We can only add 1 element at a time using insert() and append()

# To remove last element of a list we can use the instruction pop()
List = ["Bro", "Dude"]
List.pop()
print(List) # Output:- ['Bro']

List = ["Bro", "Dude", "Bhai"]
List.pop(1)
print(List) # Output:- ['Bro', 'Bhai']


# To loop through all the elements of list use 'for' loop
Dude = [11, 33, 55, 77]
for Bro in Dude:
    print(Bro)  
# Output:- 
# 11
# 33
# 55
# 77

Lists = ["Bro", "Dude"]
for List in Lists:
    print(List)
    print("*****")
# Output:-
# Bro
# *****
# Dude
# *****


# We use the len() instruction with the list name in parentheses to get the number of element in a list.
List = ["bro", "dude", "bhai"]
print(len(List)) # output:- 3

# We can use list length to create  conditional statements based on the number of elements.
List = ["Bro", "Dude", "Bhai"]
if len(List) > 0:
    print("All are legends!!")

