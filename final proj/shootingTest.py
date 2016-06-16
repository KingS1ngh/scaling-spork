from pygame import *
from math import *
from random import *
import glob

screen = display.set_mode((1024, 700))
myClock = time.Clock()
running = True
pos = ''
guyx = 290
guyy = 420
SPACE = 32
X = 0
Y = 1
VX = 2
VY = 3
C = 4
angle = 0
crateNum = 0
bombPics = []
yellow = 255, 255, 0
red = 255, 0, 0
mx, my = mouse.get_pos()
mb = mouse.get_pressed()
Class = 'Scout'
weapon = 'Rifle'
item = 'none'
currentHealth = 40
maxHealth = 40
lastRoom = 'room_1'
Heat = 20
damage = 1
guy = image.load('Pictures/'+weapon+' '+Class+'.png')
shots = []
shotgunList = []
badshots = []
gunAng = 0.0
power = 5.0
gunHeat = 0
keys = key.get_pressed()
BADSPEED = 2.5
badGuys = []
badGuys2 = []
badGuys3 = []
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
holeRect = Rect(487, 325, 50, 50)

titleScreen = image.load('Pictures/Title Screen.png').convert()
titleBack = transform.scale(titleScreen, (1035, 800))

campaignButtonPic = image.load('Pictures/Campaign.png')
campaignButton = transform.scale(campaignButtonPic, (200, 50))

endlessButtonPic = image.load('Pictures/Endless.png')
endlessButton = transform.scale(endlessButtonPic, (200, 50))

instructionsButtonPic = image.load('Pictures/Instructions.png')
instructionsButton = transform.scale(instructionsButtonPic, (300, 50))

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

next = image.load('Pictures/Next.png')
next = transform.scale(next, (125, 100))
back = image.load('Pictures/Back.png')
back = transform.scale(back, (150, 75))
story = image.load('Pictures/Story.png')
story = transform.scale(story, (525, 163))
controls = image.load('Pictures/Controls.png')
controls = transform.scale(controls, (525, 163))
roomExplain = image.load('Pictures/Rooms.png')
roomExplain = transform.scale(roomExplain, (525, 163))
goal = image.load('Pictures/Goal.png')
goal = transform.scale(goal, (525, 163))

resume = image.load('Pictures/Resume.png')
resume = transform.scale(resume, (175, 50))
saveQuit = image.load('Pictures/Save+Quit.png')
saveQuit = transform.scale(saveQuit, (275, 50))
quitButton = image.load('Pictures/Quit.png')
quitButton = transform.scale(quitButton, (100, 50))

rilfeScout = image.load('Pictures/Rifle Scout.png')
back1 = image.load("Pictures/Level One Background.png").convert()
back1 = transform.scale(back1, (2000, 2000))
back2 = image.load('Pictures/Level Two Background.png').convert()
back2 = transform.scale(back2, (1024, 700))
badguy1 = image.load("Pictures/Alien 1.png")
badguy1 = transform.scale(badguy1, (60, 60))
badguy2 = image.load('Pictures/Alien 2.png')
badguy2 = transform.scale(badguy2,(70,60))
badguy3 = image.load('Pictures/Alien 3.png')
badguy3 = transform.scale(badguy3, (80,80))
arrow = image.load('Pictures/arrow.png')
rightArrow = transform.scale(arrow, (100,50))
upArrow = transform.rotate(rightArrow, (90))
leftArrow = transform.rotate(rightArrow, (180))
downArrow = transform.rotate(rightArrow, (270))
hole = image.load('Pictures/hole.png')
hole = transform.scale(hole, (50,50))

ship1 = image.load('Pictures/Alien(1) Ship 1.png')
ship2 = image.load('Pictures/Alien(1) Ship 2.png')
ship3 = image.load('Pictures/Alien(1) Ship 3.png')
ship4 = image.load('Pictures/Alien(2) Ship 1.png')
ship4 = transform.scale(ship4, (225, 525))
ship4 = transform.rotate(ship4, (75))
ship5 = image.load('Pictures/Alien(2) Ship 2.png')
ship5 = transform.scale(ship5, (225, 575))
ship6 = image.load('Pictures/Alien(2) Ship 3.png')
ship7 = image.load('Pictures/Alien(3) Ship 1.png')
ship7 = transform.scale(ship7, (300, 450))
ship7 = transform.rotate(ship7, (-135))
ship8 = image.load('Pictures/Alien(3) Ship 2.png')
ship8 = transform.scale(ship8, (225,300))
ship9 = image.load('Pictures/Earth Ship.png')
ship9 = transform.scale(ship9, (250, 400))
build1 = image.load('Pictures/Building 1.png')
build1 = transform.scale(build1, (350, 900))
build2 = image.load('Pictures/Building 2.png')
build2 = transform.scale(build2, (200, 550))
build2 = transform.rotate(build2, (-45))
build3 = image.load('Pictures/Infected Building 1.png')
build3 = transform.scale(build3, (550, 550))
build4 = image.load('Pictures/Infected Building 2.png')
build4 = transform.scale(build4, (300, 150))
build4 = transform.rotate(build4, (90))
build5 = image.load('Pictures/Infected Building 3.png')
build5 = transform.scale(build5, (125,100))
crat = image.load("Pictures/Weapon Crate.png")
crat2 = image.load('Pictures/Item Crate.png')
crat3 = image.load('Pictures/Med Crate.png')
grenade = image.load('Pictures/Grenade.png')
overshield = image.load('Pictures/Overshield.png')
sRing = image.load('Pictures/Scizor Ring.png')
junk1 = image.load('Pictures/Junk 1.png')
junk1 = transform.scale(junk1, (75, 150))
junk2 = image.load('Pictures/Junk 2.png')
junk2 = transform.scale(junk2, (75, 150))
junk2 = transform.rotate(junk2, (180))
junk3 = image.load('Pictures/Junk 3.png')
junk3 = transform.scale(junk3, (100, 150))
junk3 = transform.rotate(junk3, (90))
junk4 = image.load('Pictures/Junk 4.png')
junk5 = image.load('Pictures/Junk 5.png')
junk5 = transform.rotate(junk5, (90))
junk6 = image.load('Pictures/Junk 6.png')
junk6 = transform.rotate(junk6, (45))


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
    if guyx > 1024 - 35: guyx = 1024 - 35
    if guyy < 0: guyy = 0
    if guyy > 700 - 35: guyy = 700 - 35


