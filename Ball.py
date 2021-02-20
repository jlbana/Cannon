from random import random
from math import cos, sin

# Gravitational constant
G = 9.81

class Ball:
	def __init__(self, x0, y0, v0, theta, t0):
		self.x0 = x0
		self.y0 = y0
		self.v0 = v0
		self.t0 = t0
		self.theta = theta

		self.color = (
		random() % 256,
		random() % 256,
		random() % 256
		)

	def getPos(self, time):
		delta = time - self.t0
		return [self.x0 + (self.v0 * cos(self.theta)) * delta,
			self.y0 + (self.v0 * sin(self.theta)) * delta
			- (1 / 2) * (delta ** 2)]

	def getColor(self):
		return self.color

