from tkinter import *
from random import *
from tkinter.messagebox import *

root=Tk()
root.title("Guessing Game")
root.geometry("1000x600+50+50")
f=("Times New Roman",40,"bold")
lab1=Label(root,text="Name",font=f)
ent1=Entry(root,font=f)
lab1.place(x=50,y=50)
ent1.place(x=400,y=50)
lab2=Label(root,text="Enter a number",font=f)
ent2=Entry(root,font=f)
lab2.place(x=30,y=200)
ent2.place(x=400,y=200)

num=randint(1,10)

def guess():
	x=int(ent2.get())
	if num==x:
		ans.configure(text="You got it right...Wohooo!")
	elif num<x:
		ans.configure(text="UhOh!,you're close to the number,try a smaller number!")
	elif num>x:
		ans.configure(text="UhOh!,you're close to the number,try a bigger number!")
	
def color():
	c=["red","brown","green","blue","purple","gray","pink","black"]
	r=randint(0,len(c)-1)
	root.configure(bg=c[r])
	root.after(5000, color)

color()

btn=Button(root,text="Submit",font=f,command=guess)
btn.place(x=300,y=300)
ans=Label(root,font=f)
ans.place(x=50,y=450)




root.mainloop()
