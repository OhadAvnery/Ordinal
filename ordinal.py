#import copy
from enum import Enum, auto
import itertools

class OrdinalType(Enum):
	ZERO = auto()
	SUCCESSOR = auto()
	LIMIT = auto()

class Ordinal:
	ZERO = None
	ONE = None
	OMEGA = None

	def __init__(self, ord_list=[]):
		if isinstance(ord_list, int):
			ord_list = [Ordinal.ZERO]*ord_list
		if not Ordinal.valid_list(ord_list):
			raise Exception("invalid list for class constructor!")
		self.ord_list = ord_list
		self.ord_type = Ordinal.ord_type(self.ord_list)

	@staticmethod
	def ord_type(ord_list):
		if not ord_list:
			return OrdinalType.ZERO
		if ord_list[-1] == Ordinal.ZERO:
			return OrdinalType.SUCCESSOR
		return OrdinalType.LIMIT

	@staticmethod
	def valid_list(ord_list):
		for j in range(len(ord_list) - 1):
			if ord_list[j] < ord_list[j + 1]:
				return False
		return True

	def __eq__(self, other):
		if isinstance(other, int):
			other = Ordinal(other)
		return isinstance(other, Ordinal) and self.ord_list == other.ord_list

	def __le__(self, other):
		if isinstance(other, int):
			other = Ordinal(other)
		if not isinstance(other, Ordinal):
			return False
		l1, l2 = self.ord_list, other.ord_list
		'''if l1 == Ordinal.ZERO:
			return l2 != Ordinal.ZERO'''
		pairs = itertools.zip_longest(l1, l2)
		for a, b in pairs:
			if a == None:
				break
			if b == None or a > b:
				return False
			if a < b:
				break
		return True

	def __lt__(self, other):
		return self <= other and self != other

	def __repr__(self):
		#return str(self.ord_list)
		return str(self)

	def __str__(self):
		if self == Ordinal.ZERO:
			return '0'
		if self == Ordinal.ONE:
			return '1'
		if self == Ordinal.OMEGA:
			return 'w'
		if self.ord_type == OrdinalType.SUCCESSOR:
			return str(self.pred()) + "+1"
		#return '+'.join([f'w^({a})' for a in self.ord_list])
		powers = []
		for a in self.ord_list:
			if a == Ordinal.ONE:
				powers.append('w')
			elif len(a.ord_list) == 1:
				powers.append(f'w^{a}')
			else:
				powers.append(f'w^({a})')
		return '+'.join(powers)

	def copy(self):
		return Ordinal(self.ord_list)

	def __add__(self, other):
		if isinstance(other, int):
			other = Ordinal(other)

		if len(other.ord_list) == 1:
			b = other.ord_list[0]
			N = len(self.ord_list) - 1 #last index in ord_list
			while N >= 0:
				if self.ord_list[N] >= b:
					break
				N -= 1
			return Ordinal(self.ord_list[:N+1] + [b])

		temp_result = self.copy()
		for b in other.ord_list:
			temp_result += Ordinal([b])
		return temp_result
		#return Ordinal(self.ord_list + other.ord_list)

	def __radd__(self, other):
		if isinstance(other, int):
			other = Ordinal(other)
		return other + self

	def __pow__(self, other):
		if self != Ordinal.OMEGA:
			raise NotImplementedError
		if isinstance(other, int):
			other = Ordinal(other)
		return Ordinal([other])

	def __mul__(self, other):
		if not isinstance(other, int):
			raise NotImplementedError
		return Ordinal(self.ord_list * other)


	'''def succ(self):
		l = self.ord_list[:]
		l.append(Ordinal.ZERO)
		return Ordinal(l)'''

	def pred(self):
		if self.ord_type != OrdinalType.SUCCESSOR:
			raise Exception("Non-successor ordinals don't have a predecessor")
		#l= self.ord_list[:]
		#del l[-1]
		return Ordinal(self.ord_list[:-1])


	def __getitem__(self, n):
		'''
		a[n] - the nth element in the fundamental sequence for a
		'''
		if self.ord_type != OrdinalType.LIMIT:
			raise Exception("Non-limit ordinals don't have a limit")

		a = self.ord_list[-1] # a > 0, as w**a is a limit ordinal
		w = Ordinal.OMEGA
		if len(self.ord_list) > 1:
			o = Ordinal(self.ord_list[:-1])
			return o + (w**a)[n]

		# else, the list has exactly one element- of the form w**a
		
		if a.ord_type == OrdinalType.SUCCESSOR:
			# b = a.pred()
			return (w ** a.pred()) * n

		#else, a is a limit ordinal
		return w ** a[n]

	@staticmethod
	def omega_tower(n):
		if n==0:
			return Ordinal.ONE
		return Ordinal.OMEGA ** (Ordinal.omega_tower(n-1))


Ordinal.ZERO = Ordinal()
Ordinal.ONE = Ordinal([Ordinal.ZERO])
Ordinal.OMEGA = Ordinal([Ordinal.ONE])