from ordinal import Ordinal

def main():
	w = Ordinal.OMEGA
	a = w+1+1+1+1+1
	print(a)
	b = Ordinal.omega_tower(6)
	print(w**(b+1))
	print(b+1>b)


if __name__ == '__main__':
	main()