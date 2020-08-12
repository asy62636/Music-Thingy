import pygame
import time
import sys
pygame.init()
win=pygame.display.set_mode((1000,800))
win.fill((105,89,205))
background_image= pygame.image.load("images1.jpg").convert()
backgroundimage1=pygame.image.load("BANDSFINAL.jpg").convert()
backgroundimage2=pygame.image.load("guitarposter.jpg").convert()
backgroundimage3=pygame.image.load("animalsasleaders.jpg").convert()
pygame.mixer.music.load("BURN.mp3")


class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 24)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isover(self, pos):
        
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False
def redrawwindow():
    
    win.fill((105,89,205))
    win.blit(background_image,[0,0])
    METRONOMEbutton.draw(win,(255,255,255))
    CHORDSbutton.draw(win,(255,255,255))
    SONGSbutton.draw(win,(255,255,255))
def redrawsongswindow():
    
    win.fill((65,105,225))
    win.blit(backgroundimage2,[0,0])
    SONG1button.draw(win)
    SONG2button.draw(win)
    SONG3button.draw(win)
    SONG4button.draw(win)
    SONG5button.draw(win)
    SONG6button.draw(win)
    SONG7button.draw(win)
    SONG8button.draw(win)
    SONG9button.draw(win)
    SONG10button.draw(win)
    returnbutton.draw(win)
def redrawwindow1():
    
    win.fill((105,89,205))
    win.blit(backgroundimage1,[0,0])
def finalwindow():
    
    win.fill((255,255,255))
    win.blit(x,[10,10])
    finalreturnbutton.draw(win)
def chordwindow():
    win.fill((0,0,0))
    win.blit(backgroundimage3,[0,0])
    CHORD1button.draw(win)
    CHORD2button.draw(win)
    CHORD3button.draw(win)
    CHORD4button.draw(win)
    CHORD5button.draw(win)
    CHORD6button.draw(win)
    CHORD7button.draw(win)
    CHORD8button.draw(win)
    CHORD9button.draw(win)
    CHORD10button.draw(win)
    CHORD11button.draw(win)
    CHORD12button.draw(win)
    returnchordbutton.draw(win)
def chords():
    win.fill((0,0,0))
    win.blit(backgroundimage3,[0,0])
    MAJORbutton.draw(win)
    MINORbutton.draw(win)
    POWERbutton.draw(win)
    SUS2button.draw(win)
    SUS4button.draw(win)
    returnchordsbutton.draw(win)

    
run=True
METRONOMEbutton=button((0,191,255),400,100,250,100,"METRONOME")
CHORDSbutton=button((0,191,255),400,250,250,100,"CH0RDS")
SONGSbutton=button((0,191,255),400,400,250,100,"SONGS")
SONG1button=button((0,191,255),10,10,150,100,"PARADISE CITY")
SONG2button=button((0,191,255),220,10,150,100,"ROCK AND ROLL")
SONG3button=button((0,191,255),420,10,150,100,"COME AS YOU ARE")
SONG4button=button((0,191,255),620,10,150,100,"ZOMBIE")
SONG5button=button((0,191,255),820,10,150,100,"PARANOID")
SONG6button=button((0,191,255),10,210,150,100,"BLACK BIRD")
SONG7button=button((0,191,255),220,210,150,100,"COUNTRY ROADS")
SONG8button=button((0,191,255),420,210,150,100,"SUMMER OF 69")
SONG9button=button((0,191,255),620,210,150,100,"HOLIDAY")
SONG10button=button((0,191,255),820,210,150,100,"SIMPLE MAN")
returnbutton=button((0,191,255),10,410,150,100,"RETURN BACK")
finalreturnbutton=button((0,191,255),10,610,150,100,"RETURN BACK")
CHORD1button=button((0,191,255),10,10,150,100,"C")
CHORD2button=button((0,191,255),220,10,150,100,"C#")
CHORD3button=button((0,191,255),420,10,150,100,"D")
CHORD4button=button((0,191,255),620,10,150,100,"D#")
CHORD5button=button((0,191,255),820,10,150,100,"E")
CHORD6button=button((0,191,255),10,210,150,100,"F")
CHORD7button=button((0,191,255),220,210,150,100,"F#")
CHORD8button=button((0,191,255),420,210,150,100,"G")
CHORD9button=button((0,191,255),620,210,150,100,"G#")
CHORD10button=button((0,191,255),820,210,150,100,"A")
CHORD11button=button((0,191,255),10,410,150,100,"A#")
CHORD12button=button((0,191,255),220,410,150,100,"B")
returnchordbutton=button((0,191,255),420,410,150,100,"RETURN BACK")
MAJORbutton= button((0,191,255),10,10,150,100,"MAJOR")
MINORbutton= button((0,191,255),250,10,150,100,"MINOR")
POWERbutton= button((0,191,255),490,10,150,100,"POWER")
SUS2button= button((0,191,255),10,200,150,100,"SUS2")
SUS4button= button((0,191,255),250,200,150,100,"SUS4")
returnchordsbutton= button((0,191,255),490,200,150,100,"RETURN")
for i in range(1):
    redrawwindow1()
    pygame.display.update()
    pygame.mixer.music.play(1)
    

time.sleep(10.5)
    
