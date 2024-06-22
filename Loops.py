# Self assignment is when we set a variable to its own value.
Bro = 20
Bro = Bro
print(Bro) # Output:- 20


# As we can self assign variables, we can increases or decrease variables set to numbers.
bro = 20
bro = bro + 49
print(bro) # Output:- 69

bro = 30
bro = bro + 49
bro = bro - 10
print(bro) # Output:- 69

name = "Name: "
name = name + "Bro"
name = name + "Dude"
print(name) # Output:- Name: Bro Dude

# Rather than rewriting the variables name, we can use the += operator to add a number
Bro = 25
Bro += 44
print(Bro) # Output:- 69

# Similarily we can use -= operator
Bro = 80
Bro -= 1
print(Bro) # Output:- 69


# To build larger programs and websites, we repeat lines of code using while loop
while True:
    print("Bro is cool")
# Output:- 
# Bro is cool
# Bro is cool
# Bro is cool
# - - - - - - 

while True:
    print("Bro is Pro")
    print("Dude is noob")
# Output:- 
# Bro is Pro
# Dude is noob
# Bro is Pro
# Dude is noob
# Bro is Pro
# Dude is noob

# A while loop will stop when its condition is satisfied

# To stop a while loop we start by creating a variable outside the loop. Inside the code block, we stop the loop by setting variable to False so that the condition returns False.
Bro = True
while Bro == True:
    print("Dude is noob")
    Bro = False # Output:- Dude is noob
    # The loop runs its entire code block because Bro is True at first but stops after we set Bro equals to False

# To control the times a while loop repeats, we start with a variable set to a number.
stop = 1
while stop < 4:
    print(stop)
    stop += 1
    # Output:- 
    # 1
    # 2
    # 3

counter = 3
while counter < 8:
    counter += 2
    print(counter)
    # output:- 
    # 4
    # 5
    # 6
    # 7
    # 8


# Using for loops, we can write programs with much less code.
for i in range(5):
   print("Bro is coding!!")
   # Output:-
   # Bro is coding!! 
   # Bro is coding!! 
   # Bro is coding!! 
   # Bro is coding!! 
   # Bro is coding!! 

# Adding a number like 3 inside range() means it will loop over the code block 3 times, from 0 until 3.
for i in range(6):
    print(i)
# Output:-    
# 0
# 1
# 2
# 3

# The variable before in, in this case, i, is the counter variable. It counts what repitition of the loop we're currently on.
for i in range(3):
    print(i)
    print("Bro is grinding")
    # Output:-
    # 0
    # Bro is grinding
    # 1
    # Bro is grinding
    # 2
    # Bro is grinding
