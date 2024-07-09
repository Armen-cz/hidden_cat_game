import pygame
from sys import exit
from time import time, sleep
from random import choice

# for the future



# Initialize Pygame
pygame.init()

# functions
def check_click(pos):
    for cat in range(len(cats_rect)):
        if cats_rect[cat].collidepoint(pos):
            return cat
    return None


# Set up display
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Find the Hidden Cats")
test_font_200 = pygame.font.SysFont("Pixeltype.ttf",200)
test_font_80 = pygame.font.SysFont("Pixeltype.ttf",90)
test_font_35 = pygame.font.SysFont("Pixeltype.ttf",35)

start_time = time()
timer_start = 0
# Load images
background_image = pygame.image.load("background_with_cats.png").convert()
the_end_image = pygame.image.load("THE_END_900.png").convert_alpha()
the_end_image_rect = the_end_image.get_rect(center = (screen_width/2, screen_height/2))
close_button_surf = pygame.image.load("close_button_400.png").convert_alpha()
close_button_rect = close_button_surf.get_rect(topright = (1900, 20))
close_button_pressed_surf = pygame.image.load("close_button_pressed_400.png").convert_alpha()
close_button_pressed_rect = close_button_pressed_surf.get_rect(topright = (1900, 20))
close_button_surf2 = pygame.image.load("close_button.png").convert_alpha()
close_button_rect2 = close_button_surf2.get_rect(topright = (1350,365))
close_button_pressed_surf2 = pygame.image.load("close_button_pressed.png").convert_alpha()
close_button_pressed_rect2 = close_button_pressed_surf2.get_rect(topright = (1350,365))
cat_button_surf = pygame.image.load("cat_icon_400.png").convert_alpha()
cat_button_rect = cat_button_surf.get_rect(topright = (1740, 20))
cat_button_pressed_surf = pygame.image.load("cat_icon_pressed_400.png").convert_alpha()
cat_button_pressed_rect = cat_button_pressed_surf.get_rect(topright = (1740, 20))
settings_button_surf = pygame.image.load("settings_icon_400.png").convert_alpha()
settings_button_rect = settings_button_surf.get_rect(topright = (1580, 20))
settings_button_pressed_surf = pygame.image.load("settings_icon_pressed_400.png").convert_alpha()
settings_button_pressed_rect = settings_button_pressed_surf.get_rect(topright = (1580, 20))
border_counter_surf = pygame.image.load("border.png").convert_alpha()
border_counter_rect = border_counter_surf.get_rect(midbottom = (screen_width/2,screen_height-20))
transparent_bg_surf = pygame.image.load("transparent_bg.png").convert_alpha()
tree_border_surf = pygame.image.load("tree_border.png").convert()
tree_border_rect = tree_border_surf.get_rect(center = (screen_width/2, screen_height/2))
box_checked_surf = pygame.image.load("box_checked.png").convert()
box_unchecked_surf = pygame.image.load("box_unchecked.png").convert()

"""if cat_colors_bool[step] is True:
    screen.blit(box_checked_surf, (738 + step * 138, 495))
else:
    screen.blit(box_unchecked_surf, (738 + step * 138, 495))
for step in range(4):
    if cat_colors_bool[step + 4] is True:
        screen.blit(box_checked_surf, (738 + step * 138, 665))
    else:
        screen.blit(box_unchecked_surf, (738 + step * 138, 665))"""

box_checked_rects = [pygame.Rect(738, 495,20,20),pygame.Rect(738+1*138, 495,20,20),pygame.Rect(738+2*138, 495,20,20),pygame.Rect(738+3*138, 495,20,20),pygame.Rect(738, 665,20,20),pygame.Rect(738+1*138, 665,20,20),pygame.Rect(738+2*138, 665,20,20),pygame.Rect(738+3*138, 665,20,20)]


