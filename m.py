import pygame as p
from sys import argv

p.init()

M = 20
TITLE = "Minesweeper"
WIDTH, HEIGHT, NUM_MINES = W, H, N = [int(argv[i]) for i in range(1,4)]
SCREEN_SIZE = (W*M, H*M)
WHITE = (255, 255, 255)

class Tile:
	def __init__(self, pos, mine=False):
		self.pos = (self.x, self.y) = pos
		self.mine = mine
		self.size = M
	
	def draw(self, surface):
		thickness = 1
		rect = [self.x, self.y, self.size, self.size]
		p.draw.rect(surface, WHITE, rect, thickness)
	
	def mouse_in(self, cursor_pos):
		if self.x < cursor_pos[0] < self.x+self.size and self.y < cursor_pos[1] < self.y+self.size:
			return True
		return False

class Board:
	def __init__(self, layout):
		self.layout = layout

screen = p.display.set_mode(SCREEN_SIZE)
p.display.set_caption(TITLE)
tiles = []

for i in range(0, W*M, M):
	for j in range(0, H*M, M):
		tiles.append(Tile((i,j)))

running = True
while running:
	for event in p.event.get():
		if event.type == p.QUIT:
			running = False

		if event.type == p.MOUSEBUTTONDOWN:
			cursor_pos = p.mouse.get_pos()
			for tile in tiles:
				if tile.mouse_in(cursor_pos):
					print(tile.mine)

	for tile in tiles:
		tile.draw(screen)
	
	p.display.flip()