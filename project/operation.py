from tkinter import*
import pymysql
from tkinter import messagebox

win3 =Tk()

def New ():
	import signup
	win3.destroy()

def Del():
	import delete
	win3.destroy()
def Update():
	import update
	win3.destroy()
def Search():
	import search
	win3.destroy()
def Show ():
	win6=Tk()
	win6.title('show record')
	win6.maxsize(500,500)
	win6.minsize(500,500)
	conobj= pymysql.connect(host='localhost',user = 'root',password='',port=3306)
	curobj=conobj.cursor()
	curobj.execute('use julybatch1;')
	curobj.execute('select * from demo;')
	data = curobj.fetchall()
	showData=''
	for i in data :
		showData += str(i)+"\n"
		l1= Label (win6,text =showData,font=('arial',10) )
		l1.grid(row=0,column=0)		
	win6.mainloop()
			

	curobj.close()
	conobj.close()
	win3.destroy()
	
win3.title('Operation Page!')
#win3.geometry('600x300')
win3.maxsize(500,500)
win3.minsize(500,500)

Button(win3,text="Add student",font=("Ebrima",15),bg='orange',fg='blue',relief=GROOVE,command = New).place(x=100,y=100)

Button(win3,text="Delete Student",font=("Ebrima",15),bg='orange',fg='blue',relief=GROOVE, command=Del).place(x=300,y=100)

Button(win3,text="Update Details",font=("Ebrima",15),bg='orange',fg='blue',relief=GROOVE,command= Update).place(x=100,y=200)

Button(win3,text="Search Student",font=("Ebrima",15),bg='orange',fg='blue',relief=GROOVE,command= Search).place(x=300,y=200)

Button(win3,text="Show All Record",font=("Ebrima",15),bg='orange',fg='blue',relief=GROOVE,command=Show ).place(x=200,y=300)


win3.mainloop()