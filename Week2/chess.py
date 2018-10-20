import pygame

pygame.init()

width, height = 800, 800
dw, dh = width // 8, height // 8
size = (width, height)

screen = pygame.display.set_mode(size)

board = pygame.image.load("images\Board.jpg")
board = pygame.transform.scale(board, size)

rook = pygame.image.load("images\Rook.png")
rook = pygame.transform.scale(rook, (dw, dh))
rect = rook.get_rect()

click = False
count = 0
dx = 0
dy = 0
speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx -= speed
            elif event.key == pygame.K_RIGHT:
                dx += speed
            elif event.key == pygame.K_UP:
                dy -= speed
            elif event.key == pygame.K_DOWN:
                dy += speed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                dx += speed
            elif event.key == pygame.K_RIGHT:
                dx -= speed
            elif event.key == pygame.K_UP:
                dy += speed
            elif event.key == pygame.K_DOWN:
                dy -= speed
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(pygame.mouse.get_pos()):
                click = True
        elif event.type == pygame.MOUSEBUTTONUP:
            click = False

    rect = rect.move(dx, dy)
    if click:
        rect.center = pygame.mouse.get_pos()

    screen.blit(board, (0, 0))
    screen.blit(rook, rect)
    pygame.display.flip()