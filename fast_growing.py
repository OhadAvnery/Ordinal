from ordinal import Ordinal, OrdinalType

#returns a new function, x-->g^n(x)
def compose(g, n):
    if n == 0:
        return lambda x: x
    h = compose(g, n-1)
    return lambda x: g(h(x))


def fast_growing(a):
	'''
	given an ordinal a,
	return the function f_a : N --> N.
	'''
	if isinstance(a, int):
		a = Ordinal(a)

	if a.ord_type == OrdinalType.ZERO:
		return lambda n: n+1

	if a.ord_type == OrdinalType.SUCCESSOR:
		b = a.pred()
		f = fast_growing(b)
		return lambda n: compose(f,n)(n)

	else:  # a is a limit ordinal
		return lambda n: fast_growing(a[n])(n)

def ordinal_stack(a, n):
	d = {OrdinalType.ZERO: '', OrdinalType.SUCCESSOR: 'successor', 
		 OrdinalType.LIMIT: 'limit'}
	while True:
		a_type = a.ord_type
		print(a, d[a_type])
		if a_type == OrdinalType.ZERO:
			break
		elif a_type == OrdinalType.SUCCESSOR:
			a = a.pred()
		else:  # limit ordinal
			a = a[n]

def f_epsilon_0(n):
	# Ordinal.omega_tower: given n, returns the power tower w**(w**...**w) of length n
	return fast_growing(Ordinal.omega_tower(n))(n)	

def main():
	w = Ordinal.OMEGA
	print(fast_growing(w)(2))


if __name__ == '__main__':
	main()