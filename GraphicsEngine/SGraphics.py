from math import floor
import os
import random
import pygame

class Object:
    def __init__(self,graphicsengine,speed=7,x=0,y=0,w=64,h=64,image="default.png"):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.velx = 0.0
        self.vely = 0.0
        self.graphics = graphicsengine
        if os.path.exists(image):
            self.image = pygame.transform.scale(pygame.image.load(image),(self.w,self.h))
        else:
            fake = pygame.Surface((self.w,self.h))
            fake.fill((0,0,0))
            self.image = pygame.transform.scale(fake,(self.w,self.h))
        self.speed = speed

    def render(self):
        self.image = pygame.transform.scale(self.image,(self.w,self.h))
        self.graphics.WIN.blit(self.image,(self.x,self.y))

class Player(Object):        
    def PacketHandler(self):
        keys = pygame.key.get_pressed()
        self.x+=self.velx
        self.y+=self.vely
        if self.velx > 0:
            self.velx-=0.5
        if self.velx < 0:
            self.velx+=0.5
        if self.vely > 0:
            self.vely-=0.5
        if self.vely < 0:
            self.vely+=0.5
        
        self.velx = max(-5.0, min(self.velx, 5.0))
        self.vely = max(-5.0, min(self.vely, 5.0))
        self.x = max(0, min(self.x, 900 - self.w))
        self.y = max(0, min(self.y, 500 - self.h))
        if keys[pygame.K_w]:
            self.vely -=self.speed
        if keys[pygame.K_s]:
            self.vely +=self.speed
        if keys[pygame.K_a]:
            self.velx -=self.speed
        if keys[pygame.K_d]:
            self.velx +=self.speed

class QuickRender():
    def __init__(self,x=80,y=40,text="",color=(0,0,0)):
        self.text = text
        self.color = color
        self.x = x
        self.y = y

def quickRender(text,x,y,color=(255,255,255)):
    return QuickRender(x=x,y=y,text=text,color=color)


class SGraphics:
    def __init__(self, WIN, clock, backgroundPath="background.png"): 
        self.WIN = WIN
        self.clock = clock
        self.objects = []
        self.quickrenders = []
        self.backgroundPath = backgroundPath
        if os.path.exists(backgroundPath):
            print("f")
            self.background = pygame.transform.scale(pygame.image.load(backgroundPath),(900,500))
        else:
            fake = pygame.Surface((900,500))
            fake.fill(self.randomcolor)
            self.background = pygame.transform.scale(fake,(900,500))

    def render(self):
        #self.randoma += random.randint(0,10)
        #self.randomb += random.randint(0,10)
        #self.randomc += random.randint(0,10)
        #if self.randoma > 255: self.randoma = 0
        #if self.randomb > 255: self.randomb = 0
        #if self.randomc > 255: self.randomc = 0
        #self.randomcolor = (self.randoma,self.randomb,self.randomc)
        self.WIN.blit(self.background,(0,0))
        font = pygame.font.Font(pygame.font.get_default_font(),16)

        for object in self.objects:
            object.render()
        for object in self.quickrenders:
            text = font.render(object.text,True,object.color)
            textRec = text.get_rect()
            textRec.center = object.x,object.y
            self.WIN.blit(text,textRec)

        self.quickrenders.clear()

        text = font.render('FPS: ' + str(floor(self.clock.get_fps())),True,(255,255,255))
        textRect = text.get_rect()
        textRect.center = 30,10

        self.WIN.blit(text,textRect)
        pygame.display.flip()
    
    
