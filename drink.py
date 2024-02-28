import pygame

class Drink:
    def __init__(self):
        self.is_clicked = False
        self.color_set = False
        self.color = ''

    def drink_updated(self, screen, mouse_pos):
        self.is_clicked = False
        self.rect.center = mouse_pos
        screen.blit(self.image, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.is_clicked = True

    def is_on_cursor(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def color_false(self):
        self.color_set = False

    def color_is_setted(self):
        return self.color_set

    def set_color(self, color):
        self.color_set = True
        self.color = color
        self.image = pygame.image.load(f'food/drinks/{color}_drink.png')
        self.image = pygame.transform.scale(self.image, (75, 125))
        self.rect = self.image.get_rect(topleft=(10, 10))

    def get_name(self):
        return self.color

    def get_is_clicked_withdrink(self, event):
        return self.is_clicked and self.is_on_cursor(event)

