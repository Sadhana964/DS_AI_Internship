'''message = " Hello world! "
print(message.strip())
print(message.upper())
print(message.replace("world","python"))
'''

'''label = "data science"
print(label[0])
print(label[5:12])
'''

'''text = "python programming"
print(text[::-1])
print(text[:6])
print(text[7:])
print(text[0:3])
'''


'''text = "Python Programming is a high level"
words = text.split()        
word = words[1]             
letter = word[-1]           

print(letter)
'''

'''text = "I love /python programming/"
result = text.split("/")[1]
print(f"\"{result}\"")
'''

'''stack = [10, 20, 30, 40, 50]
print("Initial Stack:", stack)

stack.append(60)
print("After append:", stack)

popped = stack.pop()
print("Popped element:", popped)
print("After pop:", stack)

stack.insert(2, 99)   # Insert 99 at index 2
print("After insert:", stack)

del stack[1]   # Deletes element at index 1
print("After delete:", stack)

stack.remove(99)   # Removes first occurrence of 99
print("After remove:", stack)

stack.extend([70, 80, 90])
print("After extend:", stack)

stack.clear()
print("After clear:", stack)

stack = [10, 40, 20, 10, 50]
print("New Stack:", stack)

stack.sort()
print("After sort:", stack)

stack.reverse()
print("After reverse:", stack)

print("Index of 20:", stack.index(20))

print("Count of 10:", stack.count(10))

import numpy as np

print("Index of max element:", np.argmax(stack))
'''

'''t = (10, 20, 30, 20, 40, 20)

print(t.count(20))

print(t.index(30))
'''
'''f = lambda x : x * 4
print(f(5))
'''

'''values = [1,2,3,4,5,6,7,8]
result = list(map(lambda x:x+2,values))
print(result)
'''

'''values = [1, 2, 3, 4, 5, 6, 7, 8]

result = list(filter(lambda x: x % 2 == 0, values))

print(result)
'''


from functools import reduce

values = [1, 2, 3, 4, 5, 6, 7, 8]

result = reduce(lambda x, y: x + y, values)
print(result)