def turn():
    global angle
    mx, my = mouse.get_pos()
    angle = degrees(atan2(mx-guyx, my-guyy))-180


def guyRect(x, y):
    grect = Rect(x, y, 40, 40)
    return grect


def vectToXY(mag, ang):
    rang = radians(ang)
    x = cos(rang)*mag
    y = sin(rang)*mag
    return x, y


def addShot(ang, power):
    shot = [0, 0, 0, 0]
    shot[X], shot[Y] = vectToXY(30, ang)
    shot[X] += guyx
    shot[Y] += guyy
    shot[VX], shot[VY] = vectToXY(power, ang)
    return shot


def addBadShot(bguy, ang, power):
    badshot = [0, 0, 0, 0]
    badshot[X], badshot[Y] = vectToXY(30, ang)
    badshot[X] += bguy[X]+40
    badshot[Y] += bguy[Y]+40
    badshot[VX], badshot[VY] = vectToXY(power, ang)
    return badshot

def shotgun(ang, ang1 ,ang2, power):
    shot=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    shot[0][X], shot[0][Y] = vectToXY(30,ang)
    shot[1][X], shot[1][Y] = vectToXY(30,ang1)
    shot[2][X], shot[2][Y] = vectToXY(30,ang2)
    for s in shot:
        s[X]+=guyx
        s[Y]+=guyy
    shot[0][VX], shot[0][VY]= vectToXY(power, ang)
    shot[1][VX], shot[1][VY]= vectToXY(power, ang1)
    shot[2][VX], shot[2][VY]= vectToXY(power, ang2)
    return shot


def moveShots(shots):
    global badshots
    killlist = []
    for shot in shots:
        shot[X] += shot[VX]
        shot[Y] += shot[VY]
        if shot[X] > guyx+400 or guyx-400 > shot[X] or guyy-400 > shot[Y] or shot[Y] > guyy+400:
            killlist.append(shot)
        for bguy in badGuys[:]:
            eRect=enemyRect(bguy)
            if eRect.collidepoint(shot[X], shot[Y]) and shot not in killlist:
                bguy[3]-=damage
                killlist.append(shot)
                if bguy[3]<=0:
                    badGuys.remove(bguy)
        for bguy in badGuys2:
            eRect = enemyRect(bguy)
            if eRect.collidepoint(shot[X], shot[Y]):
                badGuys2.remove(bguy)
        for bguy in badGuys3[:]:
            eRect=enemyRect(bguy)
            if eRect.collidepoint(shot[X], shot[Y]) and shot not in killlist:
                bguy[3]-=damage
                killlist.append(shot)
                if bguy[3]<=0:
                    badGuys3.remove(bguy)
                    badshots = []
    for s in killlist:
        shots.remove(s)


def moveShotgun(shotgunList):
    killlist = []
    for s in shotgunList:
        for shot in s:
            shot[X] += shot[VX]
            shot[Y] += shot[VY]
            if shot[X] > guyx+400 or guyx-400 > shot[X] or guyy-400 > shot[Y] or shot[Y] > guyy+400 and shot not in killlist:
                killlist.append(shot)
            for bguy in badGuys[:]:
                eRect=enemyRect(bguy)
                if eRect.collidepoint(shot[X], shot[Y]) and shot not in killlist:
                    bguy[3]-=damage
                    killlist.append(shot)
                    if bguy[3]<=0:
                        badGuys.remove(bguy)
                        killlist.append(shot)
            for bguy in badGuys2:
                eRect = enemyRect(bguy)
                if eRect.collidepoint(shot[X], shot[Y]):
                    badGuys2.remove(bguy)
            for bguy in badGuys3[:]:
                eRect=enemyRect(bguy)
                if eRect.collidepoint(shot[X], shot[Y]) and shot not in killlist:
                    bguy[3]-=damage
                    killlist.append(shot)
                    if bguy[3]<=0:
                        badGuys3.remove(bguy)
    for s in killlist:
        for k in shotgunList:
            for j in k:
                if s==j:
                    k.remove(j)


def moveBadShots(bguy, badshots):
    global currentHealth
    killlist = []
    for shot in badshots:
        shot[X] += shot[VX]
        shot[Y] += shot[VY]
        if shot[X] > bguy[X]+400:
            killlist.append(shot)
        gRect = guyRect(guyx, guyy)
        if gRect.collidepoint(shot[X], shot[Y]):
            currentHealth-=10/len(badshots)
            killlist.append(shot)
    for s in killlist:
        badshots.remove(s)


def badMove(bguy, x, y, BADSPEED):
    import math
    dist = max(1, distance(bguy[0], bguy[1], x, y))
    moveX = (x-bguy[0])*BADSPEED/dist
    moveY = (y-bguy[1])*BADSPEED/dist
    ang = math.atan2(-moveY, moveX)
    return moveX, moveY, math.degrees(ang)


def moveBadGuys1(bguy, guyx, guyy):
    moveX, moveY, moveAng = badMove(bguy, guyx, guyy, 2.5)
    bguy[0] += moveX
    bguy[1] += moveY
    bguy[2] = moveAng-90


def moveBadGuys2(bguy, guyx, guyy):
    moveX, moveY, moveAng = badMove(bguy, guyx, guyy, 4)
    bguy[0] += moveX
    bguy[1] += moveY
    bguy[2] = moveAng-90


def moveBadGuys3(bguy, guyx, guyy):
    moveX, moveY, moveAng = badMove(bguy, guyx, guyy, 4)
    bguy[2] = moveAng-90
    return moveAng


def boomBombs(bombs):
    rem=[]
    for bomb in bombs:
        bomb[3]+=1
        if bomb[3]==16:
            rem.append(bomb)
    for bomb in rem:
        bombs.remove(bomb)


