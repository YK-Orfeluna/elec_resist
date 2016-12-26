# -*- coding: utf-8 -*-

import sys
import Tkinter

w = 10

x1 = 10
x2 = 100
x3 = 170
x4 = 200

y1 = 10
y2 = 30
y3 = 50
y4 = 70
y5 = (y1+y2+y3+y4)/4

def teikou(V1, V2, mA) :
	v = (V1 - V2) * 1.0
	a = 1.0 * mA / 1000
	r = v / a
	r = round(r, 2)
	return r

def run(event) :
	global EditBox1, EditBox2, EditBox3, EditBox4
	v1 = EditBox1.get()
	v2 = EditBox2.get()
	ma = EditBox3.get()
	resist = EditBox4.get()

	if resist == "" :
		if not v1 == v2 == ma == "" :
			resist = teikou(float(v1), float(v2), float(ma))
			EditBox4.insert(Tkinter.END,resist)

def finish(event) :
	sys.exit("System exit")

root = Tkinter.Tk()

root.title("Software Title")
root.geometry("400x150")

Static1_1 = Tkinter.Label(text="電源電圧")
Static1_1.place(x=x1, y=y1)

EditBox1 = Tkinter.Entry(width=w)
EditBox1.place(x=x2, y=y1)


Static1_2 = Tkinter.Label(text="V")
Static1_2.place(x=x3, y=y1)


Static2_1 = Tkinter.Label(text="センサ電圧")
Static2_1.place(x=x1, y=y2)

EditBox2 = Tkinter.Entry(width=w)
EditBox2.place(x=x2, y=y2)
value2 = EditBox2.get()

Static2_2 = Tkinter.Label(text="V")
Static2_2.place(x=x3, y=y2)



Static3_1 = Tkinter.Label(text="電流")
Static3_1.place(x=x1, y=y3)

EditBox3 = Tkinter.Entry(width=w)
EditBox3.place(x=x2, y=y3)
value3 = EditBox3.get()

Static3_2 = Tkinter.Label(text="mA")
Static3_2.place(x=x3, y=y3)



Static4_1 = Tkinter.Label(text="抵抗値")
Static4_1.place(x=x1, y=y4)

EditBox4 = Tkinter.Entry(width=w)
EditBox4.place(x=x2, y=y4)
value4 = EditBox4.get()

Static4_2 = Tkinter.Label(text=u"\u03a9")
Static4_2.place(x=x3, y=y4)

Button1 = Tkinter.Button(text="Calculation")
Button1.bind("<Button-1>",run) 
# <Button-1>: click
# <Button-2>: wheel-click
# <Button-3>: right-click
Button1.place(x=x4, y=y5)

Button2 = Tkinter.Button(text="Exit")
Button2.bind("<Button-1>",finish) 
Button2.place(x=x4, y=y5+30)

root.mainloop()

def heiretsu(r_list) :
	s = 0.0
	for i in r_list :
		r = 1.0 / i
		s += r
	R = 1.0 / s
	return R

def chokuretsu(r_list) :
	s = sum(r_list)
	return s