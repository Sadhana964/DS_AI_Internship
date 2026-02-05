'''a={1,2,3,4}
b={3,4,5,6}
a.remove(3)
print(a)
a.discard(5)
print(a)
a.add(5)
print(a)
b.pop()
print(b)
a.clear()
b.clear()
print(a,b)
print(a|b)
print(a.intersection(b))
print(a.difference(b))
'''

fruits = {"apple", "banana", "mango"}
print("Original Set:", fruits)

fruits.add("orange")
print("\nAfter add('orange'):", fruits)

fruits.remove("banana")
print("\nAfter remove('banana'):", fruits)

fruits.discard("grapes")  
print("\nAfter discard('grapes'):", fruits)

removed_item = fruits.pop()
print("\nAfter pop():", fruits)
print("Removed item:", removed_item)