import random
import os
import pygame
from sys import exit
import pyautogui

size = pyautogui.size()

WIDTH  , HEIGHT = size

WIDTH , HEIGHT = WIDTH * 8 / 10 , HEIGHT * 8 / 10

getting_number = True

score = 0

number = 0

game_over = False

tiles = []

block_lst = []

colors = {
    2 : "#eee4db",
    4 : "#f0e3d0",
    8 : "#f3b177",
    16 : "#ee9a66",
    32 : "#ff7c6b",
    64 : "#f4613b",
    128 : "#eccf7a",
    256 : "#eed666",
    512 : "#f1cc47"
}

class Tile:
    def __init__(self , x , y , value , id):
        self.x = x
        self.y = y
        self.value = value
        self.id = id
        
class Block:
    def __init__(self , x , y , unit , id):
        self.x = x
        self.y = y
        self.unit = unit
        self.value = 0
        self.id = id
    
def create_tile():
    id = 1 
    for i in range(1 , number + 1):
        for j in range(1 , number + 1):
            tiles.append(Tile(i , j , 0 , id))
            id += 1
            
def r(tiles):
    run = True
    while run:
        x = random.randint(1 , number + 1)
        y = random.randint(1 , number + 1)
        for tile in tiles:
            if tile.x == x and tile.y == y and tile.value == 0:
                tile.value = 2
                run = False
                break
    return tiles

def update(lst):
    
    for i in lst:
        for j in i:
            for tile in tiles:
                if tile.x == j.x and tile.y == j.y:
                    tile.value = j.value
                    break
    return tiles

def up(tiles):
    chagneed = False
    lst = []
    for i in range(1 , number +1):
        lst1 = []
        for j in range(1 , number + 1):
            for tile in tiles:
                if tile.x == i and tile.y == j:
                    lst1.append(tile)
        lst.append(lst1)
    
    for i in lst:
        for j in range(1 , len(i)):
            if i[j].value != 0:
                while i[j-1].value == 0:
                    i[j-1].value = i[j].value
                    i[j].value = 0
                    chagneed = True
                    if j > 1:
                        j-=1
                if i[j-1].value == i[j].value:
                    i[j-1].value += i[j].value
                    i[j].value = 0
                    chagneed = True
     
    return update(lst) , chagneed
    
def down(tiles):
    changeed = False
    lst = []
    for i in range(1 , number +1):
        lst1 = []
        for j in range(number , 0 , -1):
            for tile in tiles:
                if tile.x == i and tile.y == j:
                    lst1.append(tile)
        lst.append(lst1)
    
    for i in lst:
        for j in range(1 , len(i)):
            if i[j].value != 0:
                while i[j-1].value == 0:
                    i[j-1].value = i[j].value
                    i[j].value = 0
                    if j > 1:
                        changeed = True
                        j-=1
                if i[j-1].value == i[j].value:
                    i[j-1].value += i[j].value
                    i[j].value = 0
                    changeed = True
     
    return update(lst) , changeed
    
def right(tiles):
    changeed = False
    lst = []
    for i in range(1 , number +1):
        lst1 = []
        for j in range(number , 0 , -1):
            for tile in tiles:
                if tile.x == j and tile.y == i:
                    lst1.append(tile)
        lst.append(lst1)
    
    for i in lst:
        for j in range(1 , len(i)):
            if i[j].value != 0:
                while i[j-1].value == 0:
                    i[j-1].value = i[j].value
                    i[j].value = 0
                    changeed = True
                    if j > 1:
                        j-=1
                if i[j-1].value == i[j].value:
                    i[j-1].value += i[j].value
                    i[j].value = 0
                    changeed = True
     
    return update(lst) , changeed
                