def enemyRect(bguy):
    eRect = Rect(bguy[0]+35, bguy[1]+35, 40, 40)
    return eRect

def checkHit(rect):
    global bombs
    global currentHealth
    global badGuys
    global badGuys2
    for bguy in badGuys:
        if rect.collidepoint(bguy[0]+35, bguy[1]+35):
            currentHealth -= 10
            badGuys.remove(bguy)
            bombs.append([bguy[0], bguy[1],0,0])
    for bguy in badGuys2:
        if rect.collidepoint(bguy[0]+35, bguy[1]+35):
            currentHealth -= 10
            badGuys2.remove(bguy)
            bombs.append([bguy[0], bguy[1], 0, 0])
            return True
    return False


def checkWinLevel(badGuys):
    if len(badGuys) == 0 and len(badGuys2)==0:
        return True
    return False


def checkLoseLevel(health):
    if health <= 0:
        return True


def checkUpgrade(Wcrates, Mcrates, guyx, guyy):
    global guy
    global crateNum
    global weapon
    global maxHealth
    global currentHealth
    global Heat
    global damage

    for crate in Wcrates:
        crateRect = Rect(crate[0], crate[1], 40, 40)
        if crateRect.collidepoint(guyx + 15, guyy + 15):
            crateNum = crate[2]
            Wcrates.remove(crate)

    for med in Mcrates:
        medRect = Rect(med[0], med[1], 40, 40)
        if medRect.collidepoint(guyx + 15, guyy + 15):
            currentHealth += 20
            Mcrates.remove(med)
            if currentHealth > maxHealth: currentHealth = maxHealth

    if crateNum == 1 and Class == 'Scout':
        Heat = 30
        damage = 3
        weapon = 'Sniper'
    if crateNum == 1 and Class == 'Marine':
        Heat = 20
        damage = 3
        weapon = 'Plasma'
    if crateNum == 1 and Class == 'Tank':
        Heat = 30
        damage = 1
        weapon = 'Shotgun'
    if crateNum == 2 and Class == 'Scout':
        Heat = 20
        damage = 2
        weapon = 'Cannon'
    if crateNum == 2 and Class == 'Marine':
        Heat = 30
        damage = 3
        weapon = 'Sniper'
    if crateNum == 2 and Class == 'Tank':
        Heat = 5
        damage = 1
        weapon = 'Minigun'
    if crateNum == 3 and Class == 'Marine':
        Heat = 10
        damage = 2
        weapon = 'Machine'
    if crateNum == 3 and Class == 'Tank':
        Heat = 10
        damage = 1
        weapon = 'Melee'


def goodHealthMeter(currentHealth):
    healthRect = Rect(10, 10, 10+(currentHealth*2), 20)
    return healthRect


def drawScene(badGuys, badGuys2, arrows, back, builds):
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
        weaponcrate = transform.scale(crat, (40,60))
        screen.blit(weaponcrate, (crate[0], crate[1]))
        checkUpgrade(Wcrates, Mcrates, guyx, guyy)

    for med in Mcrates:
        medcrate = transform.scale(crat3, (40, 60))
        screen.blit(medcrate, (med[0], med[1]))
        checkUpgrade(Wcrates, Mcrates, guyx, guyy)
    if weapon == 'Shotgun':
        for s in shotgunList[:]:
            for shot in s:
                screen.blit(shoot2, (int(shot[X]), int(shot[Y])))
    for shot in shots[:]:
        screen.blit(shoot2, (int(shot[X]), int(shot[Y])))

    for shot in badshots[:]:
        screen.blit(shoot2, (int(shot[X]), int(shot[Y])))

    for bguy in badGuys:
        moveBadGuys1(bguy, guyx, guyy)
        alien1 = transform.rotate(badguy1, bguy[2])
        screen.blit(alien1, bguy[:2])

    for bomb in bombs:
        screen.blit(bombPics[bomb[3]], (bomb[X],bomb[Y]))

    for bguy in badGuys2:
        moveBadGuys2(bguy, guyx, guyy)
        alien2= transform.rotate(badguy2, bguy[2])
        screen.blit(alien2, bguy[:2])

    for bguy in badGuys3:
        moveBadGuys3(bguy, guyx, guyy)
        alien3 = transform.rotate(badguy3, bguy[2])
        screen.blit(alien3, bguy[:2])


    for b in builds:
        screen.blit(b[0], (b[1], b[2]))

    grect = guyRect(guyx, guyy)
    checkHit(grect)
    healthRect = goodHealthMeter(currentHealth)
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

    lose = checkLoseLevel(currentHealth)
    if lose:
        screen.fill((0, 0, 0))
    display.flip()


def fadeIn():
    image=screen.copy().convert()
    for i in range(255):
        screen.fill((0, 0, 0))
        image.set_alpha(255-i)
        screen.blit(image, (0, 0))
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
    backRect = Rect(0, 630, 150, 75)

    while gameLoadRunning:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                gameLoadRunning = False

        screen.blit(titleBack, (0, 0))
        screen.blit(newButton, (230, 525))
        screen.blit(loadButton, (595, 525))
        screen.blit(back, (0, 630))

        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        if newRect.collidepoint(mx, my) and mb[0] == 1:
            return 'menu'
        if loadRect.collidepoint(mx, my) and mb[0] == 1:
            return 'load'
        if backRect.collidepoint(mx, my) and mb[0] == 1:
            return 'title'
        display.flip()


def load():
    global running
    loadRunning = True
    backRect = Rect(0, 555, 150, 75)
    save1 = Rect(435, 483, 160, 50)
    save2 = Rect(435, 556, 160, 50)
    save3 = Rect(435, 623, 160, 50)

    while loadRunning:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                loadRunning = False

        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        screen.blit(titleBack, (0, 0))
        screen.blit(back, (0, 555))
        myFiles = glob.glob('*.txt')
        if len(myFiles) >= 1:
            screen.blit(campaignButton, (415, 480))
        if len(myFiles) >= 2:
            screen.blit(campaignButton, (415, 553))
        if len(myFiles) == 3:
            screen.blit(campaignButton, (415, 620))
        if save1.collidepoint(mx, my) and mb[0] == 1:
            saveFile = open('Save 1.txt', 'r')
            save = saveFile.readlines()
            saveFile.close()
            print(save)
        if backRect.collidepoint(mx, my) and mb[0] == 1:
            return 'gameLoad'
        display.flip()


