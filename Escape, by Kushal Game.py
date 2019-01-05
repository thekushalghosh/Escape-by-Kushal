import pygame
import time
import random
import webbrowser
 
pygame.init()
 
display_width = 800
display_height = 600

 
black = (0,0,0)
white = (255,255,255)
cyan = (0,255,255)
yellow = (255,255,0)
red = (200,0,0)
green = (0,200,0)
blue = (0,0,255)
pink = (255,182,194)
violet = (59,0,93)

global bgcol

global bkcol

global ab

global aa

global spd

spd = 6

ab = 'bb.wav'

aa = pygame.mixer.Sound("cc.wav")

bgcol = pink

bkcol = violet

bright_red = (255,0,0)
bright_green = (0,255,0)
 

 
robot_width = 73

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('ESCAPE, by Kushal (version - 2.0.2)')
clock = pygame.time.Clock()
 
robotImg = pygame.image.load('a.png')
gameIcon = pygame.image.load('a.png')

pygame.display.set_icon(gameIcon)

pause = False


hh = 0


def urlfb():
    new = 2
    url = "www.facebook.com/thekushalghosh"
    webbrowser.open(url,new=new)

def urlin():
    new = 2
    url = "www.instagram.com/thekushalghosh"
    webbrowser.open(url,new=new)

def urltw():
    new = 2
    url = "www.twitter.com/thekushalghosh"
    webbrowser.open(url,new=new)

def urlqu():
    new = 2
    url = "www.quora.com/profile/Kushal-Ghosh-24"
    webbrowser.open(url,new=new)

def misc():
    global ab
    global aa
    ab = 'bb.wav'
    aa = pygame.mixer.Sound("cc.wav")
    pygame.display.update()
    clock.tick(15)

def musc():
    global ab
    global aa
    ab = 'sil.wav'
    aa = pygame.mixer.Sound("sil.wav")
    pygame.display.update()
    clock.tick(15)

def bcgcolgn():
    global bgcol
    bgcol = bright_green
    pygame.display.update()
    clock.tick(15)

def bcgcolyl():
    global bgcol
    bgcol = yellow
    pygame.display.update()
    clock.tick(15)


def bcgcolpn():
    global bgcol
    bgcol = pink
    pygame.display.update()
    clock.tick(15)



def blkcolvl():
    global bkcol
    bkcol = violet
    pygame.display.update()
    clock.tick(15)

def blkcolbl():
    global bkcol
    bkcol = black
    pygame.display.update()
    clock.tick(15)

def blkcolrd():
    global bkcol
    bkcol = bright_red
    pygame.display.update()
    clock.tick(15)

def spde():
    global spd
    spd = 4
    pygame.display.update()
    clock.tick(15)


def spdm():
    global spd
    spd = 6
    pygame.display.update()
    clock.tick(15)


def spdh():
    global spd
    spd = 8
    pygame.display.update()
    clock.tick(15)


def blocks_dodged(count):
    font = pygame.font.SysFont("copperplate gothic", 25)
    name = pygame.font.SysFont("Segoe UI", 25)
    text = font.render("Your Score: "+str(count), True, black)
    hs = font.render("High Score: "+str(hh), True, black)
    hmm = name.render("By : Kushal Ghosh", True, white)
    gameDisplay.blit(text,(10,10))
    gameDisplay.blit(hs,(14,35))
    gameDisplay.blit(hmm,(600,14))
 
def blocks(blockx, blocky, blockw, blockh, color):
    pygame.draw.rect(gameDisplay, color, [blockx, blocky, blockw, blockh])
 
def robot(x,y):
    gameDisplay.blit(robotImg,(x,y))
 
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
 
def crash():
    
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(aa)
    largeText = pygame.font.SysFont("chiller",155)
    TextSurf, TextRect = text_objects("GAME OVER", largeText)
    TextRect.center = ((display_width/2),(display_height/2.5))
    gameDisplay.blit(TextSurf, TextRect)
    

    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        

        button("Try Again",120,400,120,50,green,bright_green,game_loop)
        button("Main Menu",350,400,150,50,(112,128,144),(192,192,192),game_intro)
        button("Exit",600,400,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15) 

