import pygame
import sys
import random

pygame.init()

WIDTH = 600
HEIGHT = 700
IMAGE_SIZE = WIDTH // 3
mouse_pos_x = 0
mouse_pos_y = 0
blank_position = (2,2)
BL = False
game_started = False
COLOR = (0, 123, 123)
WHITE = (255, 255, 255)

text_win = "You Win!"
MyFontWin = pygame.font.SysFont("8-Bit-Madness", 100)
label_win = MyFontWin.render(text_win, 1, WHITE)
win = False



screen = pygame.display.set_mode((WIDTH, HEIGHT))
run = True
fps = pygame.time.Clock()
background = pygame.image.load('bckgrnd.png')
dark_square = pygame.image.load('dark_sqare.png')



images = [pygame.image.load('image_part_001.jpg'), pygame.image.load('image_part_002.jpg'), pygame.image.load('image_part_003.jpg'), pygame.image.load('image_part_004.jpg')
          , pygame.image.load('image_part_005.jpg'), pygame.image.load('image_part_006.jpg'), pygame.image.load('image_part_007.jpg'), pygame.image.load('image_part_008.jpg')]


class Image(object):

    def __init__(self, position):
        self.image = images[position]
        self.posx = (position%3)
        self.posy = (position//3)


    def draw(self):
        if not ((img.posx, img.posy) == blank_position):
            screen.blit(self.image, (self.posx * IMAGE_SIZE, self.posy * IMAGE_SIZE))

    def move(self):
        global blank_position
        if blank_position == (self.posx + 1, self.posy):
            blank_position = self.posx, self.posy
            self.posx, self.posy = self.posx + 1, self.posy
        elif blank_position == (self.posx -1, self.posy):
            blank_position = self.posx, self.posy
            self.posx, self.posy = self.posx -1, self.posy
        elif blank_position == (self.posx, self.posy+1):
            blank_position = self.posx, self.posy
            self.posx, self.posy = self.posx , self.posy + 1
        elif blank_position == (self.posx, self.posy-1):
            blank_position = self.posx, self.posy
            self.posx, self.posy = self.posx, self.posy-1

        return blank_position



def mouseAction(mouse_pos_x, mouse_pos_y, BL):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        (mouse_pos_x, mouse_pos_y) = pygame.mouse.get_pos()
        (BL, BM, BR) = pygame.mouse.get_pressed()
    return(mouse_pos_x, mouse_pos_y, BL)

imgs = [ Image(0), Image(1), Image(2), Image(3), Image(4), Image(5), Image(6), Image(7)]

def randomStart():


    global imgs
    r = random.randint(20,30)
    if r % 2:
        r+=1
    for i in range(r):
        k = random.randint(0,3)
        j = random.randint(4,7)
        temp2 = (imgs[k].posx, imgs[k].posy)
        (imgs[k].posx, imgs[k].posy) = (imgs[j].posx, imgs[j].posy)
        (imgs[j].posx, imgs[j].posy) = temp2


def winf():
    global win
    if not game_started:
        return False
    else:
        win = True
        for i in range(8):
            position = imgs[i].posy * 3 + imgs[i].posx
            if not (position == i):
                win = False






while(run):



    
    pygame.draw.rect(screen, COLOR, ( (0,600) , (600, 100)) )
    screen.blit(dark_square, (blank_position[0]*IMAGE_SIZE, blank_position[1]*IMAGE_SIZE))
    for img in imgs:
        if not ((img.posx, img.posy) == blank_position):
            img.draw()

    mouse_pos_x, mouse_pos_y, BL = mouseAction(mouse_pos_x, mouse_pos_y, BL)

    if BL:
        if mouse_pos_y < 600:
            posx1 = mouse_pos_x // 200
            posy1 = mouse_pos_y // 200
            for img in imgs:
                if (posx1, posy1) == (img.posx, img.posy):
                    if not win:
                        img.move()
        else:
            randomStart()
            game_started = True
    
    winf()
    if win:
        screen.blit(label_win, (170, 250))

    fps.tick(30)
    pygame.display.update()


