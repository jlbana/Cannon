from math import sqrt, acos

class Vector:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def length(self):
		return sqrt(self.x ** 2 + self.y ** 2)

	def __mul__(self, factor):
		return self.__class__(
		self.x * factor,
		self.y * factor
		)

	def angle(self, other):
		''' Calculate  the angle between V1 and V2
		    and return it.
		'''
		if not (self.length() and self.length()):
			return 0
		return acos(
		(self.x * other.x + other.y * self.y) /
		(self.length() * other.length())
		)

	def pos(self):
		return (self.x, self.y)
