import pygame as p
from random import shuffle
from sys import argv

M = 100
BOARD_SIZE = int(argv[1])
SCREEN_SIZE = (BOARD_SIZE*M, BOARD_SIZE*M)

BLACK = 	(0	,	0	,	0  )
WHITE = 	(255, 	255	, 	255)
RED = 		(255, 	0	,	0  )
GREEN = 	(0	,	255	, 	0  )
BLUE = 		(0	, 	0	,	255)
colors = [BLACK, WHITE, RED, GREEN, BLUE]

WIN_MSG = "WIN!"

class Hexagon:
	#     p2______p3
	#      /      \
	#  p1 /__size__\ p4
	#     \        /
	#    p6\______/p5
	
	def __init__(self, position, size, number):
		ep = 3 ** -0.5
		self.pos = (self.x, self.y) = position
		self.size = size
		self.num = number
		self.p1 = self.pos
		self.p2 = (p1[0] + .5 * ep * self.size	, p1[1] - .5 * self.size)
		self.p3 = (p2[0] + self.size * (1 - ep)	, p2[1]			)
		self.p4 = (p1[0] + self.size, p1[1]			)
		self.p5 = (p3[0]			, p2[1] + self.size	)
		self.p6 = (p2[0]			, p2[1] + self.size	)
		self.hex = [self.p1, self.p2, self.p3, self.p4, self.p5, self.p6]
	def draw(self, surface, textsize=M):
		blend = 1
		p.draw.aalines(surface, BLUE, True, self.hex, blend)
		
class Square:
	def __init__(self, position, size, number):
		self.pos = (self.x, self.y) = position
		self.size = size
		self.num = number
		self.square = (self.x, self.y, self.size, self.size)
	def draw(self, surface, textsize=M//2):
		font = p.font.Font(None, textsize)
		text = font.render(str(self.num), 1, RED)
		i = int(self.x + .5 * self.size - text.get_rect().centerx)
		j = int(self.y + .5 * self.size - text.get_rect().centery)
		textpos = (i, j)
		p.draw.rect(surface, BLACK, self.square, 1)
		surface.blit(text, textpos)

class Board:
		def __init__(self, order):
			self.order = order
			
		def draw(self, surface):
			c = 0
			size = M
			pos = [0,0]
			for i in range(BOARD_SIZE):
				for j in range(BOARD_SIZE):
					if self.order[c] != 0:
						Square(pos, size, self.order[c]).draw(surface)
					pos[0] += size
					c += 1
				pos[0] -= BOARD_SIZE * size
				pos[1] += size
		
		def win(self):
			win1 = [i for i in range(BOARD_SIZE**2)]
			win2 = win1[1:]
			win2.append(0)
			
			if board.order == win1 or board.order == win2:
				return(True)
				
def random_list(min, max):
	a = [i for i in range(min, max)]
	shuffle(a)
	return(a)

if __name__ == "__main__":
	p.init()
		
	screen = p.display.set_mode(SCREEN_SIZE)
	p.display.set_caption("Puzzle")
	
	board = Board(random_list(0, BOARD_SIZE**2))

	screen.fill(WHITE)
	board.draw(screen)
	p.display.flip()

	running = True
	while running:
		for event in p.event.get():
			if event.type == p.QUIT:
				running = False
		
			if event.type == p.KEYDOWN:
				o = board.order.index(0)
				offset = 0
				
				# Exit, restart and cheat
				if event.key == p.K_RETURN:
					running = False
				if event.key == p.K_SPACE:
					board = Board(random_list(0, BOARD_SIZE**2))
				if event.key == p.K_w:
					board.order = [i for i in range(1, BOARD_SIZE**2)]
					board.order.append(0)
				
				# Move squares
				if event.key == p.K_UP:
					# if 0 is not in the last row
					if o < BOARD_SIZE * (BOARD_SIZE - 1):
						offset = BOARD_SIZE
				if event.key == p.K_DOWN:	
					# if 0 is not in the first row
					if o > BOARD_SIZE - 1:
						offset = -BOARD_SIZE
				if event.key == p.K_LEFT:
					# if 0 is not in the last column
					if o in [i for i in range(BOARD_SIZE**2) if i%BOARD_SIZE != BOARD_SIZE-1]:
						offset = 1
				if event.key == p.K_RIGHT:
					# if 0 is not in the first column
					if o in [i for i in range(BOARD_SIZE**2) if i%BOARD_SIZE != 0]:
						offset = -1
				
				if offset != 0:
					board.order[o] = board.order[o+offset]
					board.order[o+offset] = 0
	
				# Draw background and board
				screen.fill(WHITE)
				board.draw(screen)
	
				# Check if board is a winner
				if board.win():
					font = p.font.Font(None, BOARD_SIZE * M//2)
					text = font.render(WIN_MSG, 1, BLUE)
					i = int(.5 * screen.get_size()[0] - text.get_rect().centerx)
					j = int(.5 * screen.get_size()[1] - text.get_rect().centery)
					textpos = (i, j)
					screen.blit(text, textpos)
											
				p.display.flip()
