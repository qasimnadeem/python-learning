
# list3= ["great","yes","no"]
# print(list3)
# print(list3[0])

#pass

list= ["great","yes","no","ok"]
# for i in list:
#     print(i)
    
# for i in range(len(list)):
#     print(i+1,list[i])

# for i in range(len(list)):
#     if i == 1: continue
#     print(list[i], end =". ")
    #if i > 1: break;

# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for i in sorted(basket):
#     print(i)

#set() removes the duplicate elements. The use of sorted() in combination with set() over a sequence is an idiomatic way to loop over unique elements of the sequence in sorted order.

# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for f in sorted(set(basket)):
#     print(f)

#List functions
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
#print(fruits.count('apple'))

# print(fruits.count('tangerine'))

#print(fruits.index('banana'))

#print(fruits.index('banana', 4))  # Find next banana starting at position 4

# fruits.reverse()
# print(fruits)

# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']

# fruits.append('grape')
# print(fruits)

# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
# fruits.sort()
# print(fruits)

# Example -> Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

