import pygame
from fruit import Fruit
from random import random


class Blender:
    def __init__(self):
        self.mixingsound = pygame.mixer.Sound('sounds/blender_mixing.mp3')
        self.sound = pygame.mixer.Sound('sounds/click_sound.mp3')
        self.blender_image = pygame.image.load('food/blender/blender.png')
        self.blender_image = pygame.transform.scale(self.blender_image, (200, 300))
        self.hover_blender_image = pygame.image.load('food/blender/hover_blender.png')
        self.hover_blender_image = pygame.transform.scale(self.hover_blender_image, (200, 300))
        self.yellow_blender = pygame.image.load('food/blender/yellow_blender.png')
        self.yellow_blender = pygame.transform.scale(self.yellow_blender, (200, 300))
        self.blue_blender = pygame.image.load('food/blender/blue_blender.png')
        self.blue_blender = pygame.transform.scale(self.blue_blender, (200, 300))
        self.green_blender = pygame.image.load('food/blender/green_blender.png')
        self.green_blender = pygame.transform.scale(self.green_blender, (200, 300))
        self.pink_blender = pygame.image.load('food/blender/pink_blender.png')
        self.pink_blender = pygame.transform.scale(self.pink_blender, (200, 300))
        self.red_blender = pygame.image.load('food/blender/red_blender.png')
        self.red_blender = pygame.transform.scale(self.red_blender, (200, 300))
        self.blender_rect = self.blender_image.get_rect(topleft=(770, 250))
        self.recipe = []
        self.is_hovered = False
        self.is_clicked = False
        self.current_image = self.hover_blender_image
        self.is_mixing = False
        self.is_ready = False
        self.start_time = 0
        self.color = 'red'


    def update_blender(self, screen, mouse_pos):
        if self.is_mixing:
            screen.blit(self.current_image, self.blender_rect.topleft)
            if (pygame.time.get_ticks() - self.start_time) // 1000 >= 5:
                self.is_ready = True
                self.is_mixing = False
                self.recipe.clear()

        elif not self.is_clicked:
            self.is_hovered = self.blender_rect.collidepoint(mouse_pos)
            if self.is_hovered:
                current_image = self.hover_blender_image
            else:
                current_image = self.blender_image
            screen.blit(current_image, self.blender_rect.topleft)
        else:
            screen.blit(self.hover_blender_image, self.blender_rect.topleft)


    def mixing(self):
        if not self.is_ready:
            self.is_clicked = False
            self.is_mixing = True
            self.start_time = pygame.time.get_ticks()
            if 'blueberry' in self.recipe:
                self.current_image = self.blue_blender
                self.color = 'blue'
            elif 'apple' in self.recipe:
                self.current_image = self.red_blender
                self.color = 'red'
            elif 'strawberry' in self.recipe:
                self.current_image = self.pink_blender
                self.color = 'pink'
            elif 'broccoli' in self.recipe:
                self.current_image = self.green_blender
                self.color = 'green'
            else:
                self.current_image = self.yellow_blender
                self.color = 'yellow'
            self.mixingsound.play()
            self.recipe.clear()


    def get_is_mixing(self):
        return self.is_mixing

    def get_is_ready(self):
        return self.is_ready
    def add_fruit(self, fruit):
        if len(self.recipe) < 2:
            self.recipe.append(fruit)

    def get_clcikedinfo(self):
        return self.is_clicked

    def set_is_ready_false(self):
        self.is_ready = False

    def get_color(self):
        return self.color

    def blender_handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.blender_rect.collidepoint(event.pos):
                self.is_clicked = not self.is_clicked

