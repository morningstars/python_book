import pygame

screen = pygame.display.set_mode((800, 90))

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            exit()

    screen.fill((255, 0, 0))
    pygame.display.flip()
