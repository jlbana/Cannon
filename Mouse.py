from Vector import Vector

class Mouse:
	def __init__(self):
		self.mvector = None

	@property
	def mVector(self):
		return self.mvector

	@mVector.setter
	def mVector(self, pos):
		self.mvector = Vector(*pos)
