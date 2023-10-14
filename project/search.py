from tkinter import*
import pymysql

from tkinter import messagebox

win5=Tk ()
def Search ():
	DUID=DUid.get()
	conobj= pymysql.connect(host='localhost',user = 'root',password='',port=3306)
	curobj=conobj.cursor()
	curobj.execute('use julybatch1;')

	test1 =f'select * from demo where UID="{DUID}";'
	curobj.execute(test1)

	record=curobj.fetchall()
	#print(record)
	if len (record):
		for a,b,c,d,e,f,g in record  :
			print(c,"details")
			print("Fname=",a)
			print("Lname=",b)
			print("Gender=",d)
			print("Acc Year=",e)
			print("Branch",f)
			
		win5.destroy()
	else:
		messagebox.showerror('showerror',"invalid userid")
		win5.destroy()


	curobj.close()
	conobj.close()
	
	
win5.title('Search Student ! ')

win5.maxsize (500,500)
win5.minsize(500,500)

Label(win5,text='Enter Uid ', font= ('Elephant',15),bg='olive',fg='maroon',width =10,relief= GROOVE).place(x=30,y=100)

DUid = Entry(win5,width =42,font=('Consolas',15),bg='pink',fg='black')
DUid.place(x=190,y=100)

Button(win5 , text = "Search",font = ("Ebrima",15),bg ='orange',fg = "blue",relief = GROOVE , command= Search ).place(x=150,y=250)

win5.mainloop()