import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_rect = mole_image.get_rect(topleft=(0, 0))
        
        while running:
            clicked = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mole_rect.collidepoint(event.pos):
                        clicked = True
            
            if clicked:
                molerow = random.randrange(0, 16)
                molecol = random.randrange(0, 20)
                mole_rect = mole_image.get_rect(topleft=(molecol * 32, molerow * 32))
            
            screen.fill((47, 167, 247))
            screen.blit(mole_image, mole_rect)
            # Draw the grid
            for i in range(20):
                pygame.draw.line(screen, (252, 36, 3), ((i + 1) * 32, 0), ((i + 1) * 32, 512))
            for i in range(16):
                pygame.draw.line(screen, (252, 36, 3), (0, (i + 1) * 32), (640, (i + 1) * 32))    
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
