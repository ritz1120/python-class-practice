try:
    a=int(input("enter a number"))
    b=int(input("enter a number"))
    if b==0:
        raise Exception ("no zeros allowed in b")
    c=a+b
    d=a/b
    print(c,d)
except Exception as e:
    print(e)

balance=int(input("enter your balance"))
assert balance>0,"balance should be not nil"
print("transaction")
          
