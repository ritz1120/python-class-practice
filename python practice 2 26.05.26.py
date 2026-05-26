#create a list
a=[1,2,34,76,90]
print(a)
print(type(a))
#adding elt using append()
a.append(15)
print(a)
#insert at index 2
a.insert(2,10)
print(a)
#remove elt using remove()
a.remove(10)
print(a)
#remove elt using pop()
a.pop()
print(a)
#length of a list
print(len(a))
#first and last elt
first=a[0]
last=a[-1]
print("first element:",first)
print("last element:",last)
#sum of all elements
print(sum(a))
#maximum and minimum
b=max(a)
print(b)
c=min(a)
print(c)
#count no of times a number appears
n=int(input("enter a number"))
b=a.count(n)
print(b)


