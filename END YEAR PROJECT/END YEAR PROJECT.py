#please make sure u read and not delete comments.all working codelines in "##" and all comments in "#"
import pygame
import sys
pygame.init()
size = (width, height) = (1280, 720)
black = (0, 0, 0)
white = (255, 255, 255)
screen = pygame.display.set_mode(size)
colour = ()
textcolour = ()



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
 #button class declared  
def winredraw(item):
    item.bdraw(screen)


        
bands = pygame.image.load("Bands.png")
##drum1 = pygame.image.load("Drum Kit.jpg")
##drum1rect = drum1.get_rect()
##drum2 = pygame.image.load('Drum.jpg')
##guit1 = pygame.image.load('Guitar.jpg')
pygame.display.set_caption('Application')
bandsrect = bands.get_rect()
screen.fill(black)
##startbutton = button((27, 44, 54), (67, 85, 99), 0, 550, 180, 90, 'START') #initialising start button


while True:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
            quit()
            break
        curpos = pygame.mouse.get_pos()
        if evt.type == pygame.MOUSEMOTION:
            screen.blit(bands, bandsrect)
##            pygame.mixer.music.load("Pistol Shot.mp3")
##            pygame.mixer.music.play(0)
 #all working codelines in "##" and all comments in "#"         
            # after opening screen
#interaction begins. Menu screen
##            screen.blit(drum1, drum1rect)
##            winredraw()
##            if startbutton.isOn(curpos):
##                startbutton.textcolour = (194, 212, 216)
##                startbutton.colour = (154, 171, 181)
##            else:
##                startbutton.textcolour = (67, 85, 99)
##                startbutton.colour = (27, 44, 54)
##        if evt.type == pygame.MOUSEBUTTONDOWN:
##            if startbutton.isOn(curpos):
##                print ('Starting App')
##                screen.fill(black)
##                del startbutton
##                drum2rect = drum2.get_rect()
##                guit1rect = guit1.get_rect()
##                screen.blit(drum2rect, guit1rect)
##                gbutton = button((37, 48, 64), (77, 95, 89), 0, 550, 180, 90, 'GUITAR')
##                gbutton.bdraw(screen)
##                dbutton = button((37, 48, 64), (77, 95, 89), 560, 550, 180, 90, 'DRUMS')
##                dbutton.bdraw(screen)
##            pygame.display.flip()
    pygame.display.flip()

