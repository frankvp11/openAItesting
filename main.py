#imports
import pygame
import os
from classes import Button, TextBox
from pygametextboxinput import TextInputBox
import openai 
openai.api_key = "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"

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


promptBox = TextInputBox(50, 50, font_family="Arial" "Enter prompt here", max_width=1650, max_height=250)
clearButton = Button(None, (1700, 30), "Clear", font=get_font(20), base_color="white", hovering_color="green")
postButton = Button(None, (1700, 100), "Post", font=get_font(20), base_color="white", hovering_color="green")
aiOutput = TextInputBox(50, 500, font_family="Arial" "", max_width=1650, max_height=500)

def post_to_ai(text):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=text,
        temperature=0.7,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=0.1,
        presence_penalty=0.1
    )
    return response


def main():

    while True:
        screen.fill("black") # always keep at top
        mouse_position = pygame.mouse.get_pos()
        clearButton.changeColor(mouse_position)
        clearButton.update(screen)
        postButton.changeColor(mouse_position)
        postButton.update(screen)
        events = pygame.event.get()

        for event in events:
            if (event.type == pygame.QUIT):
                pygame.quit()
            if (event.type == pygame.KEYDOWN):
                if event.key == pygame.K_v and event.mod & pygame.KMOD_CTRL:
                    pasted_text =  pygame.scrap.get("text/plain;charset=utf-8").decode()

                    if promptBox.max_string_length == -1 or len(promptBox.input_string) < promptBox.max_string_length:
                        promptBox.input_string = (
                            promptBox.input_string[:promptBox.cursor_position]
                            + pasted_text
                            + promptBox.input_string[promptBox.cursor_position-1:]
                        )
                        promptBox.cursor_position += len(pasted_text)
                        
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if (clearButton.checkForInput(mouse_position)):
                    promptBox.input_string = ""
                    promptBox.cursor_position = 0
                if (postButton.checkForInput(mouse_position)):
                    output_text = post_to_ai(promptBox.input_string)
                    print(output_text)
                    aiOutput.set_text(output_text["choices"][0]["text"])
                    
#Write an essay about Jungian Psychology
        aiOutput.render(screen)     
        aiOutput.update(events, False)   
        promptBox.update(events)
        promptBox.render(screen)


        pygame.display.update()



main()