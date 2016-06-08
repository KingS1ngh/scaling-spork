from pygame import *
from random import *
from math import *

<<<<<<< HEAD
screen = display.set_mode((1024, 768), FULLSCREEN)
myClock = time.Clock()
running = True
pos = ''
=======
screen = display.set_mode((1350, 768), FULLSCREEN)
back1 = image.load("back1.png").convert()
back1 = transform.scale(back1, (2000, 2000))
back2 = image.load("Back2.png").convert()
back2 = transform.scale(back2, (800, 600))

>>>>>>> origin/master
guyx = 100
guyy = 100
SPACE = 32
X = 0
Y = 1
VX = 2
VY = 3
C = 4
angle = 0
crateNum = 0
bombPics = []
MarineHealth = 70
TankHealth = 100
ScoutHealth = 30
yellow = 255, 255, 0
red = 255, 0, 0
page = 'title'
mx, my = mouse.get_pos()
mb = mouse.get_pressed()
Class = 'Scout'
weapon = 'Rifle'
shots = []
gunAng = 0.0
power = 3.0
gunHeat = 0
guy = image.load('Pictures/'+weapon+' '+Class+'.png')
keys = key.get_pressed()
BADSPEED = 1
badGuys = [[randint(0, 800), randint(0, 600), 0], [randint(0, 800), randint(0, 600), 0],
           [randint(0, 800), randint(0, 600), 0], [randint(0, 800), randint(0, 600), 0],
           [randint(0, 800), randint(0, 600), 0], [randint(0, 800), randint(0, 600), 0],
           [randint(0, 800), randint(0, 600), 0], [randint(0, 800), randint(0, 600), 0]]
Wcrates = [[200, 300], [500, 70], [400, 400]]
bombs = []

titleScreen = image.load('Pictures/Title Screen.png').convert()
titleBack = transform.scale(titleScreen, (1035, 800))
campaignButtonPic = image.load('Pictures/Campaign Pressed.png')
campaignButton = transform.scale(campaignButtonPic, (200, 50))

endlessButtonPic = image.load('Pictures/Endless Pressed.png')
endlessButton = transform.scale(endlessButtonPic, (200, 50))

armoryButtonPic = image.load('Pictures/Armory Pressed.png')
armoryButton = transform.scale(armoryButtonPic, (200, 50))

newPic = image.load('Pictures/New Game Button.png')
newButton = transform.scale(newPic, (200, 50))
loadPic = image.load('Pictures/Load Game Button.png')
loadButton = transform.scale(loadPic, (200, 50))

classScreen = image.load('Pictures/Class Selection Background.jpg').convert()
classBack = transform.scale(classScreen, (1035, 800))

scout1 = image.load('Pictures/Rifle Scout.png')
rScout = transform.scale(scout1, (50, 50))
marine1 = image.load('Pictures/Rifle Marine.png')
rMarine = transform.scale(marine1, (50, 50))
tank1 = image.load('Pictures/Pistol Tank.png')
pTank = transform.scale(tank1, (50, 50))

classScreenName = image.load('Pictures/pick your class.png')
classTitle = transform.scale(classScreenName, (400, 100))
startPic = image.load('Pictures/Start Button.png')
start = transform.scale(startPic, (200, 75))
scoutName = image.load('Pictures/Scout Name.png')
scoutLable = transform.scale(scoutName, (150, 50))
scoutWords = image.load('Pictures/Scout Stats.png')
scoutInfo = transform.scale(scoutWords, (300, 175))
marineName = image.load('Pictures/Marine Name.png')
marineLable = transform.scale(marineName, (150, 50))
marineWords = image.load('Pictures/Marine Stats.png')
marineInfo = transform.scale(marineWords, (300, 175))
tankName = image.load('Pictures/Tank Name.png')
tankLable = transform.scale(tankName, (100, 50))
tankWords = image.load('Pictures/Tank Stats.png')
tankInfo = transform.scale(tankWords, (300, 175))

