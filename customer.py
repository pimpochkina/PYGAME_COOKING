import random

import pygame
from random import choice


class CustomerPlace:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.free_space = True
        self.ok = False
        self.time_from_last_customer = pygame.time.get_ticks()
        self.customer_here = False

    def check_place(self):
        if self.free_space:
            if (pygame.time.get_ticks() - self.time_from_last_customer) // 1000 >= choice([ 1, 2, 3, 4]):
                self.ok = True

    def customer_left(self):
        self.free_space = True
        self.customer_here = False
        self.time_from_last_customer = pygame.time.get_ticks()

    def get_coords(self):
        return self.x, self.y

    def get_ok(self):
        return self.ok

    def customer_arrived(self):
        self.free_space = False
        self.ok = False
        self.customer_here = True

    def get_customer_info(self):
        return self.customer_here


class Customer:
    def __init__(self):
        self.order = []
        self.is_here = True
        self.drinks = ['blue', 'green', 'pink',
                       'red', 'yellow']

        self.time_from_ok = 0

    def customer_updated(self, screen):
        screen.blit(self.image, self.rect.topleft)
        screen.blit(self.bubble, self.bubble_rect.topleft)
        screen.blit(self.order_image, self.order_rect)
        if (pygame.time.get_ticks() - self.time_from_ok) // 1000 >= 2 and len(self.order) == 0:
            self.is_here = False

    def new_order(self):
        self.order = []
        self.order.append(choice(self.drinks))
        self.order_image = pygame.image.load(f'food/drinks/{self.order[0]}_drink.png')
        self.order_image = pygame.transform.scale(self.order_image, (75, 125))
        self.order_rect = self.order_image.get_rect(topleft=(10, 10))
        self.order_rect.center = (self.bubble_rect.center[0] + 15, self.bubble_rect.center[1] - 15)
        print(self.order, self.bubble_rect.center)

    def set_info(self, info, coord):
        self.is_here = True
        self.image = pygame.image.load(info[0])
        self.image = pygame.transform.scale(self.image, (265, 340))
        self.happy_image = pygame.image.load(info[1])
        self.happy_image = pygame.transform.scale(self.happy_image, (265, 340))
        self.x, self.y = coord
        self.rect = self.image.get_rect(topleft=coord)
        self.bubble = pygame.image.load('customers/bubble.png')
        self.bubble = pygame.transform.scale(self.bubble, (165, 295))
        self.bubble_rect = self.bubble.get_rect(topleft=(self.x + 185, self.y - 100))

    def check_correct_order(self, color, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            if color in self.order:
                self.order.remove(color)
                if len(self.order) == 0:
                    self.time_from_ok = pygame.time.get_ticks()
                    self.image = self.happy_image

    def get_is_here(self):
        return self.is_here




