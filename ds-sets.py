basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
#print(basket)                     

# show that duplicates have been removed {'orange', 'banana', 'pear', 'apple'}

# fast membership testing
# print('orange' in basket)         
# print('crabgrass' in basket)


# Demonstrate set operations on unique letters from two words, but python takes string as list

a = set('abracadabra')
b = set('alacazam')
print("a =",a)
print("b =",b)                                  # unique letters in a & b


#print(a - b)                              # letters in a but not in b


#print(a | b)                              # letters in a or b or both, example of union
# {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}

#print(a & b)                              # letters in both a and b
# {'a', 'c'}

#print(a ^ b)                              # letters in a or b but not both
# {'r', 'd', 'b', 'm', 'z', 'l'}

# Similarly to list comprehensions, set comprehensions are also supported:

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

# {'r', 'd'}