import pygame
import sys
  
pygame.init()
  
clock = pygame.time.Clock()
  
screen = pygame.display.set_mode([600, 500])
  
base_font = pygame.font.Font(None, 32)

rects = [(200, 200, 140, 32), (200, 264, 140, 32), (200, 328,140,32)]
user_texts = {"name":"", "first_name":"", "siret":"", }


input_rect_name = pygame.Rect(rects[0])
input_rect_first_name = pygame.Rect(rects[1])
input_rect_siret = pygame.Rect(rects[2])
color_active = pygame.Color('lightskyblue3')
  
color_passive = pygame.Color('chartreuse4')
color = color_passive
  
active = [False, False, False]
  
while True:
    for event in pygame.event.get():
  
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
  
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 0<event.pos[0]<100 and 0<event.pos[1]<100:
                user_texts["name"]=''
            if input_rect_name.collidepoint(event.pos):
                active[0], active[1], active[2] = True, False, False
            elif input_rect_first_name.collidepoint(event.pos):
                active[0], active[1], active[2] = False, True, False
            elif input_rect_siret.collidepoint(event.pos):
                active[0], active[1], active[2] = False, False, True
            else:
                active[0], active[1], active[2] = False, False, False
  
        if event.type == pygame.KEYDOWN and active[0]:
            if event.key == pygame.K_BACKSPACE:
                user_texts["name"] = user_texts["name"][:-1]
        if event.type == pygame.KEYDOWN and active[1]:
            if event.key == pygame.K_BACKSPACE:
                user_texts["first_name"] = user_texts["first_name"][:-1]
        if event.type == pygame.KEYDOWN and active[2]:
            if event.key == pygame.K_BACKSPACE:
                user_texts["siret"] = user_texts["siret"][:-1]
  
            else:
                user_texts["name"] += event.unicode
      
    screen.fill((255, 255, 255))
          
    pygame.draw.rect(screen, color_active if active[0] else color_passive, input_rect_name)
    pygame.draw.rect(screen, color_active if active[1] else color_passive, input_rect_first_name)
    pygame.draw.rect(screen, color_active if active[2] else color_passive, input_rect_siret)
  
    text_surface_name = base_font.render(user_texts["name"], True, (255, 255, 255))
    text_surface_first_name = base_font.render(user_texts["first_name"], True, (255, 255, 255))
    text_surface_siret = base_font.render(user_texts["siret"], True, (255, 255, 255))
      
    screen.blit(text_surface_name, (input_rect_name.x+5, input_rect_name.y+5))
    screen.blit(text_surface_first_name, (input_rect_first_name.x+5, input_rect_first_name.y+5))
    screen.blit(text_surface_siret, (input_rect_siret.x+5, input_rect_siret.y+5))
      
    input_rect_name.w = max(100, text_surface_name.get_width()+10)
    input_rect_first_name.w = max(100, text_surface_first_name.get_width()+10)
    input_rect_siret.w = max(100, text_surface_siret.get_width()+10)
      
    pygame.display.flip()
      
    clock.tick(60)