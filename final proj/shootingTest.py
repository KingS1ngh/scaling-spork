#############TO DO##############

from pygame import *
from random import *
from math import *
#MA NAME JEF
#random BS
screen=display.set_mode((800,600))
back1=image.load("back1.png").convert()
back1=transform.scale(back1,(2000,2000))#lolololololololololololololollolololololol
back2=image.load("Back2.png").convert()
back2=transform.scale(back2,(800,600))
guyx=100
guyy=100
UP=273
DOWN=274
RIGHT=275
LEFT=276
SPACE=32
X = 0
Y = 1
VX = 2
VY = 3
C = 4
angle=0
crateNum=0
guy=image.load("Marine/MMarine.png")
al=image.load("alien1/alien1.png")
crat=image.load("stuff/Weapon Crate.png")
myClock=time.Clock()
def distance(x1,y1,x2,y2):
    return((x1-x2)**2+(y1-y2)**2)**0.5
def moveGuy(x,y):
    global guyx
    global guyy
    keys=key.get_pressed()
    if keys[ord("a")]:
        guyx-=8
    if keys[ord("d")]:
        guyx+=8
    if keys[ord("w")]:
        guyy-=8
    if keys[ord("s")]:
        guyy+=8
    if guyx<0:guyx=0
    if guyx>800-35:guyx=800-35
    if guyy<0:guyy=0
    if guyy>600-35:guyy=600-35
    
def turn():
    global angle
    mx,my=mouse.get_pos()
    angle = degrees(atan2(mx-guyx,my-guyy))-180

def guyRect(x,y):
    grect=rect(x,y,x+30,y+30)
    return grect

def vectToXY(mag, ang):
    global badGuys
    rang = radians(ang)
    x = cos(rang) * mag
    y = sin(rang) * mag
    return x,y

def addShot(ang, power):
    shot = [0,0,0,0,(255,0,0)]
    shot[X], shot[Y] = vectToXY(30,ang)
    shot[X] += guyx
    shot[Y] += guyy
    shot[VX], shot[VY] = vectToXY(power,ang)
    return shot

def badMove(bguy,x,y):
    import math
    dist=max(1,distance(bguy[0],bguy[1],x,y))
    moveX=(x-bguy[0])*BADSPEED/dist
    moveY=(y-bguy[1])*BADSPEED/dist
    ang=math.atan2(-moveY,moveX)
    return moveX, moveY, math.degrees(ang)

def moveBadGuys(badguys,guyx,guyy):
    global badGuys
    for bguy in badGuys:
        moveX,moveY,moveAng=badMove(bguy,guyx,guyy)
        bguy[0]+=moveX
        bguy[1]+=moveY
        bguy[2]=moveAng-90
        
def moveShots(shots):
    killlist = []
    for shot in shots:
        shot[X] += shot[VX]
        shot[Y] += shot[VY]
        if shot[X]>guyx+800 or guyx-800>shot[X] or guyy-600>shot[Y] or shot[Y]>guyy+600:
            killlist.append(shot)
    for s in killlist:
        shots.remove(s)
        
def enemyRect(bguy):
    eRect=Rect(bguy[0],bguy[1],40,40)
    return eRect

def checkKill(x,y):
    for bguy in badGuys[:]:
        rect=enemyRect(bguy)
        if rect.collidepoint(x,y):
            badGuys.remove(bguy)
            return True
    return False
def checkHit(rect,x,y):
    if rect.collidepoint(x,y):
        return True
    return False        

def checkWinLevel(badGuys):
    if len(badGuys)==0:
        return True
    return False

def checkUpgrade(crates,guyx,guyy):
    global guy
    global crateNum
    for crate in crates:
        crateRect=Rect(crate[0],crate[1],40,40)
        draw.rect(screen,(0,0,0),(crateRect),1)
        if crateRect.collidepoint (guyx+15,guyy+15):
            crates.remove(crate)
            crateNum+=1
    if crateNum==1:guy=image.load("Marine/Plasma Marine.png")
    if crateNum==2:guy=image.load("Marine/Rifle Marine.png")
    if crateNum==3:guy=image.load("Marine/Sniper Marine.png")
    
def drawScene(screen):
    screen.blit(back2,(0,0))
    pic=transform.scale(guy,(50,50))
    turn()
    pic=transform.rotate(pic,angle)
    screen.blit(pic,(guyx-17,guyy-17))
    shoot1=image.load("stuff/shot.png")
    shoot1=transform.scale(shoot1,(10,10))
    shoot2=image.load("stuff/redbullet.png").convert()
    shoot2=transform.scale(shoot2,(7,7))
    for crate in crates:
        weaponcrate=transform.scale(crat,(40,40))
        screen.blit(weaponcrate,(crate[0],crate[1]))
        checkUpgrade(crates,guyx,guyy)
    for shot in shots[:]:
        screen.blit(shoot2,(int(shot[X]),int(shot[Y])))
        #draw.circle(screen,(30,30,255),(int(shot[X]),int(shot[Y])),3)
        used = checkKill(shot[X],shot[Y])
        if used:
            shots.remove(shot)
    for bguy in badGuys:
        badguy1=transform.scale(al,(50,50))
        moveBadGuys(badGuys,guyx,guyy)
        badMove(bguy,guyx,guyy)
        badguy1=transform.rotate(badguy1,bguy[2])
        screen.blit(badguy1,bguy[:2])
    win=checkWinLevel(badGuys)
    if win:
        screen.fill((211,211,211))
        screen.blit((transform.scale((image.load("stuff/victory.png")),(1000,600))),(-100,0))
    display.flip()
running=True
shots=[]
gunAng=0.0
power=10
gunHeat=0
BADSPEED=0.5
badGuys=[[randint(0,800),randint(0,600),0],[randint(0,800),randint(0,600),0],[randint(0,800),randint(0,600),0],[randint(0,800),randint(0,600),0],[randint(0,800),randint(0,600),0],[randint(0,800),randint(0,600),0],[randint(0,800),randint(0,600),0],[randint(0,800),randint(0,600),0]]
crates=[[200,300],[500,70],[400,400]]
while running:
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
    keys=key.get_pressed()
    mb=mouse.get_pressed()
    if mb[0]==1 and gunHeat<=0:
        gunHeat=10
        shots.append(addShot(-angle-90,power))
    gunHeat -= 1
    moveShots(shots)
    moveGuy(guyx,guyy)
    drawScene(screen)
    myClock.tick(60)
quit()
