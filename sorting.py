import pygame
import random
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
button_lst = []
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
    for index,num in enumerate(random_list):
        rect_hight = num*(WINDOW_HIGHT-120)//limit
        addRect(index,x1,x2,rect_hight,num)
    pygame.display.update()
    clock.tick(FPS)
    

def addRect(index, x1 ,x2,rect_hight,text) -> None:
    color = BLUE if index == x1 else PINK if index == x2 else WHITE
    pygame.draw.rect(DISPLAY, color, (index*COLUMN_WIDTH, WINDOW_HIGHT-rect_hight, COLUMN_WIDTH, rect_hight))
    DISPLAY.blit(ARIEL.render(f'{text}', True, BLACK), (index*COLUMN_WIDTH + COLUMN_WIDTH//2 - 5 , WINDOW_HIGHT-20))

def Finish() -> None:
    DISPLAY.fill(BLACK)
    for index,num in enumerate(random_list):
        rect_hight = num*(WINDOW_HIGHT-120)//limit
        color = GREEN
        pygame.draw.rect(DISPLAY, color, (index*COLUMN_WIDTH, WINDOW_HIGHT-rect_hight, COLUMN_WIDTH, rect_hight))
        DISPLAY.blit(ARIEL.render(f'{num}', True, BLACK), (index*COLUMN_WIDTH + COLUMN_WIDTH//2 - 5 , WINDOW_HIGHT-20))
    pygame.display.update()
    clock.tick(FPS)


def bubble_sort(random_list):
    for i in range(len(random_list)):
        for j in range(len(random_list)-i-1):
            if random_list[j] > random_list[j+1]:
                drawing_graph(j, j+1)
                random_list[j], random_list[j+1] = random_list[j+1], random_list[j]         
                drawing_graph(j, j+1)
            if is_sorted(random_list):
                sort_flag = False
                Finish()
                break



'''
    Loop
'''
while running:
    DISPLAY.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    is_sorted(random_list)
    if not sort_flag:
        if switch == 'bubble':
            bubble_sort(random_list)
        elif switch == 'quick':
            pass
    


pygame.quit()