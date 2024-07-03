
#use a list as a stack, where the last element added is the first element retrieved (“last-in, first-out”)
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
#print(stack)
# [3, 4, 5, 6, 7]
#print(stack.pop())
# 7
# print(stack)
# [3, 4, 5, 6]
# print(stack.pop())
# 6
# print(stack.pop())
# 5
# print(stack)
# [3, 4]


#list as a queue, where the first element added is the first element retrieved (“first-in, first-out”);
#While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one).

#To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends. For example:

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
# print(queue.popleft())                 # The first to arrive now leaves

# print(queue.popleft())                 # The second to arrive now leaves
queue.popleft()
queue.popleft()
print(queue)                           # Remaining queue in order of arrival
#output: deque(['Michael', 'Terry', 'Graham'])