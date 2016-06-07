#############TO DO##############

from pygame import *
from random import *
from math import *

screen = display.set_mode((1350, 768), FULLSCREEN)
back1 = image.load("back1.png").convert()
back1 = transform.scale(back1, (2000, 2000))
back2 = image.load("Back2.png").convert()
back2 = transform.scale(back2, (800, 600))
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
guy = image.load("Marine/MMarine.png")
badguy1 = image.load("alien1/alien1.png")
crat = image.load("stuff/Weapon Crate.png")
MarineHealth = 70
TankHealth = 100
ScoutHealth = 30
myClock = time.Clock()

for i in range(1, 17):
    # bombPics+=image.load("explosion/explosion"+str(i)+".png")
    print(i)


def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


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
    if guyx > 800 - 35: guyx = 800 - 35
    if guyy < 0: guyy = 0
    if guyy > 600 - 35: guyy = 600 - 35


def turn():
    global angle
    mx, my = mouse.get_pos()
    angle = degrees(atan2(mx - guyx, my - guyy)) - 180


def guyRect(x, y):
    grect = Rect(x, y, 30, 30)
    return grect


def vectToXY(mag, ang):
    global badGuys
    rang = radians(ang)
    x = cos(rang) * mag
    y = sin(rang) * mag
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
    moveX = (x - bguy[0]) * BADSPEED / dist
    moveY = (y - bguy[1]) * BADSPEED / dist
    ang = math.atan2(-moveY, moveX)
    return moveX, moveY, math.degrees(ang)


def moveBadGuys(bguy, guyx, guyy):
    moveX, moveY, moveAng = badMove(bguy, guyx, guyy)
    bguy[0] += moveX
    bguy[1] += moveY
    bguy[2] = moveAng - 90


def moveShots(shots):
    killlist = []
    for shot in shots:
        shot[X] += shot[VX]
        shot[Y] += shot[VY]
        if shot[X] > guyx + 800 or guyx - 800 > shot[X] or guyy - 600 > shot[Y] or shot[Y] > guyy + 600:
            killlist.append(shot)
    for s in killlist:
        shots.remove(s)


def enemyRect(bguy):
    eRect = Rect(bguy[0], bguy[1], 40, 40)
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
        if rect.collidepoint(bguy[0], bguy[1]):
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
    for crate in Wcrates:
        crateRect = Rect(crate[0], crate[1], 40, 40)
        draw.rect(screen, (0, 0, 0), (crateRect), 1)
        if crateRect.collidepoint(guyx + 15, guyy + 15):
            Wcrates.remove(crate)
            crateNum += 1
    if crateNum == 1: guy = image.load("Marine/Plasma Marine.png")
    if crateNum == 2: guy = image.load("Marine/Rifle Marine.png")
    if crateNum == 3: guy = image.load("Marine/Sniper Marine.png")


def goodHealthMeter(health):
    healthRect = Rect(10, 10, 10 + (health * 2), 20)
    return healthRect


def drawScene(screen):
    screen.blit(back1, (0, 0))
    pic = transform.scale(guy, (50, 50))
    turn()
    pic = transform.rotate(pic, angle)
    screen.blit(pic, (guyx - 17, guyy - 17))
    shoot1 = image.load("stuff/shot.png")
    shoot1 = transform.scale(shoot1, (10, 10))
    shoot2 = image.load("stuff/redbullet.png").convert()
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

    grect = guyRect(guyx, guyy)
    draw.rect(screen, (0, 0, 0), (grect), 1)
    checkHit(grect)
    healthRect = goodHealthMeter(MarineHealth)
    draw.rect(screen, (0, 255, 0), (healthRect))

    win = checkWinLevel(badGuys)
    if win:
        screen.fill((211, 211, 211))
        screen.blit((transform.scale((image.load("stuff/victory.png")), (1000, 600))), (-100, 0))

    lose = checkLoseLevel(MarineHealth)
    if lose:
        screen.fill((0, 0, 0))
    display.flip()


running = True
shots = []
gunAng = 0.0
power = 10
gunHeat = 0
BADSPEED = 1
badGuys = [[randint(0, 800), randint(0, 600), 0], [randint(0, 800), randint(0, 600), 0],
           [randint(0, 800), randint(0, 600), 0], [randint(0, 800), randint(0, 600), 0],
           [randint(0, 800), randint(0, 600), 0], [randint(0, 800), randint(0, 600), 0],
           [randint(0, 800), randint(0, 600), 0], [randint(0, 800), randint(0, 600), 0]]
Wcrates = [[200, 300], [500, 70], [400, 400]]
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
quit()
