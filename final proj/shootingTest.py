from pygame import *
from random import *
from math import *
import glob

screen = display.set_mode((1024, 700))
myClock = time.Clock()
running = True
pos = ''
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
mx, my = mouse.get_pos()
mb = mouse.get_pressed()
Class = 'Scout'
weapon = 'Rifle'
guy = image.load('Pictures/'+weapon+' '+Class+'.png')
shots = []
gunAng = 0.0
power = 5.0
gunHeat = 0
keys = key.get_pressed()
BADSPEED = 1
badGuys = []
Wcrates = [[200, 300], [500, 70], [400, 400]]
bombs = []
right = (924, 325)
up = (487, 0)
left = (0, 325)
down = (487, 600)
rightRect = Rect(934, 330, 80, 30)
upRect = Rect(492, 5, 30, 80)
leftRect = Rect(5, 335, 80, 30)
downRect = Rect(497, 605, 30, 80)
holeRect = Rect(512, 350, 50, 50)

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
back2 = image.load('Pictures/Level Two Background.png').convert()
back2 = transform.scale(back2, (2000, 2000))
badguy1 = image.load("Pictures/Alien 1.png")
badguy1 = transform.scale(badguy1, (60, 60))
crat = image.load("Pictures/Crate 1.png")
arrow = image.load('Pictures/arrow.png')
rightArrow = transform.scale(arrow, (100,50))
upArrow = transform.rotate(rightArrow, (90))
leftArrow = transform.rotate(rightArrow, (180))
downArrow = transform.rotate(rightArrow, (270))
hole = image.load('Pictures/hole.png')
hole = transform.scale(hole, (50,50))


for i in range(1, 17):
    bombPics.append(image.load("explosion/explosion"+str(i)+".png"))


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
    eRect = Rect(bguy[0]+35, bguy[1]+35, 40, 40)
    return eRect


def checkKill(x, y):
    for bguy in badGuys[:]:
        rect = enemyRect(bguy)
        if rect.collidepoint(x, y):
            badGuys.remove(bguy)


def checkHit(rect):
    global bombs
    global MarineHealth
    global badGuys
    for bguy in badGuys:
        if rect.collidepoint(bguy[0]+35, bguy[1]+35):
            MarineHealth -= 10
            badGuys.remove(bguy)
            bombs.append([bguy[0], bguy[1]])
            return True
    return False


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
    global weapon
    for crate in Wcrates:

        crateRect = Rect(crate[0], crate[1], 40, 40)

        if crateRect.collidepoint(guyx + 15, guyy + 15):
            crateNum = crate[2]
            Wcrates.remove(crate)

    if crateNum == 1 and Class == 'Scout': weapon = 'Sniper'
    if crateNum == 1 and Class == 'Marine': weapon = 'Plasma'
    if crateNum == 1 and Class == 'Tank': weapon = 'Shotgun'
    if crateNum == 2 and Class == 'Scout': weapon = 'Cannon'
    if crateNum == 2 and Class == 'Marine': weapon = 'Sniper'
    if crateNum == 2 and Class == 'Tank': weapon = 'Minigun'
    if crateNum == 3 and Class == 'Marine': weapon = 'Machine'
    if crateNum == 3 and Class == 'Tank': weapon = 'Melee'


def goodHealthMeter(health):
    healthRect = Rect(10, 10, 10+(health*2), 20)
    return healthRect