def menu():
    global running
    menuRunning = True
    buttons = [Rect(420, 480, 190, 55), Rect(435, 553, 160, 45), Rect(435, 623, 160, 50)]
    screens = ['classSelect', 'endless', 'instructions']
    backRect = Rect(0, 555, 150, 75)

    while menuRunning:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                menuRunning = False

        screen.blit(titleBack, (0, 0))
        screen.blit(campaignButton, (415, 480))
        screen.blit(endlessButton, (415, 553))
        screen.blit(instructionsButton, (415, 620))
        screen.blit(back, (0, 555))

        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        for b, s in zip(buttons, screens):
            if b.collidepoint(mx, my) and mb[0] == 1:
                return s
        if backRect.collidepoint(mx, my) and mb[0] == 1:
            return 'title'
        display.flip()


def classSelect():
    global running
    classSelectRunning = True
    global Class
    global weapon
    global maxHealth
    global currentHealth
    backRect = Rect(0, 630, 150, 75)
    scoutRect = Rect(173, 390, 75, 75)
    marineRect = Rect(470, 390, 75, 75)
    tankRect = Rect(787, 390, 75, 75)
    startRect = Rect(410, 555, 200, 75)

    while classSelectRunning:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                classSelectRunning = False

        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        screen.blit(classBack, (0, 0))
        screen.blit(rScout, (185, 400))
        screen.blit(pTank, (800, 400))
        screen.blit(rMarine, (483, 400))
        screen.blit(classTitle, (325, 100))
        screen.blit(scoutLable, (140, 475))
        screen.blit(marineLable, (435, 475))
        screen.blit(tankLable, (775, 475))
        screen.blit(back, (0, 630))
        screenBuff = screen.copy()
        if scoutRect.collidepoint(mx, my) and mb[0] == 1:
            Class = 'Scout'
            weapon = 'Rifle'
            maxHealth = 40
            currentHealth = 40
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
            maxHealth = 70
            currentHealth = 70
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
            maxHealth = 100
            currentHealth = 100
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
        if backRect.collidepoint(mx, my) and mb[0] == 1:
            return 'menu'
        display.flip()


def endless():
    global running
    endlessRunning = True

    while endlessRunning:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                endlessRunning = False

        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        display.flip()
    return 'menu'


def instructions():
    global running
    instructionsRunning = True
    backRect = Rect(0, 630, 150, 75)

    while instructionsRunning:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                instructionsRunning = False

        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        screen.blit(classBack, (0, 0))
        screen.blit(story, (250, 10))
        screen.blit(controls, (250, 183))
        screen.blit(roomExplain, (250, 346))
        screen.blit(goal, (250, 515))
        screen.blit(hole, (600, 635))
        screen.blit(back, (0, 630))
        if backRect.collidepoint(mx, my) and mb[0] == 1:
            return 'menu'
        display.flip()


def pause():
    global running
    global lastRoom
    pauseRunning = True
    resumeRect = Rect(425, 225, 175, 50)
    saveQuitRect = Rect(375, 325, 275, 50)
    quitRect = Rect(462, 425, 100, 50)
    image = screen.copy().convert()

    while pauseRunning:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                pauseRunning = False

        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        screen.fill((0, 0, 0))
        image.set_alpha(150)
        screen.blit(image, (0, 0))
        screen.blit(resume, (425, 225))
        screen.blit(saveQuit, (375, 325))
        screen.blit(quitButton, (462, 425))
        display.flip()
        if resumeRect.collidepoint(mx, my) and mb[0] == 1:
            return lastRoom
        if saveQuitRect.collidepoint(mx, my) and mb[0] == 1:
            return 'menu'
        if quitRect.collidepoint(mx, my) and mb[0] == 1:
            return 'menu'


def room_1():
    fadeIn()
    global running
    global Class
    global gunHeat
    global weapon
    global badGuys
    global badGuys3
    global Wcrates
    global Mcrates
    global guyx
    global guyy
    global lastRoom
    global shots
    global shotgunList
    shots = []
    room_1Running = True
    lastRoom = 'room_1'
    badGuys=[[100,100,0,2]]
    badGuys3=[[400,300,0,3],[100,600,0,3]]
    Wcrates=[]
    arrows = [up]
    builds = [[ship9, 50, 300]]
    Mcrates = []
    while room_1Running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                room_1Running = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_p:
                    return pause()

        keys = key.get_pressed()
        if keys[27]:
            break
        mb = mouse.get_pressed()
        if mb[0] == 1 and gunHeat <= 0:
            gunHeat = Heat
            if weapon == 'Shotgun':
                shotgunList.append(shotgun(-angle - 90, -angle - (90+randint(0,10)), -angle - (90-randint(0,10)), power))
            else:
                shots.append(addShot(-angle - 90, power))
        for bguy in badGuys3:
            ang = moveBadGuys3(bguy, guyx, guyy)
            if randint(0,50)==1:
                badshots.append(addBadShot(bguy,-ang,10))
            moveBadShots(bguy,badshots)

        gunHeat -= 1
        boomBombs(bombs)
        moveShots(shots)
        moveShotgun(shotgunList)
        drawScene(badGuys, badGuys2, arrows, back1, builds)
        moveGuy(guyx, guyy)
        myClock.tick(60)
        display.flip()
        win = checkWinLevel(badGuys)
        if win:
            if upRect.collidepoint(guyx, guyy):
                guyx = 512
                guyy = 660
                return 'room_2'
    return 'menu'


