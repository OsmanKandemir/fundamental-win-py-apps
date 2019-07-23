#usr/bin/env python
#-*- coding:utf-8 -*-

import os
import pymysql
from tkinter import ttk
from tkinter import *
from tkinter import messagebox


class App:
	"""docstring for ClassName"""
	def __init__(self, top,host,user,passwd,db):
		super(App, self).__init__()
		try:
			self.host = host
			self.user = user
			self.passwd = passwd
			self.db = db
			self.l2 = Label(top,text="Adi Soyadi").place(x=10,y=0)
			self.E2=Entry(top,bd=1,width=20)
			self.E2.place(x=100,y=0)

			self.l3 = Label(top,text="E-mail").place(x=10,y=30)
			self.E3=Entry(top,bd=1,width=20)
			self.E3.place(x=100,y=30)

			self.l4 = Label(top,text="Password").place(x=10,y=60)
			self.E4=Entry(top,bd=1,width=20)
			self.E4.place(x=100,y=60)

			self.l5 = Label(top,text="Status").place(x=10,y=90)
			self.E5=ttk.Combobox(top,values=['Online','Offline'],width=20)
			self.E5.place(x=100,y=90)

			self.kaydet=Button(top,text='KAYDET',command= lambda : self.ekle(self.E2.get(),self.E3.get(),self.E4.get(),self.E5.get()))
			self.kaydet.place(x=50,y=120)
			self.guncelle=Button(top,text='GÜNCELLE',command= self.guncelle)
			self.guncelle.place(x=150,y=120)
			self.sil=Button(top,text='SİL',command= self.sil)
			self.sil.place(x=270,y=120)


			self.conn = pymysql.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
			self.cur = self.conn.cursor()
			self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)




			self.liste = ttk.Treeview(top)
			self.liste["columns"] = ("s1","s2","s3","s4")
			self.liste.place(x=0,y=150,)
			self.liste.heading("#0",text="Id")
			self.liste.column('#0', anchor='center', width=100)
			self.liste.heading("s1",text="Adi Soyadi")
			self.liste.column('s1', anchor='center', width=100)
			self.liste.heading("s2",text="Email")
			self.liste.column('s2', anchor='center', width=100)
			self.liste.heading("s3",text="Passwords")
			self.liste.column('s3', anchor='center', width=100)
			self.liste.heading("s4",text="Status")
			self.liste.column('s4', anchor='center', width=100)
			self.listele()
			self.liste.bind("<ButtonRelease-1>",self.pulldata,self.guncelle)

	
		
		except:
			messagebox.showinfo("Connection", "Connection Failed")
			top.destroy()

	def pulldata(self,event):
		self.idno=self.liste.item(self.liste.selection()[0])['text']
		self.sql = "SELECT * FROM users WHERE id='%s'" %self.idno
		self.cur.execute(self.sql)
		self.results =self.cur.fetchone()

		self.E2.delete(0,END)
		self.E2.insert(0, self.results[1])
		self.E3.delete(0,END)
		self.E3.insert(0, self.results[2])
		self.E4.delete(0,END)
		self.E4.insert(0, self.results[3])
		self.E5.delete(0,END)
		self.E5.insert(0, self.results[4])

	def mesaj(self):
		self.msg = messagebox.showinfo("Basarili","İslem Tamamlandi.")
	def ekle(self,isimsoyisim,email,status,password):
		if isimsoyisim == "" or password == "" or email == "":
			messagebox.showinfo("", "Bos Birakilamaz")
		elif "@" and ".com" not in email:
			messagebox.showinfo("", "Yanlis Email")
		else:
			sql = "INSERT INTO users (isimsoyisim,email,status,types,password,roles) VALUES ('%s','%s','%s','','%s','')" %(isimsoyisim,email,password,status)
			self.cursor.execute(sql)
			self.conn.commit()
			messagebox.showinfo("Basarili", "Eklendi.")
			self.listele()

	def listele(self):
		self.liste.delete(*self.liste.get_children())
		self.sql = "SELECT * FROM users"
		self.res = self.cursor.execute(self.sql)
		self.r = self.cursor.fetchall()
		for i in self.r:
			self.liste.insert("", 0,text=i['id'],values=(i['isimsoyisim'],i['email'],i['password'],i['status']))	

	def guncelle(self):
		self.idno=self.liste.item(self.liste.selection()[0])['text']
		self.sql = "UPDATE users SET isimsoyisim = '%s',email = '%s',status = '%s',password = '%s',roles = '',types = '' WHERE id='%s'" %(self.E2.get(),self.E3.get(),self.E5.get(),self.E4.get(),self.idno)
		self.cursor.execute(self.sql)
		self.conn.commit()
		self.listele()

	def sil(self):
		self.idno=self.liste.item(self.liste.selection()[0])['text']
		print(self.idno)
		self.sql = "DELETE FROM users WHERE id='%s'" %(self.idno)
		self.cursor.execute(self.sql)
		self.conn.commit()
		self.listele()



class App2:
	"""docstring for App2"""
	def __init__(self,top):
		super(App2, self).__init__()
		self.l2 = Label(top,text="Host").place(x=10,y=0)
		v = StringVar(top, value='localhost')
		self.E2=Entry(top,bd=1,width=20,textvariable=v)
		self.E2.place(x=100,y=0)

		self.l3 = Label(top,text="User").place(x=10,y=30)
		v1 = StringVar(top, value='root')
		self.E3=Entry(top,bd=1,width=20,textvariable=v1)
		self.E3.place(x=100,y=30)

		self.l4 = Label(top,text="Password").place(x=10,y=60)
		self.E4=Entry(top,bd=1,width=20)
		self.E4.place(x=100,y=60)

		self.l5 = Label(top,text="Database").place(x=10,y=90)
		self.E5=Entry(top,bd=1,width=20)
		self.E5.place(x=100,y=90)

		self.baglanti=Button(top,text='Connect',command= lambda : self.connect(self.E2.get(),self.E3.get(),self.E4.get(),self.E5.get()))
		self.baglanti.place(x=100,y=120)

	def connect(self,host,user,passwd,db):
		try:
			if db != "":
				self.conn = pymysql.connect(host=host,user=user,passwd=passwd,db=db)
				self.cur = self.conn.cursor()
				self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
				if self.cursor:
					messagebox.showinfo("Connection", "Connection Successful")
					root = Tk()
					root.geometry("800x600")
					application = App(root,host,user,passwd,db)
					root.mainloop()
			else:
				messagebox.showinfo("Connection", "Connection Failed")
		except:

			messagebox.showinfo("Connection", "Connection Failed")

if __name__ == '__main__':
	root1 = Tk()
	root1.geometry("300x150")
	application1 = App2(root1)
	root1.mainloop()
	#main()