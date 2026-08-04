import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Rectangle")

def gameloop():
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.draw.rect(screen,(146,78,123), pygame.Rect(50,100,200,120))
        pygame.display.flip()

if __name__ == '__main__':
    gameloop()