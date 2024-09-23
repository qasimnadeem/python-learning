#String is sequence of characters
# s= "Wonderful great"
# print(s)

# Multiline Strings
# You can assign a multiline string to a variable by using three quotes:

# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)

#Or three single quotes:

# a = '''Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.'''
# print(a)

# Strings in Python are Arrays of bytes representing unicode characters. However, Python does not have a character data type, a single character is simply a string with a length of 1.

# Square brackets can be used to access elements of the string.

# a = "Good to GO"
# print(a[1])

# for x in "Trainings":
#   print(x)

#IN
# txt = "The best things in life are free!"
# print("free" in txt)


#Not In
# txt = "The best things in life are free!"
# if "expensive" not in txt:
#   print("No, 'expensive' is NOT present.")

#Concatenate
# a = "Hello"
# b = "World"
# c = a + b
# print(c)

#Formatting

# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

# To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

# age = 36
# txt = f"My name is John, I am {age}"
# print(txt)

# price = 59
# txt = f"The price is {price:.2f} dollars"
# print(txt)

#Escape Characters
# txt = "We are the so-called \"Vikings\" from the \nnorth."
# print(txt)