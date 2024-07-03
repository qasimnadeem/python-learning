# Dictionaries are another useful data type built into Python is the dictionary.
# Dictionaries are sometimes found in other languages as “associative memories” or “associative arrays”. Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys.

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
#print(tel)

# output: {'jack': 4098, 'sape': 4139, 'guido': 4127}

# print(tel['jack'])

del tel['sape']
tel['irv'] = 4127
#print(tel)

# list(tel)
# ['jack', 'guido', 'irv']

#print(sorted(tel))

# print('guido' in tel)

# print('jack' not in tel)

# The dict() constructor builds dictionaries directly from sequences of key-value pairs:

print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098),('amir',6023)]))

# {'sape': 4139, 'guido': 4127, 'jack': 4098}

# In addition, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:

# {x: x**2 for x in (2, 4, 6)}

# {2: 4, 4: 16, 6: 36}

# When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:
# print(dict(sape=4139, guido=4127, jack=4098))

# {'sape': 4139, 'guido': 4127, 'jack': 4098}  