def drawScene(badGuys,arrows,back):
    screen.blit(back, (0, 0))
    guy = image.load('Pictures/' + weapon + ' ' + Class + '.png')
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
    draw.rect(screen, (0, 255, 0), healthRect)

    win = checkWinLevel(badGuys)
    if win:
        for arrow in arrows:
            if arrow == right:
                screen.blit(rightArrow, right)
            if arrow == up:
                screen.blit(upArrow, up)
            if arrow == left:
                screen.blit(leftArrow, left)
            if arrow == down:
                screen.blit(downArrow, down)
            if arrow == hole:
                screen.blit(hole, (487, 325))

    lose = checkLoseLevel(MarineHealth)
    if lose:
        screen.fill((0, 0, 0))
    display.flip()


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
        saveRects = [Rect(435, 483, 160, 50), Rect(435, 556, 160, 50), Rect(435, 623, 160, 50)]
        myFiles = glob.glob('*.txt')
        for s, f in zip(saveRects, myFiles):
            draw.rect(screen, yellow, s, 2)
            if len(myFiles) >= 1:
                screen.blit(armoryButton, (415, 480))
            if len(myFiles) >= 2:
                screen.blit(armoryButton, (415, 553))
            if len(myFiles) == 3:
                screen.blit(armoryButton, (415, 620))
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
    buttons = [Rect(420, 480, 190, 55), Rect(435, 553, 160, 45), Rect(435, 623, 160, 50)]
    screens = ['classSelect', 'endless', 'armory']
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()

    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                menuRunning = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_ESCAPE:
                    menuRunning = False
        screen.blit(titleBack, (0, 0))
        screen.blit(campaignButton, (415, 480))
        screen.blit(endlessButton, (415, 553))
        screen.blit(armoryButton, (415, 620))

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
        scoutRect = Rect(173, 390, 75, 75)
        marineRect = Rect(470, 390, 75, 75)
        tankRect = Rect(787, 390, 75, 75)
        startRect = Rect(410, 555, 200, 75)
        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()

        screen.blit(classBack, (0, 0))
        screen.blit(rScout, (185, 400))
        screen.blit(rMarine, (483, 400))
        screen.blit(pTank, (800, 400))
        screen.blit(classTitle, (325, 100))
        screen.blit(scoutLable, (140, 475))
        screen.blit(marineLable, (435, 475))
        screen.blit(tankLable, (775, 475))
        screenBuff = screen.copy()
        if scoutRect.collidepoint(mx, my) and mb[0] == 1:
            Class = 'Scout'
            weapon = 'Rifle'
        if Class == 'Scout':
            screen.blit(screenBuff, (0, 0))
            draw.rect(screen, red, scoutRect, 2)
            screen.blit(start, (410, 555))
            screen.blit(scoutInfo, (360, 200))
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
            screen.blit(start, (410, 555))
            screen.blit(marineInfo, (360, 200))
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
            screen.blit(start, (410, 555))
            screen.blit(tankInfo, (360, 200))
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
    global Class
    global gunHeat
    global weapon
    global badGuys
    global Wcrates
    global guyx
    global guyy
    room_1Running = True
    badGuys=[[100,700,0],[10,500,0]]
    Wcrates=[]
    arrows = [up]

    while room_1Running:
        print(round(myClock.get_fps()))
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
            gunHeat = 15
            shots.append(addShot(-angle - 90, power))

        gunHeat -= 1
        moveShots(shots)
        drawScene(badGuys, arrows,back1)
        moveGuy(guyx, guyy)
        myClock.tick(60)
        display.flip()


        win = checkWinLevel(badGuys)
        if win:
            if upRect.collidepoint(guyx, guyy):
                guyx = 512
                guyy = 660
                return 'room_2'


def room_2():
    global running
    global Class
    global gunHeat
    global weapon
    global badGuys
    global Wcrates
    global guyx
    global guyy
    room_2Running = True
    badGuys=[[100,700,0],[10,500,0],[200,400,0],[500,450,0]]
    Wcrates=[]
    arrows = [up,right,left,down]

    while room_2Running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                room_2Running = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_ESCAPE:
                    room_2Running = False

        keys = key.get_pressed()
        if keys[27]:
            break

        mb = mouse.get_pressed()
        if mb[0] == 1 and gunHeat <= 0:
            gunHeat = 15
            shots.append(addShot(-angle - 90, power))

        gunHeat -= 1
        moveShots(shots)
        drawScene(badGuys, arrows, back1)
        moveGuy(guyx, guyy)
        myClock.tick(60)
        display.flip()

        win = checkWinLevel(badGuys)
        if win:
            if upRect.collidepoint(guyx, guyy):
                guyx = 512
                guyy = 660
                return 'room_6'
            if leftRect.collidepoint(guyx, guyy):
                guyx = 1000
                guyy = 350
                return 'room_3'
            if rightRect.collidepoint(guyx, guyy):
                guyx = 25
                guyy = 350
                return 'room_4'
            if downRect.collidepoint(guyx, guyy):
                guyx = 512
                guyy = 25
                return 'room_1'
    return 'title'