cat_color = (190, 110, 255)
cat_colors = [(50, 150, 255, 255), (50, 50, 255, 255),(255, 60, 65, 255),(255, 140, 0, 255),(50, 250, 55, 255),(250, 150, 155, 255),(10, 155, 55, 255),(250, 150, 255, 255)]
cat_colors_bool = [True,False,False,False,False,False,False,False]
# load cats
cat_menu_border_surf = pygame.image.load("cat_border_300.png").convert_alpha()
cat_menu_self_surf = pygame.image.load("cat_to_border_300.png").convert_alpha()
cat_menu_self_surfaces = []
for step in range(8):
    cat_menu_self_surfaces.append(cat_menu_self_surf.copy())
for step in range(8):
    cat_menu_self_surfaces[step].fill(cat_colors[step],special_flags=pygame.BLEND_RGBA_MIN)

cat_menu_border_rect = cat_menu_border_surf.get_rect(center = (720,420))
notguessed_kocky_surf =  []
guessed_kocky_surf = []
for kocka in range(1,21):
    notguessed_kocky_surf.append(pygame.image.load(f"kocky/kocka{kocka}.png").convert_alpha())
for kocka in range(1,21):
    guessed_kocky_surf.append(pygame.image.load(f"kocky/kocka{kocka}.png").convert_alpha())
guessed_kocky_surf_white = guessed_kocky_surf.copy()
for kocka in guessed_kocky_surf:
    kocka.fill(cat_color, special_flags=pygame.BLEND_RGBA_MIN)
meow_sounds = []
for meow in range(1,11):
    meow_sounds.append(pygame.mixer.Sound(f"meow/meow{meow}.mp3"))
cat_number = "20"


back_arrow_button_surf = pygame.image.load("back_arrow_400.png").convert_alpha()
back_arrow_button_rect = back_arrow_button_surf.get_rect(topleft = (10, 10))
back_arrow_button_pressed_surf = pygame.image.load("back_arrow_pressed_400.png").convert_alpha()
back_arrow_button_pressed_rect = back_arrow_button_pressed_surf.get_rect(topleft = (10, 10))

# text sufraces
text_cat_number_surf = test_font_80.render("20", False, "Black")
text_cat_number_rect = text_cat_number_surf.get_rect(midbottom = (int(screen_width / 2+8), screen_height-17))
text_cat_game_surf = test_font_200.render("Sneaky Cats", False, "Black")
text_cat_game_rect = text_cat_game_surf.get_rect(center = (int(screen_width/2), int(screen_height/2)))
text_start_game_surf = test_font_80.render("Press space to start", False, "Black")
text_start_game_rect = text_start_game_surf.get_rect(center = (int(screen_width/2), screen_height-250))
text_start_speed_game_surf = test_font_80.render("Press S for Timer mode", False, "Black")
text_start_speed_game_rect = text_start_speed_game_surf.get_rect(center = (int(screen_width/2), screen_height-250))
text_cat_color_error_surf = test_font_80.render("Doesn't work and I am too lazy to fix this.", False, "White")
text_cat_color_error_rect = text_cat_color_error_surf.get_rect(center = (int(screen_width/2), screen_height-100))


#the_end_image = pygame.transform.rotozoom

# List of cat positions (x, y, width, height)
cats_rect = [
    pygame.Rect(1228, 487, 30, 13),
    pygame.Rect(1690, 759, 12, 30),
    pygame.Rect(1707, 990, 40, 28),
    pygame.Rect(586, 649, 22, 20),
    pygame.Rect(727, 872, 25, 30),
    pygame.Rect(417, 1030, 13, 16),
    pygame.Rect(54, 924, 46, 22),
    pygame.Rect(290, 570, 18, 21),
    pygame.Rect(1448, 131, 72, 70),
    pygame.Rect(159, 714, 14, 13),
    pygame.Rect(680, 339, 30, 70),
    pygame.Rect(826, 558, 24, 46),
    pygame.Rect(1072, 453, 26, 30),
    pygame.Rect(124, 504, 30, 18),
    pygame.Rect(1644, 502, 24, 32),
    pygame.Rect(280, 965, 30, 13),
    pygame.Rect(525, 780, 58, 17),
    pygame.Rect(877, 655, 23, 37),
    pygame.Rect(1210, 965, 22, 30),
    pygame.Rect(1503, 653, 26, 27)
]

