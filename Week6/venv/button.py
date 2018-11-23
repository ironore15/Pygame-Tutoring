import pygame


class Button(object):

    """
    Class for making button

    # Button(image object, center position, text on button, font name)
    button = Button(pygame.image.load("button.png"), (300, 300))
    button = Button(pygame.image.load("button.png"), (300, 300), "Press it!")
    button = Button(pygame.image.load("button.png"), (300, 300), "Press it!", "Times New Roman")

    # Button.resize(scale)
    button.resize(0.5)

    # Button.setText(color, fontsize)
    button.setText("white")
    button.setText("white", 24)     # see pygame.colordict.THECOLORS to check supporting colorname

    while True:
        for event in pygame.event.get():
            if button.eventHandler(event):
                # do Something...

        button.display(screen)
        pygame.display.flip()
    """

    def __init__(self, image, pos, text=None, font_name=None):
        self.button = image
        self.button_rect = self.button.get_rect()
        self.button_rect.center = pos
        self.text = text
        if font_name is None:
            self.font_name = pygame.font.get_default_font()
        else:
            self.font_name = pygame.font.match_font(font_name)
        self.click = False

        self.setText()


    def resize(self, scale):
        pos = self.button_rect.center
        width = int(round(self.button_rect.width * scale))
        height = int(round(self.button_rect.height * scale))
        self.button = pygame.transform.scale(self.button, (width, height))
        self.button_rect = self.button.get_rect()
        self.button_rect.center = pos
        self.setText()


    def setText(self, color="black", size=0):
        if self.text is not None:
            if size <= 0:
                size = self.button_rect.height // 2
            self.font = pygame.font.Font(self.font_name, size)

            self.text_image = self.font.render(self.text, True, pygame.Color(color))
            self.text_rect = self.text_image.get_rect()
            self.text_rect.center = self.button_rect.center

            self.font.set_underline(True)
            self.btext_image = self.font.render(self.text, True, pygame.Color(color))
            self.btext_rect = self.btext_image.get_rect()
            self.btext_rect.center = self.button_rect.center


    def eventHandler(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(pygame.mouse.get_pos()):
                self.click = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if self.button_rect.collidepoint(pygame.mouse.get_pos()):
                if self.click:
                    self.click = False
                    return True
            self.click = False
        return False


    def display(self, screen):
        screen.blit(self.button, self.button_rect)
        if self.text is not None:
            if self.click:
                screen.blit(self.btext_image, self.btext_rect)
            else:
                screen.blit(self.text_image, self.text_rect)