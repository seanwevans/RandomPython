import pygame
import sean

pygame.init()
res = (w, h) = (500, 500)
screen = pygame.display.set_mode(res)
i = 1
maxprime = 1000000
pos = [x_pos, y_pos] = [100, 100]
color = [255, 255, 255]
primes = sean.primesbelow(maxprime)

class walker(object):
	def __init__(self, position, orientation):
		self.pos = position		# (x,y)
		self.num = complex(position[0], position[1])
		self.ori = orientation	# 0,1,2,3
		self.turns = (complex(1,0), complex(0,-1), complex(-1,0), complex(0,1))
	def turn(self):
		self.ori = (self.ori + 1) % 4
	def advance(self):
		self.num += self.turns[self.ori]
		self.pos = (int(self.num.real), int(self.num.imag))
	def draw(self, canvas):
		pygame.draw.circle(canvas, (255,255,255), self.pos, 1)
		pygame.display.flip()
		
walk = walker((250,10), 1)

running = True

while running:
	for event in pygame.event.get():
		if i > maxprime or event.type == pygame.QUIT:
			running = False
	walk.draw(screen)
	if i in primes:
		walk.turn()
	walk.advance()
	i += 1