# Game colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Main game loop
def main():
    found_cat_numbers = []
    game_active = False
    menu_active = True
    close_button_hovered = False
    cat_menu_active = False
    timer_mode = False
    settings_menu_active = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_active = False
                pygame.quit()
                exit()
            if menu_active:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        if close_button_rect.collidepoint(pygame.mouse.get_pos()):
                            pygame.quit()
                            exit()
                        elif cat_button_rect.collidepoint(pygame.mouse.get_pos()):
                            cat_menu_active = True
                            menu_active = False
                        elif settings_button_rect.collidepoint(pygame.mouse.get_pos()):
                            settings_menu_active = True
                            menu_active = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        timer_start = time()
                        game_active = True
                        menu_active = False
                    elif event.key == pygame.K_s:
                        found_cat_numbers.clear()
                        timer_start = time()
                        game_active = True
                        menu_active = False
                        timer_mode = True
            if game_active:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        if back_arrow_button_rect.collidepoint(pygame.mouse.get_pos()):
                            game_active = False
                            menu_active = True
                            if timer_mode:
                                print("found cat numbers")
                                found_cat_numbers.clear()
                            timer_mode = False
                    click_pos = pygame.mouse.get_pos()
                    clicked_cat = check_click(click_pos)
                    if clicked_cat is not None and clicked_cat not in found_cat_numbers:
                        found_cat_numbers.append(clicked_cat)
                        choice(meow_sounds).play()
            if cat_menu_active:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        if pygame.mouse.get_pressed()[0]:
                            if close_button_rect2.collidepoint(pygame.mouse.get_pos()):
                                cat_menu_active = False
                                menu_active = True
                        for step in range(8):
                            if box_checked_rects[step].collidepoint(pygame.mouse.get_pos()):
                                choice(meow_sounds).play()
                                for step2 in range(8):
                                    cat_colors_bool[step2] = False
                                cat_colors_bool[step] = True
            if settings_menu_active:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        if pygame.mouse.get_pressed()[0]:
                            if close_button_rect2.collidepoint(pygame.mouse.get_pos()):
                                settings_menu_active = False
                                menu_active = True



        # Draw everything
        if game_active:
            screen.fill(WHITE)
            screen.blit(background_image, (0, 0))
            screen.blit(border_counter_surf,border_counter_rect)
            cat_number = str(20 - len(found_cat_numbers))
            text_cat_number_surf = test_font_80.render(cat_number, False, "Black")
            screen.blit(text_cat_number_surf,text_cat_number_rect)
            if timer_mode:
                pygame.draw.rect(screen,"White",(1743, 20, 170, 100))
                timer = int(time() - timer_start)
                if timer < 60:
                    screen.blit(test_font_80.render(f"{timer}s", False, "Black"), (1800, 30))
                else:
                    minute = int(timer/60)
                    second = timer%60
                    screen.blit(test_font_80.render(f"{minute}m {second}s", False, "Black"), (1750, 30))
            for kocka in notguessed_kocky_surf:
                screen.blit(kocka, (0,0))
            if back_arrow_button_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(back_arrow_button_pressed_surf, back_arrow_button_pressed_rect)
            else:
                screen.blit(back_arrow_button_surf, back_arrow_button_rect)
            for kocka in found_cat_numbers:
                screen.blit(guessed_kocky_surf[kocka], (0,0))
            if len(found_cat_numbers) == len(cats_rect):
                screen.blit(the_end_image, the_end_image_rect)
                if timer_mode:
                    pygame.draw.rect(screen, (255, 255, 255, 100), (screen_width / 2 - 50, 100, 250, 100))
                    if timer < 60:
                        screen.blit(test_font_200.render(f"{timer}s", False, "Black"), (screen_width/2-50, 100))
                    else:
                        minute = int(timer / 60)
                        second = timer % 60
                        screen.blit(test_font_200.render(f"{minute}m {second}s", False, "Black"), (screen_width/2-50, 100))
                pygame.display.update()
                sleep(4)
                menu_active = True
                game_active = False
                found_cat_numbers.clear()
                timer_mode = False

        if menu_active:
            screen.fill(WHITE)
            screen.blit(text_cat_game_surf, text_cat_game_rect)
            if close_button_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(close_button_pressed_surf, close_button_pressed_rect)
            else:
                screen.blit(close_button_surf, close_button_rect)
            if cat_button_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(cat_button_pressed_surf, cat_button_pressed_rect)
            else:
                screen.blit(cat_button_surf, cat_button_rect)
            if settings_button_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(settings_button_pressed_surf,settings_button_pressed_rect)
            else:
                screen.blit(settings_button_surf, settings_button_rect)
            current_time = start_time-time()
            if int(current_time) % 2 == 0:
                screen.blit(text_start_game_surf, text_start_game_rect)
            if int(current_time) % 2 != 0:
                screen.blit(text_start_speed_game_surf, text_start_speed_game_rect)
        if cat_menu_active:
            screen.fill(WHITE)
            screen.blit(text_cat_game_surf, text_cat_game_rect)
            screen.blit(close_button_surf, close_button_rect)
            screen.blit(cat_button_pressed_surf, cat_button_pressed_rect)
            screen.blit(settings_button_surf, settings_button_rect)
            screen.blit(transparent_bg_surf, (0,0))
            screen.blit(tree_border_surf, tree_border_rect)
            screen.blit(text_cat_color_error_surf,text_cat_color_error_rect)
            for step in range(4):
                screen.blit(cat_menu_border_surf,(700+step*138,390))
                screen.blit(cat_menu_self_surfaces[step],(700+step*138,390))
            for step in range(4):
                screen.blit(cat_menu_border_surf, (700 + step * 138, 560))
                screen.blit(cat_menu_self_surfaces[step+4], (700 + step * 138, 560))
            for step in range(4):
                if cat_colors_bool[step] is True:
                    screen.blit(box_checked_surf, (738+step*138,495))
                else:
                    screen.blit(box_unchecked_surf, (738 + step * 138, 495))
            for step in range(4):
                if cat_colors_bool[step+4] is True:
                    screen.blit(box_checked_surf, (738+step*138,665))
                else:
                    screen.blit(box_unchecked_surf, (738 + step * 138, 665))
            if close_button_rect2.collidepoint(pygame.mouse.get_pos()):
                screen.blit(close_button_pressed_surf2, close_button_pressed_rect2)
            else:
                screen.blit(close_button_surf2, close_button_rect2)
        if settings_menu_active:
            screen.fill(WHITE)
            screen.blit(text_cat_game_surf, text_cat_game_rect)
            screen.blit(close_button_surf, close_button_rect)
            screen.blit(cat_button_surf, cat_button_rect)
            screen.blit(settings_button_pressed_surf, settings_button_pressed_rect)
            screen.blit(transparent_bg_surf, (0, 0))
            screen.blit(tree_border_surf, tree_border_rect)
            krok = 80
            screen.blit(test_font_35.render("Hi, I am developer of Sneaky cats.", False, "White"), (702, 302 + krok))
            screen.blit(test_font_35.render("This is an attempt of making a 'hidden cat game' genre", False, "White"),
                        (702, 342 + krok))
            screen.blit(test_font_35.render("withou any experience in pygame.", False, "White"), (702, 382 + krok))
            screen.blit(test_font_35.render("Yeah, and it only works with 1920x1080 display.", False, "White"),
                        (702, 422 + krok))
            screen.blit(test_font_35.render("lol", False, "White"), (702, 482 + krok))
            if close_button_rect2.collidepoint(pygame.mouse.get_pos()):
                screen.blit(close_button_pressed_surf2, close_button_pressed_rect2)
            else:
                screen.blit(close_button_surf2, close_button_rect2)
        pygame.display.flip()


if __name__ == "__main__":
    main()