def left(tiles):
    changeed = False
    lst = []
    for i in range(1 , number +1):
        lst1 = []
        for j in range(1 , number + 1):
            for tile in tiles:
                if tile.x == j and tile.y == i:
                    lst1.append(tile)
        lst.append(lst1)
    
    for i in lst:
        for j in range(1 , len(i)):
            if i[j].value != 0:
                while i[j-1].value == 0:
                    i[j-1].value = i[j].value
                    i[j].value = 0
                    changeed = True
                    if j > 1:
                        j-=1
                if i[j-1].value == i[j].value:
                    i[j-1].value += i[j].value
                    i[j].value = 0
                    changeed = True
     
    return update(lst) , changeed

def count_score():
    score = 0
    for tile in tiles:
        score += tile.value
    return score    

def check_end_game(tiles):
    for tile in tiles:
        if tile.value == 0:
            return False
    else:
        return True
def create_block(number):
    global block_lst
    id = 1
    unit = (HEIGHT -100) / (number + 1)
    edge = (WIDTH / 2) - (HEIGHT-100) / 2 
    edge2 = (HEIGHT / 2) - (HEIGHT-100) / 2
    block_lst = []
    for i in range(1 , number + 1):
        for j in range(1 , number + 1):
            block_lst.append(Block(i * unit + edge , j * unit + edge2  , unit , id))
            id += 1
        
def draw():
    global block_lst
    global tiles
    
    screen.blit(border_sur , border_sur_rect)
    
    
    for block in block_lst:
        b = pygame.Surface( (block.unit - 4 , block.unit - 4) )
        b.fill("#d0c2b9")
        b_rect = b.get_rect(center = (block.x , block.y))
        screen.blit(b , b_rect)
        for tile in tiles:
            if tile.id == block.id and tile.value != 0:
                b.fill(colors[tile.value])
                screen.blit(b , b_rect)
                
                text = pygame.font.Font(None , 30)
                text = text.render(f"{tile.value}" , "black" , True)
                text_rect = text.get_rect(center = (block.x , block.y))
                screen.blit(text , text_rect)
                break
                
                

pygame.init()
screen = pygame.display.set_mode( (WIDTH , HEIGHT) )
screen.fill("#fbf8f1")
pygame.display.set_caption("2048")
clock = pygame.time.Clock()

begin_text = pygame.font.Font(None , 40)
begin_text = begin_text.render("How big should the table be ?" , "black" , False)
begin_text_rect = begin_text.get_rect(center = (WIDTH / 2 , HEIGHT / 2 - 50))

sur = pygame.Surface( (100 , 30) )
sur.fill("white")
sur_rect = sur.get_rect(center = (WIDTH / 2 , HEIGHT / 2))

border_sur = pygame.Surface( (HEIGHT - 100 ,  HEIGHT - 100) )
border_sur.fill("#bbada2")
border_sur_rect = border_sur.get_rect(center = (WIDTH / 2 , HEIGHT / 2))


text = ""
changed = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if getting_number:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                if event.key == pygame.K_SPACE:
                    if 3 <= int(text) <= 6 :
                        number = int(text)
                        getting_number = False 
                        create_block(number) 

                else:
                    if event.unicode.isdigit():
                        text += str(event.unicode)
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    tiles , changed = up(tiles)
                if event.key == pygame.K_DOWN:
                    tiles , changed = down(tiles)
                if event.key == pygame.K_RIGHT:
                    tiles , changed = right(tiles)
                if event.key == pygame.K_LEFT:
                    tiles , changed = left(tiles)
    if getting_number:
        
        screen.blit(begin_text , begin_text_rect)
        screen.blit(sur , sur_rect)
        
        number_text = pygame.font.Font(None , 30)
        number_text = number_text.render(text , "black" , True)
        number_text_rect = number_text.get_rect(center = (WIDTH / 2 , HEIGHT / 2))
        screen.blit(number_text , number_text_rect)
    else:
        if not game_over:
            
            # print(len(tiles))
            if not tiles:
                create_tile()
            if check_end_game(tiles):
                game_over = True    
            if changed :
                tiles = r(tiles)
                changed = False

            if len(block_lst) != number * number:
                create_block()
            draw()
    pygame.display.update()
    clock.tick(60)