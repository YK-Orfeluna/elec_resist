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
	value1 = EditBox1.get()
	value2 = EditBox2.get()
	value3 = EditBox3.get()
	value4 = EditBox4.get()

	if value4 == "" :
		if not value1 == value2 == value3 == "" :
			value4 = teikou(float(value1), float(value2), float(value3))
			EditBox4.insert(Tkinter.END,value4)

root = Tkinter.Tk()

root.title("Software Title")
root.geometry("400x300")

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

Button = Tkinter.Button(text="Button")
Button.bind("<Button-1>",run) 
# <Button-1>: click
# <Button-2>: wheel-click
# <Button-3>: right-click
Button.place(x=x4, y=y5)


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
"""
if __name__ == "__main__" :

	root = Tkinter.Tk()
	root.title("elect")
	root.geometry("400x300")

	Val1 = Tkinter.BooleanVar()
	Val2 = Tkinter.BooleanVar()
	Val3 = Tkinter.BooleanVar()

	Val1.set(False)
	Val2.set(False)
	Val3.set(False)

	CheckBox1 = Tkinter.Checkbutton(text=u"項目1", variable=Val1)
	CheckBox1.pack()

	CheckBox2 = Tkinter.Checkbutton(text=u"項目2", variable=Val2)
	CheckBox2.pack()

	CheckBox3 = Tkinter.Checkbutton(text=u"項目3", variable=Val3)
	CheckBox3.pack()


	root.mainloop()
	root2.mainloop()
	exit()

	flag = int(input("計算の種類を選んでください\n抵抗値の計算: 1，並列抵抗の計算: 2，直列抵抗の計算: 3\n>>>"))
	r_list = []

	if flag == 1 :
		v1 = input("電源電圧(V)を入力してください\n>>>")
		v2 = input("流したい電圧(V)を入力してください\n>>>")
		ma = input("流したい電流(mA)を入力してください\n>>>")
		r = teikou(float(v1), float(v2), float(ma))
		print("抵抗は%sです" %r)
		exit()

	elif flag == 2 :
		while True :
			r = input("抵抗値を入力してください\n終了する場合は'-1'を入力してください\n>>>")
			if int(r) == -1 :
				exit()
			else :
				r_list.append(float(r))
		r = heiretsu(r_list)
		print("並列抵抗の合計値は%sです" %r)

	elif flag == 3 :
		while True :
			r = input("抵抗値を入力してください\n終了する場合は'-1'を入力してください\n>>>")
			if int(r) == -1 :
				if len(r_list) != 0 :
					r = chokuretsu(r_list)
					print("直列抵抗の合計値は%sです" %r)
				exit()
			else :
				r_list.append(float(r))
"""