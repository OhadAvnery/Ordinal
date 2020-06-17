def main():
	from ordinal import Ordinal
	from fast_growing import *
	w = Ordinal.OMEGA
	1+w
	w+1
	print(1+w == w+1)
	a,b,c = 1, w**w, w
	(a+b)+c == a+(b+c)
	a = (w+1)*(w+2)
	a
	b = Ordinal.omega_tower(5)
	b
	b > a
	c = w**w**(w+5)
	c[10]
	ordinal_stack(w**w**w, 2)
	ordinal_stack(w**w**w, 3)  # oh my! need to ctrl+c this
	f2 = fast_growing(2)
	f2(5)
	f_omega = fast_growing(w)
	f_omega(2)
	f_omega(3) #ctrl+c


if __name__ == '__main__':
	main()