def room_3():
    global running
    global Class
    global gunHeat
    global weapon
    global badGuys
    global Wcrates
    global guyx
    global guyy
    room_3Running = True
    badGuys=[[100,700,0],[10,500,0],[200,400,0],[500,450,0]]
    Wcrates=[]
    arrows = [up, right]

    while room_3Running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                room_3Running = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_ESCAPE:
                    room_3Running = False

        keys = key.get_pressed()
        if keys[27]:
            break

        mb = mouse.get_pressed()
        if mb[0] == 1 and gunHeat <= 0:
            gunHeat = 15
            shots.append(addShot(-angle - 90, power))

        gunHeat -= 1
        moveShots(shots)
        drawScene(badGuys, arrows, back1)
        moveGuy(guyx, guyy)
        myClock.tick(60)
        display.flip()

        win = checkWinLevel(badGuys)
        if win:
            if upRect.collidepoint(guyx, guyy):
                guyx = 512
                guyy = 660
                return 'room_5'
            if rightRect.collidepoint(guyx, guyy):
                guyx = 25
                guyy = 350
                return 'room_2'
    return 'title'


def room_4():
    global running
    global Class
    global gunHeat
    global weapon
    global badGuys
    global Wcrates
    global guyx
    global guyy
    room_4Running = True
    badGuys=[[100,700,0],[10,500,0],[200,400,0],[500,450,0]]
    Wcrates=[[100,600,1]]
    arrows = [up, left]

    while room_4Running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                room_4Running = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_ESCAPE:
                    room_4Running = False

        keys = key.get_pressed()
        if keys[27]:
            break

        mb = mouse.get_pressed()
        if mb[0] == 1 and gunHeat <= 0:
            gunHeat = 15
            shots.append(addShot(-angle - 90, power))

        gunHeat -= 1
        moveShots(shots)
        drawScene(badGuys, arrows, back1)
        moveGuy(guyx, guyy)
        myClock.tick(60)
        display.flip()

        win = checkWinLevel(badGuys)
        if win:
            if upRect.collidepoint(guyx, guyy):
                guyx = 512
                guyy = 660
                return 'room_7'
            if leftRect.collidepoint(guyx, guyy):
                guyx = 1000
                guyy = 350
                return 'room_2'
    return 'title'


def room_5():
    global running
    global Class
    global gunHeat
    global weapon
    global badGuys
    global Wcrates
    global guyx
    global guyy
    room_5Running = True
    badGuys=[[100,700,0],[10,500,0],[200,400,0],[500,450,0]]
    Wcrates=[]
    arrows = [up, right, down]

    while room_5Running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                room_5Running = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_ESCAPE:
                    room_5Running = False

        keys = key.get_pressed()
        if keys[27]:
            break

        mb = mouse.get_pressed()
        if mb[0] == 1 and gunHeat <= 0:
            gunHeat = 15
            shots.append(addShot(-angle - 90, power))

        gunHeat -= 1
        moveShots(shots)
        drawScene(badGuys, arrows, back1)
        moveGuy(guyx, guyy)
        myClock.tick(60)
        display.flip()

        win = checkWinLevel(badGuys)
        if win:
            if upRect.collidepoint(guyx, guyy):
                guyx = 512
                guyy = 660
                return 'room_8'
            if rightRect.collidepoint(guyx, guyy):
                guyx = 25
                guyy = 350
                return 'room_6'
            if downRect.collidepoint(guyx, guyy):
                guyx = 512
                guyy = 25
                return 'room_3'
    return 'title'


def room_6():
    global running
    global Class
    global gunHeat
    global weapon
    global badGuys
    global Wcrates
    global guyx
    global guyy
    room_6Running = True
    badGuys=[[100,700,0],[10,500,0],[200,400,0],[500,450,0]]
    Wcrates=[]
    arrows = [up,right,left,down]

    while room_6Running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                room_6Running = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_ESCAPE:
                    room_6Running = False

        keys = key.get_pressed()
        if keys[27]:
            break

        mb = mouse.get_pressed()
        if mb[0] == 1 and gunHeat <= 0:
            gunHeat = 15
            shots.append(addShot(-angle - 90, power))

        gunHeat -= 1
        moveShots(shots)
        drawScene(badGuys, arrows, back1)
        moveGuy(guyx, guyy)
        myClock.tick(60)
        display.flip()

        win = checkWinLevel(badGuys)
        if win:
            if upRect.collidepoint(guyx, guyy):
                guyx = 512
                guyy = 660
                return 'room_9'
            if leftRect.collidepoint(guyx, guyy):
                guyx = 1000
                guyy = 350
                return 'room_5'
            if rightRect.collidepoint(guyx, guyy):
                guyx = 25
                guyy = 350
                return 'room_7'
            if downRect.collidepoint(guyx, guyy):
                guyx = 512
                guyy = 25
                return 'room_2'
    return 'title'


