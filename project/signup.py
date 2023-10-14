from tkinter import*

from tkinter import messagebox

win2=Tk()

def Submit():
	

	import pymysql
	conobj=pymysql.connect(host='localhost',user ='root',password='',port=3306)


	curobj=conobj.cursor()

	
	a=RFname.get()
	b=RLname.get()
	c=Ruid.get()
	d=Gvar.get()
	e=AcYear.get()
	f=Bvar.get()
	g=Rpwd.get()
	#print(a,b,c,d,e,f,g)
	

	#import database
	#r='insert into DEMO(Fname="{RFname}")'
	#cuobj.execute('use JulyBatch')

	

	#curobj.execute('create database julybatch1;')


	curobj.execute('use julybatch1;')
	#curobj.execute('create table DEMO(Fname varchar(20), Lname varchar(20),UID varchar(30),Gender varchar(6), AccYear varchar(10), Branch varchar(10),Password varchar(20)); ')
	

	r='insert into Demo value("{Fname}","{Lname}","{UID}","{Gender}","{AccYear}","{Branch}","{Password}");'
	
	r1=r.format(Fname= a,Lname=b, UID=c , Gender= d , AccYear=e, Branch=f, Password=g)	
	#print(r1)

	curobj.execute(r1)
	conobj.commit()


	curobj.close()
	conobj.close()
	messagebox.showinfo('showinfo',"Registration Successful")
	
	win2.destroy()




def Reset():
	RFname . delete(0,END)
	RLname.delete(0,END)
	Ruid .delete(0,END)
	Gvar . set(None)
	AcYear.set(None)
	Bvar.set(None)
	Rpwd.delete(0,END)


def Exit():
	win2.destroy()




win2.title("signup")
win2.maxsize(550,500)
win2.minsize(550,500)

Label(win2,text='Please signup here !',font=('Felix Titling',20),bg='brown',fg='white',width=17,relief=GROOVE).place(x=100,y=50)


Label(win2,text='ENTER FIRST NAME',font=('Felix Titling',15),bg='Silver',fg='Green',width=17,relief=GROOVE).place(x=20,y=100)

RFname=Entry(win2,font=('Flex Texting',15),bg='yellow',fg='Black',width=17,relief=GROOVE)
RFname.place(x=280,y=100)


Label(win2,text='ENTER LAST NAME',font=('Felix Titling',15),bg='Silver',fg='Green',width=17,relief=GROOVE).place(x=20,y=150)


RLname=Entry(win2,font=('Flex Texting',15),bg='yellow',fg='Black',width=17,relief=GROOVE)
RLname.place(x=280,y=150)



Label(win2,text='ENTER USER NAME',font=('Felix Titling',15),bg='Silver',fg='Green',width=17,relief=GROOVE).place(x=20,y=200)



Ruid=Entry(win2,font=('Flex Texting',15),bg='yellow',fg='Black',width=17,relief=GROOVE)
Ruid.place(x=280,y=200)


Label(win2,text='SELECT GENDER',font=('Felix Titling',15),bg='Silver',fg='Blue',width=17,relief=GROOVE).place(x=20,y=250)




Gvar = StringVar()
#R1 =Radiobutton(win2,text="Male",font=('felix Titling',15),variable=Gvar,value ='m').place(x=330),=250)
#R2=Radiobutton(win2,text='Female',font=('Flex Texting',15),variable=Gvar,value='0').place(x=380,y=250)

Gvar.set('Select gender')
G = OptionMenu(win2,Gvar,"Male","Female")
G.place(x=330)
G.place(y=250)



Label(win2,text='ACCADEMIC YEAR',font=('Felix Titling',15),bg='Silver',fg='Blue',width=17,relief=GROOVE).place(x=20,y=300)


AcYear=StringVar()
AcYear.set('Select any Acc Year')
A=OptionMenu(win2,AcYear,'18-22','19-23','20-24','21-25')
A.place(x=330,y=300)



Label(win2,text='SELECT BRANCH',font=('Felix Titling',15),bg='Silver',fg='Blue',width=17,relief=GROOVE).place(x=20,y=350)



Bvar=StringVar()
Bvar.set('Select Any Branch')
B=OptionMenu(win2,Bvar,'CSE','Mech','Civil','EEE','EE','ECE')
B.place(x=330,y=350)


Label(win2,text='ENTER PASSWORD',font=('Felix Titling',15),bg='Silver',fg='Green',width=17,relief=GROOVE).place(x=20,y=400)



Rpwd=Entry(win2,font=('Flex Texting',15),bg='yellow',fg='Black',width=17,relief=GROOVE,show='*')
Rpwd.place(x=280,y=400)







Button (win2,text='Signup',font = ('connsolas',15),bg='pink',fg='gray',width=6,command=Submit).place(x=100,y=450)


Button (win2,text='Reset',font = ('connsolas',15),bg='pink',fg='gray',width=6,command=Reset).place(x=200,y=450)



Button (win2,text='Exit',font = ('connsolas',15),bg='pink',fg='gray',width=20,command=Exit).place(x=300,y=450)




win2.mainloop()