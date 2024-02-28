import pygame


class Button:
    def __init__(self, x, y, width, height, text, image_path, hover_path=None, sound_path=None, font_size=36):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size

        self.image = pygame.image.load(image_path)  # загружаем и масштабируем изображение кнопки
        self.image = pygame.transform.scale(self.image, (width, height))
        if hover_path:
            self.hover_image = pygame.image.load(hover_path)
            self.hover_image = pygame.transform.scale(self.hover_image, (width, height))
        else:
            self.hover_image = self.image

        self.rect = self.image.get_rect(topleft=(x, y))

        if sound_path:
            self.sound = pygame.mixer.Sound(sound_path)
        else:
            self.sound = None

        self.is_hovered = False

    def update_btn(self, screen, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)
        if self.is_hovered:
            current_image = self.hover_image
        else:
            current_image = self.image

        screen.blit(current_image, self.rect.topleft)

        if self.text:
            font = pygame.font.Font('buttons/m5x7.ttf', self.font_size)
            text_surface = font.render(self.text, True, (255, 239, 213))
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.rect.collidepoint(event.pos):
                if self.sound:
                    self.sound.play()
                pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))