def room_2():
    fadeIn()
    global running
    global Class
    global gunHeat
    global weapon
    global badGuys
    global Wcrates
    global Mcrates
    global guyx
    global guyy
    global lastRoom
    global shots
    global shotgunList
    global badguys3
    shots = []
    shotgunList = []
    room_2Running = True
    lastRoom = 'room_2'
    badGuys=[[100,700,0,2],[10,500,0,2],[200,400,0,2],[500,450,0,2]]
    Wcrates=[]
    arrows = [up,right,left,down]
    builds = [[build2, 100, 100]]
    Mcrates = []

    while room_2Running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                room_2Running = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_p:
                    return pause()

        keys = key.get_pressed()
        if keys[27]:
            break

        mb = mouse.get_pressed()
        if mb[0] == 1 and gunHeat <= 0:
            gunHeat = Heat
            if weapon == 'Shotgun':
                shotgunList.append(shotgun(-angle - 90, -angle - (90+randint(0,10)), -angle - (90-randint(0,10)), power))
            else:
                shots.append(addShot(-angle - 90, power))
        for bguy in badGuys3:
            ang = moveBadGuys3(bguy, guyx, guyy)
            if randint(0,50)==1:
                badshots.append(addBadShot(bguy,-ang,10))
            moveBadShots(bguy,badshots)


        gunHeat -= 1
        boomBombs(bombs)
        moveShots(shots)
        moveShotgun(shotgunList)
        drawScene(badGuys, badGuys2, arrows, back1, builds)
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
    fadeIn()
    global running
    global Class
    global gunHeat
    global weapon
    global badGuys
    global Wcrates
    global Mcrates
    global guyx
    global guyy
    global lastRoom
    global shots
    global shotgunList
    shots = []
    shotgunList = []
    room_3Running = True
    lastRoom = 'room_3'
    badGuys=[[100,700,0,2],[10,500,0,2],[200,400,0,2],[500,450,0,2]]
    Wcrates=[]
    arrows = [up, right]
    builds = [[ship8, 650, 50]]
    Mcrates = [[150,550]]

    while room_3Running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                room_3Running = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_p:
                    return 'pause'

        keys = key.get_pressed()
        if keys[27]:
            break

        mb = mouse.get_pressed()
        if mb[0] == 1 and gunHeat <= 0:
            gunHeat = Heat
            if weapon == 'Shotgun':
                shotgunList.append(shotgun(-angle - 90, -angle - (90+randint(0,10)), -angle - (90-randint(0,10)), power))
            else:
                shots.append(addShot(-angle - 90, power))
        for bguy in badGuys3:
            ang = moveBadGuys3(bguy, guyx, guyy)
            if randint(0,50)==1:
                badshots.append(addBadShot(bguy,-ang,10))
            moveBadShots(bguy,badshots)

        gunHeat -= 1
        boomBombs(bombs)
        moveShots(shots)
        moveShotgun(shotgunList)
        drawScene(badGuys, badGuys2, arrows, back1, builds)
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
    fadeIn()
    global running
    global Class
    global gunHeat
    global weapon
    global badGuys
    global Wcrates
    global Mcrates
    global guyx
    global guyy
    global lastRoom
    global shots
    global shotgunList
    shots = []
    shotgunList = []
    room_4Running = True
    lastRoom = 'room_4'
    badGuys=[[100,700,0,2],[10,500,0,2],[200,400,0,2],[500,450,0,2]]
    Wcrates=[[100,600,1]]
    arrows = [up, left]
    builds = [[junk1, 175, 145], [junk2, 550, 480], [junk3, 750, 200]]
    Mcrates = []

    while room_4Running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                room_4Running = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_p:
                    return pause()

        keys = key.get_pressed()
        if keys[27]:
            break

        mb = mouse.get_pressed()
        if mb[0] == 1 and gunHeat <= 0:
            gunHeat = Heat
            if weapon == 'Shotgun':
                shotgunList.append(shotgun(-angle - 90, -angle - (90+randint(0,10)), -angle - (90-randint(0,10)), power))
            else:
                shots.append(addShot(-angle - 90, power))
        for bguy in badGuys3:
            ang = moveBadGuys3(bguy, guyx, guyy)
            if randint(0,50)==1:
                badshots.append(addBadShot(bguy,-ang,10))
            moveBadShots(bguy,badshots)

        gunHeat -= 1
        boomBombs(bombs)
        moveShots(shots)
        moveShotgun(shotgunList)
        drawScene(badGuys, badGuys2, arrows, back1, builds)
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
    fadeIn()
    global running
    global Class
    global gunHeat
    global weapon
    global badGuys
    global Wcrates
    global Mcrates
    global guyx
    global guyy
    global lastRoom
    global shots
    global shotgunList
    shots = []
    shotgunList = []
    room_5Running = True
    lastRoom = 'room_5'
    badGuys=[[100,700,0,2],[10,500,0,2],[200,400,0,2],[500,450,0,2]]
    Wcrates=[]
    arrows = [up, right, down]
    builds = [[junk4, 150, 100], [junk5, 275, 500], [junk6, 600, 150]]
    Mcrates = []

    while room_5Running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                room_5Running = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_p:
                    return pause()

        keys = key.get_pressed()
        if keys[27]:
            break

        mb = mouse.get_pressed()
        if mb[0] == 1 and gunHeat <= 0:
            gunHeat = Heat
            if weapon == 'Shotgun':
                shotgunList.append(shotgun(-angle - 90, -angle - (90+randint(0,10)), -angle - (90-randint(0,10)), power))
            else:
                shots.append(addShot(-angle - 90, power))
        for bguy in badGuys3:
            ang = moveBadGuys3(bguy, guyx, guyy)
            if randint(0,50)==1:
                badshots.append(addBadShot(bguy,-ang,10))
            moveBadShots(bguy,badshots)

        gunHeat -= 1
        boomBombs(bombs)
        moveShots(shots)
        moveShotgun(shotgunList)
        drawScene(badGuys, badGuys2, arrows, back1, builds)
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
    fadeIn()
    global running
    global Class
    global gunHeat
    global weapon
    global badGuys
    global Wcrates
    global Mcrates
    global guyx
    global guyy
    global lastRoom
    global shots
    global shotgunList
    shots = []
    shotgunList = []
    room_6Running = True
    lastRoom = 'room_6'
    badGuys=[[100,700,0,2],[10,500,0,2],[200,400,0,2],[500,450,0,2]]
    Wcrates=[]
    arrows = [up,right,left,down]
    builds = [[ship7, 200, 150]]
    Mcrates = [[850,150]]

    while room_6Running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                room_6Running = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_p:
                    return pause()

        keys = key.get_pressed()
        if keys[27]:
            break

        mb = mouse.get_pressed()
        if mb[0] == 1 and gunHeat <= 0:
            gunHeat = Heat
            if weapon == 'Shotgun':
                shotgunList.append(shotgun(-angle - 90, -angle - (90+randint(0,10)), -angle - (90-randint(0,10)), power))
            else:
                shots.append(addShot(-angle - 90, power))
        for bguy in badGuys3:
            ang = moveBadGuys3(bguy, guyx, guyy)
            if randint(0,50)==1:
                badshots.append(addBadShot(bguy,-ang,10))
            moveBadShots(bguy,badshots)

        gunHeat -= 1
        boomBombs(bombs)
        moveShots(shots)
        moveShotgun(shotgunList)
        drawScene(badGuys, badGuys2, arrows, back1, builds)
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
    fadeIn()
    global running
    global Class
    global gunHeat
    global weapon
    global badGuys
    global Wcrates
    global Mcrates
    global guyx
    global guyy
    global lastRoom
    global badGuys2
    global shots
    global shotgunList
    shots = []
    shotgunList = []
    room_7Running = True
    lastRoom = 'room_7'
    badGuys=[[100,700,0,2],[10,500,0,2],[200,400,0,2],[500,450,0,2]]
    badGuys2=[[200,400,0],[500,100,0],[400,600,0]]
    Wcrates=[]
    arrows = [up,left,down]
    builds = [[ship4, 300, 150]]
    Mcrates = []

    while room_7Running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                room_7Running = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_p:
                    return pause()

        keys = key.get_pressed()
        if keys[27]:
            break

        mb = mouse.get_pressed()
        if mb[0] == 1 and gunHeat <= 0:
            gunHeat = Heat
            if weapon == 'Shotgun':
                shotgunList.append(shotgun(-angle - 90, -angle - (90+randint(0,10)), -angle - (90-randint(0,10)), power))
            else:
                shots.append(addShot(-angle - 90, power))
        for bguy in badGuys3:
            ang = moveBadGuys3(bguy, guyx, guyy)
            if randint(0,50)==1:
                badshots.append(addBadShot(bguy,-ang,10))
            moveBadShots(bguy,badshots)

        gunHeat -= 1
        boomBombs(bombs)
        moveShots(shots)
        moveShotgun(shotgunList)
        drawScene(badGuys, badGuys2, arrows, back1, builds)
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
    fadeIn()
    global running
    global Class
    global gunHeat
    global weapon
    global badGuys
    global Wcrates
    global Mcrates
    global guyx
    global guyy
    global lastRoom
    global shots
    global shotgunList
    shots = []
    shotgunList = []
    room_8Running = True
    lastRoom = 'room_8'
    badGuys=[[100,700,0,2],[10,500,0,2],[200,400,0,2],[500,450,0,2]]
    Wcrates=[[100,600,2]]
    arrows = [up,right,down]
    builds = [[junk3, 200, 225], [ship5, 650, 50]]
    Mcrates = []

    while room_8Running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                room_8Running = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_p:
                    return pause()

        keys = key.get_pressed()
        if keys[27]:
            break

        mb = mouse.get_pressed()
        if mb[0] == 1 and gunHeat <= 0:
            gunHeat = Heat
            if weapon == 'Shotgun':
                shotgunList.append(shotgun(-angle - 90, -angle - (90+randint(0,10)), -angle - (90-randint(0,10)), power))
            else:
                shots.append(addShot(-angle - 90, power))
        for bguy in badGuys3:
            ang = moveBadGuys3(bguy, guyx, guyy)
            if randint(0,50)==1:
                badshots.append(addBadShot(bguy,-ang,10))
            moveBadShots(bguy,badshots)

        gunHeat -= 1
        boomBombs(bombs)
        moveShots(shots)
        moveShotgun(shotgunList)
        drawScene(badGuys, badGuys2, arrows, back1, builds)
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
    fadeIn()
    global running
    global Class
    global gunHeat
    global weapon
    global badGuys
    global Wcrates
    global Mcrates
    global guyx
    global guyy
    global lastRoom
    global shots
    global shotgunList
    shots = []
    shotgunList = []
    room_9Running = True
    lastRoom = 'room_9'
    badGuys=[[100,700,0,2],[10,500,0,2],[200,400,0,2],[500,450,0,2]]
    Wcrates=[]
    arrows = [up,right,left,down]
    builds = [[build3, 250, 75]]
    Mcrates = []

    while room_9Running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                room_9Running = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_p:
                    return pause()

        keys = key.get_pressed()
        if keys[27]:
            break

        mb = mouse.get_pressed()
        if mb[0] == 1 and gunHeat <= 0:
            gunHeat = Heat
            if weapon == 'Shotgun':
                shotgunList.append(shotgun(-angle - 90, -angle - (90+randint(0,10)), -angle - (90-randint(0,10)), power))
            else:
                shots.append(addShot(-angle - 90, power))
        for bguy in badGuys3:
            ang = moveBadGuys3(bguy, guyx, guyy)
            if randint(0,50)==1:
                badshots.append(addBadShot(bguy,-ang,10))
            moveBadShots(bguy,badshots)

        gunHeat -= 1
        boomBombs(bombs)
        moveShots(shots)
        moveShotgun(shotgunList)
        drawScene(badGuys, badGuys2, arrows, back1, builds)
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
    fadeIn()
    global running
    global Class
    global gunHeat
    global weapon
    global badGuys
    global Wcrates
    global Mcrates
    global guyx
    global guyy
    global lastRoom
    global shots
    global shotgunList
    shots = []
    shotgunList = []
    room_10Running = True
    lastRoom = 'room_10'
    badGuys=[[100,700,0,2],[10,500,0,2],[200,400,0,2],[500,450,0,2]]
    Wcrates=[]
    arrows = [up,left,down]
    builds = [[build5, 125, 150], [build5, 175, 400], [build5, 420, 250], [build5, 600, 180], [build5, 620, 500]]
    Mcrates = []

    while room_10Running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                room_10Running = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_p:
                    return pause()

        keys = key.get_pressed()
        if keys[27]:
            break

        mb = mouse.get_pressed()
        if mb[0] == 1 and gunHeat <= 0:
            gunHeat = Heat
            if weapon == 'Shotgun':
                shotgunList.append(shotgun(-angle - 90, -angle - (90+randint(0,10)), -angle - (90-randint(0,10)), power))
            else:
                shots.append(addShot(-angle - 90, power))
        for bguy in badGuys3:
            ang = moveBadGuys3(bguy, guyx, guyy)
            if randint(0,50)==1:
                badshots.append(addBadShot(bguy,-ang,10))
            moveBadShots(bguy,badshots)

        gunHeat -= 1
        boomBombs(bombs)
        moveShots(shots)
        moveShotgun(shotgunList)
        boomBombs(bombs)
        drawScene(badGuys, badGuys2, arrows, back1, builds)
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
    fadeIn()
    global running
    global Class
    global gunHeat
    global weapon
    global badGuys
    global Wcrates
    global Mcrates
    global guyx
    global guyy
    global lastRoom
    global shots
    global shotgunList
    shots = []
    shotgunList = []
    room_11Running = True
    lastRoom = 'room_11'
    badGuys=[[100,700,0,2],[10,500,0,2],[200,400,0,2],[500,450,0,2]]
    Wcrates=[]
    arrows = [down, hole]
    builds = [[build4, 200, 150], [build4, 650, 200]]
    Mcrates = []

    while room_11Running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                room_11Running = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_p:
                    return pause()

        keys = key.get_pressed()
        if keys[27]:
            break

        mb = mouse.get_pressed()
        if mb[0] == 1 and gunHeat <= 0:
            gunHeat = Heat
            if weapon == 'Shotgun':
                shotgunList.append(shotgun(-angle - 90, -angle - (90+randint(0,10)), -angle - (90-randint(0,10)), power))
            else:
                shots.append(addShot(-angle - 90, power))
        for bguy in badGuys3:
            ang = moveBadGuys3(bguy, guyx, guyy)
            if randint(0,50)==1:
                badshots.append(addBadShot(bguy,-ang,10))
            moveBadShots(bguy,badshots)

        gunHeat -= 1
        boomBombs(bombs)
        moveShots(shots)
        moveShotgun(shotgunList)
        drawScene(badGuys, badGuys2, arrows, back1, builds)
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
    fadeIn()
    global running
    global Class
    global gunHeat
    global weapon
    global badGuys
    global Wcrates
    global Mcrates
    global guyx
    global guyy
    global lastRoom
    global shots
    global shotgunList
    shots = []
    shotgunList = []
    room_12Running = True
    lastRoom = 'room_12'
    badGuys=[[100,700,0,2],[10,500,0,2],[200,400,0,2],[500,450,0,2]]
    Wcrates=[]
    arrows = [down]
    builds = [[build5, 200, 300], [build1, 825, -75]]
    Mcrates = [[550, 200]]

    while room_12Running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                room_12Running = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_p:
                    return pause()

        keys = key.get_pressed()
        if keys[27]:
            break

        mb = mouse.get_pressed()
        if mb[0] == 1 and gunHeat <= 0:
            gunHeat = Heat
            if weapon == 'Shotgun':
                shotgunList.append(shotgun(-angle - 90, -angle - (90+randint(0,10)), -angle - (90-randint(0,10)), power))
            else:
                shots.append(addShot(-angle - 90, power))
        for bguy in badGuys3:
            ang = moveBadGuys3(bguy, guyx, guyy)
            if randint(0,50)==1:
                badshots.append(addBadShot(bguy,-ang,10))
            moveBadShots(bguy,badshots)

        gunHeat -= 1
        boomBombs(bombs)
        moveShots(shots)
        moveShotgun(shotgunList)
        drawScene(badGuys, badGuys2, arrows, back1, builds)
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
    fadeIn()
    global running
    global Class
    global gunHeat
    global weapon
    global badGuys
    global Wcrates
    global Mcrates
    global guyx
    global guyy
    global lastRoom
    global shots
    global shotgunList
    shots = []
    shotgunList = []
    room_13Running = True
    lastRoom = 'room_13'
    badGuys=[[100,700,0,2],[10,500,0,2],[200,400,0,2],[500,450,0,2]]
    Wcrates=[[900,100,3]]
    arrows = [down]
    builds = [[build5, 400, 275], [ship6, -250, -50]]
    Mcrates = []

    while room_13Running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                room_13Running = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_p:
                    return pause()

        keys = key.get_pressed()
        if keys[27]:
            break

        mb = mouse.get_pressed()
        if mb[0] == 1 and gunHeat <= 0:
            gunHeat = Heat
            if weapon == 'Shotgun':
                shotgunList.append(shotgun(-angle - 90, -angle - (90+randint(0,10)), -angle - (90-randint(0,10)), power))
            else:
                shots.append(addShot(-angle - 90, power))
        for bguy in badGuys3:
            ang = moveBadGuys3(bguy, guyx, guyy)
            if randint(0,50)==1:
                badshots.append(addBadShot(bguy,-ang,10))
            moveBadShots(bguy,badshots)

        gunHeat -= 1
        boomBombs(bombs)
        moveShots(shots)
        moveShotgun(shotgunList)
        drawScene(badGuys, badGuys2, arrows, back1, builds)
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
    fadeIn()
    global badGuys2
    global running
    global Class
    global gunHeat
    global weapon
    global badGuys
    global Wcrates
    global Mcrates
    global guyx
    global guyy
    global lastRoom
    global shots
    global shotgunList
    shots = []
    shotgunList = []
    room_1BRunning = True
    lastRoom = 'room_1B'
    badGuys=[[100,700,0,2],[10,500,0,2],[200,400,0,2],[500,450,0,2]]
    badGuys2=[[100,100,0],[500,400,0]]
    Wcrates=[]
    arrows = [up]
    builds = []
    Mcrates = []

    while room_1BRunning:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                room_1BRunning = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_p:
                    return pause()

        keys = key.get_pressed()
        if keys[27]:
            break

        mb = mouse.get_pressed()
        if mb[0] == 1 and gunHeat <= 0:
            gunHeat = Heat
            if weapon == 'Shotgun':
                shotgunList.append(shotgun(-angle - 90, -angle - (90+randint(0,10)), -angle - (90-randint(0,10)), power))
            else:
                shots.append(addShot(-angle - 90, power))
        for bguy in badGuys3:
            ang = moveBadGuys3(bguy, guyx, guyy)
            if randint(0,50)==1:
                badshots.append(addBadShot(bguy,-ang,10))
            moveBadShots(bguy,badshots)

        gunHeat -= 1
        boomBombs(bombs)
        moveShots(shots)
        moveShotgun(shotgunList)
        drawScene(badGuys, badGuys2, arrows, back2, builds)
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
    fadeIn()
    global running
    global Class
    global gunHeat
    global weapon
    global badGuys
    global Wcrates
    global Mcrates
    global guyx
    global guyy
    global lastRoom
    global shots
    global shotgunList
    shots = []
    shotgunList = []
    room_2BRunning = True
    lastRoom = 'room_2B'
    badGuys=[[100,700,0,2],[10,500,0,2],[200,400,0,2],[500,450,0,2]]
    Wcrates=[]
    arrows = [up]
    builds = []
    Mcrates = []

    while room_2BRunning:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                room_2BRunning = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_p:
                    return pause()

        keys = key.get_pressed()
        if keys[27]:
            break

        mb = mouse.get_pressed()
        if mb[0] == 1 and gunHeat <= 0:
            gunHeat = Heat
            if weapon == 'Shotgun':
                shotgunList.append(shotgun(-angle - 90, -angle - (90+randint(0,10)), -angle - (90-randint(0,10)), power))
            else:
                shots.append(addShot(-angle - 90, power))
        for bguy in badGuys3:
            ang = moveBadGuys3(bguy, guyx, guyy)
            if randint(0,50)==1:
                badshots.append(addBadShot(bguy,-ang,10))
            moveBadShots(bguy,badshots)

        gunHeat -= 1
        boomBombs(bombs)
        moveShots(shots)
        moveShotgun(shotgunList)
        drawScene(badGuys, badGuys2, arrows, back2, builds)
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
    fadeIn()
    global running
    global Class
    global gunHeat
    global weapon
    global badGuys
    global Wcrates
    global Mcrates
    global guyx
    global guyy
    global lastRoom
    global shots
    global shotgunList
    shots = []
    shotgunList = []
    room_3BRunning = True
    lastRoom = 'room_3B'
    badGuys=[[100,700,0,2],[10,500,0,2],[200,400,0,2],[500,450,0,2]]
    Wcrates=[]
    arrows = []
    builds = []
    Mcrates = []

    while room_3BRunning:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                room_3BRunning = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_p:
                    return pause()

        keys = key.get_pressed()
        if keys[27]:
            break

        mb = mouse.get_pressed()
        if mb[0] == 1 and gunHeat <= 0:
            gunHeat = Heat
            if weapon == 'Shotgun':
                shotgunList.append(shotgun(-angle - 90, -angle - (90+randint(0,10)), -angle - (90-randint(0,10)), power))
            else:
                shots.append(addShot(-angle - 90, power))
        for bguy in badGuys3:
            ang = moveBadGuys3(bguy, guyx, guyy)
            if randint(0,50)==1:
                badshots.append(addBadShot(bguy,-ang,10))
            moveBadShots(bguy,badshots)

        gunHeat -= 1
        boomBombs(bombs)
        moveShots(shots)
        moveShotgun(shotgunList)
        drawScene(badGuys, badGuys2, arrows, back2, builds)
        moveGuy(guyx, guyy)
        myClock.tick(60)
        display.flip()

        win = checkWinLevel(badGuys)
        if win:
            return 'menu'
    return 'title'


