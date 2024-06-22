 # We use an if statement to write code that adapts to different situations.
if True:
    print("Hello Bro!!")
# The if statement only runs code only if the boolean its relying on is True.

# Setting the boolean to false skips the code.
if False:
    print("Bye Bro") # Output:- Code gets skipped

# Instead of using boolean True or False we can save it in a variable and use it as a condition
Bro = True
if Bro:
    print("Hello Dude")


# To make smarter decisions in our programs, we use if statements.
Smart = "Bro"
if Smart == "Bro":
    print(Smart + "is cool") # Output:- Bro is cool

Noob = "Dude"
if Noob == "Dude":
    print(Noob + "is noob") # Output:- Dude is noob


# Add another if statement to get output if condition is false (This is called nesting of if statements)
ARC = True
if ARC:
    print("Bro is cool")
if not ARC:
    print("Dude is cool")  # Output:- Bro is cool

# Instead of using multiple if statements we can use if/else statement.
ARC = True
if ARC:
    print("Bro is cool")
else:
    print("Dude is cool") # Output:- Bro is cool


# Elif stands for else if. elif is used when there is a second condition to be checked when the condition of if block was not met.
dude = 12
if dude < 17:
    print("Dude is teen")
elif dude < 13:
    print("Dude is kid") # Output:- Dude is kid


marks = 78
if marks > 90:
    print("You get an A")
elif marks > 70:
    print("You passed")
else: 
    print("Better luck next time") # Output:- You passed


# We use 'and' if we want to run code depending upon two conditions  
Bro_age = 19
Bro_exp = True
if Bro_age >= 18 and Bro_exp:
    print("Bro can Drive")

# We can use and multiple times.
Bro_age = 19
Bro_exp = True
Bro_insured = True
if Bro_age > 18 and Bro_exp and Bro_insured:
    print("Bro can Drive")


# To run code when either one of the conditions is True, we use 'or' operator
Bro_grade = "B"
Bro_marks = 180
if Bro_grade == "B" or Bro_marks > 150:
    print("Bro Passed")


Bro = False
views = 100
shares = 30
likes = 70

if views > 150 or shares >= 50 or likes >= 60:
    Bro = True