def room_7():
    global running
    global Class
    global gunHeat
    global weapon
    global badGuys
    global Wcrates
    global guyx
    global guyy
    room_7Running = True
    badGuys=[[100,700,0],[10,500,0],[200,400,0],[500,450,0]]
    Wcrates=[]
    arrows = [up,left,down]

    while room_7Running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                room_7Running = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_ESCAPE:
                    room_7Running = False

        keys = key.get_pressed()
        if keys[27]:
            break

        mb = mouse.get_pressed()
        if mb[0] == 1 and gunHeat <= 0:
            gunHeat = 15
            shots.append(addShot(-angle - 90, power))

        gunHeat -= 1
        moveShots(shots)
        drawScene(badGuys, arrows, back1)
        moveGuy(guyx, guyy)
        myClock.tick(60)
        display.flip()

        win = checkWinLevel(badGuys)
        if win:
            if upRect.collidepoint(guyx, guyy):
                guyx = 512
                guyy = 660
                return 'room_10'
            if leftRect.collidepoint(guyx, guyy):
                guyx = 1000
                guyy = 350
                return 'room_6'
            if downRect.collidepoint(guyx, guyy):
                guyx = 512
                guyy = 25
                return 'room_4'
    return 'title'


def room_8():
    global running
    global Class
    global gunHeat
    global weapon
    global badGuys
    global Wcrates
    global guyx
    global guyy
    room_8Running = True
    badGuys=[[100,700,0],[10,500,0],[200,400,0],[500,450,0]]
    Wcrates=[[100,600,2]]
    arrows = [up,right,down]

    while room_8Running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                room_8Running = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_ESCAPE:
                    room_8Running = False

        keys = key.get_pressed()
        if keys[27]:
            break

        mb = mouse.get_pressed()
        if mb[0] == 1 and gunHeat <= 0:
            gunHeat = 15
            shots.append(addShot(-angle - 90, power))

        gunHeat -= 1
        moveShots(shots)
        drawScene(badGuys, arrows, back1)
        moveGuy(guyx, guyy)
        myClock.tick(60)
        display.flip()

        win = checkWinLevel(badGuys)
        if win:
            if upRect.collidepoint(guyx, guyy):
                guyx = 512
                guyy = 660
                return 'room_12'
            if rightRect.collidepoint(guyx, guyy):
                guyx = 25
                guyy = 350
                return 'room_9'
            if downRect.collidepoint(guyx, guyy):
                guyx = 512
                guyy = 25
                return 'room_5'
    return 'title'


def room_9():
    global running
    global Class
    global gunHeat
    global weapon
    global badGuys
    global Wcrates
    global guyx
    global guyy
    room_9Running = True
    badGuys=[[100,700,0],[10,500,0],[200,400,0],[500,450,0]]
    Wcrates=[]
    arrows = [up,right,left,down]

    while room_9Running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                room_9Running = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_ESCAPE:
                    room_9Running = False

        keys = key.get_pressed()
        if keys[27]:
            break

        mb = mouse.get_pressed()
        if mb[0] == 1 and gunHeat <= 0:
            gunHeat = 15
            shots.append(addShot(-angle - 90, power))

        gunHeat -= 1
        moveShots(shots)
        drawScene(badGuys, arrows, back1)
        moveGuy(guyx, guyy)
        myClock.tick(60)
        display.flip()

        win = checkWinLevel(badGuys)
        if win:
            if upRect.collidepoint(guyx, guyy):
                guyx = 512
                guyy = 660
                return 'room_11'
            if leftRect.collidepoint(guyx, guyy):
                guyx = 1000
                guyy = 350
                return 'room_8'
            if rightRect.collidepoint(guyx, guyy):
                guyx = 25
                guyy = 350
                return 'room_10'
            if downRect.collidepoint(guyx, guyy):
                guyx = 512
                guyy = 25
                return 'room_6'
    return 'title'


