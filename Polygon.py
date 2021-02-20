from math import cos, sin

class Polygon:
	def __init__(self, *p):
		self.points = p

	def getPoints(self):
		return self.points

	def rotatePoints(self, angle, tX = 0, tY = 0):
		rotated = list()
		for point in self.points:
			c, s = cos(angle), sin(angle)
			rotated.append(
			((point[0] * c - point[1] * s) + tX,
			 (point[1] * c + point[0] * s) + tY)
			)
		return rotated

	def __add__(self, dxy):
		return self.__class__(*[
			(dxy[0] + p[0], dxy[1] + p[1])
			for p in self.points
		])

	def __mul__(self, factor):
		self.points = [	(p[0] * factor, p[1] * factor)
				for p in self.points]
		return self
