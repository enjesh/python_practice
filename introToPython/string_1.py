# A string can be surrounded by either single quotes or double quotes. 'word' "a sentence"

print("Welcome to the world of Python")

word = 'Marathon'

print(word[0]) # character in position 0
print(word[5]) # character in position 5
print(word[-1]) # last character
print(word[-2]) # second-last character
print(word[0:2])  # characters from position 0 (included) to 2 (excluded)
print(word[2:5])  # characters from position 2 (included) to 5 (excluded)
print(word[:2])   # character from the beginning to position 2 (excluded)
print(word[4:])   # characters from position 4 (included) to the end
print(word[-2:])  # characters from the second-last (included) to the end


print(len(word))
print(word)

name = 'Monty'
print(name)

# Type a string across multiple lines (with line breaks) so that the string is easier to read in the program.
# use a triple quote (""") before and after the string.
story = """Once upon a time in
a galaxy far far away was a coder
who loved nothing more than to code in Python!"""
print(story)


# If string includes apostrophes, consider surrounding the string with double quotes
advice = "You shouldn't eat candy for dinner."
print(advice)

book = 'My favorite book is "Where the Red Fern Grows" by Wilson Rawls.'
print(book)

# Escape Characters \(backslash), \n(new line)
# Backslash followed by the character you want to use
feedback = 'The teacher said "You shouldn\'t quit! Keep trying!"'
print(feedback)

# \n escape character creates a new line in the string
quote = 'Dream it.\nWish it.\nDo it.'
print(quote)

# capitalize() method capitalizes the first character
name = 'bridget'
print(name.capitalize())

# title() method capitalizes the first character for each word
book = "the linux command line a complete introduction"
author = "william shotts"

print(book.title())
print(author.capitalize())
print(author.title())


# strip() takes away the unnecessary characters
mood = '!!!happy!!!'
print(mood.strip('!'))

season = ' Summer'
print(season.strip())

# lower() turns all characters to lowercase characters.
whisper = 'DO YOU WANT TO HEAR A SECRET?'
print(whisper.lower())

# upper() turns all characters to uppercase characters
yell = "today's the greatest day ever!"
print(yell.upper())

# replace() the selected character is replaced with your desired character 
# selected character & desired character are referred to as arguments
opinion = 'Learning Python is hard!'
print(opinion.replace('hard', 'interesting'))


# len() counts the total number of characters in a string.
city = "Nairoberry"
print(len(city))

# concatenation of strings using + operator
animal_first_half = 'mon'
animal_second_half = 'key'
print(animal_first_half + animal_second_half)

#  Python does not automatically include a space when you concatenate. Add it to code
first_hobby = 'I like to crochet'
second_hobby = 'and take a walk in nature.'
print(first_hobby + ' ' + second_hobby)


# Python does not allow you to concatenate a string and integer variable together
# Calling str() on either a float or an int will change the value to a str
# This change applies only to the output and does not change the type of the original variable

# city = 'Los Angeles'
# state = 'CA'
# zip_code = 90028
# location = city + ', '+ state + ' ' + zip_code

city = "Nairobi"
country = "Kenya"
postal_code = 100
location = city + ', ' + country + ' ' + str(postal_code)
print(location)
print(f"Hello I am Elizabeth from {city}, {country} and postal address is 00{postal_code}")

# String Formatting
dog_breed = 'poodle'
name = 'Lola'
age = 3
print(f'I have a pet {dog_breed}. Her name is {name}.She is {age}.')


# Python starts to count with the number 0! 
# Each character in a string is assigned a position or index
# Index indicates the position of the character in the string
# The last character has an index of –1 and python can count backwards.
# Slicing enables you to specify two indexes:
#       (1) where to start looking for characters
#       (2) where to stop looking for characters
#       variable[start:stop]