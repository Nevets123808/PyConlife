import pygame
from Grid import Grid

def main():
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720

    #Menu will always be full height of the Screen
    MENU_WIDTH = 250

    #This is Cells not pixels
    BOARD_WIDTH = 72
    BOARD_HEIGHT = 48

    
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    
    main_surf = pygame.Surface((SCREEN_WIDTH-MENU_WIDTH, SCREEN_HEIGHT))
    grid = Grid(BOARD_WIDTH, BOARD_HEIGHT, (SCREEN_WIDTH-MENU_WIDTH)//BOARD_WIDTH, (SCREEN_HEIGHT)//BOARD_HEIGHT, 'Green', 'Black')
    FPS = 10
    
    while running:
        #This handles the window closing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_0]:
            FPS = 20
        if keys[pygame.K_1]:
            FPS = 2
        if keys[pygame.K_2]:
            FPS = 4
        if keys[pygame.K_3]:
            FPS = 6
        if keys[pygame.K_4]:
            FPS = 8
        if keys[pygame.K_5]:
            FPS = 10
        if keys[pygame.K_6]:
            FPS = 12
        if keys[pygame.K_7]:
            FPS = 14
        if keys[pygame.K_8]:
            FPS = 16
        if keys[pygame.K_9]:
            FPS = 18
        if keys[pygame.K_r]:
            grid = Grid(BOARD_WIDTH, BOARD_HEIGHT, 10, 10, 'Green', 'Black')
        if keys[pygame.K_ESCAPE]:
            running=False
        #grid.step()
        #print(grid)
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")
        grid.update([])
        grid.draw(main_surf)
        screen.blit(main_surf, (250, 0))
        pygame.display.flip()
        clock.tick(FPS)
        
    pygame.quit()
    
if __name__ == "__main__":
    main()