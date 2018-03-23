import sean
import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))
pi = 3.1415926
running = True
v = sean.Vector(10,10)
u = v.rot(3*pi/2)
init_pos = [250,250]
end_pos = [init_pos[0]+v.x, init_pos[1]+v.y]
end_pos2 = [init_pos[0]+u.x, init_pos[1]+u.y]
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	pygame.draw.line(screen,(255,255,255),init_pos,end_pos)
	pygame.draw.line(screen,(255,255,255),init_pos,end_pos2)
	pygame.display.flip()