#creating a file
r'''a = open(r"C:\Users\ritz1\OneDrive\Desktop\python.txt", "x")
print("done")'''
#inserting data
r'''a = open(r"C:\Users\ritz1\OneDrive\Desktop\python.txt",'w')
a.write("this is file handling")
a.close()
print("done")'''
#appending data
r'''a = open(r"C:\Users\ritz1\OneDrive\Desktop\python.txt",'a')
a.write(" hello")
a.close()
print("done")'''
#reading data
r'''a = open(r"C:\Users\ritz1\OneDrive\Desktop\python.txt",'r')
print(a.read())
print(a.read(2))'''
#deleting a file
import os
os.remove(r"C:\Users\ritz1\OneDrive\Desktop\python.txt")
print("deleted")