def button(msg,x,y,w,h,ic,ac,action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("calibri",30)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    




def quitgame():
    pygame.quit()
    quit()

def unpause():
    pygame.mixer.music.unpause()
    global pause
    pause = False
    

def paused():
    
    pygame.mixer.music.pause()
    largeText = pygame.font.SysFont("calculator",135)
    TextSurf, TextRect = text_objects("PAUSED", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    while pause:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    unpause()
                
            

       
        button("Resume",150,450,100,50,green,bright_green,unpause)
        button("Exit",550,450,100,50,red,bright_red,quitgame)


        pygame.display.update()
        clock.tick(15)

def instrc():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    
        gameDisplay.fill(cyan)
        
        hdng = pygame.font.SysFont("Algerian",77)
        blkcol = pygame.font.SysFont("Segoe UI",25)
        gmms = pygame.font.SysFont("Segoe UI",25)
        sppd = pygame.font.SysFont("Segoe UI",25)
        edac = pygame.font.SysFont("Segoe UI",25)
        cred = pygame.font.SysFont("Segoe UI",60)
        cred1 = pygame.font.SysFont("Segoe UI",25)
        cred2 = pygame.font.SysFont("Segoe UI",25)
        TextSurf, TextRect = text_objects("Info Menu", hdng)
        TextSurf2, TextRect2 = text_objects("-> Ed, a robot has to dodge the falling blocks.", blkcol)
        TextSurf3, TextRect3 = text_objects("-> Use the Left and Right Arrow keys to move Ed left and right.", sppd)
        TextSurf4, TextRect4 = text_objects("-> Press P to pause the game anytime.",gmms)
        TextSurf5, TextRect5 = text_objects("-> Visit the Settings menu to customise your game.",edac)
        TextSurf6, TextRect6 = text_objects("Credits :-",cred)
        TextSurf7, TextRect7 = text_objects("Developer : KUSHAL GHOSH  :: Contact Links-",cred1)
        TextSurf8, TextRect8 = text_objects("Special thanks to Ketchapp Inc. for the music.",cred2)
        TextRect.center = (400,60)
        TextRect2.center = (330,120)
        TextRect3.center = (420,160)
        TextRect4.center = (295,200)
        TextRect5.center = (356,240)
        TextRect6.center = (392,344)
        TextRect7.center = (338,400)
        TextRect8.center = (347,440)
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        gameDisplay.blit(TextSurf3, TextRect3)
        gameDisplay.blit(TextSurf4, TextRect4)
        gameDisplay.blit(TextSurf5, TextRect5)
        gameDisplay.blit(TextSurf6, TextRect6)
        gameDisplay.blit(TextSurf7, TextRect7)
        gameDisplay.blit(TextSurf8, TextRect8)
        button("<- RETURN",329,500,150,50,cyan,(100,255,255),game_intro)
        button("f",577,383,35,35,(59,89,239),(68,143,255),urlfb)
        button("[o]",623,383,35,35,(255,20,149),(95,95,95),urlin)
        button("t",668,383,35,35,(29,161,242),(0,0,255),urltw)
        button("Q",713,383,35,35,(239,0,0),(255,0,0),urlqu)
        
        pygame.display.update()
        clock.tick(15)
        
def sett():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    
        gameDisplay.fill(cyan)
        
        bgdcol = pygame.font.SysFont("Segoe UI",40)
        blkcol = pygame.font.SysFont("Segoe UI",40)
        gmms = pygame.font.SysFont("Segoe UI",40)
        sppd = pygame.font.SysFont("Segoe UI",40)
        TextSurf3, TextRect3 = text_objects("Choose Background Colour", bgdcol)
        TextSurf4, TextRect4 = text_objects("Choose Block Colour", blkcol)
        TextSurf5, TextRect5 = text_objects("Choose Difficulty", sppd)
        TextSurf6, TextRect6 = text_objects("Game Music",gmms)
        TextRect3.center = (257,40)
        TextRect4.center = (203,160)
        TextRect5.center = (170,280)
        TextRect6.center = (132,400)
        gameDisplay.blit(TextSurf3, TextRect3)
        gameDisplay.blit(TextSurf4, TextRect4)
        gameDisplay.blit(TextSurf5, TextRect5)
        gameDisplay.blit(TextSurf6, TextRect6)
        button("<- RETURN",302,540,150,50,cyan,(100,255,255),game_intro)
        button("Green",100,70,100,50,green,bright_green,bcgcolgn)
        button("Yellow",275,70,100,50,yellow,(255,255,100),bcgcolyl)
        button("Pink",450,70,100,50,(255,116,140),(255,141,161),bcgcolpn)
        button("Violet",100,190,100,50,(167,0,237),(189,33,255),blkcolvl)
        button("Black",275,190,100,50,(169,169,169),(207,207,207),blkcolbl)
        button("Red",450,190,100,50,red,bright_red,blkcolrd)
        button("Easy",100,310,100,50,green,bright_green,spde)
        button("Medium",275,310,100,50,yellow,(255,255,100),spdm)
        button("Hard",450,310,100,50,red,bright_red,spdh)
        button("On",100,430,100,50,green,bright_green,misc)
        button("Off",275,430,100,50,red,bright_red,musc)
        
        pygame.display.update()
        clock.tick(15)
        
    
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(cyan)
        largeText = pygame.font.SysFont("broadway",115)
        smallText = pygame.font.SysFont("forte",60)
        name = pygame.font.SysFont("Segoe UI", 25)
        TextSurf, TextRect = text_objects("ESCAPE", largeText)
        TextSurf1, TextRect1 = text_objects("BY KUSHAL", smallText)
        TextRect.center = ((display_width/2),(display_height/2.5))
        TextRect1.center = ((display_width/2),(display_height/1.8))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf1, TextRect1)

        button("f",623,14,35,35,(59,89,239),(68,143,255),urlfb)
        button("[o]",668,14,35,35,(255,20,149),(95,95,95),urlin)
        button("t",713,14,35,35,(29,161,242),(0,0,255),urltw)
        button("Q",759,14,35,35,(239,0,0),(255,0,0),urlqu)

        button("Play",120,450,100,50,green,bright_green,game_loop)
        button("Info",270,450,100,50,yellow,(255,255,100),instrc)
        button("Settings",425,450,120,50,(112,128,144),(192,192,192),sett)
        button("Exit",600,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)
        
        
    
    

    
def game_loop():
    global hh
    global k
    global pause
    global bgcol
    global bkcol
    global ab

    pygame.mixer.music.load(ab)
    pygame.mixer.music.play(-1)

    x = (display_width * 0.45)
    y = (display_height * 0.86)
 
    x_change = 0
 
    block_startx = random.randrange(0, display_width)
    block_starty = -600
    block_speed = spd
    block_width = 60
    block_height = 60
 
    blockCount = 1
 
    dodged = 0
 
    gameExit = False
 
    while not gameExit:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                    
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
 
        x += x_change
        gameDisplay.fill(bgcol)
        
        blocks(block_startx, block_starty, block_width, block_height, bkcol)
 
 
        
        block_starty += block_speed
        robot(x,y)
        blocks_dodged(dodged)
 
        if x > display_width - robot_width or x < 0:
            crash()
 
        if block_starty > display_height:
            block_starty = 0 - block_height
            block_startx = random.randrange(0,display_width)
            dodged += 1
            block_speed += 1
        if dodged > hh:
            hh = dodged
            
 
        if y < block_starty+block_height:
 
            if x > block_startx and x < block_startx + block_width or x+robot_width > block_startx and x + robot_width < block_startx+block_width:
                crash()

        
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
