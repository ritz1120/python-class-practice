from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
main=tk.Tk()
main.geometry('1000x1000')
main.title('tourism')
main.config(bg="light pink")
l=Label(main,font=('Arial',20),fg='black',bg='white',text="Create Account").place(x=400,y=100)
n=Label(main,font=16,fg='black',bg='white',text="Name").place(x=350,y=200)
p=Label(main,font=16,fg='black',bg='white',text="Password").place(x=350,y=270)
d=Label(main,font=16,fg='black',bg='white',text="Destination").place(x=350,y=340)
g=Label(main,font=16,fg='black',bg='white',text="Gender").place(x=350,y=410)
def show():
    name=ne.get()
    password=pe.get()
    place=places.get()
    gen=gender.get()
    print("Name:",name)
    print("Password:",password)
    print("destination of interest:",place)
    print("gender:",gen)
    
ne=Entry(main)
ne.place(x=500,y=210)
pe=Entry(main,show="*")
pe.place(x=500,y=280)
places=Combobox(main)
places["values"]=("select","paris","london","dubai","qatar","vietnam","singapore","malaysia","thailand")
places.current(0)
places.place(x=500,y=350)

Button(main,text='submit',command=show).place(x=450,y=500)

gender=StringVar(value="Female")
rb=Radiobutton(main,text="Female",variable=gender,value="Female")
rb.place(x=500,y=415)
rb1=Radiobutton(main,text="Male",variable=gender,value="Male")
rb1.place(x=600,y=415)


         
