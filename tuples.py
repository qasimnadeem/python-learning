# tuple consists of a number of values separated by commas:

t = 12345, 54321, 'hello!'
print(t[0])

#output: 12345

#print(t)
#output: (12345, 54321, 'hello!')

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)
# output: ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

# Tuples are immutable:
t[0] = 88888
# TypeError: 'tuple' object does not support item assignment 
# but they can contain mutable objects:

# v = ([1, 2, 3], [3, 2, 1])
# print(v)
# output: ([1, 2, 3], [3, 2, 1])