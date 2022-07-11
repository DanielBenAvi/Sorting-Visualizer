import pygame
import random
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
PINK = (255,51,153)
BLUE = (0,102,204)
GREEN = (0,204,0)
font = pygame.font.SysFont('David', 25)
FPS = 1
clock = pygame.time.Clock()

WINDOW_WIDTH = 1280
WINDOW_HIGHT = 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HIGHT))
pygame.display.set_caption("pinki_sorting")


sort_flag = False

randomlist = random.sample(range(1, 21), 20)


    
def addRect(index, i ,j,rect_width,rect_hight,text):
    color = PINK if index == i else BLUE if index == j else WHITE
    pygame.draw.rect(display_surface, color, (index*rect_width, WINDOW_HIGHT-rect_hight, rect_width, rect_hight))
    # display_surface.blit(font.render(f'{text}', True, BLACK), (index*rect_width - rect_width//2 - 5 , WINDOW_HIGHT-30))



def NE():
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
       running = False



# main game loop
running = True
def is_sorted(lst) -> bool:
    for i in range(len(lst)-1):
        if (lst[i]>lst[i+1]):
            return False
    return True
   
def drawing_graph( display_surface, randomlist, rect_width, i, j):
    display_surface.fill(BLACK)
    for index,num in enumerate(randomlist):
        rect_hight = num*30
        addRect(index,i,j,rect_width,rect_hight,num)
        # pygame.draw.rect(display_surface, PINK if index == i else BLUE if index == j else WHITE, pygame.Rect(0+index*rect_width, WINDOW_HIGHT-rect_hight, rect_width, rect_hight))
    pygame.display.update()
    clock.tick(FPS)

while running:
    NE()
    is_sorted(randomlist)
    if not sort_flag:
        display_surface.fill(BLACK)
        rect_width = 1280//20
        for i in range(len(randomlist)):
            for j in range(len(randomlist)):
                if randomlist[i] < randomlist[j]:
                    temp = randomlist[i]
                    randomlist[i] = randomlist[j]
                    randomlist[j] = temp             
                    drawing_graph( display_surface, randomlist, rect_width, i, j)
                    
                if is_sorted(randomlist):
                    break
    


	

# end of game
pygame.quit()