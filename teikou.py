# -*- coding: utf-8 -*-

import sys

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