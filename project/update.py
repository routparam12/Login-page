from tkinter import*
import pymysql

from tkinter import messagebox

win7=Tk ()
def Update ():
	DUID=DUid.get()
	conobj= pymysql.connect(host='localhost',user = 'root',password='',port=3306)
	curobj=conobj.cursor()
	curobj.execute('use julybatch1;')

	test1 =f'select * from demo where UID="{DUID}";'
	curobj.execute(test1)

	record=curobj.fetchall()
	#print(record)
	if len (record):
		win8=Tk ()
		def Save():
			a = UFName.get()
			b = ULName.get()
			c = Uvar.get()
			d = UAcYear.get()
			e = UBvar.get()
			U = f'update demo set FName ="{a}",LName = "{b}",Gender="{c}",AccYear="{d}",Branch= "{e}" where UID = "{DUID}";'		
			#print(U)									
			curobj.execute(U)
			conobj.commit()
			win8.destroy ()
				
			#print(a,b,c,d,e)

		win8.title('Update Info !')
		
		win8.maxsize(700,700)
		win8.minsize(700,700)
		#print('valid user')

		Label(win8,text='ENTER FIRST NAME',font=('Felix Titling',15),bg='Silver',fg='Green',width=17,relief=GROOVE).place(x=20,y=100)

		UFName=Entry(win8,font=('Flex Texting',15),bg='yellow',fg='Black',width=17,relief=GROOVE)
		UFName.place(x=280,y=100)


		Label(win8,text='ENTER LAST NAME',font=('Felix Titling',15),bg='Silver',fg='Green',width=17,relief=GROOVE).place(x=20,y=150)


		ULName=Entry(win8,font=('Flex Texting',15),bg='yellow',fg='Black',width=17,relief=GROOVE)
		ULName.place(x=280,y=150)
		
		
		Label(win8,text='SELECT GENDER',font=('Felix Titling',15),bg='Silver',fg='Blue',width=17,relief=GROOVE).place(x=20,y=250)
		



		Uvar = StringVar()
		#R1=Radiobutton(win8,text='Male',font=('Flex Texting',15),variable=Uvar,value='M').place(x=280,y=250)
		#R2=Radiobutton(win8,text='Female',font=('Flex Texting',15),variable=Uvar,value='F').place(x=380,y=250)
		Uvar.set('Select gender')
		U = OptionMenu(win8,Uvar,"Male","Female")
		U.place(x=330)
		U.place(y=250)



		Label(win8,text='ACCADEMIC YEAR',font=('Felix Titling',15),bg='Silver',fg='Blue',width=17,relief=GROOVE).place(x=20,y=300)


		UAcYear=StringVar()
		UAcYear.set('Select any Acc Year')
		A=OptionMenu(win8,UAcYear,'18-22','19-23','20-24','21-25')
		A.place(x=330,y=300)



		Label(win8,text='SELECT BRANCH',font=('Felix Titling',15),bg='Silver',fg='Blue',width=17,relief=GROOVE).place(x=20,y=350)



		UBvar=StringVar()
		UBvar.set('Select Any Branch')
		B=OptionMenu(win8,UBvar,'CSE','Mech','Civil','EEE','EE','ECE')
		B.place(x=330,y=350)
		
		Button(win8,text='update',font=('Consolas',15),bg='gray',width=6,command=Save).place(x=80,y=400)

	
		win8.mainloop()
		'''
		d=f'delete from demo where  UID ="{DUID}";'
		#print(d)
		curobj.execute(d)
		conobj.commit()
		messagebox.showinfo('showinfo','one record is deleted')
		win7.destroy()
		'''
	else:
		messagebox.showerror('showerror',"invalid userid")
		win7.destroy()


	curobj.close()
	conobj.close()
	
	
win7.title('Update Student ! ')

win7.maxsize (500,500)
win7.minsize(500,500)

Label(win7,text='Enter Uid ', font= ('Elephant',15),bg='olive',fg='maroon',width =10,relief= GROOVE).place(x=30,y=100)

DUid = Entry(win7,width =42,font=('Consolas',15),bg='pink',fg='black')
DUid.place(x=190,y=100)

Button(win7 , text = "Update",font = ("Ebrima",15),bg ='orange',fg = "blue",relief = GROOVE , command= Update ).place(x=150,y=250)

win7.mainloop()