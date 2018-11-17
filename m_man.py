import pygame
 

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
 
def draw_stick_figure(screen, x, y):
    
    pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)
 
    
    pygame.draw.line(screen, GREEN, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, GREEN, [5 + x, 17 + y], [x, 27 + y], 2)
 
    
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [5 + x, 7 + y], 2)
 
    
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)
 

pygame.init()
 

size = [700, 500]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Moving Man")
 

done = False
 

clock = pygame.time.Clock()
 

pygame.mouse.set_visible(0)
 

x_speed = 0
y_speed = 0
 

x_coord = 10
y_coord = 10
 
while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
 
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3
 
        
        elif event.type == pygame.KEYUP:
            
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
 
    
 
    
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed
 
    
    screen.fill(WHITE)
 
    draw_stick_figure(screen, x_coord, y_coord)
 
 
    
    pygame.display.flip()
 

    clock.tick(80)
 

pygame.quit()
