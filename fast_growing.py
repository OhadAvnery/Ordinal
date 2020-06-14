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
	if a.ord_type == OrdinalType.ZERO:
		return lambda n: n+1

	if a.ord_type == OrdinalType.SUCCESSOR:
		b = a.pred()
		f = fast_growing(b)
		return lambda n: compose(f,n)(n)

	else:  # a is a limit ordinal
		return lambda n: fast_growing(a[n])(n)

def main():
	w = Ordinal.OMEGA
	print(fast_growing(w)(2))


if __name__ == '__main__':
	main()