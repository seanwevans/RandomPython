import pygame
from sean import Vector, isprime
from math import pi as PI
from math import floor

pygame.init()
SCREEN_RESOLUTION = (W,H) = (500, 500)
SCREEN = pygame.display.set_mode(SCREEN_RESOLUTION)
PHI = (1/2) * (1 + 5**0.5)
running = True

class walker(object):
	def __init__(self, position, heading):
		self.pos = position
		self.hdg = heading

walk = walker(Vector(500,500), Vector(1,0))
n = 1

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	pygame.draw.circle(SCREEN, (255,255,255), [floor(walk.pos.x), floor(walk.pos.y)], 2, 1)
	
	if isprime(n):
		walk.hdg = walk.hdg.rot((2*PI)*(2-PHI))
		
	walk.pos = walk.pos.add(walk.hdg)
	
	n += 1
	
	pygame.display.flip()