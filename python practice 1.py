#list functions
a=(2,2,4,6,34)
print(a.count(2))
print(a.index(6))

#set functions
a={1,2,3,4,5,2,4,6,7}
b={4,6,7,8,4,2}
print(a.difference(b))
print(a.intersection(b))
print(a.isdisjoint(b))
print(a.issubset(b))
print(a.issuperset(b))
print(a.pop())
a.remove(7)
print(a.symmetric_difference(b))
print(a.union(b))
a.update(b)

#dictionary functions
dict={1:"chocolate",2:"butterscotch",3:"strawberry"}
'''dict.clear()'''
print(dict.get(2))
print(dict.items())
print(dict.keys())
print(dict.pop(2))
print(dict.popitem())
dict.update({3:"vanilla"})


a={"apple","banana","pineapple"}
b="fruits"
n=dict.fromkeys(a,b)
print(n)