backOne = image.load('Pictures/Level One Background.png')
firstBack = transform.scale(backOne, (800, 600))
rilfeScout = image.load('Pictures/Rifle Scout.png')
back1 = image.load("Pictures/Level One Background.png").convert()
back1 = transform.scale(back1, (2000, 2000))
badguy1 = image.load("Pictures/Alien 1.png")
badguy1 = transform.scale(badguy1, (60, 60))
crat = image.load("Pictures/Crate 1.png")

for i in range(1, 17):
    bombPics+=[(image.load("explosion/explosion"+str(i)+".png"))]


def distance(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5


def moveGuy(x, y):
    global guyx
    global guyy
    keys = key.get_pressed()
    if keys[ord("a")]:
        guyx -= 5
    if keys[ord("d")]:
        guyx += 5
    if keys[ord("w")]:
        guyy -= 5
    if keys[ord("s")]:
        guyy += 5
    if guyx < 0: guyx = 0
    if guyx > 1350 - 35: guyx = 1350 - 35
    if guyy < 0: guyy = 0
    if guyy > 768 - 35: guyy = 768 - 35


def turn():
    global angle
    mx, my = mouse.get_pos()
    angle = degrees(atan2(mx-guyx, my-guyy))-180


def guyRect(x, y):
    grect = Rect(x, y, 35, 35)
    return grect


def vectToXY(mag, ang):
    rang = radians(ang)
    x = cos(rang)*mag
    y = sin(rang)*mag
    return x, y


def addShot(ang, power):
    shot = [0, 0, 0, 0, (255, 0, 0)]
    shot[X], shot[Y] = vectToXY(30, ang)
    shot[X] += guyx
    shot[Y] += guyy
    shot[VX], shot[VY] = vectToXY(power, ang)
    return shot


def badMove(bguy, x, y):
    import math
    dist = max(1, distance(bguy[0], bguy[1], x, y))
    moveX = (x-bguy[0])*BADSPEED/dist
    moveY = (y-bguy[1])*BADSPEED/dist
    ang = math.atan2(-moveY, moveX)
    return moveX, moveY, math.degrees(ang)


def moveBadGuys(bguy, guyx, guyy):
    moveX, moveY, moveAng = badMove(bguy, guyx, guyy)
    bguy[0] += moveX
    bguy[1] += moveY
    bguy[2] = moveAng-90


def moveShots(shots):
    killlist = []
    for shot in shots:
        shot[X] += shot[VX]
        shot[Y] += shot[VY]
        if shot[X] > guyx+800 or guyx-800 > shot[X] or guyy-600 > shot[Y] or shot[Y] > guyy+600:
            killlist.append(shot)
    for s in killlist:
        shots.remove(s)


def enemyRect(bguy):
    eRect = Rect(bguy[0]+35, bguy[1]+35, 30, 30)
    return eRect


def checkKill(x, y):
    for bguy in badGuys[:]:
        rect = enemyRect(bguy)
        if rect.collidepoint(x, y):
            badGuys.remove(bguy)
            return True
    return False

def checkHit(rect):
    global bombs
    global MarineHealth
    global badGuys
    for bguy in badGuys:
        if rect.collidepoint(bguy[0]+35, bguy[1]+35):
            MarineHealth -= 10
            badGuys.remove(bguy)
            bombs.append([bguy[0], bguy[1]])


def checkWinLevel(badGuys):
    if len(badGuys) == 0:
        return True
    return False


def checkLoseLevel(health):
    if health <= 0:
        return True


def checkUpgrade(Wcrates, guyx, guyy):
    global guy
    global crateNum
    global bullet
    for crate in Wcrates:

        crateRect = Rect(crate[0], crate[1], 40, 40)
        draw.rect(screen, (0, 0, 0), crateRect, 1)

        if crateRect.collidepoint(guyx + 15, guyy + 15):
            Wcrates.remove(crate)
            crateNum += 1

<<<<<<< HEAD
    if crateNum == 1: guy = image.load("Pictures/Plasma Marine.png")
    if crateNum == 2: guy = image.load("Pictures/Rifle Marine.png")
    if crateNum == 3: guy = image.load("Pictures/Sniper Marine.png")
=======
    if crateNum == 1:
        bullet = transform.scale((image.load("stuff/Plasma Flash.png")), (30, 30))
        guy = image.load("Marine/Plasma Marine.png")
    if crateNum == 2:
        bullet = transform.scale((image.load("stuff/shot.png")), (12, 12))
        guy = image.load("Marine/Rifle Marine.png")
    if crateNum == 3: guy = image.load("Marine/Sniper Marine.png")
>>>>>>> origin/master



def goodHealthMeter(health):
    healthRect = Rect(10, 10, 10+(health*2), 20)
    return healthRect


<<<<<<< HEAD
def title():
    global running
    startRect = Rect(422, 525, 200, 75)

    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
        screen.blit(titleBack, (0, 0))
        screen.blit(start, (425, 525))
        draw.rect(screen, yellow, startRect, 2)
        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        if startRect.collidepoint(mx, my) and mb[0] == 1:
            return 'gameLoad'
        display.flip()


def gameLoad():
    global running
    gameLoadRunning = True
    newRect = Rect(230, 525, 198, 45)
    loadRect = Rect(595, 525, 198, 45)

    while gameLoadRunning:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                gameLoadRunning = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_ESCAPE:
                    gameLoadRunning = False
        screen.blit(titleBack, (0, 0))
        screen.blit(newButton, (230, 525))
        screen.blit(loadButton, (595, 525))

        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        draw.rect(screen, yellow, newRect, 2)
        draw.rect(screen, yellow, loadRect, 2)
        if newRect.collidepoint(mx, my) and mb[0] == 1:
            return 'menu'
        if loadRect.collidepoint(mx, my) and mb[0] == 1:
            return 'load'
        display.flip()
    return 'title'


def load():
    global running
    loadRunning = True

    while loadRunning:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                loadRunning = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_ESCAPE:
                    loadRunning = False
        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        screen.blit(titleBack, (0, 0))
        saveRects = [Rect(305, 375, 190, 55), Rect(320, 450, 160, 45), Rect(320, 515, 160, 50)]
        myFiles = glob.glob('*.txt')
        for s, f in zip(saveRects, myFiles):
            draw.rect(screen, yellow, s, 2)
            if len(myFiles) >= 1:
                screen.blit(armoryButton, (300, 375))
            if len(myFiles) >= 2:
                screen.blit(armoryButton, (300, 450))
            if len(myFiles) == 3:
                screen.blit(armoryButton, (300, 515))
        if Rect(305, 375, 190, 55).collidepoint(mx, my) and mb[0] == 1:
            saveFile = open('Save 1.txt', 'r')
            save = saveFile.readlines()
            saveFile.close()
            print(save)
        display.flip()
    return 'title'


def menu():
    global running
    menuRunning = True
    buttons = [Rect(305, 375, 190, 55), Rect(320, 450, 160, 45), Rect(320, 515, 160, 50)]
    screens = ['classSelect', 'endless', 'armory']

    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                menuRunning = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_ESCAPE:
                    menuRunning = False
        screen.blit(titleBack, (0, 0))
        screen.blit(campaignButton, (300, 375))
        screen.blit(endlessButton, (300, 450))
        screen.blit(armoryButton, (300, 510))

        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        for b, s in zip(buttons, screens):
            draw.rect(screen, yellow, b, 2)
            if b.collidepoint(mx, my) and mb[0] == 1:
                return s
        display.flip()
    return 'title'


def classSelect():
    global running
    classSelectRunning = True
    global Class
    global weapon

    while classSelectRunning:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                classSelectRunning = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_ESCAPE:
                    classSelectRunning = False
        scoutRect = Rect(88, 290, 75, 75)
        marineRect = Rect(362, 290, 75, 75)
        tankRect = Rect(638, 290, 75, 75)
        startRect = Rect(300, 475, 200, 75)
        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()

        screen.blit(classBack, (0, 0))
        screen.blit(rScout, (100, 300))
        screen.blit(rMarine, (375, 300))
        screen.blit(pTank, (650, 300))
        screen.blit(classTitle, (210, 25))
        screen.blit(scoutLable, (50, 375))
        screen.blit(marineLable, (325, 375))
        screen.blit(tankLable, (625, 375))
        screenBuff = screen.copy()
        if scoutRect.collidepoint(mx, my) and mb[0] == 1:
            Class = 'Scout'
            weapon = 'Rifle'
        if Class == 'Scout':
            screen.blit(screenBuff, (0, 0))
            draw.rect(screen, red, scoutRect, 2)
            screen.blit(start, (300, 475))
            screen.blit(scoutInfo, (250, 115))
            screenBuff = screen.copy()
        if Class != 'Scout':
            screen.blit(screenBuff, (0, 0))
            screenBuff = screen.copy()
        if marineRect.collidepoint(mx, my) and mb[0] == 1:
            Class = 'Marine'
            weapon = 'Rifle'
        if Class == 'Marine':
            screen.blit(screenBuff, (0, 0))
            draw.rect(screen, red, marineRect, 2)
            screen.blit(start, (300, 475))
            screen.blit(marineInfo, (250, 115))
            screenBuff = screen.copy()
        if Class != 'Marine':
            screen.blit(screenBuff, (0, 0))
            screenBuff = screen.copy()
        if tankRect.collidepoint(mx, my) and mb[0] == 1:
            Class = 'Tank'
            weapon = 'Pistol'
        if Class == 'Tank':
            screen.blit(screenBuff, (0, 0))
            draw.rect(screen, red, tankRect, 2)
            screen.blit(start, (300, 475))
            screen.blit(tankInfo, (250, 115))
            screenBuff = screen.copy()
        if Class != 'Tank':
            screen.blit(screenBuff, (0, 0))
            screenBuff = screen.copy()
        if startRect.collidepoint(mx, my) and mb[0] == 1 and Class != '':
            return 'room_1'
        display.flip()
    return 'menu'


def endless():
    global running
    endlessRunning = True

    while endlessRunning:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                endlessRunning = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_ESCAPE:
                    endlessRunning = False
        display.flip()
    return 'menu'


def armory():
    global running
    armoryRunning = True

    while armoryRunning:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                armoryRunning = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_ESCAPE:
                    armoryRunning = False
        display.flip()
    return 'menu'


def room_1():
    global running
    global gunHeat
    global Class
    global weapon
    room_1Running = True

    while room_1Running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                room_1Running = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_ESCAPE:
                    room_1Running = False

        keys = key.get_pressed()
        if keys[27]:
            break

        mb = mouse.get_pressed()
        if mb[0] == 1 and gunHeat <= 0:
            gunHeat = 10
            shots.append(addShot(-angle - 90, power))

        gunHeat -= 1
        moveShots(shots)
        moveGuy(guyx, guyy)
        myClock.tick(60)

        screen.blit(back1, (0, 0))
        pic = transform.scale(guy, (50, 50))
        turn()
        pic = transform.rotate(pic, angle)
        screen.blit(pic, (guyx - 17, guyy - 17))
        shoot1 = image.load("Pictures/shot.png")
        shoot1 = transform.scale(shoot1, (10, 10))
        shoot2 = image.load("Pictures/redbullet.png").convert()
        shoot2 = transform.scale(shoot2, (7, 7))

        for crate in Wcrates:
            weaponcrate = transform.scale(crat, (40, 40))
            screen.blit(weaponcrate, (crate[0], crate[1]))
            checkUpgrade(Wcrates, guyx, guyy)

        for shot in shots[:]:
            screen.blit(shoot2, (int(shot[X]), int(shot[Y])))
            #draw.circle(screen,(30,30,255),(int(shot[X]),int(shot[Y])),3)
            used = checkKill(shot[X], shot[Y])

            if used:
                shots.remove(shot)

        for bguy in badGuys:
            moveBadGuys(bguy, guyx, guyy)
            alien1 = transform.rotate(badguy1, bguy[2])
            screen.blit(alien1, bguy[:2])
            eRect = enemyRect(bguy)

        grect = guyRect(guyx, guyy)
        draw.rect(screen, (0, 0, 0), (grect), 1)
        checkHit(grect)
        healthRect = goodHealthMeter(MarineHealth)
        draw.rect(screen, (0, 255, 0), healthRect)

        win = checkWinLevel(badGuys)
        if win:
            screen.fill((211, 211, 211))
            screen.blit((transform.scale((image.load("Pictures/victory.png")), (1000, 600))), (10, 0))

        lose = checkLoseLevel(MarineHealth)
        if lose:
            screen.fill((0, 0, 0))
        display.flip()
    return 'title'


while page != 'exit':
    if page == 'title':
        page = title()
    if page == 'menu':
        page = menu()
    if page == 'gameLoad':
        page = gameLoad()
    if page == 'load':
        page = load()
    if page == 'classSelect':
        page = classSelect()
    if page == 'endless':
        page = endless()
    if page == 'armory':
        page = armory()
    if page == 'room_1':
        page = room_1()
    if not running:
        page = 'exit'
=======
def drawScene(screen):
    FRAME=0
    screen.blit(back1, (0, 0))
    pic = transform.scale(guy, (50, 50))
    turn()
    pic = transform.rotate(pic, angle)
    screen.blit(pic, (guyx - 17, guyy - 17))
    shoot1 = image.load("stuff/shot.png")
    shoot1 = transform.scale(shoot1, (10, 10))

    for crate in Wcrates:
        weaponcrate = transform.scale(crat, (40, 40))
        screen.blit(weaponcrate, (crate[0], crate[1]))
        checkUpgrade(Wcrates, guyx, guyy)

    for shot in shots[:]:
        screen.blit(bullet, (int(shot[X]), int(shot[Y])))
        # draw.circle(screen,(30,30,255),(int(shot[X]),int(shot[Y])),3)
        used = checkKill(shot[X], shot[Y])

        if used:
            shots.remove(shot)

    for bguy in badGuys:
        moveBadGuys(bguy, guyx, guyy)
        alien1 = transform.rotate(badguy1, bguy[2])
        screen.blit(alien1, bguy[:2])
        eRect = enemyRect(bguy)

    grect = guyRect(guyx, guyy)
    checkHit(grect)
    healthRect = goodHealthMeter(MarineHealth)
    draw.rect(screen, (0, 255, 0), (healthRect))

    for bomb in bombs:
        for pic in bombPics[:]:
            screen.blit(pic,(bomb[0],bomb[1]))
            bombPics.remove(pic)
            display.flip()

    win = checkWinLevel(badGuys)
#    if win:
#        screen.fill((211, 211, 211))
#        screen.blit((transform.scale((image.load("stuff/victory.png")), (1000, 600))), (10, 0))

    lose = checkLoseLevel(MarineHealth)
    if lose:
        screen.fill((0, 0, 0))
    display.flip()


running = True
bullet = image.load("stuff/redbullet.png").convert()
bullet = transform.scale(bullet, (7, 7))
shots = []
gunAng = 0.0
power = 10
gunHeat = 0
BADSPEED = 2
badGuys = [[randint(0, 800), randint(0, 600), 0], [randint(0, 800), randint(0, 600), 0],
           [randint(0, 800), randint(0, 600), 0], [randint(0, 800), randint(0, 600), 0],
           [randint(0, 800), randint(0, 600), 0], [randint(0, 800), randint(0, 600), 0],
           [randint(0, 800), randint(0, 600), 0], [randint(0, 800), randint(0, 600), 0]]
Wcrates = [[200, 300], [500, 700], [1200, 500]]
badguy1 = transform.scale(badguy1, (60, 60))
bombs = []

while running:
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False

    keys = key.get_pressed()
    if keys[27]:
        break

    mb = mouse.get_pressed()
    if mb[0] == 1 and gunHeat <= 0:
        gunHeat = 10
        shots.append(addShot(-angle - 90, power))

    gunHeat -= 1
    moveShots(shots)
    moveGuy(guyx, guyy)
    drawScene(screen)
    myClock.tick(60)
>>>>>>> origin/master
quit()
