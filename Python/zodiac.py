#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "anandadwipra"


import tkinter as tk
from tkinter import messagebox
import re,time,webbrowser

class master(tk.Tk):

	def __init__(self):
		tk.Tk.__init__(self)
		self.geometry("520x400")
		self.frame0()
		self.menu()
		self.title("Tugas")
		self.entry=[]
		self.v=[]
		self.validation = self.register(lambda a,b,c:self.only_numbers(a,b,c))
	
	def frame0(self):
		self.window0=tk.Frame(self,bg="grey")
		self.window0.pack(fill="both",expand=True)
		tk.Label(self.window0,text='Daftar Program',bg="grey",font=("BatangChe",20)).place(x=160,y=30)
		tk.Button(self.window0,text="Hitung Luas Persegi",font=("BatangChe",10),bg="grey",command=self.frame2).place(x=80,y=80)
		tk.Button(self.window0,text="Cari Tahu zodiakmu",font=("BatangChe",10),bg='grey',command=self.frame1).place(x=280,y=80)
		tk.Button(self.window0,text="Tes Ujian Kelulusan Sim",font=("BatangChe",10),bg="grey",command=self.frame3).place(x=170,y=140)

	def frame3(self):
		self.window=tk.Frame(self,bg="grey",width=520,height=400);self.window.pack(fill="both",expand=True)
		tk.Label(self.window,text="Hasil Tes Ujian Sim",bg="grey",font=("BatangChe",20)).place(x=120,y=10)
		tk.Label(self.window,text="Nilai Anda :",bg="grey",font=("BatangChe",15)).place(x=50,y=90)
		tk.Label(self.window,text="Tanggal Ujian  :",bg="grey",font=("BatangChe",15)).place(x=50,y=130)
		self.v.append(tk.StringVar());self.v.append(tk.StringVar())
		self.entry.append(tk.Entry(self.window,textvariable=self.v[0],font=("BatangChe",15),validate='key',validatecommand=(self.validation,"%S",0,2)))
		self.entry[0].place(x=160,y=90)
		self.entry.append(tk.Entry(self.window,textvariable=self.v[1],font=("BatangChe",15)));self.entry[1].place(x=160,y=130)
		tk.Button(self.window,text="Cek Hasil",command=self.cek,font=("BatangChe",10),bg="grey").place(x=220,y=200)
		tk.Button(self.window,text="Menu",command=self.destroythis,font=('BatangChe',10),bg="grey").place(x=170,y=200)
	def cek(self):
		if int(self.v[0].get())>=75:
			messagebox.showinfo("Selamat","Selamat Anda Lulus")
		else:
			t = (int(self.v[1].get()[6:]), int(self.v[1].get()[3:5]), int(self.v[1].get()[:2]), 8, 44, 4, 4, 362, 0)
			local_time = time.mktime(t)
			messagebox.showinfo("Jangan Menyerah ",f"Remidi Pada { time.ctime(local_time+(86400*10))}")
	def menu(self):
		self.menubar=tk.Menu(self)
		self.config(menu=self.menubar)
		# help
		helpmenu=tk.Menu(self.menubar,tearoff=0)
		helpmenu.add_command(label="About",command=lambda :webbrowser.open("https://github.com/anandadwipra/All_Python"))
		helpmenu.add_command(label="Help",command=lambda :webbrowser.open("https://www.instagram.com/ananda.dwi.p/"))
		self.menubar.add_cascade(label="help",menu=helpmenu)
	def frame2(self):
		self.window=(tk.Frame(self,bg='grey',width=520,height=400))
		self.window.pack(fill="both",expand=True)
		tk.Label(self.window,text="Hitung Luas Persegi",bg="grey",font=("BatangChe",20)).place(x=120,y=10)
		self.v.append(tk.StringVar());self.v.append(tk.StringVar())
		tk.Label(self.window,text="Panjang : ",bg="grey",font=("BatangChe",15)).place(x=50,y=80)
		tk.Label(self.window,text="Lebar    : ",bg="grey",font=("BatangChe",15)).place(x=50,y=120)
		self.entry.append( tk.Entry(self.window,textvariable=self.v[0],validate="key",font=("BatangChe",15), validatecommand=(self.validation,'%S',0,8)));self.entry[0].place(x=150,y=80)
		self.entry.append(tk.Entry(self.window,textvariable=self.v[1],validate="key",font=("BatangChe",15),validatecommand=(self.validation,'%S',1,8)));self.entry[1].place(x=150,y=120)
		tk.Button(self.window,text="Hitung Luas !!!",font=("BatangChe",10),command=self.luas,bg="grey").place(x=220,y=180)
		tk.Button(self.window,text="Menu",command=self.destroythis,font=('BatangChe',10),bg="grey").place(x=170,y=180)

	def destroythis(self):
		self.window.destroy()
		self.entry=[];self.v=[]
	def only_numbers(self,char,v1,v2):
		if len(self.entry[int(v1)].get())>=int(v2):
			return False
		return char.isdigit()
	def luas(self):
		messagebox.showinfo("Hasil Luas ",f"Luas Dari Pesegi Panjang Dengan Panjang {self.v[0].get()}, dan Lebar {self.v[1].get()}.\n\t\t adalah {int(self.v[0].get())*int(self.v[1].get())}")

	def frame1(self):
		self.window=tk.Frame(self,bg="grey",width=520,height=400)
		self.window.pack(fill="both", expand=True)
		tk.Label(self.window,text="Cari Tahu Zodiakmu...!!!",bg="grey",font=("BatangChe",20)).place(x=120,y=10)
		self.v.append(tk.StringVar())
		self.entry.append(tk.Entry(self.window,bg="white",font=("BatangChe",18),width=34,textvariable=self.v[0]))
		self.entry[0].place(x=35,y=90)
		self.entry[0].insert(0,"Masukan Tanggal dan Bulanmu")
		self.entry[0].bind("<Return>",self.cari)
		self.entry[0].bind("<Button-1>", lambda event: self.clear_entry(event))
		tk.Button(self.window,text="cari",command=self.cari,font=("BatangChe",15),bg='grey').place(x=260,y=200)
		tk.Button(self.window,text="Menu",command=self.destroythis,font=('BatangChe',15),bg='grey').place(x=180,y=200)
	
	def cari(self,event=None):
		self.nul()
		self.destroythis()
		self.frame1()
	
	def clear_entry(self,event):
		self.entry[0].delete(0,tk.END)
	
	def nul(self):
		zodiak={"Capicorn":"21 desember 19 januari","Aquarius":"20 Januari – 18 Februari","Pisces":"19 Februari – 20 Maret","Aries":"21 Maret – 20 April","Taurus":"21 April – 20 Mei","Gemini":"21 Mei – 20 Juni","Cancer":"21 Juni – 20 Juli","Leo":"21 Juli – 21 Agustus","Virgo":"22 Agustus – 22 September","Libra":"23 September – 22 Oktober","Scorpio":"23 Oktober – 22 November","Sagitarius":"23 November – 20 Desember",}
		bulvalid=["april,juni,september,november","januari,maret,mei,juli,agustus,oktober,desember"]
		while True:
			soal=self.v[0].get().lower()
			try:
				tanggal = int(re.findall(r"\d+",soal)[0])
				bulan = re.findall(r"\w+",soal)[1].lower()
				if ((bulan not in bulvalid[0])^ (bulan not in bulvalid[1])) ^ (bulan != "februari"):
					messagebox.showinfo("Invalid Input","Masukan Input dengan benar contoh:6 agustus")
			except:
				messagebox.showinfo("Invalid Input","Masukan Input dengan benar contoh:12 mei")
				return
			if tanggal <= 0 or tanggal >= 32:
				messagebox.showinfo("Zodiak ",f"Zodiak anda adalah {key}")
			elif tanggal >= 28:
				if (tanggal < 29 and bulan == "februari") or tanggal < 31 and (bulan in bulvalid[0]) or tanggal < 32 and (bulan in bulvalid[1]):
					break
				else:
					messagebox.showinfo("Zodiak ",f"Zodiak anda adalah {key}")
			else:
				break
		for key, value in zodiak.items():
			if bulan in value.lower():
				tanggale=re.findall(r"\d+ \w+",value)
				if bulan in tanggale[0].lower() :
					tanggalbro=int(tanggale[0][0:2])
					if int(tanggal) >= tanggalbro :
						messagebox.showinfo("Zodiak ",f"Zodiak anda adalah {key}")
						return
				elif bulan in tanggale[1].lower():
					tanggalbro=int(tanggale[1][0:2])
					if int(tanggal) <= tanggalbro :
						messagebox.showinfo("Zodiak ",f"Zodiak anda adalah {key}")
						return
zodiak= master()
zodiak.mainloop()
