import pygame
import random
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
PINK = (255,51,153)
BLUE = (0,102,204)
GREEN = (0,204,0)
font = pygame.font.SysFont('David', 25)
FPS = 15
clock = pygame.time.Clock()

WINDOW_WIDTH = 1280
WINDOW_HIGHT = 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HIGHT))
pygame.display.set_caption("Visual Sorting Algorithm")


sort_flag = False

randomlist = random.sample(range(1, 21), 20)


def is_sorted(lst) -> bool:
    for i in range(len(lst)-1):
        if (lst[i]>lst[i+1]):
            return False
    return True
   
def drawing_graph(display_surface, randomlist, rect_width, x1, x2):
    display_surface.fill(BLACK)
    for index,num in enumerate(randomlist):
        rect_hight = num*30
        addRect(index,x1,x2,rect_width,rect_hight,num)
    pygame.display.update()
    clock.tick(FPS)
    

def addRect(index, x1 ,x2,rect_width,rect_hight,text):
    color = BLUE if index == x1 else PINK if index == x2 else WHITE
    pygame.draw.rect(display_surface, color, (index*rect_width, WINDOW_HIGHT-rect_hight, rect_width, rect_hight))
    display_surface.blit(font.render(f'{text}', True, BLACK), (index*rect_width + rect_width//2 - 5 , WINDOW_HIGHT-30))

def Finish():
    display_surface.fill(BLACK)
    for index,num in enumerate(randomlist):
        rect_hight = num*30
        color = GREEN
        pygame.draw.rect(display_surface, color, (index*rect_width, WINDOW_HIGHT-rect_hight, rect_width, rect_hight))
        display_surface.blit(font.render(f'{num}', True, BLACK), (index*rect_width + rect_width//2 - 5 , WINDOW_HIGHT-30))
    pygame.display.update()
    clock.tick(FPS)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    is_sorted(randomlist)
    if not sort_flag:
        display_surface.fill(BLACK)
        rect_width = 1280//20
        for i in range(len(randomlist)):
            for j in range(len(randomlist)-i-1):
                if randomlist[j] > randomlist[j+1]:
                    drawing_graph(display_surface, randomlist, rect_width, j, j+1)
                    randomlist[j], randomlist[j+1] = randomlist[j+1], randomlist[j]         
                    drawing_graph(display_surface, randomlist, rect_width, j, j+1)
                    
                if is_sorted(randomlist):
                    Finish()
                    break
    


pygame.quit()