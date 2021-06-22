# Using and Managing Strings
# string casting
# string concatenation
# Casting methods

# single and double quotes
single_quotes = 'These\'re single quotes and working perfectly fine' #
double_quotes =  "These're double quotes also working fine"

# print(single_quotes)
# print(double_quotes)

# concatenation
First_Name = "James"
Last_Name = 'Bond'
#print(First_Name + " "+ Last_Name)

# Create a variable called age with int value and display age in the same line as James Bond
age ="20"
# print(f'{First_Name} {Last_Name} {age}')
# print("{} {} {}".format(First_Name, Last_Name, age))
# print(First_Name + " "+ Last_Name + age)
# print(type(age))
# print(type(int(age)))  # example of casting

# String slicing and Indexing (starts with 0)
greetings = "Hello World!"
            #01234567891011
#print(greetings)
# To confirm the length of this string method called len()
# print(len(greetings))
# print(greetings[0:5]) # slicing the string from index 0 - 4 upto 5
# print(greetings[-1]) #slicing the string from right to left
#
# print(greetings[6:]) # slice to print World!
# print(greetings[-6:]) # slicing using negative index

white_spaces = "Lots of white spaces                                                 "
#print(str(len(white_spaces))+" including white spaces")  #length of string including/with white spaces
# we have strip() that removes all the white spaces
#print(str(len(white_spaces.strip()))+" excluding white spaces") #length of string excluding/without white spaces

# some more built-in methods that we can use with strings
example_text = "here's Some text With lots of text"

print(example_text.count("text")) # count() method counts the word in the string
print(example_text.lower())
print(example_text.upper())
print(example_text.capitalize())
print(example_text.replace("With", ","))
