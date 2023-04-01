# import random, time
# autorun = False
# exit = False
# ast = 0
# autor = False
# ui = ""
# while not exit:
#     ast += 1
#     p1 = random.randint(1, 6)
#     p2 = random.randint(1, 6)
#     print("Число гравця 1:",p1,"\nЧисло гравця 2:", p2)
#     if p1 < p2:
#         print("ГРАВЕЦЬ 2 ВИГРАВ!!!!!")
#     elif p2 < p1:
#         print("ГРАВЕЦЬ 1 ВИГРАВ!!!!!")
#     elif p1 == p2:
#         print("НІЧИЯ!!!!")

#     if autor == True and ast%5 == 0:
#         ui = input("Продовжити гру (Y/N)? ")
#         if ui.upper() == "N":
#             exit = True
#         ui = input("Може ввімкнути/вимкнути автопродовження? (Y/N) ")
#         if ui.upper() == "Y":
#             autor = True
#         else:
#             autor = False
#         time.wait(1)
#     elif autor == False:
#         ui = input("Продовжити гру (Y/N)? ")
#         if ui.upper() == "N":
#             exit = True
#         ui = input("Може ввімкнути/вимкнути автопродовження? (Y/N) ")
#         if ui.upper() == "Y":
#             autor = True
#         else:
#             autor = False
import pygame
import os
import sys
import random
import time

# Define some colors
BLACK = (0, 0, 0)
WHITE = (225, 217, 209)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
FPS = 60
pygame.init()


class Ball(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(Ball, self).__init__()
        self.image = pygame.Surface((100, 100))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass


class p1(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(p1, self).__init__()
        print(os.path.join(os.getcwd(), os.path.join('resources', 'Red.png')))
        self.image = pygame.transform.scale(
            pygame.image.load("resources\Red.png"), (80, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.target_x = 0
        self.target_y = 250
        self.ay = False
        self.cycles = 1
        self.mc = 0
        self.moves = 0
    def update(self):
        global ch
        if ch == 1:
            self.rect.x += 120 / (FPS * 2) 
            if self.rect.x % 120 == 0:
                self.moves += 1
            if (self.moves >= self.mc):
                ch = 2


class p2(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(p2, self).__init__()
        self.image = self.image = pygame.transform.scale(
            pygame.image.load("resources\Blue.png"), (80, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.cycles = 1
        self.mc = 0
        self.moves = 0
    def update(self):
        global ch
        if ch == 2:
            self.rect.x += 120 / (FPS * 2) 
            if self.rect.x % 120 == 0:
                self.moves += 1
            if (self.moves >= self.mc):
                ch = 3


# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("By RemoteAccess01")

# Loop until the user clicks the close button.
done = False
ch = 1
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
all_sprites.add(Ball(0, 250))
all_sprites.add(Ball(120, 270))
all_sprites.add(Ball(240, 250))
all_sprites.add(Ball(360, 270))
all_sprites.add(Ball(480, 250))
all_sprites.add(Ball(600, 270))
all_sprites.add(Ball(0, 50))
all_sprites.add(Ball(120, 70))
all_sprites.add(Ball(240, 50))
all_sprites.add(Ball(360, 70))
all_sprites.add(Ball(480, 50))
all_sprites.add(Ball(600, 70))
pn1 = p1(0, 250)
pn2 = p2(0, 50)
all_sprites.add(pn1)
all_sprites.add(pn2)
move2 = random.randint(1, 6)
move1 = random.randint(1, 6)
pn1.mc = move1 
pn2.mc = move2
print(move1, move2)
GAME_FONT = pygame.freetype.Font("resources/font.ttf", 24)
# -------- Main Program Loop -----------
while not done:
 
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 0))
    
    all_sprites.update()
    all_sprites.draw(surface=screen)
    if (ch == 3):
        if pn1.mc > pn2.mc:
            GAME_FONT.render_to(screen, (40, 350), "Червоний виграв!", (0, 0, 0))
        if pn2.mc > pn1.mc:
            GAME_FONT.render_to(screen, (40, 350), "Синій виграв!", (0, 0, 0))
        else:
            
             GAME_FONT.render_to(screen, (40, 350), "Нічия!", (0, 0, 0))
    # or just `render_to` the target surface.
        
    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(FPS)

# Close the window and quit.
pygame.quit()
