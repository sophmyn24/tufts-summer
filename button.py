
import pygame, sys

class Button:
    def __init__(self, text, width, height, pos, clock, text_font, screen):
        #core attributes?
        self.pressed = False

        #what the button will look like
        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = "#475F77"

        #text inside button
        self.text_surf = text_font.render(text, True, "#FFFFFF")
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

        self.clicked = False  # by default

    def draw(self, screen):
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius = 12)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed == True:
                    print("click")
                    self.pressed = False
        return self.pressed

    def print_out(self):
        pass

# pygame.init()
# screen = pygame.display.set_mode((500, 500))
# pygame.display.set_caption("Menu")
# clock = pygame.time.Clock()
# text_font = pygame.font.Font(None, 30)
#
# button1 = Button("Click me", 200, 40,(200, 250))
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#
#     screen.fill("#DCDDD8")
#     button1.draw()
#
#     pygame.display.update()
#     clock.tick(60)