def room_4B():
    fadeIn()
    global running
    global Class
    global gunHeat
    global weapon
    global badGuys
    global Wcrates
    global Mcrates
    global guyx
    global guyy
    global lastRoom
    global shots
    global shotgunList
    shots = []
    shotgunList = []
    room_4BRunning = True
    lastRoom = 'room_4B'
    badGuys=[[100,700,0,2],[10,500,0,2],[200,400,0,2],[500,450,0,2]]
    Wcrates=[]
    arrows = [left]
    builds = []
    Mcrates = []

    while room_4BRunning:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                room_4BRunning = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_p:
                    return pause()

        keys = key.get_pressed()
        if keys[27]:
            break

        mb = mouse.get_pressed()
        if mb[0] == 1 and gunHeat <= 0:
            gunHeat = Heat
            if weapon == 'Shotgun':
                shotgunList.append(shotgun(-angle - 90, -angle - (90+randint(0,10)), -angle - (90-randint(0,10)), power))
            else:
                shots.append(addShot(-angle - 90, power))
        for bguy in badGuys3:
            ang = moveBadGuys3(bguy, guyx, guyy)
            if randint(0,50)==1:
                badshots.append(addBadShot(bguy,-ang,10))
            moveBadShots(bguy,badshots)

        gunHeat -= 1
        boomBombs(bombs)
        moveShots(shots)
        moveShotgun(shotgunList)
        drawScene(badGuys, badGuys2, arrows, back2, builds)
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


page = 'title'
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
    if page == 'instructions':
        page = instructions()
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
