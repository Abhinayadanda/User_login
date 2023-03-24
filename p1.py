#wapp using gui(tkinter)to calc age

from tkinter import *
from tkinter.messagebox import *
from datetime import *

root=Tk()
root.title("Age Calculator App")
root.geometry("1000x600+50+50")
f=("Arial",40,"bold")

lab_1=Label(root,text="Age Calculator",font=f)
lab_1.pack()
lab_name=Label(root,text="Name",font=f)
ent_name=Entry(root,font=f)
lab_name.place(x=50,y=100)
ent_name.place(x=300,y=100)
lab_gen=Label(root,text="Gender",font=f)
lab_gen.place(x=50,y=200)

rad1=Radiobutton(root,font=f,text="M",value=1)
rad2=Radiobutton(root,font=f,text="F",value=2)
rad1.place(x=300,y=200)
rad2.place(x=500,y=200)

lab_dob=Label(root,text="D.O.B(Yr)",font=f)
ent_dob=Entry(root,font=f)
lab_dob.place(x=50,y=300)
ent_dob.place(x=300,y=300)

def age():
	x=ent_dob.get()
	a=int(x)
	sol=2023-a
	msg="You're "+str(sol)+" yrs old!"
	ans.configure(text=msg)

btn=Button(root,font=f,text="Submit",command=age)
btn.place(x=400,y=400)
ans=Label(root,font=f)
ans.place(x=200,y=500)


		


root.mainloop()