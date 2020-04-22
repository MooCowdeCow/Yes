import pygame
import random
from settings import *
import sprites2
from pygame.sprite import Sprite

class Player(Sprite):
    # sprite for player
    # properties of the class
    def __init__(self):
        Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill(GREEN)
        '''sets image path to correct location joining image folder to file name then converting to a more efficient format'''
        # self.image = pygame.image.load(os.path.join(img_folder, "Tie.png")).convert()
        '''sets transparent color key to black'''
        # self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        # self.screen_rect = screen.get_rect()
        self.vx = 0
        self.vy = 0
        self.cofric = 2
    # stuff it can do....
    def friction(self):
        # print("friction...")
        # if self.vx > -0.5 or self.vx < 0.5:
        #     print("velocity is in range...")
        #     self.vx = 0
        if self.vx > 2:
            self.vx -= self.cofric
        elif self.vx < -2:
            self.vx += self.cofric
        else:
            self.vx = 0
        if self.vy > 2:
            self.vy -= self.cofric
        elif self.vy < -2:
            self.vy += self.cofric
        else:
            self.vy = 0
    def update(self):
        # print(self.vx)
        self.friction()
        # self.vy += 9.8
        self.rect.x += self.vx
        self.rect.y += self.vy
        # print(self.vx)
        # if self.rect.right > WIDTH:
        #     self.rect.x = -50
        #     print("running off screen")
        # if self.rect.top > 500:
        #     self.vy = -5
        # if self.rect.top < 100:
        #     self.vy = 5
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.vy -= 3
        if keystate[pygame.K_a]:
            self.vx -= 3
        if keystate[pygame.K_s]:
            self.vy += 3
        if keystate[pygame.K_d]:
            self.vx += 3
        # if keystate[pygame.K_SPACE]:
        #     self.shoot()
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.vx = 0

            # print("touched the right side...")
        if self.rect.left < 0:
            self.rect.left = 0
            self.vx = 0
            # print("touched the left side...")
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.vy = 0
            # print("touched the bottom")
        if self.rect.top < 0:
            self.rect.top = 0
            self.vy = 0
            # print("touched the top")
    def jump(self):
        print("I jumped...")

# init pygame and create window
pygame.init()
# init sound mixer
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A game that doesn't work")
clock = pygame.time.Clock() 

all_sprites = pygame.sprite.Group()
player = Player()
# player2 = Player()
testSprite = Sprite()
testSprite.image = pygame.Surface((50,50))
testSprite.image.fill(GREEN)
testSprite.rect = testSprite.image.get_rect()
testSprite.rect.center = (WIDTH / 2, HEIGHT / 2)
# all_sprites.add(player)
# all_sprites.add(player2)
# all_sprites.add(testSprite)

for i in range(0,1):
    i = Player()
    i.rect[0] = random.randint(0,WIDTH)
    i.rect[1] = random.randint(0,HEIGHT)
    all_sprites.add(i)

class Enemy(Sprite):
    # sprite for enemy
    # properties of the class
    def __init__(self):
        Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill(BLACK)
        '''sets image path to correct location joining image folder to file name then converting to a more efficient format'''
        # self.image = pygame.image.load(os.path.join(img_folder, "Tie.png")).convert()
        '''sets transparent color key to black'''
        # self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        # self.screen_rect = screen.get_rect()
        self.vx = 10
        self.vy = 0
        self.cofric = 0
    # stuff it can do....
    def friction(self):
        # print("friction...")
        # if self.vx > -0.5 or self.vx < 0.5:
        #     print("velocity is in range...")
        #     self.vx = 0
        if self.vx > 0.5:
            self.vx -= self.cofric
        elif self.vx < -0.5:
            self.vx += self.cofric
        else:
            self.vx = 0
        # if self.vy > 0.5:
        #     self.vy -= self.cofric
        # # elif self.vy < -0.5:
        # #     self.vy += self.cofric
        # else:
        self.vy = 0
    def update(self):
        # print(self.vx)
        self.friction()
        # self.vy += 9.8
        self.rect.x += self.vx
        self.rect.y += self.vy
        # print(self.vx)
        if self.rect.right > WIDTH:
            self.rect.x = -50
        #     print("running off screen")
        if self.rect.top > 500:
            self.vy = -5
        if self.rect.top < 100:
            self.vy = 5
        # if keystate[pygame.K_SPACE]:
        #     self.shoot()
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.vx = 10
            # print("touched the right side...")
        if self.rect.left < 0:
            self.rect.left = 0
            self.vx = 10
            # print("touched the left side...")
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.vy = 0
            # print("touched the bottom")
        if self.rect.top < 0:
            self.rect.top = 0
            self.vy = 0
            # print("touched the top")
    def jump(self):
        print("I jumped...")
