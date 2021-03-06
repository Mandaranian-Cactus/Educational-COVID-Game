from pygame import *
from Boy import *
from Girl import *
from BoyAI import *
from GirlAI import *
import pygame
import sys
import random


class Window:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.screen = pygame.display.set_mode((self.w, self.h))

    def fill(self):
        self.screen.fill((200, 222, 255))

screen = Window(800, 800)

class ProximityGame:
    def __init__(self):
        self.background = pygame.image.load("Assets/lockers.png")
        self.background = pygame.transform.scale(self.background, (screen.w, screen.h))
        self.p = Boy(100, 700, [[0 for x in range(3)] for y in range(4)], screen.screen)
        self.otherP = []
        for i in range(7):
            self.otherP.append(BoyAI(4 * random.randrange(screen.w//4), 4 * random.randrange(75, screen.h//4), [[0 for x in range(3)] for y in range(4)],
                                 4 * random.randrange(screen.w//4), 4 * random.randrange(75, screen.h//4),4 * random.randrange(screen.w//4), 4 * random.randrange(75, screen.h//4)))
            self.otherP.append(BoyAI(0, 500, [[0 for x in range(3)] for y in range(4)], screen.w, 500, 0, 500))

    def checkCollision(self, p1, p2):
        if p1.x_pos > p2.x_pos and p1.x_pos < p2.x_pos + 72 and p1.y_pos > p2.y_pos and p1.y_pos < p2.y_pos + 72:
            p1.x_pos = 100
            p1.y_pos = 700
        elif p2.x_pos > p1.x_pos and p2.x_pos < p1.x_pos + 72 and p2.y_pos > p1.y_pos and p2.y_pos < p1.y_pos + 72:
            p1.x_pos = 100
            p1.y_pos = 700

    def update(self):
        # print(self.p)
        self.p.update()

    def draw(self):

        screen.screen.blit(self.background,(0,0,screen.w,screen.h))

        hallwayFont = font.SysFont("Comic Sans MS", 48)
        hallwayTitle = "Make it to the door and avoid the students!"
        hallwayText = hallwayFont.render(hallwayTitle, True, (255,255,255))
        screen.screen.blit(hallwayText, (40,0))
        
        self.p.moveBoy(self.p)
        self.p.drawBoy()
        self.p.x_pos = min(max(35, self.p.x_pos), 800 - 35)
        self.p.y_pos = min(max(350, self.p.y_pos), 800 - 35)


        if self.p.x_pos > 589 and self.p.x_pos < 762 and self.p.y_pos > 337 and self.p.y_pos < 422:
            return "Break"

        for other in self.otherP:
            self.checkCollision(self.p, other)
            other.drawBoyAI()
            if other.moveBoy(other.targetX, other.targetY) == "Turn":
                if other.targetX == other.endX and other.targetY == other.endY:
                    other.targetX = other.startX
                    other.targetY = other.startY
                else:
                    other.targetX = other.endX
                    other.targetY = other.endY
