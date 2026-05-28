#calculate the salary
def calculate(c,d,e):
    gross_salary=c+d
    final_salary=gross_salary-e
    print(final_salary)
c=int(input("enter the salary"))
d=int(input("enter the bonus"))
e=int(input("enter tax amt"))
calculate(c,d,e)        
          
#check wifi signal
def a():
    a=int(input("enter the signal percentage"))
    if 0<=a<=30:
        print("weak")
    elif 31<=a<=70:
        print("moderate")
    else:
        print("strong")
a()

#movie rating
def b():
    b=int(input("enter movie rating"))
    if b>8:
        print("excellent")
    elif 5<=b<=8:
        print("good")
    elif b<5:
        print("average")
b()
    
