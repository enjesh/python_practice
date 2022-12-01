# This app will ask classmates their name and a few questions about themselves.
# Afterward, the app will share the answers given by the classmates.

# Greeting
print ("""Hello everyone. I trust that you enjoyed your break.
    Welcome back to school!! Please answer the following questions
        to introduce yourself""")

# Question 1      
name = input("What is your name? ")
# print (name)

# Question 2
color = input("What is your favorite color?")
# print (color)

# Question 3
food = input("What is your favorite food?")
# print (food)

# Question 4
show = input("What is your favorite TV show?")
# print (show)

# OUTPUT
print (f"""Everyone, meet {name}! {name}'s favorite 
color is {color}. {name}'s favorite food 
is {food}. {name}'s favorite TV show is 
{show}.""")