def room_10():
    global running
    global Class
    global gunHeat
    global weapon
    global badGuys
    global Wcrates
    global guyx
    global guyy
    room_10Running = True
    badGuys=[[100,700,0],[10,500,0],[200,400,0],[500,450,0]]
    Wcrates=[]
    arrows = [up,left,down]

    while room_10Running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                room_10Running = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_ESCAPE:
                    room_10Running = False

        keys = key.get_pressed()
        if keys[27]:
            break

        mb = mouse.get_pressed()
        if mb[0] == 1 and gunHeat <= 0:
            gunHeat = 15
            shots.append(addShot(-angle - 90, power))

        gunHeat -= 1
        moveShots(shots)
        drawScene(badGuys, arrows, back1)
        moveGuy(guyx, guyy)
        myClock.tick(60)
        display.flip()

        win = checkWinLevel(badGuys)
        if win:
            if upRect.collidepoint(guyx, guyy):
                guyx = 512
                guyy = 660
                return 'room_13'
            if leftRect.collidepoint(guyx, guyy):
                guyx = 1000
                guyy = 350
                return 'room_9'
            if downRect.collidepoint(guyx, guyy):
                guyx = 512
                guyy = 25
                return 'room_7'
    return 'title'


def room_11():
    global running
    global Class
    global gunHeat
    global weapon
    global badGuys
    global Wcrates
    global guyx
    global guyy
    room_11Running = True
    badGuys=[[100,700,0],[10,500,0],[200,400,0],[500,450,0]]
    Wcrates=[]
    arrows = [down,hole]

    while room_11Running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                room_11Running = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_ESCAPE:
                    room_11Running = False

        keys = key.get_pressed()
        if keys[27]:
            break

        mb = mouse.get_pressed()
        if mb[0] == 1 and gunHeat <= 0:
            gunHeat = 15
            shots.append(addShot(-angle - 90, power))

        gunHeat -= 1
        moveShots(shots)
        drawScene(badGuys, arrows, back1)
        moveGuy(guyx, guyy)
        myClock.tick(60)
        display.flip()

        win = checkWinLevel(badGuys)
        if win:
            if downRect.collidepoint(guyx, guyy):
                guyx = 512
                guyy = 25
                return 'room_9'
            if holeRect.collidepoint(guyx, guyy):
                guyx = 512
                guyy = 350
                return 'room_1B'
    return 'title'


def room_12():
    global running
    global Class
    global gunHeat
    global weapon
    global badGuys
    global Wcrates
    global guyx
    global guyy
    room_12Running = True
    badGuys=[[100,700,0],[10,500,0],[200,400,0],[500,450,0]]
    Wcrates=[]
    arrows = [down]

    while room_12Running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                room_12Running = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_ESCAPE:
                    room_12Running = False

        keys = key.get_pressed()
        if keys[27]:
            break

        mb = mouse.get_pressed()
        if mb[0] == 1 and gunHeat <= 0:
            gunHeat = 15
            shots.append(addShot(-angle - 90, power))

        gunHeat -= 1
        moveShots(shots)
        drawScene(badGuys, arrows, back1)
        moveGuy(guyx, guyy)
        myClock.tick(60)
        display.flip()

        win = checkWinLevel(badGuys)
        if win:
            if downRect.collidepoint(guyx, guyy):
                guyx = 512
                guyy = 25
                return 'room_8'
    return 'title'


def room_13():
    global running
    global Class
    global gunHeat
    global weapon
    global badGuys
    global Wcrates
    global guyx
    global guyy
    room_13Running = True
    badGuys=[[100,700,0],[10,500,0],[200,400,0],[500,450,0]]
    Wcrates=[[100,600,3]]
    arrows = [down]

    while room_13Running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                room_13Running = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_ESCAPE:
                    room_13Running = False

        keys = key.get_pressed()
        if keys[27]:
            break

        mb = mouse.get_pressed()
        if mb[0] == 1 and gunHeat <= 0:
            gunHeat = 15
            shots.append(addShot(-angle - 90, power))

        gunHeat -= 1
        moveShots(shots)
        drawScene(badGuys, arrows, back1)
        moveGuy(guyx, guyy)
        myClock.tick(60)
        display.flip()

        win = checkWinLevel(badGuys)
        if win:
            if downRect.collidepoint(guyx, guyy):
                guyx = 512
                guyy = 25
                return 'room_10'
    return 'title'


def room_1B():
    global running
    global Class
    global gunHeat
    global weapon
    global badGuys
    global Wcrates
    global guyx
    global guyy
    room_1BRunning = True
    badGuys=[[100,700,0],[10,500,0],[200,400,0],[500,450,0]]
    Wcrates=[]
    arrows = [up]

    while room_1BRunning:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                room_1BRunning = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_ESCAPE:
                    room_1BRunning = False

        keys = key.get_pressed()
        if keys[27]:
            break

        mb = mouse.get_pressed()
        if mb[0] == 1 and gunHeat <= 0:
            gunHeat = 15
            shots.append(addShot(-angle - 90, power))

        gunHeat -= 1
        moveShots(shots)
        drawScene(badGuys, arrows, back2)
        moveGuy(guyx, guyy)
        myClock.tick(60)
        display.flip()

        win = checkWinLevel(badGuys)
        if win:
            if upRect.collidepoint(guyx, guyy):
                guyx = 512
                guyy = 660
                return 'room_2B'
    return 'title'


