#!/usr/bin/python3

from Vector import Vector
from Mouse import Mouse
from Cannon import Cannon, Support
from Ball import Ball
from random import seed
import time
import pygame
import pygame.gfxdraw

# Boundaries and Intervals
xMax, yMax	= 319, 199
intIn		= (__import__('math').sqrt(
		  xMax ** 2 + yMax ** 2
		  ), 0)

# Initialization
pygame.init()
pygame.display.set_caption("CANNON")
screen	= pygame.display.set_mode((xMax + 1, yMax + 1))
mouse	= Mouse()
clock	= pygame.time.Clock()
seed(time.time())

# Cannon Location and Vector
cx, cy	= (0, yMax)
cVec	= Vector(cx + 1, 0)

# Colors
skyColor	= (0x34, 0x98, 0xdb)
supportColor	= (0x79, 0x56, 0x44)
cannonColor	= (0, 0, 0)
lineColor	= (0xff, 0, 0)

# Balls
cBalls	= list()

def updateScreen():
	# Background
	screen.fill(skyColor)

	# Acquire mouse position and
	# calculate angle.
	pos	= pygame.mouse.get_pos()
	mouse.mVector = (pos[0], yMax - pos[1])
	angle	= mouse.mVector.angle(cVec)
	mouse.mVector = pos

	# Normalize vector, scale and
	# draw it.
	pygame.draw.line(
	screen,				# Surface to draw on
	lineColor,			# Color of line(RED)
	(cx, cy), mouse.mVector.pos(),	# Start, End points
	2)				# Width of line(2)

	cannon	= Cannon.rotatePoints(-angle, 4, (yMax - 8))
	pygame.gfxdraw.filled_polygon(
	screen,
	cannon,
	cannonColor)

	pygame.gfxdraw.filled_polygon(
	screen,
	Support.getPoints(),
	supportColor)

	return angle

def getTime():
	return pygame.time.get_ticks()

def drawBalls():
	for i, ball in enumerate(cBalls):
		location = ball.getPos(
		getTime() * (10 ** -3) * 8
		)
		color	 = ball.getColor()

		if location[0] > xMax or location[1] < 0:
			cBalls.pop(i)
			continue

		location[1] = yMax - location[1]
		pygame.draw.circle(
		screen,
		color,
		location,
		4)

def mapInterval(x, intIn, intOut):
	return (
	(x - intIn[0]) *
	((intOut[1] - intOut[0]) / (intIn[1] - intIn[0]))
	+ intOut[0]
	)

def mainLoop():
	# Initial angle and length
	# to be updated on events.
	angle, length = 0, 0

	while True:
		angle = updateScreen()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				return
			elif event.type == pygame.MOUSEBUTTONDOWN:
				length	= mapInterval(
				mouse.mVector.length(),
				intIn,
				(0, 32))

				cBalls.append(Ball(
				8, 16, length, angle,
				getTime() * (10 ** -3) * 8
				))

		# Draw all balls on the screen.
		drawBalls()

		# Update screen and time.
		pygame.display.update()
		clock.tick(60)

if __name__ == '__main__':
	mainLoop()
