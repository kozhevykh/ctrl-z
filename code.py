import pygame
size = wi, he = 300, 300
screen = pygame.display.set_mode(size)
screen2 = pygame.Surface(screen.get_size())
x1, y1, w, h = 0, 0, 0, 0
drawing = False
running = True
list = []
screen.fill((0,0,0))
while running:
    if len(list):
        for el in range(0, len(list), 2):
             pygame.draw.rect(screen, (250, 250, 250), (list[el], list[el+1]), 1)
        pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            x1, y1 = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            screen2.blit(screen, (0, 0))
            drawing = False
            list.append((x1, y1))
            list.append((w, h))
        if event.type == pygame.MOUSEMOTION:
            if drawing:
                w, h = event.pos[0] - x1, event.pos[1] - y1
        if event.type == pygame.KEYDOWN:
            if pygame.KMOD_LCTRL & pygame.key.get_mods() and event.key == pygame.K_z:
                if list:
                    list.pop()
                    list.pop()
                    screen.fill((0,0,0))
                    screen2.fill((0,0,0))
        screen.fill(pygame.Color('black'))
        screen.blit(screen2, (0, 0))
        if drawing:
            pygame.draw.rect(screen, (250, 250, 250), ((x1, y1), (w, h)), 1)
        pygame.display.flip()
