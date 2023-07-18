import pygame
from pygame import time
from pygame import mouse
from pygame import font

def main():
    pygame.init()
    screen = pygame.display.set_mode((890, 880))
    clock = pygame.time.Clock()
    title_image = pygame.image.load("finalhope.png")

    running = True
    while running:
        #title screen
        screen.blit(title_image, (0, 0))
        pygame.display.update()
        start_music()
        #check if music has played for 5 seconds
        time.delay(9500)
        if time.get_ticks() >= 9500:
            stop_music()
            screen.fill("pink")
            pygame.display.update()
        #check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

#appearance
displaysurface = pygame.display.set_mode((400,300))
color_dark = (100, 100, 100)
pygame.draw.rect(displaysurface, color_dark, [590, 315, 80, 30])

#adding text
font.init()
smallfont = pygame.font.SysFont('Corbel', 16)
text = smallfont.render('LOAD', True, 'pink')
displaysurface.blit(smallfont, (600, 320))

#making interactable
mouse = mouse.get_pos()

while True:
    for event in pygame.event.get():
        # For events that occur upon clicking the mouse (left click)
        if event.type == pygame.MOUSEBUTTONDOWN:
              if 590 <= mouse[0] <= 670 and 315 <= mouse[1] <= 345:
                    event_handler.load()