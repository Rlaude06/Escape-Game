import pygame, sys
from positions import *
from pygame.locals import *



def main () :
    pygame.init()
 
    FPS = 60
    fpsClock = pygame.time.Clock()
    
    
    WINDOW_WIDTH, WINDOW_HEIGHT = 1240, 720 #pygame.display.list_modes()[0]
    WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Escape Game!')
    
    
    background = pygame.image.load('background.png').convert()
    background = pygame.transform.smoothscale(background, WINDOW.get_size())
    
    
    
    
    def draw_background():
        WINDOW.blit(background, (0, 0))
    
    def draw_post_it():
        return None

    def open_menu():
        exec(open("text.py").read())
        return True

    
    def get_fun(i):
        funs = [draw_post_it, open_menu]
        return funs[i]
    
    looping = True
  
    while looping :
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
          
            if event.type == pygame.MOUSEBUTTONDOWN:
                if check_click(*event.pos)!=False:
                    print("-")
                    print(get_fun(check_click(*event.pos))())
        
        draw_background()
    

        pygame.display.update()
        fpsClock.tick(FPS)
 
if __name__ == '__main__':
    main()