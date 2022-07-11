import pygame
import random
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
FPS = 15 
WINDOW_WIDTH = 1280
WINDOW_HIGHT = 720
DISPLAY = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HIGHT))
pygame.display.set_caption("Visual Sorting Algorithm")

'''
    Variables
'''
button_lst = []
sort_flag = False
randomlist = random.sample(range(1, 21), 20)
COLUMN_WIDTH = 1280//20
 


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
    for index,num in enumerate(randomlist):
        rect_hight = num*30
        addRect(index,x1,x2,rect_hight,num)
    pygame.display.update()
    clock.tick(FPS)
    

def addRect(index, x1 ,x2,rect_hight,text) -> None:
    color = BLUE if index == x1 else PINK if index == x2 else WHITE
    pygame.draw.rect(DISPLAY, color, (index*COLUMN_WIDTH, WINDOW_HIGHT-rect_hight, COLUMN_WIDTH, rect_hight))
    DISPLAY.blit(ARIEL.render(f'{text}', True, BLACK), (index*COLUMN_WIDTH + COLUMN_WIDTH//2 - 5 , WINDOW_HIGHT-25))

def Finish() -> None:
    DISPLAY.fill(BLACK)
    for index,num in enumerate(randomlist):
        rect_hight = num*30
        color = GREEN
        pygame.draw.rect(DISPLAY, color, (index*COLUMN_WIDTH, WINDOW_HIGHT-rect_hight, COLUMN_WIDTH, rect_hight))
        DISPLAY.blit(ARIEL.render(f'{num}', True, BLACK), (index*COLUMN_WIDTH + COLUMN_WIDTH//2 - 5 , WINDOW_HIGHT-25))
    pygame.display.update()
    clock.tick(FPS)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    is_sorted(randomlist)
    if not sort_flag:
        DISPLAY.fill(BLACK)
        for i in range(len(randomlist)):
            for j in range(len(randomlist)-i-1):
                if randomlist[j] > randomlist[j+1]:
                    drawing_graph(j, j+1)
                    randomlist[j], randomlist[j+1] = randomlist[j+1], randomlist[j]         
                    drawing_graph(j, j+1)
                    
                if is_sorted(randomlist):
                    sort_flag = False
                    Finish()
                    break
    


pygame.quit()