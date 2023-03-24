#Login page

from tkinter import *
from tkinter.messagebox import *
from pymongo import *
from random import *
from getpass import *

root=Tk()
root.title("User Login ")
root.geometry("500x600+50+50")
f=("Arial",30,"bold")

lab1=Label(root,text="Enter Username",font=f)
ent1=Entry(root,font=f)
lab1.pack()
ent1.pack()

lab2=Label(root,text="Enter Password",font=f)
ent2=Entry(root,font=f,show="*")
lab2.pack()
ent2.pack()

lab4=Label(root,font=f)
lab4.pack()

x=randint(1000,9999)
lab4.configure(text=x)

	
def login():
	con=None
	try: 
		con=MongoClient("localhost",27017)
		db=con["logincreds"]
		coll=db["users"]
		y=int(ent3.get())
		if x==y:
			showinfo("Successfull login","Thankyou")
			username=ent1.get()
			password=ent2.get()
			info={"username":username,"password":password}
			coll.insert_one(info)
		else:
			showinfo("Unsuccessfull login","Retry!")
		
	except Exception as e:
		showerror("Issue ",e)
	finally:
		ent1.delete(0,END)
		ent2.delete(0,END)
		ent3.delete(0,END)
		ent1.focus()


lab3=Label(root,text="Enter Captcha",font=f)
ent3=Entry(root,font=f)
lab3.pack()
ent3.pack()

btn=Button(root,text="Login",font=f,command=login)
btn.pack()

root.mainloop()