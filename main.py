#imports
import pygame
import os
from classes import Button
from pygametextboxinput import TextInputBox

#font stuff
def get_font(size): 
    return pygame.font.Font("font.ttf", size)
pygame.font.init()
font = pygame.font.Font("font.ttf", 16)
font2 = pygame.font.Font(pygame.font.match_font('Arial'), 14)


#initializing stuff
pygame.init()
pygame.scrap.init()
pygame.scrap.set_mode(pygame.SCRAP_CLIPBOARD)
screen = pygame.display.set_mode((1800, 1000))
pygame.display.set_caption("Menu")


promptBox = TextInputBox(50, 50, font_family="Arial" "Enter prompt here", max_width=1700, max_height=250)
clearButton = Button(None, (300,400), "Clear", font=get_font(20), base_color="white", hovering_color="green")


def main():
    while True:
        screen.fill("black") # always keep at top
        mouse_position = pygame.mouse.get_pos()
        clearButton.changeColor(mouse_position)
        clearButton.update(screen)

        events = pygame.event.get()

        for event in events:
            if (event.type == pygame.QUIT):
                pygame.quit()
            if (event.type == pygame.KEYDOWN):
                if event.key == pygame.K_v and event.mod & pygame.KMOD_CTRL:
                    pasted_text =  pygame.scrap.get("text/plain;charset=utf-8").decode()
                    #promptBox.text = promptBox.text[:-1]
                    #promptBox.text += pasted_text
                    if promptBox.max_string_length == -1 or len(promptBox.input_string) < promptBox.max_string_length:
                    # If no special key is pressed, add unicode of key to input_string
                        promptBox.input_string = (
                            promptBox.input_string[:promptBox.cursor_position]
                            + pasted_text
                            + promptBox.input_string[promptBox.cursor_position:]
                        )
                        promptBox.cursor_position += len(pasted_text)
                        
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if (clearButton.checkForInput(mouse_position)):
                    #promptBox.text = ""
                    pass


        promptBox.update(events)
        promptBox.render(screen)

        pygame.display.update()



main()