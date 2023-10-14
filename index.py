from tkinter import * # import module
from tkinter import messagebox
import pymysql
win = Tk() # Tk() is a predefined class,win is the obj of Tk()

def Login():
	Lusername=uid.get()
	Lpassword=pwd.get()
	#print(Lusername,Lpassword)
	conobj=pymysql.connect(host='localhost',user='root',password='',port=3306)
	curobj=conobj.cursor()
	curobj.execute('use julybatch1;')
	test = f'select* from demo where UID ="{Lusername}" and password="{Lpassword}";'
	curobj.execute(test)
	record=curobj.fetchall()
	if len(record):
		messagebox.showinfo('showinfo',"login Successful")
		import operation
	else:
		messagebox.showerror('showerror','invalid username & password')
		win.destroy()
	

	curobj.close()
	conobj.close()

def Reset():
	uid.delete(0,END)
	pwd.delete(0,END)

def Exit():

	win.destroy()
def NewUser():
	import signup






win .title('login page!')
#win.geometry('600X300')
win.maxsize(600,500)
win.minsize(500,550)


Label(win,text='Please Login Here!',font=('Elephant',15),bg='orange',fg='green',width=30,height=2,relief=GROOVE).place(x=50,y=50)


Label(win,text='ENTER USER ID : ',font=('Consolas',12),bg='red',fg='blue',width=20,height=2,relief=GROOVE).place(x=80,y=150)



uid=Entry(win,width=25,font=('consolas',27),bg = 'silver',fg='black')
uid.place(x=270,y=150)


Label(win,text='ENTER PASSWORD : ',font=('Consolas',12),bg='red',fg='blue',width=20,height=2,relief=GROOVE).place(x=80,y=200)



pwd=Entry(win,width=25,font=('consolas',27),bg = 'silver',fg='black',show='*')
pwd.place(x=270,y=200)



Button (win,text='login',font = ('connsolas',15),bg='green',fg='white',width=6,command=Login).place(x=100,y=300)


Button (win,text='Reset',font = ('connsolas',15),bg='pink',fg='gray',width=6,command=Reset).place(x=200,y=300)

Button (win,text='Exit',font = ('connsolas',15),bg='pink',fg='gray',width=6,command =Exit).place(x=300,y=300)


Button (win,text='New Registration',font = ('connsolas',15),bg='orange',fg='gray',width=20,command=NewUser).place(x=120,y=350)



win . mainloop()