import pygame


class Fruit:
    def __init__(self, info):
        self.name = info[0]
        self.image_path = info[1]
        self.hover_path = info[2]
        self.sound = pygame.mixer.Sound('sounds/click_sound.mp3')
        self.is_clicked = False
        self.fruit_is_hovered = False

        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (110, 110))
        self.hover_image = pygame.image.load(self.hover_path)
        self.hover_image = pygame.transform.scale(self.hover_image, (110, 110))
        self.rect = self.image.get_rect(topleft=info[3])

    def fruit_updated(self, screen, mouse_pos):
        self.fruit_is_hovered = self.rect.collidepoint(mouse_pos)
        if self.fruit_is_hovered:
            current_image = self.hover_image
        else:
            current_image = self.image
        self.is_clicked = False

        screen.blit(current_image, self.rect.topleft)

    def get_clicked(self):
        return self.is_clicked

    def get_name(self):
        return self.name

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.fruit_is_hovered:
            if self.rect.collidepoint(event.pos):
                self.sound.play()
                self.is_clicked = True
