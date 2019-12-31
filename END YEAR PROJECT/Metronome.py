import pygame, sys, time

pygame.init()
screen = pygame.display.set_mode((1120, 630))

class button():
    
    def __init__(self, colour, textcolour, xpos, ypos, bwidth, bheight, text= ''):
        self.colour = colour
        self.textcolour = textcolour
        self.xpos = xpos
        self.ypos = ypos
        self.bheight = bheight
        self.bwidth = bwidth
        self.text = text
    #button initialisation
    
    def bdraw(self, win, outline=None):
        if outline:
            pygame.draw.rect(screen, outline, (self.xpos-2, self.ypos-2, self.bwidth+4, self.bheight+4),0)
            #if desired, outline can be drawn
        pygame.draw.rect(screen, self.colour, (self.xpos, self.ypos, self.bwidth, self.bheight), 0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 40,)
            text = font.render(self.text, 1, self.textcolour)
            screen.blit(text, (self.xpos + (self.bwidth/2 - text.get_width()/2), self.ypos + (self.bheight/2 - text.get_height()/2)))
    
    def isOn(self, curpos):
        if curpos[0] > self.xpos and curpos[0] < self.xpos + self.bwidth:
            if curpos[1] > self.ypos and curpos[1] < self.ypos + self.bheight:
                return True
        return False
    
FONT = pygame.font.Font(None, 32)

class InputBox:

    def __init__(self, tx, ty, tw, th, text=''):
        self.rect = pygame.draw.rect(tx, ty, tw, th)
        self.color = ((49, 129, 40))
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def eventhandle(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.tw = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

beat44 = ['1', '2', '3', '4']
beat34 = ['1', '2', '3']
beat24 = ['1', '2']
beat14 = ['1']
button14 = button((81, 81, 81), black, 1000, 250, 100, 50, '1/4')
button24 = button((81, 81, 81), black, 1000, 310, 100, 50, '2/4')
button34 = button((81, 81, 81), black, 1000, 370, 100, 50, '3/4')
button44 = button((81, 81, 81), black, 1000, 430, 100, 50, '4/4')


run = True
while run:
    screen.fill(black)
    curpos = pygame.mouse.get_pos()
    button14.bdraw(screen)
    button24.bdraw(screen)
    button34.bdraw(screen)
    button44.bdraw(screen)
    disfont = pygame.font.SysFont('timesnewroman', 72)
    for event in pygame.event.get():
        #quitting
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
            quit()
            run = False
        #mouse over the buttons
        if event.type == pygame.MOUSEMOTION:
            #1/4 button
            if button14.isOn(curpos):
                button14.textcolour = (white)
                button14.colour = (65, 65, 65)
            else:
                button14.textcolour = (black)
                button14.colour = (81, 81, 81)
            #2/4 button
            if button24.isOn(curpos):
                button24.textcolour = (white)
                button24.colour = (65, 65, 65)
            else:
                button24.textcolour = (black)
                button24.colour = (81, 81, 81)
            #3/4 button
            if button34.isOn(curpos):
                button34.textcolour = (white)
                button34.colour = (65, 65, 65)
            else:
                button34.textcolour = (black)
                button34.colour = (81, 81, 81)
            #4/4 button
            if button44.isOn(curpos):
                button44.textcolour = (white)
                button44.colour = (65, 65, 65)
            else:
                button44.textcolour = (black)
                button14.colour = (81, 81, 81)
        #event of clicking
        if event.type == pygame.MOUSEBUTTONDOWN:
            #1/4 button
            if button14.isOn(curpos):
                button14.textcolour = (white)
                button14.colour = (65, 65, 65)
                print ('1/4 timing chosen')
                for i in beat14:
                    distext = disfont.render(i, 2, white)
                    screen.blit(distext, (200, 200))
                    pygame.display.update()
                    pygame.time.delay(3000)
                pygame.display.update()
            else:
                button14.textcolour = (black)
                button14.colour = (81, 81, 81)
            #2/4 button
            if button24.isOn(curpos):
                button24.textcolour = (white)
                button24.colour = (65, 65, 65)
                print ('2/4 timing chosen')
            else:
                button24.textcolour = (black)
                button24.colour = (81, 81, 81)
            #3/4 button
            if button34.isOn(curpos):
                button34.textcolour = (white)
                button34.colour = (65, 65, 65)
                print ('3/4 timing chosen')
            else:
                button34.textcolour = (black)
                button34.colour = (81, 81, 81)
            #4/4 button
            if button44.isOn(curpos):
                button44.textcolour = (white)
                button44.colour = (65, 65, 65)
                print ('4/4 timing chosen')
            else:
                button44.textcolour = (black)
                button14.colour = (81, 81, 81)
    pygame.display.update()
