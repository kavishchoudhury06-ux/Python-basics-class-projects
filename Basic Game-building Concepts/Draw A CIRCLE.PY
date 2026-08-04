import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Rectangle")
screen.fill((255,255,255))
pygame.draw.circle(screen,(146,78,123), (100,100),50)
pygame.draw.circle(screen,(146,78,123), (300,300),50,5)
pygame.display.update()

def gameloop():
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    

if __name__ == '__main__':
    gameloop()