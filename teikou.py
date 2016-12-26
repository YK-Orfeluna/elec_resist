# -*- coding: utf-8 -*-

import sys
import Tkinter

def teikou(V1, V2, mA) :
	v = (V1 - V2) * 1.0
	a = 1.0 * mA / 1000
	r = v / a
	r = round(r, 2)
	return r

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

