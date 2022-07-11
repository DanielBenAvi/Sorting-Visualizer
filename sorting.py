import pygame
import random
from Button import Button
'''
    Pygame
'''
pygame.init()
clock = pygame.time.Clock()

'''
    Colors
'''
BLACK = (0,0,0)
WHITE = (255,255,255)
PINK = (255,51,153)
BLUE = (0,102,204)
GREEN = (0,204,0)

'''
    font
'''
ARIEL = pygame.font.SysFont('Ariel', 25)

'''
    Screen Setting
'''
FPS = 30
WINDOW_WIDTH = 1280
WINDOW_HIGHT = 720
DISPLAY = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HIGHT))
pygame.display.set_caption("Visual Sorting Algorithm")

'''
    Variables
'''
limit = 20
random_list = random.sample(range(1, limit+1), limit)
COLUMN_WIDTH = WINDOW_WIDTH//limit
running = True
sort_flag = False
switch = 'bubble'


'''
    Functions
'''
def is_sorted(lst) -> bool:
    for i in range(len(lst)-1):
        if (lst[i]>lst[i+1]):
            return False
    return True
   
def drawing_graph(x1, x2) -> None:
    DISPLAY.fill(BLACK)
    draw_all_buttons()
    for index,num in enumerate(random_list):
        rect_hight = num*(WINDOW_HIGHT-120)//limit
        addRect(index,x1,x2,rect_hight,num)
    update()

    

def addRect(index, x1 ,x2,rect_hight,text) -> None:
    color = BLUE if index == x1 else PINK if index == x2 else WHITE
    pygame.draw.rect(DISPLAY, color, (index*COLUMN_WIDTH, WINDOW_HIGHT-rect_hight, COLUMN_WIDTH, rect_hight))
    DISPLAY.blit(ARIEL.render(f'{text}', True, BLACK), (index*COLUMN_WIDTH + COLUMN_WIDTH//2 - 5 , WINDOW_HIGHT-20))

def finish() -> None:
    for index,num in enumerate(random_list):
        rect_hight = num*(WINDOW_HIGHT-120)//limit
        color = GREEN
        pygame.draw.rect(DISPLAY, color, (index*COLUMN_WIDTH, WINDOW_HIGHT-rect_hight, COLUMN_WIDTH, rect_hight))
        DISPLAY.blit(ARIEL.render(f'{num}', True, BLACK), (index*COLUMN_WIDTH + COLUMN_WIDTH//2 - 5 , WINDOW_HIGHT-20))
    update()


def bubble_sort(random_list):
    for i in range(len(random_list)):
        for j in range(len(random_list)-i-1):
            if random_list[j] > random_list[j+1]:
                drawing_graph(j, j+1)
                random_list[j], random_list[j+1] = random_list[j+1], random_list[j]         
                drawing_graph(j, j+1)
            if is_sorted(random_list):
                sort_flag = False
                finish()
                break

def draw_all_buttons():
    bubble_button.draw(DISPLAY)

def update():
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False  
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if bubble_button.isOver(pos):
                random_list = random.sample(range(1, limit+1), limit)
                sort_flag = False

                
        if event.type == pygame.MOUSEMOTION:
            if bubble_button.isOver(pos):
                bubble_button.color = BLUE
            else:
                bubble_button.color = PINK
        
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
    draw_all_buttons()
    pygame.display.update()
    clock.tick(FPS)

def reset():
    pass
'''
    Loop
'''
bubble_button = Button(GREEN,0,0,200,100,'Bubble Sort')
while running:
    is_sorted(random_list)
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False
    
    if not sort_flag:
        if switch == 'bubble':
            bubble_sort(random_list)
        elif switch == 'quick':
            pass
    


pygame.quit()