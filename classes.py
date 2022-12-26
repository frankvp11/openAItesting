import pygame
pygame.font.init()
import time
text_font = pygame.font.Font("font.ttf", 16)
leftover = 0
class Button():
	def __init__(self, image, pos, text_input, font, base_color="green", hovering_color="blue"):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

class TextBox():
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x,y,w,h)
        self.color = (255, 255, 255)
        self.text = text
        self.txt_surface = text_font.render(text, True, self.color)
        self.txt_rect = self.txt_surface.get_rect()
    def update(self):
        # Re-render the text.
        self.txt_surface = text_font.render(self.text, True, self.color)
    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 10))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 1)


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = (255,255,255)
        self.text = text
        self.txt_surface = text_font.render(text, True, self.color)
        self.active = False
        self.score = 1
        # Cursor declare
        self.txt_rect = self.txt_surface.get_rect()
        self.cursor = pygame.Rect(self.txt_rect.topright, (3, self.txt_rect.height + 2))

    def handle_event(self, event, screen):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    global leftover
                    leftover += self.score
                    self.score = 0
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    try:
                        self.text = self.text[:-1]
                    except TypeError:
                        pass
                else:
                    try:
                        self.text += event.unicode
                    except TypeError:
                        pass
                    # Cursor

                    self.txt_rect.size = self.txt_surface.get_size()
                    self.cursor.topleft = self.txt_rect.topright

                    # Limit characters           -20 for border width
                    if self.txt_surface.get_width() > self.rect.w - 15:
                        self.text = self.text[:-1]

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 10))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 1)
        # Blit the  cursor
        if time.time() % 1 > 0.5:
            text_rect = self.txt_surface.get_rect(topleft = (self.rect.x + 5, self.rect.y + 10))

            # set cursor position
            self.cursor.midleft = text_rect.midright
            if self.active:
                pygame.draw.rect(screen, self.color, self.cursor)



    def update(self):
        # Re-render the text.
        self.txt_surface = text_font.render(self.text, True, self.color)

