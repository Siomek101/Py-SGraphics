from math import floor
import os
from GraphicsEngine import SGraphics
import pygame

# Setting Variables
WIDTH,HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

FPS = 60


def Main():
    # Clock 
    clock = pygame.time.Clock()
    # Graphics Engine
    graphics = SGraphics.SGraphics(WIN,clock)

    run = True 

    # Creating Objects
    player = SGraphics.Player(graphicsengine=graphics,speed=3,image="player.png")
    object = SGraphics.Object(graphicsengine=graphics,speed=3,image="player.png",x=50,y=50)

    # Adding objects to render objects
    graphics.objects.append(object)
    graphics.objects.append(player)

    # Lasttick function for printing FPS
    lasttick = pygame.time.get_ticks()/1000

    # Initialization of Fonts and others
    pygame.init()
    
    # Game Loop
    while run:
        # Limiting FPS
        clock.tick(FPS)
        
        # Handling Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        # Handling Movement for Player
        player.PacketHandler()

        # Quickly rendering text.
        # IMPORTANT!!! quickRender() requires (text,x,y) 
        # but QuickRender() requires nothing
        graphics.quickrenders.append(SGraphics.quickRender("HELLO WORLD",80,40))
        # graphics.quickrenders.append(SGraphics.QuickRender("HELLO WORLD",80,40))

        # Rendering Graphics
        graphics.render()

        if floor(pygame.time.get_ticks()/1000) is not lasttick: 
            print(floor(clock.get_fps()))
            lasttick = floor(pygame.time.get_ticks()/1000)

        # Disabled loading image every second for optimization
        if floor(pygame.time.get_ticks()/1000) is not "disabled": 
            if os.path.exists(graphics.backgroundPath):
                try:
                    graphics.background = pygame.transform.scale(pygame.image.load(graphics.backgroundPath),(900,500))
                except:
                    pass
        
    # Quiting pygame after exit
    pygame.quit()

if __name__ == "__main__":
    Main()

