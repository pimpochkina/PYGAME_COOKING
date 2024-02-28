import pygame

class TrashBin:
    def __init__(self):
        self.image = pygame.image.load('food/Trashbin.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect(topleft=(950, 550))
        self.is_clicked = False
        self.sound = pygame.mixer.Sound('sounds/click_sound.mp3')

    def update_trashbin(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.sound.play()
                self.is_clicked = True