while run:
    redrawwindow()
    pygame.display.update()
    for event in pygame.event.get():
        pos=pygame.mouse.get_pos()
        if event.type== pygame.MOUSEBUTTONDOWN:
            if SONGSbutton.isover(pos):
                onclick=True
                while(onclick):
                    SONGSbutton.color=(255,255,255)
                    
                    redrawsongswindow()
                    pygame.display.update()
                    for event in pygame.event.get():
                                 pos=pygame.mouse.get_pos()
                                 if event.type== pygame.MOUSEBUTTONDOWN:
                                    if SONG1button.isover(pos):
                                        def draw1():
                                            
                                            bgimage=pygame.image.load("Paradisecity.jpg").convert()
                                            win.fill((105,89,205))
                                            win.blit(bgimage,[0,0])
                                            Paradisecity1button.draw(win)
                                            Paradisecity2button.draw(win)
                                            return1button.draw(win)
                                        Paradisecity1button=button((0,191,255),400,200,150,100,"PART 1")
                                        Paradisecity2button=button((0,191,255),400,400,150,100,"PART 2")
                                        return1button=button((0,191,255),400,600,150,100,"RETURN BACK")

                                        o=True
                                        while o:
                                            draw1()
                                            pygame.display.update()
                                            for event in pygame.event.get():
                                                pos=pygame.mouse.get_pos()
                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                    if return1button.isover(pos):
                                                         o= False
                                                         redrawsongswindow()
                                                         pygame.display.update()
                                                    elif Paradisecity1button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("Paradisecity1.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif Paradisecity2button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("Paradisecity2.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()

                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()
                                                    
                                                        
                                                elif event.type==pygame.QUIT:
                                                        run= False
                                                        pygame.quit()
                                                        quit()
                                                    
                                                                                    
                                    elif SONG2button.isover(pos):
                                        def draw1():
                                            x=(0,255,0)
                                            bgimage=pygame.image.load("ROCKANDROLL.jpg").convert()
                                            win.fill((105,89,205))
                                            win.blit(bgimage,[0,0])
                                            Rockandroll1button.draw(win)
                                            Rockandroll2button.draw(win)
                                            Rockandroll3button.draw(win)
                                            Rockandroll4button.draw(win)
                                            Rockandroll5button.draw(win)
                                            Rockandroll6button.draw(win)
                                            Rockandroll7button.draw(win)
                                            Rockandroll8button.draw(win)
                                            Rockandroll9button.draw(win)
                                            return1button.draw(win)
                                        Rockandroll1button=button((0,191,255),20,20,150,100,"PART 1")
                                        Rockandroll2button=button((0,191,255),335,20,150,100,"PART 2")
                                        Rockandroll3button=button((0,191,255),660,20,150,100,"PART 3")
                                        Rockandroll4button=button((0,191,255),20,160,150,100,"PART 4")
                                        Rockandroll5button=button((0,191,255),335,160,150,100,"PART 5")
                                        Rockandroll6button=button((0,191,255),660,160,150,100,"PART 6")
                                        Rockandroll7button=button((0,191,255),20,300,150,100,"PART 7")
                                        Rockandroll8button=button((0,191,255),335,300,150,100,"PART 8")
                                        Rockandroll9button=button((0,191,255),660,300,150,100,"PART 9")
                                        return1button=button((0,191,255),335,450,150,100,"RETURN BACK")

                                        o=True
                                        while o:
                                            draw1()
                                            pygame.display.update()
                                            for event in pygame.event.get():
                                                pos=pygame.mouse.get_pos()
                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                    if return1button.isover(pos):
                                                         o= False
                                                         redrawsongswindow()
                                                         pygame.display.update()
                                                    elif Rockandroll1button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("ROCKANDROLL1.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif Rockandroll2button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("ROCKANDROLL2.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif Rockandroll3button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("ROCKANDROLL3.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif Rockandroll4button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("ROCKANDROLL4.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif Rockandroll5button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("ROCKANDROLL5.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif Rockandroll6button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("ROCKANDROLL6.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif Rockandroll7button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("ROCKANDROLL7.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif Rockandroll8button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("ROCKANDROLL8.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif Rockandroll9button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("ROCKANDROLL9.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()
                                                elif event.type==pygame.QUIT:
                                                        run= False
                                                        pygame.quit()
                                                        quit()
                                    elif SONG3button.isover(pos):
                                        def draw1():
                                            
                                            bgimage=pygame.image.load("COMEASYOUARE.jpg").convert()
                                            win.fill((105,89,205))
                                            win.blit(bgimage,[0,0])
                                            COMEASYOUARE1button.draw(win)
                                            COMEASYOUARE2button.draw(win)
                                            COMEASYOUARE3button.draw(win)
                                            COMEASYOUARE4button.draw(win)
                                            COMEASYOUARE5button.draw(win)
                                            COMEASYOUARE6button.draw(win)
                                            COMEASYOUARE7button.draw(win)
                                            COMEASYOUARE8button.draw(win)
                                            return1button.draw(win)
                                        COMEASYOUARE1button=button((0,191,255),20,20,150,100,"PART 1")
                                        COMEASYOUARE2button=button((0,191,255),335,20,150,100,"PART 2")
                                        COMEASYOUARE3button=button((0,191,255),660,20,150,100,"PART 3")
                                        COMEASYOUARE4button=button((0,191,255),20,160,150,100,"PART 4")
                                        COMEASYOUARE5button=button((0,191,255),335,160,150,100,"PART 5")
                                        COMEASYOUARE6button=button((0,191,255),660,160,150,100,"PART 6")
                                        COMEASYOUARE7button=button((0,191,255),20,300,150,100,"PART 7")
                                        COMEASYOUARE8button=button((0,191,255),335,300,150,100,"PART 8")
                                        return1button=button((0,191,255),335,450,150,100,"RETURN BACK")

                                        o=True
                                        while o:
                                            draw1()
                                            pygame.display.update()
                                            for event in pygame.event.get():
                                                pos=pygame.mouse.get_pos()
                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                    if return1button.isover(pos):
                                                         o= False
                                                         redrawsongswindow()
                                                         pygame.display.update()
                                                    elif COMEASYOUARE1button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("COMEASYOUARE1.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif COMEASYOUARE2button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("COMEASYOUARE2.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif COMEASYOUARE3button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("COMEASYOUARE3.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif COMEASYOUARE4button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("COMEASYOUARE4.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif COMEASYOUARE5button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("COMEASYOUARE5.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif COMEASYOUARE6button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("COMEASYOUARE6.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif COMEASYOUARE7button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("COMEASYOUARE7.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif COMEASYOUARE8button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("COMEASYOUARE8.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()
                                                elif event.type==pygame.QUIT:
                                                        run= False
                                                        pygame.quit()
                                                        quit()

                                    elif SONG4button.isover(pos):
                                        def draw1():
                                            
                                            bgimage=pygame.image.load("ZOMBIE.jpg").convert()
                                            win.fill((105,89,205))
                                            win.blit(bgimage,[0,0])
                                            ZOMBIE1button.draw(win)
                                            ZOMBIE2button.draw(win)
                                            ZOMBIE3button.draw(win)
                                            ZOMBIE4button.draw(win)
                                            ZOMBIE5button.draw(win)
                                            return1button.draw(win)
                                        ZOMBIE1button=button((0,191,255),20,20,150,100,"PART 1")
                                        ZOMBIE2button=button((0,191,255),335,20,150,100,"PART 2")
                                        ZOMBIE3button=button((0,191,255),660,20,150,100,"PART 3")
                                        ZOMBIE4button=button((0,191,255),20,160,150,100,"PART 4")
                                        ZOMBIE5button=button((0,191,255),335,160,150,100,"PART 5")
                                        return1button=button((0,191,255),335,450,150,100,"RETURN BACK")

                                        o=True
                                        while o:
                                            draw1()
                                            pygame.display.update()
                                            for event in pygame.event.get():
                                                pos=pygame.mouse.get_pos()
                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                    if return1button.isover(pos):
                                                         o= False
                                                         redrawsongswindow()
                                                         pygame.display.update()
                                                    elif ZOMBIE1button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("ZOMBIE1.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif ZOMBIE2button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("ZOMBIE2.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif ZOMBIE3button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("ZOMBIE3.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif ZOMBIE4button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("ZOMBIE4.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif ZOMBIE5button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("ZOMBIE5.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()
                                                elif event.type==pygame.QUIT:
                                                        run= False
                                                        pygame.quit()
                                                        quit()


                                    elif SONG5button.isover(pos):
                                        def draw1():
                                            
                                            bgimage=pygame.image.load("PARANOID.jpg").convert()
                                            win.fill((105,89,205))
                                            win.blit(bgimage,[0,0])
                                            PARANOID1button.draw(win)
                                            PARANOID2button.draw(win)
                                            PARANOID3button.draw(win)
                                            PARANOID4button.draw(win)
                                            PARANOID5button.draw(win)
                                            PARANOID6button.draw(win)
                                            PARANOID7button.draw(win)
                                            PARANOID8button.draw(win)
                                            return1button.draw(win)
                                        PARANOID1button=button((0,191,255),20,20,150,100,"PART 1")
                                        PARANOID2button=button((0,191,255),335,20,150,100,"PART 2")
                                        PARANOID3button=button((0,191,255),660,20,150,100,"PART 3")
                                        PARANOID4button=button((0,191,255),20,160,150,100,"PART 4")
                                        PARANOID5button=button((0,191,255),335,160,150,100,"PART 5")
                                        PARANOID6button=button((0,191,255),660,160,150,100,"PART 6")
                                        PARANOID7button=button((0,191,255),20,300,150,100,"PART 7")
                                        PARANOID8button=button((0,191,255),335,300,150,100,"PART 8")
                                        return1button=button((0,191,255),335,450,150,100,"RETURN BACK")

                                        o=True
                                        while o:
                                            draw1()
                                            pygame.display.update()
                                            for event in pygame.event.get():
                                                pos=pygame.mouse.get_pos()
                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                    if return1button.isover(pos):
                                                         o= False
                                                         redrawsongswindow()
                                                         pygame.display.update()
                                                    elif PARANOID1button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("PARANOID1.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif PARANOID2button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("PARANOID2.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif PARANOID3button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("PARANOID3.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif PARANOID4button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("PARANOID4.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif PARANOID5button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("PARANOID5.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif PARANOID6button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("PARANOID6.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif PARANOID7button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("PARANOID7.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif PARANOID8button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("PARANOID8.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()
                                                elif event.type==pygame.QUIT:
                                                        run= False
                                                        pygame.quit()
                                                        quit()


                                    elif SONG6button.isover(pos):
                                        def draw1():
                                            
                                            bgimage=pygame.image.load("BLACKBIRD.jpg").convert()
                                            win.fill((105,89,205))
                                            win.blit(bgimage,[0,0])
                                            BLACKBIRD1button.draw(win)
                                            BLACKBIRD2button.draw(win)
                                            BLACKBIRD3button.draw(win)
                                            BLACKBIRD4button.draw(win)
                                            BLACKBIRD5button.draw(win)
                                            return1button.draw(win)
                                        BLACKBIRD1button=button((0,191,255),20,20,150,100,"PART 1")
                                        BLACKBIRD2button=button((0,191,255),335,20,150,100,"PART 2")
                                        BLACKBIRD3button=button((0,191,255),660,20,150,100,"PART 3")
                                        BLACKBIRD4button=button((0,191,255),20,160,150,100,"PART 4")
                                        BLACKBIRD5button=button((0,191,255),335,160,150,100,"PART 5")
                                        return1button=button((0,191,255),335,450,150,100,"RETURN BACK")

                                        o=True
                                        while o:
                                            draw1()
                                            pygame.display.update()
                                            for event in pygame.event.get():
                                                pos=pygame.mouse.get_pos()
                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                    if return1button.isover(pos):
                                                         o= False
                                                         redrawsongswindow()
                                                         pygame.display.update()
                                                    elif BLACKBIRD1button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("BLACKBIRD1.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif BLACKBIRD2button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("BLACKBIRD2.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif BLACKBIRD3button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("BLACKBIRD3.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif BLACKBIRD4button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("BLACKBIRD4.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif BLACKBIRD5button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("BLACKBIRD5.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()
                                                elif event.type==pygame.QUIT:
                                                        run= False
                                                        pygame.quit()
                                                        quit()


                                    elif SONG7button.isover(pos):
                                        def draw1():
                                            
                                            bgimage=pygame.image.load("COUNTRYROADS.jpg").convert()
                                            win.fill((105,89,205))
                                            win.blit(bgimage,[0,0])
                                            COUNTRYROADS1button.draw(win)
                                            COUNTRYROADS2button.draw(win)
                                            COUNTRYROADS3button.draw(win)
                                            COUNTRYROADS4button.draw(win)
                                            COUNTRYROADS5button.draw(win)
                                            return1button.draw(win)
                                        COUNTRYROADS1button=button((0,191,255),20,20,150,100,"PART 1")
                                        COUNTRYROADS2button=button((0,191,255),335,20,150,100,"PART 2")
                                        COUNTRYROADS3button=button((0,191,255),660,20,150,100,"PART 3")
                                        COUNTRYROADS4button=button((0,191,255),20,160,150,100,"PART 4")
                                        COUNTRYROADS5button=button((0,191,255),335,160,150,100,"PART 5")
                                        return1button=button((0,191,255),335,450,150,100,"RETURN BACK")

                                        o=True
                                        while o:
                                            draw1()
                                            pygame.display.update()
                                            for event in pygame.event.get():
                                                pos=pygame.mouse.get_pos()
                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                    if return1button.isover(pos):
                                                         o= False
                                                         redrawsongswindow()
                                                         pygame.display.update()
                                                    elif COUNTRYROADS1button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("COUNTRYROADS1.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif COUNTRYROADS2button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("COUNTRYROADS2.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif COUNTRYROADS3button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("COUNTRYROADS3.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif COUNTRYROADS4button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("COUNTRYROADS4.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif COUNTRYROADS5button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("COUNTRYROADS5.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()
                                                elif event.type==pygame.QUIT:
                                                        run= False
                                                        pygame.quit()
                                                        quit()
                
                                    elif SONG8button.isover(pos):
                                        def draw1():
                                            
                                            bgimage=pygame.image.load("SUMMEROF69.jpg").convert()
                                            win.fill((105,89,205))
                                            win.blit(bgimage,[0,0])
                                            SUMMEROF691button.draw(win)
                                            SUMMEROF692button.draw(win)
                                            return1button.draw(win)
                                        SUMMEROF691button=button((0,191,255),400,200,150,100,"PART 1")
                                        SUMMEROF692button=button((0,191,255),400,400,150,100,"PART 2")
                                        return1button=button((0,191,255),400,600,150,100,"RETURN BACK")

                                        o=True
                                        while o:
                                            draw1()
                                            pygame.display.update()
                                            for event in pygame.event.get():
                                                pos=pygame.mouse.get_pos()
                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                    if return1button.isover(pos):
                                                         o= False
                                                         redrawsongswindow()
                                                         pygame.display.update()
                                                    elif SUMMEROF691button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("SUMMEROF691.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif SUMMEROF692button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("SUMMEROF692.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()

                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()
                                                    
                                                        
                                                elif event.type==pygame.QUIT:
                                                        run= False
                                                        pygame.quit()
                                                        quit()
                                        
                                    elif SONG9button.isover(pos):
                                        def draw1():
                                            
                                            bgimage=pygame.image.load("HOLIDAY.jpg").convert()
                                            win.fill((105,89,205))
                                            win.blit(bgimage,[0,0])
                                            HOLIDAY1button.draw(win)
                                            HOLIDAY2button.draw(win)
                                            HOLIDAY3button.draw(win)
                                            HOLIDAY4button.draw(win)
                                            HOLIDAY5button.draw(win)
                                            HOLIDAY6button.draw(win)
                                            HOLIDAY7button.draw(win)
                                            HOLIDAY8button.draw(win)
                                            return1button.draw(win)
                                        HOLIDAY1button=button((0,191,255),20,20,150,100,"PART 1")
                                        HOLIDAY2button=button((0,191,255),335,20,150,100,"PART 2")
                                        HOLIDAY3button=button((0,191,255),660,20,150,100,"PART 3")
                                        HOLIDAY4button=button((0,191,255),20,160,150,100,"PART 4")
                                        HOLIDAY5button=button((0,191,255),335,160,150,100,"PART 5")
                                        HOLIDAY6button=button((0,191,255),660,160,150,100,"PART 6")
                                        HOLIDAY7button=button((0,191,255),20,300,150,100,"PART 7")
                                        HOLIDAY8button=button((0,191,255),335,300,150,100,"PART 8")
                                        return1button=button((0,191,255),335,450,150,100,"RETURN BACK")

                                        o=True
                                        while o:
                                            draw1()
                                            pygame.display.update()
                                            for event in pygame.event.get():
                                                pos=pygame.mouse.get_pos()
                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                    if return1button.isover(pos):
                                                         o= False
                                                         redrawsongswindow()
                                                         pygame.display.update()
                                                    elif HOLIDAY1button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("HOLIDAY1.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif HOLIDAY2button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("HOLIDAY2.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif HOLIDAY3button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("HOLIDAY3.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif HOLIDAY4button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("HOLIDAY4.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif HOLIDAY5button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("HOLIDAY5.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif HOLIDAY6button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("HOLIDAY6.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif HOLIDAY7button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("HOLIDAY7.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif HOLIDAY8button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("HOLIDAY8.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()
                                                elif event.type==pygame.QUIT:
                                                        run= False
                                                        pygame.quit()
                                                        quit()

                                    elif SONG10button.isover(pos):
                                        def draw1():
                                            
                                            bgimage=pygame.image.load("SIMPLEMAN.jpg").convert()
                                            win.fill((105,89,205))
                                            win.blit(bgimage,[0,0])
                                            SIMPLEMAN1button.draw(win)
                                            SIMPLEMAN2button.draw(win)
                                            SIMPLEMAN3button.draw(win)
                                            SIMPLEMAN4button.draw(win)
                                            SIMPLEMAN5button.draw(win)
                                            SIMPLEMAN6button.draw(win)
                                            return1button.draw(win)
                                        SIMPLEMAN1button=button((0,191,255),20,20,150,100,"PART 1")
                                        SIMPLEMAN2button=button((0,191,255),335,20,150,100,"PART 2")
                                        SIMPLEMAN3button=button((0,191,255),660,20,150,100,"PART 3")
                                        SIMPLEMAN4button=button((0,191,255),20,160,150,100,"PART 4")
                                        SIMPLEMAN5button=button((0,191,255),335,160,150,100,"PART 5")
                                        SIMPLEMAN6button=button((0,191,255),660,160,150,100,"PART 6")
                                        return1button=button((0,191,255),335,450,150,100,"RETURN BACK")

                                        o=True
                                        while o:
                                            draw1()
                                            pygame.display.update()
                                            for event in pygame.event.get():
                                                pos=pygame.mouse.get_pos()
                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                    if return1button.isover(pos):
                                                         o= False
                                                         redrawsongswindow()
                                                         pygame.display.update()
                                                    elif SIMPLEMAN1button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("SIMPLEMAN1.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif SIMPLEMAN2button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("HOLIDAY2.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif SIMPLEMAN3button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("SIMPLEMAN3.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif SIMPLEMAN4button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("SIMPLEMAN4.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif SIMPLEMAN5button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("SIMPLEMAN5.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                    elif SIMPLEMAN6button.isover(pos):
                                                        c=True
                                                        while (c):
                                                            x= pygame.image.load("SIMPLEMAN6.jpg").convert()
                                                            finalwindow()
                                                            pygame.display.update()                                                        
                                                            for event in pygame.event.get():
                                                                pos=pygame.mouse.get_pos()
                                                                if event.type== pygame.MOUSEBUTTONDOWN:
                                                                         if finalreturnbutton.isover(pos):
                                                                               c= False
                                                                               draw1()
                                                                               pygame.display.update()
                                                                elif event.type==pygame.QUIT:
                                                                        run= False
                                                                        pygame.quit()
                                                                        quit()

                                                elif event.type==pygame.QUIT:
                                                        run= False
                                                        pygame.quit()
                                                        quit()

                                    elif returnbutton.isover(pos):
                                         onclick= False
                                         redrawwindow()
                                         pygame.display.update()
                                         
                                         SONGSbutton.color=(0,191,255)
                                         
                                 if event.type==pygame.QUIT:
                                         run= False
                                         pygame.quit()
                                         quit()
            elif CHORDSbutton.isover(pos):
                             onclick= True
                             while onclick:
                                    chordwindow()
                                    pygame.display.update()
                                    for event in pygame.event.get():
                                        if event.type== pygame.MOUSEBUTTONDOWN:
                                            pos=pygame.mouse.get_pos()
                                            if CHORD1button.isover(pos):
                                                n=True
                                                while n:
                                                    chords()
                                                    pygame.display.update()
                                                    for event in pygame.event.get():
                                                        if event.type== pygame.MOUSEBUTTONDOWN:
                                                            pos= pygame.mouse.get_pos()
                                                            if MAJORbutton.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("CMAJOR.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()
                                                            elif SUS2button.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("CSUS2.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            elif SUS4button.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("CSUS4.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            if MINORbutton.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("CMINOR.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            elif POWERbutton.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("CPOWER.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            elif returnchordsbutton.isover(pos):
                                                                n= False
                                                                chordwindow()
                                                                pygame.display.update()
                                                        elif event.type==pygame.QUIT:
                                                            run= False
                                                            pygame.quit()
                                                            quit()
                                            if CHORD2button.isover(pos):
                                                n=True
                                                while n:
                                                    chords()
                                                    pygame.display.update()
                                                    for event in pygame.event.get():
                                                        if event.type== pygame.MOUSEBUTTONDOWN:
                                                            pos= pygame.mouse.get_pos()
                                                            if MAJORbutton.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("C#MAJOR.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()
                                                            elif SUS2button.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("C#SUS2.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            elif SUS4button.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("C#SUS4.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            if MINORbutton.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("C#MINOR.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            elif POWERbutton.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("C#POWER.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            elif returnchordsbutton.isover(pos):
                                                                n= False
                                                                chordwindow()
                                                                pygame.display.update()
                                                        elif event.type==pygame.QUIT:
                                                            run= False
                                                            pygame.quit()
                                                            quit()

                                            
                                            elif CHORD3button.isover(pos):
                                                n=True
                                                while n:
                                                    chords()
                                                    pygame.display.update()
                                                    for event in pygame.event.get():
                                                        if event.type== pygame.MOUSEBUTTONDOWN:
                                                            pos= pygame.mouse.get_pos()
                                                            if MAJORbutton.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("DMAJOR.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()
                                                            elif SUS2button.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("DSUS2.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            elif SUS4button.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("DSUS4.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            if MINORbutton.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("DMINOR.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            elif POWERbutton.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("DPOWER.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            elif returnchordsbutton.isover(pos):
                                                                n= False
                                                                chordwindow()
                                                                pygame.display.update()
                                                        elif event.type==pygame.QUIT:
                                                            run= False
                                                            pygame.quit()
                                                            quit()

                                            if CHORD4button.isover(pos):
                                                n=True
                                                while n:
                                                    chords()
                                                    pygame.display.update()
                                                    for event in pygame.event.get():
                                                        if event.type== pygame.MOUSEBUTTONDOWN:
                                                            pos= pygame.mouse.get_pos()
                                                            if MAJORbutton.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("D#MAJOR.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()
                                                            elif SUS2button.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("D#SUS2.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            elif SUS4button.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("D#SUS4.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            if MINORbutton.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("D#MINOR.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            elif POWERbutton.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("D#POWER.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            elif returnchordsbutton.isover(pos):
                                                                n= False
                                                                chordwindow()
                                                                pygame.display.update()
                                                        elif event.type==pygame.QUIT:
                                                            run= False
                                                            pygame.quit()
                                                            quit()

                                            if CHORD5button.isover(pos):
                                                n=True
                                                while n:
                                                    chords()
                                                    pygame.display.update()
                                                    for event in pygame.event.get():
                                                        if event.type== pygame.MOUSEBUTTONDOWN:
                                                            pos= pygame.mouse.get_pos()
                                                            if MAJORbutton.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("EMAJOR.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()
                                                            elif SUS2button.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("ESUS2.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            elif SUS4button.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("ESUS4.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            if MINORbutton.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("EMINOR.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            elif POWERbutton.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("EPOWER.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            elif returnchordsbutton.isover(pos):
                                                                n= False
                                                                chordwindow()
                                                                pygame.display.update()
                                                        elif event.type==pygame.QUIT:
                                                            run= False
                                                            pygame.quit()
                                                            quit()

                                            
                                            if CHORD6button.isover(pos):
                                                n=True
                                                while n:
                                                    chords()
                                                    pygame.display.update()
                                                    for event in pygame.event.get():
                                                        if event.type== pygame.MOUSEBUTTONDOWN:
                                                            pos= pygame.mouse.get_pos()
                                                            if MAJORbutton.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("FMAJOR.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()
                                                            elif SUS2button.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("FSUS2.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            elif SUS4button.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("FSUS4.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            if MINORbutton.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("FMINOR.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            elif POWERbutton.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("FPOWER.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            elif returnchordsbutton.isover(pos):
                                                                n= False
                                                                chordwindow()
                                                                pygame.display.update()
                                                        elif event.type==pygame.QUIT:
                                                            run= False
                                                            pygame.quit()
                                                            quit()
                                            if CHORD7button.isover(pos):
                                                n=True
                                                while n:
                                                    chords()
                                                    pygame.display.update()
                                                    for event in pygame.event.get():
                                                        if event.type== pygame.MOUSEBUTTONDOWN:
                                                            pos= pygame.mouse.get_pos()
                                                            if MAJORbutton.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("F#MAJOR.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()
                                                            elif SUS2button.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("F#SUS2.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            elif SUS4button.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("F#SUS4.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            if MINORbutton.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("F#MINOR.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            elif POWERbutton.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("F#POWER.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            elif returnchordsbutton.isover(pos):
                                                                n= False
                                                                chordwindow()
                                                                pygame.display.update()
                                                        elif event.type==pygame.QUIT:
                                                            run= False
                                                            pygame.quit()
                                                            quit()
                                            if CHORD8button.isover(pos):
                                                n=True
                                                while n:
                                                    chords()
                                                    pygame.display.update()
                                                    for event in pygame.event.get():
                                                        if event.type== pygame.MOUSEBUTTONDOWN:
                                                            pos= pygame.mouse.get_pos()
                                                            if MAJORbutton.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("GMAJOR.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()
                                                            elif SUS2button.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("GSUS2.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            elif SUS4button.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("GSUS4.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            if MINORbutton.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("GMINOR.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            elif POWERbutton.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("GPOWER.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            elif returnchordsbutton.isover(pos):
                                                                n= False
                                                                chordwindow()
                                                                pygame.display.update()
                                                        elif event.type==pygame.QUIT:
                                                            run= False
                                                            pygame.quit()
                                                            quit()
                                            if CHORD9button.isover(pos):
                                                n=True
                                                while n:
                                                    chords()
                                                    pygame.display.update()
                                                    for event in pygame.event.get():
                                                        if event.type== pygame.MOUSEBUTTONDOWN:
                                                            pos= pygame.mouse.get_pos()
                                                            if MAJORbutton.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("G#MAJOR.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()
                                                            elif SUS2button.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("G#SUS2.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            elif SUS4button.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("G#SUS4.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            if MINORbutton.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("G#MINOR.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            elif POWERbutton.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("G#POWER.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            elif returnchordsbutton.isover(pos):
                                                                n= False
                                                                chordwindow()
                                                                pygame.display.update()
                                                        elif event.type==pygame.QUIT:
                                                            run= False
                                                            pygame.quit()
                                                            quit()
                                            if CHORD10button.isover(pos):
                                                n=True
                                                while n:
                                                    chords()
                                                    pygame.display.update()
                                                    for event in pygame.event.get():
                                                        if event.type== pygame.MOUSEBUTTONDOWN:
                                                            pos= pygame.mouse.get_pos()
                                                            if MAJORbutton.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("AMAJOR.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()
                                                            elif SUS2button.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("ASUS2.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            elif SUS4button.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("ASUS4.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            if MINORbutton.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("AMINOR.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            elif POWERbutton.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("APOWER.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            elif returnchordsbutton.isover(pos):
                                                                n= False
                                                                chordwindow()
                                                                pygame.display.update()
                                                        elif event.type==pygame.QUIT:
                                                            run= False
                                                            pygame.quit()
                                                            quit()
                                            if CHORD11button.isover(pos):
                                                n=True
                                                while n:
                                                    chords()
                                                    pygame.display.update()
                                                    for event in pygame.event.get():
                                                        if event.type== pygame.MOUSEBUTTONDOWN:
                                                            pos= pygame.mouse.get_pos()
                                                            if MAJORbutton.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("A#MAJOR.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()
                                                            elif SUS2button.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("A#SUS2.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            elif SUS4button.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("A#SUS4.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            if MINORbutton.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("A#MINOR.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            elif POWERbutton.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("A#POWER.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            elif returnchordsbutton.isover(pos):
                                                                n= False
                                                                chordwindow()
                                                                pygame.display.update()
                                                        elif event.type==pygame.QUIT:
                                                            run= False
                                                            pygame.quit()
                                                            quit()
                                            if CHORD12button.isover(pos):
                                                n=True
                                                while n:
                                                    chords()
                                                    pygame.display.update()
                                                    for event in pygame.event.get():
                                                        if event.type== pygame.MOUSEBUTTONDOWN:
                                                            pos= pygame.mouse.get_pos()
                                                            if MAJORbutton.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("BMAJOR.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()
                                                            elif SUS2button.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("BSUS2.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            elif SUS4button.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("BSUS4.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            if MINORbutton.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("BMINOR.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            elif POWERbutton.isover(pos):
                                                                m=True
                                                                while m:
                                                                   x= pygame.image.load("BPOWER.jpg").convert()
                                                                   finalwindow()
                                                                   pygame.display.update()
                                                                   for event in pygame.event.get():
                                                                       if event.type== pygame.MOUSEBUTTONDOWN:
                                                                           pos= pygame.mouse.get_pos()
                                                                           if finalreturnbutton.isover(pos):
                                                                               m=False
                                                                               chords()
                                                                               pygame.display.update()
                                                                       elif event.type==pygame.QUIT:     
                                                                               run=False
                                                                               pygame.quit()
                                                                               quit()              
                                                            elif returnchordsbutton.isover(pos):
                                                                n= False
                                                                chordwindow()
                                                                pygame.display.update()
                                                        elif event.type==pygame.QUIT:
                                                            run= False
                                                            pygame.quit()
                                                            quit()
                                            elif returnchordbutton.isover(pos):
                                                onclick= False
                                                redrawwindow()
                                                pygame.display.update()

                                        elif event.type== pygame.QUIT:
                                            run= False
                                            pygame.quit()
                                            quit()
            elif METRONOMEbutton.isover(pos):
                colour = ()
                textcolour = ()
                black=(0,0,0)
                white=(255,255,255)

                class Button():
                    
                    def __init__(self, colour, textcolour, xpos, ypos, bwidth, bheight, text= ''):
                        self.colour = colour
                        self.textcolour = textcolour
                        self.xpos = xpos
                        self.ypos = ypos
                        self.bheight = bheight
                        self.bwidth = bwidth
                        self.text = text
                    
                    
                    def bdraw(self, win, outline=None):
                        if outline:
                            pygame.draw.rect(win, outline, (self.xpos-2, self.ypos-2, self.bwidth+4, self.bheight+4),0)
                            #if desired, outline can be drawn
                        pygame.draw.rect(win, self.colour, (self.xpos, self.ypos, self.bwidth, self.bheight), 0)
                        
                        if self.text != '':
                            font = pygame.font.SysFont('comicsans', 40,)
                            text = font.render(self.text, 1, self.textcolour)
                            win.blit(text, (self.xpos + (self.bwidth/2 - text.get_width()/2), self.ypos + (self.bheight/2 - text.get_height()/2)))
                    
                    def isOn(self, curpos):
                        if curpos[0] > self.xpos and curpos[0] < self.xpos + self.bwidth:
                            if curpos[1] > self.ypos and curpos[1] < self.ypos + self.bheight:
                                return True
                        return False
                def metronomewindow():
                    win.fill(black)
                    button14.bdraw(win)
                    button24.bdraw(win)
                    button34.bdraw(win)
                    button44.bdraw(win)
                    stopbutton.bdraw(win)
                    returnbuttonm.bdraw(win)
                #def innerwindow():
                    #win.fill((255,255,255))
                    #returnbuttonm1.bdraw(win)
                #def stop():
                    #pygame.mixer.music.stop()
                    #Run1=False
                    #metronomewindow()
                    #pygame.display.update()
                FONT = pygame.font.Font(None, 32)
                button14 = Button((81, 81, 81), black, 800, 250, 100, 50, '1/4')
                button24 = Button((81, 81, 81), black, 800, 310, 100, 50, '2/4')
                button34 = Button((81, 81, 81), black, 800, 370, 100, 50, '3/4')
                button44 = Button((81, 81, 81), black, 800, 430, 100, 50, '4/4')
                returnbuttonm= Button((81, 81, 81), black, 375, 370, 150, 75, 'RETURN')
                stopbutton= Button((81, 81, 81), black, 375, 280, 150, 75, 'STOP')
                Run = True
                while Run:
                    metronomewindow()
                    pygame.display.update()
                    curpos = pygame.mouse.get_pos()
                    disfont = pygame.font.SysFont('timesnewroman', 72)
                    for event in pygame.event.get():
                        #quitting
                        if event.type == pygame.QUIT:
                            run=False
                            pygame.quit()
                            quit()
                        #event of clicking
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            #1/4 button
                            if button14.isOn(curpos):
                                print ('1/4 timing chosen')
                                pygame.mixer.music.load('tick14.mp3')
                                
                                Run1=True
                                while Run1:
                                    pygame.mixer.music.play(1)
                                    
                                    for event in pygame.event.get():
                                        pos=pygame.mouse.get_pos()
                                        if event.type== pygame.MOUSEBUTTONDOWN:
                                            if stopbutton.isOn(pos):
                                                pygame.mixer.music.stop()
                                                Run1=False
                                            if returnbuttonm.isOn(pos):
                                                pygame.mixer.music.stop()
                                                Run1=False
                                                Run= False
                                                redrawwindow()
                                                pygame.display.update()
                                        elif event.type==pygame.QUIT:     
                                                run=False
                                                pygame.quit()
                                                quit()
                                    time.sleep(0.25)
                                    

                                             
                            #2/4 button
                            elif button24.isOn(curpos):
                                print ('2/4 timing chosen')
                                pygame.mixer.music.load('tick24.mp3')
                                
                                Run1=True
                                while Run1:
                                    pygame.mixer.music.play(1)
                                    
                                    #innerwindow()
                                    for event in pygame.event.get():
                                        pos=pygame.mouse.get_pos()
                                        if event.type== pygame.MOUSEBUTTONDOWN:
                                            if stopbutton.isOn(pos):
                                                pygame.mixer.music.stop()
                                                Run1=False
                                            if returnbuttonm.isOn(pos):
                                                pygame.mixer.music.stop()
                                                Run1=False
                                                Run= False
                                                redrawwindow()
                                                pygame.display.update()
                                        elif event.type==pygame.QUIT:     
                                                run=False
                                                pygame.quit()
                                                quit()
                                    time.sleep(0.9)

                            #3/4 button
                            elif button34.isOn(curpos):
                                print ('3/4 timing chosen')
                                pygame.mixer.music.load('tick34.mp3')
                                
                                Run1=True
                                while Run1:
                                    pygame.mixer.music.play(1)
                                    
                                    for event in pygame.event.get():
                                        pos=pygame.mouse.get_pos()
                                        if event.type== pygame.MOUSEBUTTONDOWN:
                                            if stopbutton.isOn(pos):
                                                pygame.mixer.music.stop()
                                                Run1=False
                                            if returnbuttonm.isOn(pos):
                                                pygame.mixer.music.stop()
                                                Run1=False
                                                Run= False
                                                redrawwindow()
                                                pygame.display.update()
                                        elif event.type==pygame.QUIT:     
                                                run=False
                                                pygame.quit()
                                                quit()
                                    time.sleep(1.3)                       

                            #4/4 button
                            elif button44.isOn(curpos):
                                print ('4/4 timing chosen')
                                pygame.mixer.music.load('tick44.mp3')
                                
                                Run1=True
                                while Run1:
                                    pygame.mixer.music.play(1)
                                    
                                    for event in pygame.event.get():
                                        pos=pygame.mouse.get_pos()
                                        if event.type== pygame.MOUSEBUTTONDOWN:
                                            if stopbutton.isOn(pos):
                                                pygame.mixer.music.stop()
                                                Run1=False
                                            if returnbuttonm.isOn(pos):
                                                pygame.mixer.music.stop()
                                                Run1=False
                                                Run= False
                                                redrawwindow()
                                                pygame.display.update()
                                        elif event.type==pygame.QUIT:     
                                                run=False
                                                pygame.quit()
                                                quit()
                                    time.sleep(2)
                                                
                            elif returnbuttonm.isOn(curpos):
                                Run= False
                                redrawwindow()
                                pygame.display.update()

        if event.type==pygame.QUIT:
            run= False
            pygame.quit()
            quit()
        
        
            
                

