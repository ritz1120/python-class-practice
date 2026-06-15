'''def countevenandodd(a):
    even=0
    odd=0

    for num in a:
        if num%2==0:
            even+=1
        else:
            odd+=1

    print(even,odd)

countevenandodd([1,6,7,5,9])

def remove_duplicates(a):
    b=[]

    for i in a:
        if i not in b:
            b.append(i)
    print(b)
remove_duplicates([1,2,3,2,1,5])'''

def movezerotoend(a):
    result=[]
    zeros=0

    for x in a:
        if x==0:
            zeros+=1
        else:
            result.append(x)
    for i in range (zeros):
        result.append(0)
    print(result)

movezerotoend([1,3,0,5,6,0,9])
    


    


            

