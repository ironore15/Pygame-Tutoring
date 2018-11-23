import pygame


class Player(object):

    """
    Class for making player

    # Player(image object, center position, movement speed, angular speed)
    player = Player(pygame.image.load("player.png"), (300, 300), 5, 10)

    while True:
        for event in pygame.event.get():
            player.eventHandler(event)

        player.move()
        player.display(screen)
        pygame.display.flip()
    """

    def __init__(self, image, pos, speed, aspeed):
        self.image = image
        self.rotate_image = image
        self.pos = pos
        self.speed = speed
        self.aspeed = aspeed
        self.angle = 0
        self.prev_angle = 0
        self.dx = 0
        self.dy = 0
        self.da = 0


    def eventHandler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.dy -= self.speed
            elif event.key == pygame.K_a:
                self.dx -= self.speed
            elif event.key == pygame.K_s:
                self.dy += self.speed
            elif event.key == pygame.K_d:
                self.dx += self.speed
            elif event.key == pygame.K_q:
                self.da += self.aspeed
            elif event.key == pygame.K_e:
                self.da -= self.aspeed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.dy += self.speed
            elif event.key == pygame.K_a:
                self.dx += self.speed
            elif event.key == pygame.K_s:
                self.dy -= self.speed
            elif event.key == pygame.K_d:
                self.dx -= self.speed
            elif event.key == pygame.K_q:
                self.da -= self.aspeed
            elif event.key == pygame.K_e:
                self.da += self.aspeed


    def move(self):
        x, y = self.pos
        self.pos = x + self.dx, y + self.dy
        self.angle += self.da
        self.angle %= 360


    def display(self, screen):
        if self.angle != self.prev_angle:
            self.prev_angle = self.angle
            self.rotate_image = pygame.transform.rotate(self.image, self.angle)
        rect = self.rotate_image.get_rect()
        rect.center = self.pos
        screen.blit(self.rotate_image, rect)