def room_2B():
    global running
    global Class
    global gunHeat
    global weapon
    global badGuys
    global Wcrates
    global guyx
    global guyy
    room_2BRunning = True
    badGuys=[[100,700,0],[10,500,0],[200,400,0],[500,450,0]]
    Wcrates=[]
    arrows = [up]

    while room_2BRunning:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                room_2BRunning = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_ESCAPE:
                    room_2BRunning = False

        keys = key.get_pressed()
        if keys[27]:
            break

        mb = mouse.get_pressed()
        if mb[0] == 1 and gunHeat <= 0:
            gunHeat = 15
            shots.append(addShot(-angle - 90, power))

        gunHeat -= 1
        moveShots(shots)
        drawScene(badGuys, arrows, back2)
        moveGuy(guyx, guyy)
        myClock.tick(60)
        display.flip()

        win = checkWinLevel(badGuys)
        if win:
            if upRect.collidepoint(guyx, guyy):
                guyx = 512
                guyy = 660
                return 'room_3B'
            if rightRect.collidepoint(guyx, guyy):
                guyx = 25
                guyy = 350
                return 'room_4B'
    return 'title'


def room_3B():
    global running
    global Class
    global gunHeat
    global weapon
    global badGuys
    global Wcrates
    global guyx
    global guyy
    room_3BRunning = True
    badGuys=[[100,700,0],[10,500,0],[200,400,0],[500,450,0]]
    Wcrates=[]
    arrows = []

    while room_3BRunning:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                room_3BRunning = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_ESCAPE:
                    room_3BRunning = False

        keys = key.get_pressed()
        if keys[27]:
            break

        mb = mouse.get_pressed()
        if mb[0] == 1 and gunHeat <= 0:
            gunHeat = 15
            shots.append(addShot(-angle - 90, power))

        gunHeat -= 1
        moveShots(shots)
        drawScene(badGuys, arrows, back2)
        moveGuy(guyx, guyy)
        myClock.tick(60)
        display.flip()

        win = checkWinLevel(badGuys)
        if win:
            return 'menu'
    return 'title'


def room_4B():
    global running
    global Class
    global gunHeat
    global weapon
    global badGuys
    global Wcrates
    global guyx
    global guyy
    room_4BRunning = True
    badGuys=[[100,700,0],[10,500,0],[200,400,0],[500,450,0]]
    Wcrates=[]
    arrows = [left]

    while room_4BRunning:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                room_4BRunning = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_ESCAPE:
                    room_4BRunning = False

        keys = key.get_pressed()
        if keys[27]:
            break

        mb = mouse.get_pressed()
        if mb[0] == 1 and gunHeat <= 0:
            gunHeat = 15
            shots.append(addShot(-angle - 90, power))

        gunHeat -= 1
        moveShots(shots)
        drawScene(badGuys, arrows, back2)
        moveGuy(guyx, guyy)
        myClock.tick(60)
        display.flip()

        win = checkWinLevel(badGuys)
        if win:
            if leftRect.collidepoint(guyx, guyy):
                guyx = 1000
                guyy = 350
                return 'room_2B'
    return 'title'


page = 'room_1'
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
    if page == 'room_2':
        page = room_2()
    if page == 'room_3':
        page = room_3()
    if page == 'room_4':
        page = room_4()
    if page == 'room_5':
        page = room_5()
    if page == 'room_6':
        page = room_6()
    if page == 'room_7':
        page = room_7()
    if page == 'room_8':
        page = room_8()
    if page == 'room_9':
        page = room_9()
    if page == 'room_10':
        page = room_10()
    if page == 'room_11':
        page = room_11()
    if page == 'room_12':
        page = room_12()
    if page == 'room_13':
        page = room_13()
    if page == 'room_1B':
        page = room_1B()
    if page == 'room_2B':
        page = room_2B()
    if page == 'room_3B':
        page = room_3B()
    if page == 'room_4B':
        page = room_4B()
    if not running:
        page = 'exit'
quit()
