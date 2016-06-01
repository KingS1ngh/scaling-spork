from pygame import *
from random import *
screen=display.set_mode((800,600))#screen size
myClock=time.Clock()
posx,posy=0,300#initial position of characters and other stuff
eend=""
end=""
name="MTank"
back1=image.load("Back1.png").convert()
back1=transform.scale(back1,(800,600))
screenBuff=screen.copy()
mclock=250
eposx,eposy=100,100
eend=""
def goodMove():
    global posx
    global posy
    
    global end
    if keys[K_w]:
        posy-=2
        end=""
    if keys[K_s]:
        posy+=2
        end="D"
    if keys[K_d]:
        posx+=2
        end="R"
    if keys[K_a]:
        posx-=2
        end="L"
    if 0>posx: posx=0
    if 765<posx: posx=765
    if 0>posy: posy=0
    if 565<posy: posy=565
def good(size):
    global posx
    global posy
    global end
    global name
    goodMove()
    gguy=image.load(name+"\\"+name+end+".png")
    gguy=transform.scale(gguy,size)
    screen.blit(gguy,(posx,posy))
def badMove(name,x,y,size):
    #global eposx
    #global eposy
    global posx
    global posy
    global eend
    bguy=image.load(name+"\\"+name+eend+".png")
    bguy=transform.scale(bguy,size)
    screen.blit(bguy,(x,y))
    if y<posy:
        y+=1
        eend="D"
    if y>posy:
        y-=1
        eend=""
    if x<posx:
        x+=1
        eend="R"
    if x>posx:
        x-=1
        eend="L"
def bad(name,size,x,y):
    bguy=image.load(name+"\\"+name+eend+".png")
    bguy=transform.scale(bguy,size)
    screen.blit(bguy,(x,y))
def change():
    global posx
    global posy
    global name
    boxRect=Rect(0,0,10,10)
    if boxRect.collidepoint(posx,posy):
        name="MMarine"
def shoot(shotType,size):#function for shooting
    global end#to check which way the bullet should be going
    n=""
    if end=="R":n=""
    if end=="L":n="1"
    if end=="D":n="3"
    if end=="":n="2"
    sx,sy=posx,posy#bullet starts at the position of the character
    bullet=image.load("stuff//"+shotType+n+".png")#the image used for the bullet
    bullet=transform.scale(bullet,(size))#changes bullet to desired size
    screenBuff=screen.copy()#takes a screen shot so it can blit it so
    #each movement frame is visible as the bullet moves
    for i in range (150):
        screen.blit(bullet,(sx,sy))#draws bullet
        display.flip()#so you can see the bullet move
        screen.blit(screenBuff,(0,0))#blits the screenshot between every
        #time the bullet moves
        myClock.tick(1000)#speed at which bullet travels
        if end=="R":sx+=2#these are to know which direction the bullet
        if end=="L":sx-=2#should travel
        if end=="D":sy+=2
        if end=="":sy-=2
def checkCollide():
    global eposx
    global eposy
    global posx
    global posy
    if eposx==posx and eposy==posy:
        slash=image.load("stuff\\slash.png")
        slash=transform.scale(slash,(40,40))
        screen.blit(slash,(eposx,eposy))
        myClock.tick(1000)
def drawScene():
    screen.blit(back1,(0,0))
    good((35,35))
    badMove("alien1",100,200,(55,55))
    badMove("alien1",100,400,(55,55))
    change()

running=True
keys=key.get_pressed()
if keys[K_1]:
    name="MTank"
if keys[K_2]:
    name="MMarine"
if keys[K_3]:
    name="CScout"
while running:
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
    keys=key.get_pressed()
    drawScene()
    if keys[K_SPACE]:
        shoot("shot",(20,20))
    myClock.tick(mclock)
    display.flip()
quit()
