import pygame
from button import Button
from blender import Blender
from fruit import Fruit
import random
from customer import Customer, CustomerPlace
from drink import Drink
from trashbin import TrashBin

if __name__ == '__main__':
    pygame.init()
    size = width, height = 1000, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Cooking game !')
    main_menu_background = pygame.image.load('backgrounds/main_manu_bg.png')
    end_screen_bg = pygame.image.load('backgrounds/end_screen.png')
    game_bg = pygame.image.load('backgrounds/game_bg.png')
    clock = pygame.time.Clock()


    def end_screen(score):
        screen.fill((0, 0, 0))
        screen.blit(end_screen_bg, (0, 0))

        name_font = pygame.font.Font('buttons/shr.ttf', 140)
        score_font = pygame.font.Font('buttons/shr.ttf', 80)
        text_surface = name_font.render("FINISH!", True, (255, 150, 112))
        text_rect = text_surface.get_rect(center=(width / 2 + 20, 100))
        score_surface = score_font.render(f"Your score: {str(score)}", True, (255, 239, 213))
        score_rect = text_surface.get_rect(center=(width / 2, 250))
        retry_button = Button(350, 300, 300, 100, "RETRY", 'buttons/ok_button.png', 'buttons/hovered_button.png',
                              'sounds/click_sound.mp3', 70)
        menu_button = Button(350, 415, 300, 50, "back to main menu", 'buttons/ok_button.png',
                             'buttons/hovered_button.png',
                             'sounds/click_sound.mp3', 40)

        running = True

        while running:
            screen.fill((0, 0, 0))
            screen.blit(end_screen_bg, (0, 0))
            screen.blit(text_surface, text_rect)
            screen.blit(score_surface, score_rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.USEREVENT and event.button == menu_button:
                    main_menu()
                if event.type == pygame.USEREVENT and event.button == retry_button:
                    start_game()
                for btn in [retry_button, menu_button]:
                    btn.handle_event(event)
            for btn in [retry_button, menu_button]:
                btn.update_btn(screen, pygame.mouse.get_pos())

            pygame.display.flip()
            clock.tick(60)
        pygame.quit()


    def start_game():
        score = 0
        trash = TrashBin()
        pygame.mixer.music.load('sounds/game_bg_music.wav')
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)
        start_game_time = pygame.time.get_ticks()
        door_sound = pygame.mixer.Sound('sounds/door_sound.mp3')
        fruits = [('mango', 'food/fruits/mango.png', 'food/fruits/hover_mango.png', (400, 350)),
                  ('apple', 'food/fruits/apple.png', 'food/fruits/hover_apple.png', (500, 350)),
                  ('banana', 'food/fruits/banana.png', 'food/fruits/hover_banana.png', (600, 350)),
                  ('strawberry', 'food/fruits/strawberry.png', 'food/fruits/hover_strawberry.png', (400, 450)),
                  ('blueberry', 'food/fruits/blueberry.png', 'food/fruits/hover_blueberry.png', (500, 450)),
                  ('broccoli', 'food/fruits/broccoli.png', 'food/fruits/hover_broccoli.png', (600, 450))]
        customers = [('customers/customer1_default.png', 'customers/customer1_happy.png'),
                     ('customers/customer2_default.png', 'customers/customer2_happy.png'),
                     ('customers/customer3_default.png', 'customers/customer3_happy.png'),
                     ('customers/customer4_default.png', 'customers/customer4_happy.png'),
                     ('customers/customer5_default.png', 'customers/customer5_happy.png'),
                     ('customers/customer6_default.png', 'customers/customer6_happy.png'),
                     ('customers/customer7_default.png', 'customers/customer7_happy.png'),
                     ('customers/customer8_default.png', 'customers/customer8_happy.png'),
                     ('customers/customer9_default.png', 'customers/customer_9_happy.png')]
        mixing_button = Button(800, 200, 125, 75, 'MIX!', 'buttons/ok_button.png', 'buttons/hovered_button.png',
                               'sounds/click_sound.mp3', 50)
        mango = Fruit(fruits[0])
        apple = Fruit(fruits[1])
        banana = Fruit(fruits[2])
        strawberry = Fruit(fruits[3])
        blueberry = Fruit(fruits[4])
        broccoli = Fruit(fruits[5])
        running = True
        blender = Blender()
        customer1 = Customer()
        customer2 = Customer()
        customer3 = Customer()
        place1 = CustomerPlace(30, 100)
        place2 = CustomerPlace(320, 100)
        place3 = CustomerPlace(600, 100)
        drink = Drink()
        name_font = pygame.font.Font('buttons/shr.ttf', 40)
        score_surface = name_font.render(str(score), True, (255, 239, 213))
        score_rect = score_surface.get_rect(center=(900, 25))
        while running:
            screen.fill((0, 0, 0))
            screen.blit(game_bg, (0, 0))
            score_surface = name_font.render(str(score), True, (255, 239, 213))
            place1.check_place()
            place2.check_place()
            place3.check_place()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                blender.blender_handle_event(event)
                if event.type == pygame.USEREVENT and event.button == mixing_button:
                    blender.mixing()
                    drink.color_false()
                trash.handle_event(event)
                if blender.get_clcikedinfo():
                    for fr in [mango, apple, banana, strawberry, blueberry, broccoli]:
                        fr.handle_event(event)
                    mixing_button.handle_event(event)
                if blender.get_is_ready():
                    drink.handle_event(event)
                if trash.is_clicked:
                    blender.is_ready = False
                    trash.is_clicked = False
                if place1.get_ok():
                    place1.customer_arrived()
                    customer1.set_info(random.choice(customers), place1.get_coords())
                    customer1.new_order()
                    door_sound.play()
                    place1.ok = False
                if drink.get_is_clicked_withdrink(pygame.mouse.get_pos()):
                    customer1.check_correct_order(drink.color, pygame.mouse.get_pos())
                    blender.is_ready = False
                if place2.get_ok():
                    place2.customer_arrived()
                    customer2.set_info(random.choice(customers), place2.get_coords())
                    customer2.new_order()
                    door_sound.play()
                    place2.ok = False
                if drink.get_is_clicked_withdrink(pygame.mouse.get_pos()):
                    customer2.check_correct_order(drink.color, pygame.mouse.get_pos())
                    blender.is_ready = False
                if place3.get_ok():
                    place3.customer_arrived()
                    customer3.set_info(random.choice(customers), place3.get_coords())
                    customer3.new_order()
                    door_sound.play()
                    place3.ok = False
                if drink.get_is_clicked_withdrink(pygame.mouse.get_pos()):
                    customer3.check_correct_order(drink.color, pygame.mouse.get_pos())
                    blender.is_ready = False

            if place1.get_customer_info():
                customer1.customer_updated(screen)
            if not customer1.get_is_here():
                score += 200
                place1.customer_left()
            if place2.get_customer_info():
                customer2.customer_updated(screen)
            if not customer2.get_is_here():
                score += 200
                place2.customer_left()
            if place3.get_customer_info():
                customer3.customer_updated(screen)
            if not customer3.get_is_here():
                score += 200
                place3.customer_left()
            trash.update_trashbin(screen)
            for fr in [mango, apple, banana, strawberry, blueberry, broccoli]:
                if fr.get_clicked():
                    blender.add_fruit(fr.get_name())
            if blender.get_clcikedinfo():
                for fr in [mango, apple, banana, strawberry, blueberry, broccoli]:
                    fr.fruit_updated(screen, pygame.mouse.get_pos())
                mixing_button.update_btn(screen, pygame.mouse.get_pos())
            if blender.get_is_ready():
                if not drink.color_is_setted():
                    drink.set_color(blender.get_color())
                drink.drink_updated(screen, pygame.mouse.get_pos())

            blender.update_blender(screen, pygame.mouse.get_pos())
            elapsed_time = (pygame.time.get_ticks() - start_game_time) // 1000
            if elapsed_time >= 120:
                end_screen(score)
            customer1.is_here = True
            customer2.is_here = True
            customer3.is_here = True
            screen.blit(score_surface, score_rect)
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()


    def main_menu():
        pygame.mixer.music.load('sounds/bg_mus.wav')
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)
        play_button = Button(350, 300, 300, 100, "NEW GAME", 'buttons/ok_button.png', 'buttons/hovered_button.png',
                             'sounds/click_sound.mp3', 70)
        quit_button = Button(425, 415, 150, 50, "QUIT", 'buttons/ok_button.png', 'buttons/hovered_button.png',
                             'sounds/click_sound.mp3', 50)

        running = True

        while running:
            screen.fill((0, 0, 0))
            screen.blit(main_menu_background, (0, 0))
            name_font = pygame.font.Font('buttons/shr.ttf', 100)
            text_surface = name_font.render("COOKING GAME !", True, (255, 150, 112))
            text_rect = text_surface.get_rect(center=(width / 2, 200))
            screen.blit(text_surface, text_rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.USEREVENT and event.button == play_button:
                    start_game()
                if event.type == pygame.USEREVENT and event.button == quit_button:
                    running = False

                for btn in [play_button, quit_button]:
                    btn.handle_event(event)

            for btn in [play_button, quit_button]:
                btn.update_btn(screen, pygame.mouse.get_pos())

            pygame.display.flip()
            clock.tick(60)
        pygame.quit()


    main_menu()
