from tkinter import*
import pymysql

from tkinter import messagebox

win4=Tk ()
def Delete ():
	DUID=DUid.get()
	conobj= pymysql.connect(host='localhost',user = 'root',password='',port=3306)
	curobj=conobj.cursor()
	curobj.execute('use julybatch1;')

	test1 =f'select * from demo where UID="{DUID}";'
	curobj.execute(test1)

	record=curobj.fetchall()
	#print(record)
	if len (record):
		d=f'delete from demo where  UID ="{DUID}";'
		#print(d)
		curobj.execute(d)
		conobj.commit()
		messagebox.showinfo('showinfo','one record is deleted')
		win4.destroy()
	else:
		messagebox.showerror('showerror',"invalid userid")
		win4.destroy()


	curobj.close()
	conobj.close()
	
	
win4.title('Delete Student ! ')

win4.maxsize (500,500)
win4.minsize(500,500)

Label(win4,text='Enter Uid ', font= ('Elephant',15),bg='olive',fg='maroon',width =10,relief= GROOVE).place(x=30,y=100)

DUid = Entry(win4,width =42,font=('Consolas',15),bg='pink',fg='black')
DUid.place(x=190,y=100)

Button(win4 , text = "Delete",font = ("Ebrima",15),bg ='orange',fg = "blue",relief = GROOVE , command= Delete ).place(x=150,y=250)

win4.mainloop()