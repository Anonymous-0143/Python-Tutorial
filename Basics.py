# To create a variable, we need to give it a name. Variable names need to be a single words and therefore have no spaces.
# Example: home, home_city
# Variable names can contain numbers too. Example: Car_2
# After creating and naming a variable we can store value inside it too. Exapmle:
City = "Miami"
device_type="Windows"
# The values we are storing like "Miami", "Windows" are strings.
# String can contain spaces too. Example: 
Action = "Bro is coding"


# With the special instruction 'print()' we tell the computer to display a value in an area called the console or shell.
print("Hello Bro")
# We can use print() to print values of variables.
Name = "BigBro"
print(Name)


# Variables are called variables because their values can be changed/updated.
action = "Bro is Grinding"
action = "Bro is coding"
print(action)


# We can also give variables the value of other variables.
default = "Bro"
New = "Dude"

New = default
print("New")


# We can add string values together with a + sign
print("Followers:" + "55")
#Output will be:- Followers:55


# We will explore many kinds of values in Python without double quotes around them
Bro_age=19

# We can create expressions with numbers too.
Bro_Age=19+1
print(Bro_Age) # Output:- 20

# We use * sign to multiply numbers and / sign to divide numbers
Bro_relationships=17*0
print(Bro_relationships) # Output:- 0

Bro_class=69/69
print(Bro_class) # Output:- 1


# Since expressions become values, we can store calculation results in variables.
Bro_d=6
Dude_d=5
Total_d= Bro_d + Dude_d
print(Total_d) # Output:- 11


# True is a special value thats neither a string nor a number. True is great for situations like checking if a feature is on or if a data is available
Bro_exp=True
print(Bro_exp) # Output:- True

# False is another special value, opposite of true
print("Happy")
status= False
print(status) # Output:- False


# Not is a negation operator. It turns values into their opposite
print(not True) # Output:- False


# To compare if two numbers are same, we use equality operator, ==
# When comparing there are only two results: True or False.
print(69 == 96) #Output:- False


# To check if a number isn't equal to another number, we use the inequality operator, !=
print(69!=96) # Output:- True
