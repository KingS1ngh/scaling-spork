from pygame import *
from math import *
from random import *
import glob
#imports
screen = display.set_mode((1024, 700))  #screen size
myClock = time.Clock()  #used for fps and to make sure things dont move way too fast
running = True  #program is running
font.init() #initializing font
arialFont2 = font.SysFont('Times New Roman', 20)    #setting font style and size
guyx = 300  #character starting x
guyy = 420  #character starting y
lastx = 310 #last position character was(used for colliding with objects)
lasty = 420
X = 0   #the x coordinate in our lists is usually the first/ 0 pos, so X for that
Y = 1   #same thing as X but for Y coordinate
VX = 2  #when shooting, spot 2 in the list is the velocity X, so VX to rep that
VY = 3  #same as VX but for Y velocity
angle = 0   #setting variable for the angle the guy(character being played) faces
crateNum = 0    #setting crate number variable, used to check which weapon is recieved after upgrade
bombPics = []   #list of sprite pics for bomb will be added here
bossshots = []  #list of shots made by the boss will be added in this
Boss = []   #boss x,y,angle, and health will be set in this list
yellow = 255, 255, 0    #RGB values for yellow
red = 255, 0, 0 #RGB values for red
mx, my = mouse.get_pos()    #gets x and y position of mouse
mb = mouse.get_pressed()    #used to check if left click
Class = 'Scout' #setting variable for class, player will be allowed to pick during class select
weapon = 'Rifle'    #weapon being used, will change based on class and powerups
currentHealth = 40  #set for scout class, but will change according to class selected #is the current health of player
maxHealth = 40  #player max health, so health cant extend more than max after getting healing pack
Heat = 20   #default distance between every bullet fired by player, changes as upgrades are recieved
damage = 1  #damage each bullet does, changes as upgrades are recived
guy = image.load('Pictures/'+weapon+' '+Class+'.png')   #picture can change according to class and weapon being used
shots = []  #list where all shots made by player will be added
shotgunList = []    #shotgunList is a the same as shots but is a 3d list and is only for shotgun tank(for each shot in shots there are 3 shots)
badshots = []   #shots made by badguys(alien 3) will be added to this list
power = 5.0     #speed at which bullets travel
gunHeat = 0     #cooldown for when bullets are shot, creating space between each shot
keys = key.get_pressed()    #checks which key is pressed
BADSPEED = 2.5  #speed for da badguys
badGuys = []    #all of the badguys will be added in these lists, but at the beginning of each room function cuz enemies are specific to each room
badGuys2 = []
badGuys3 = []
Wcrates = []    #powerups are specific to rooms, so they will be added to this list in the rooms they are supposed to be in
bombs = []      #coordinates and frame number for where the bombs will blow up will be added here
right = (924, 325)  #directions are for ease of blitting of arrows
up = (487, 0)
left = (0, 325)
down = (487, 600)
rightRect = Rect(934, 330, 80, 30)  #rects for each direction
upRect = Rect(492, 5, 30, 80)
leftRect = Rect(5, 335, 80, 30)
downRect = Rect(497, 605, 30, 80)
holeRect = Rect(487, 325, 50, 50)    #rect for hole that leads to the boss rooms
#----------Pictures being Loaded------------#

titleScreen = image.load('Pictures/Title Screen.png').convert()
titleBack = transform.scale(titleScreen, (1035, 800))

campaignButtonPic = image.load('Pictures/Campaign.png').convert_alpha()
campaignButton = transform.scale(campaignButtonPic, (200, 50))

endlessButtonPic = image.load('Pictures/Endless.png').convert_alpha()
endlessButton = transform.scale(endlessButtonPic, (200, 50))

instructionsButtonPic = image.load('Pictures/Instructions.png').convert_alpha()
instructionsButton = transform.scale(instructionsButtonPic, (300, 50))

newPic = image.load('Pictures/New Game Button.png').convert_alpha()
newButton = transform.scale(newPic, (200, 50))
loadPic = image.load('Pictures/Load Game Button.png').convert_alpha()
loadButton = transform.scale(loadPic, (200, 50))

classScreen = image.load('Pictures/Class Selection Background.jpg').convert()
classBack = transform.scale(classScreen, (1035, 800))

scout1 = image.load('Pictures/Rifle Scout.png').convert_alpha()
rScout = transform.scale(scout1, (50, 50))
marine1 = image.load('Pictures/Rifle Marine.png').convert_alpha()
rMarine = transform.scale(marine1, (50, 50))
tank1 = image.load('Pictures/Pistol Tank.png').convert_alpha()
pTank = transform.scale(tank1, (50, 50))

classScreenName = image.load('Pictures/pick your class.png').convert_alpha()
classTitle = transform.scale(classScreenName, (400, 100))
startPic = image.load('Pictures/Start Button.png').convert_alpha()
start = transform.scale(startPic, (200, 75))
scoutName = image.load('Pictures/Scout Name.png').convert_alpha()
scoutLable = transform.scale(scoutName, (150, 50))
scoutWords = image.load('Pictures/Scout Stats.png').convert_alpha()
scoutInfo = transform.scale(scoutWords, (300, 175))
marineName = image.load('Pictures/Marine Name.png').convert_alpha()
marineLable = transform.scale(marineName, (150, 50))
marineWords = image.load('Pictures/Marine Stats.png').convert_alpha()
marineInfo = transform.scale(marineWords, (300, 175))
tankName = image.load('Pictures/Tank Name.png').convert_alpha()
tankLable = transform.scale(tankName, (100, 50))
tankWords = image.load('Pictures/Tank Stats.png').convert_alpha()
tankInfo = transform.scale(tankWords, (300, 175))

back = image.load('Pictures/Back.png').convert_alpha()
back = transform.scale(back, (150, 75))
story = image.load('Pictures/Story.png').convert_alpha()
story = transform.scale(story, (525, 163))
controls = image.load('Pictures/Controls.png').convert_alpha()
controls = transform.scale(controls, (525, 163))
roomExplain = image.load('Pictures/Rooms.png').convert_alpha()
roomExplain = transform.scale(roomExplain, (525, 163))
goal = image.load('Pictures/Goal.png').convert_alpha()
goal = transform.scale(goal, (525, 163))

resume = image.load('Pictures/Resume.png').convert_alpha()
resume = transform.scale(resume, (175, 50))
saveQuit = image.load('Pictures/Save+Quit.png').convert_alpha()
saveQuit = transform.scale(saveQuit, (275, 50))
quitButton = image.load('Pictures/Quit.png').convert_alpha()
quitButton = transform.scale(quitButton, (100, 50))

rilfeScout = image.load('Pictures/Rifle Scout.png').convert_alpha()
back1 = image.load("Pictures/Level One Background.png").convert()
back1 = transform.scale(back1, (2000, 2000))
back2 = image.load('Pictures/Level Two Background.png').convert()
back2 = transform.scale(back2, (1024, 700))
badguy1 = image.load("Pictures/Alien 1.png").convert_alpha()
badguy1 = transform.scale(badguy1, (60, 60))
badguy2 = image.load('Pictures/Alien 2.png').convert_alpha()
badguy2 = transform.scale(badguy2,(70,60))
badguy3 = image.load('Pictures/Alien 3.png').convert_alpha()
badguy3 = transform.scale(badguy3, (80,80))
boss = image.load('Pictures/Boss Alien.png').convert_alpha()
boss = transform.scale(boss,(80,80))
arrow = image.load('Pictures/arrow.png').convert_alpha()
rightArrow = transform.scale(arrow, (100,50))
upArrow = transform.rotate(rightArrow, (90))
leftArrow = transform.rotate(rightArrow, (180))
downArrow = transform.rotate(rightArrow, (270))
hole = image.load('Pictures/hole.png').convert_alpha()
hole = transform.scale(hole, (50,50))

ship4 = image.load('Pictures/Alien(2) Ship 1.png').convert_alpha()
ship4 = transform.scale(ship4, (225, 525))
ship5 = image.load('Pictures/Alien(2) Ship 2.png').convert_alpha()
ship5 = transform.scale(ship5, (225, 575))
ship6 = image.load('Pictures/Alien(2) Ship 3.png').convert_alpha()
ship7 = image.load('Pictures/Alien(3) Ship 1.png').convert_alpha()
ship7 = transform.scale(ship7, (300, 450))
ship8 = image.load('Pictures/Alien(3) Ship 2.png').convert_alpha()
ship8 = transform.scale(ship8, (225,300))
ship9 = image.load('Pictures/Earth Ship.png').convert_alpha()
ship9 = transform.scale(ship9, (250, 400))
build1 = image.load('Pictures/Building 1.png').convert_alpha()
build1 = transform.scale(build1, (350, 900))
build2 = image.load('Pictures/Building 2.png').convert_alpha()
build2 = transform.scale(build2, (200, 550))
build3 = image.load('Pictures/Infected Building 1.png').convert_alpha()
build3 = transform.scale(build3, (480, 480))
build4 = image.load('Pictures/Infected Building 2.png').convert_alpha()
build4 = transform.scale(build4, (300, 150))
build4 = transform.rotate(build4, (90))
build5 = image.load('Pictures/Infected Building 3.png').convert_alpha()
build5 = transform.scale(build5, (125,100))
crat = image.load("Pictures/Weapon Crate.png").convert_alpha()
crat3 = image.load('Pictures/Med Crate.png').convert_alpha()
junk1 = image.load('Pictures/Junk 1.png').convert_alpha()
junk1 = transform.scale(junk1, (75, 150))
junk2 = image.load('Pictures/Junk 2.png').convert_alpha()
junk2 = transform.scale(junk2, (75, 150))
junk2 = transform.rotate(junk2, (180))
junk3 = image.load('Pictures/Junk 3.png').convert_alpha()
junk3 = transform.scale(junk3, (100, 150))
junk3 = transform.rotate(junk3, (90))
junk4 = image.load('Pictures/Junk 4.png').convert_alpha()
junk5 = image.load('Pictures/Junk 5.png').convert_alpha()
junk5 = transform.rotate(junk5, (90))
junk6 = image.load('Pictures/Junk 6.png').convert_alpha()
speed = 5   #speed for player movement (changes based on class

mixer.init()    #initialized the music system
mixer.music.load("Music/Ambient Space Music.mp3")   #background music file loaded

for i in range(1, 17):  #adding sprites to pics list
    bombPics+=[(image.load("explosion/explosion"+str(i)+".png"))]


def distance(x1, y1, x2, y2):   #uses trig to get distance from one point to another
    return ((x1-x2)**2+(y1-y2)**2)**0.5


def moveGuy(x, y): #moves player based on key pressed and speed
    global guyx
    global guyy
    global lastx
    global lasty
    keys = key.get_pressed()
    if keys[ord("a")]:
        lastx = guyx
        guyx -= speed
    if keys[ord("d")]:
        lastx = guyx
        guyx += speed
    if keys[ord("w")]:
        lasty = guyy
        guyy -= speed
    if keys[ord("s")]:
        lasty = guyy
        guyy += speed
    if guyx < 0: guyx = 0   #preventing player from walking off the screen
    if guyx > 1024 - 35: guyx = 1024 - 35
    if guyy < 0: guyy = 0
    if guyy > 700 - 35: guyy = 700 - 35


def turn(): #turns player image based on where mx my are so player points at mouse
    global angle
    mx, my = mouse.get_pos()
    angle = degrees(atan2(mx-guyx, my-guyy))-180


def guyRect(x, y):  #rect around the player, used for checking collides in things such as bullets and junk
    grect = Rect(x, y, 40, 40)
    return grect


def bossRect(b):    #rect for boss, used to check if bullets hit and if player hit
    bossRect=Rect(b[0]+20,b[1]+20, 80, 80)
    return bossRect


def vectToXY(mag, ang):  #takes magnitude(length)and angle of a vector and splits into x and y components
    rang = radians(ang)  #using basic trig
    x = cos(rang)*mag
    y = sin(rang)*mag
    return x, y


def addShot(ang, power):    #function to add x, y and velocity values to each shot taken, which will be added
    shot = [0, 0, 0, 0]     #to shots list
    shot[X], shot[Y] = vectToXY(30, ang) #gets distance needed to be travelled by bullet x and y positions
    shot[X] += guyx #makes shot start from guy
    shot[Y] += guyy# ^
    shot[VX], shot[VY] = vectToXY(power, ang) #gets velocity x and y needed
    return shot


def addBadShot(bguy, ang, power):   #adds each shot taken by the badguys into a list which will be added to another
    badshot = [0, 0, 0, 0]          #list
    badshot[X], badshot[Y] = vectToXY(30, ang)
    badshot[X] += bguy[X]+40
    badshot[Y] += bguy[Y]+40
    badshot[VX], badshot[VY] = vectToXY(power, ang)
    return badshot

def shotgun(ang, ang1 ,ang2, power):    #same idea as addShot, but shot has 3 shots in it and is a 3d list instead of 2d
    shot=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]    #because it shoots 3 bullets at a time
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
    global Boss
    global badshots
    killlist = []   #bullets that need to be removed from the screen will be added here
    for shot in shots: #adding velicity x and y to every bullet in shots
        shot[X] += shot[VX]
        shot[Y] += shot[VY]
        if shot[X] > guyx+Range or guyx-Range > shot[X] or guyy-Range > shot[Y] or shot[Y] > guyy+Range:
            #add bullet to killlist if it reaches maximum range(each class has diff range)
            killlist.append(shot)
        for bguy in badGuys[:]:
            eRect=enemyRect(bguy)
            if eRect.collidepoint(shot[X], shot[Y]) and shot not in killlist:
                #if bullet hits enemy and it isnt already in killlist
                bguy[3]-=damage #subtract damage from enemy 1 health
                killlist.append(shot) #add the shot to be deleted from screen
                if bguy[3]<=0:#if health is 0 or less the badguy dies
                    badGuys.remove(bguy)
        for bguy in badGuys2:   #mostly same as badGuys but is 1 hit KO
            eRect = enemyRect(bguy)
            if eRect.collidepoint(shot[X], shot[Y]):
                badGuys2.remove(bguy)
        for bguy in badGuys3[:]: #same as other two but has 3 health
            eRect=enemyRect(bguy)
            if eRect.collidepoint(shot[X], shot[Y]) and shot not in killlist:
                bguy[3]-=damage
                killlist.append(shot)
                if bguy[3]<=0:
                    badGuys3.remove(bguy)
                    badshots = []
        for b in Boss: #does same as other loops but with boss, and boss has 50 health
            bossrect = bossRect(b)
            if bossrect.collidepoint(shot[X],shot[Y]) and shot not in killlist:
                b[3]-=damage
                killlist.append(shot)
                print(b[3])
                if b[3]<=0:
                    Boss.remove(b)
    for s in killlist:
        shots.remove(s)


def moveShotgun(shotgunList):   #does the exact same thing as moveShots but specialized for the shotgun
    global badshots
    killlist = []
    for s in shotgunList:
        for shot in s:
            shot[X] += shot[VX]
            shot[Y] += shot[VY]
            if shot[X] > guyx+200 or guyx-200 > shot[X] or guyy-200 > shot[Y] or shot[Y] > guyy+200 and shot not in killlist:
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
                        badshots = []
            for boss in Boss:
                bossrect = bossRect(boss)
                if bossrect.collidepoint(shot[X],shot[Y]) and shot not in killlist:
                    boss[3]-=damage
                    killlist.append(shot)
                    print(boss[3])
                    if boss[3]<=0:
                        Boss.remove(boss)
    for s in killlist:
        for k in shotgunList:
            for j in k:
                if s==j:
                    k.remove(j)


def moveBadShots(bguy, badshots, domage):   #same as moveShots but uses the shots shot by badguys and inflicts damage to the player
    global currentHealth
    killlist = []
    for shot in badshots:
        shot[X] += shot[VX]
        shot[Y] += shot[VY]
        if shot[X] > bguy[X]+4000:
            killlist.append(shot)
        gRect = guyRect(guyx, guyy)
        if gRect.collidepoint(shot[X], shot[Y]):
            currentHealth-=domage
            killlist.append(shot)
    for s in killlist:
        badshots.remove(s)


def badMove(bguy, x, y, BADSPEED):  #gets the amount the badguy needs to move in order to follow the player
    #and gets the angle needed to trun and face the guy
    import math
    dist = max(1, distance(bguy[0], bguy[1], x, y))
    moveX = (x-bguy[0])*BADSPEED/dist #the move from bguy x to guyx
    moveY = (y-bguy[1])*BADSPEED/dist #the move from bguy y to guyy
    ang = math.atan2(-moveY, moveX) #the angle at which the bguy turns to face the player
    return moveX, moveY, math.degrees(ang)


def moveBadGuys1(bguy, guyx, guyy): #adds the values calculated in badMove to the bguy1s
    moveX, moveY, moveAng = badMove(bguy, guyx, guyy, 2.5)
    bguy[0] += moveX
    bguy[1] += moveY
    bguy[2] = moveAng-90


def moveBadGuys2(bguy, guyx, guyy): #adds the values calculated in badMove to the bguy2s, move faster than bguy1
    moveX, moveY, moveAng = badMove(bguy, guyx, guyy, 4)
    bguy[0] += moveX
    bguy[1] += moveY
    bguy[2] = moveAng-90


def moveBadGuys3(bguy, guyx, guyy): #shooter enemies, so they dont move only rotate, so only adds teh angle to the bguy list
    moveX, moveY, moveAng = badMove(bguy, guyx, guyy, 4)
    bguy[2] = moveAng-90
    return moveAng


def boomBombs(bombs): #goes through the coordinates in bombs, and blits the booom sprites at those coordinates,
    #and goes through each picture in teh sprites list
    rem=[]
    for bomb in bombs:
        bomb[3]+=1
        if bomb[3]==16:
            rem.append(bomb)
    for bomb in rem: #removes bombs that have finished explofing
        bombs.remove(bomb)


def enemyRect(bguy): #makes a rect around bguy
    eRect = Rect(bguy[0]+35, bguy[1]+35, 40, 40)
    return eRect

def checkHit(rect):     #checks if an enemey hits player, so enemies coordinates can be added
    global bombs        #to the bombs list
    global currentHealth
    global badGuys
    global badGuys2
    for bguy in badGuys: #if a bguy from badGuys hits player, the coordinates are added to bomb list
        if rect.collidepoint(bguy[0]+35, bguy[1]+35):
            currentHealth -= 10 #subtracts 10 health if bomb goes boomb
            badGuys.remove(bguy) #enemies are suicide bombers, so they die too
            bombs.append([bguy[0], bguy[1],0,0])
    for bguy in badGuys2: #same as previous loop but with badGuys2
        if rect.collidepoint(bguy[0]+35, bguy[1]+35):
            currentHealth -= 10
            badGuys2.remove(bguy)
            bombs.append([bguy[0], bguy[1], 0, 0])
            return True
    return False

def instaDeath(guyx,guyy,rect): #if guy collides with the boss, inst death (welcome to dark souls)
    global currentHealth
    if rect.collidepoint(guyx,guyy):
        currentHealth = 0

def checkWinLevel(badGuys): #if all enemies in the room are dead, level is won
    if len(badGuys) == 0 and len(badGuys2) == 0 and len(badGuys3) == 0 and len(Boss) == 0:
        return True
    return False


def checkLoseLevel(health): #if you have 0 health, you die and lose the game
    if health <= 0:
        return True


def checkUpgrade(Wcrates, Mcrates, guyx, guyy): #checks if any crate is collided with, and gives powerup accordingly
    global guy
    global crateNum
    global weapon
    global maxHealth
    global currentHealth
    global Heat
    global damage

    for crate in Wcrates:   #blits crates to designated coordinates and makes a rect to check if you collide with it
        crateRect = Rect(crate[0], crate[1], 40, 40)
        if crateRect.collidepoint(guyx + 15, guyy + 15):
            crateNum = crate[2]
            Wcrates.remove(crate)

    for med in Mcrates:     #checks if you collide with the medrect, and if you do add 20 health, with a cap of maxhealth
        medRect = Rect(med[0], med[1], 40, 40)
        if medRect.collidepoint(guyx + 15, guyy + 15):
            currentHealth += 20
            Mcrates.remove(med)
            if currentHealth > maxHealth: currentHealth = maxHealth
#-------Upgrades respective to class and cratenum--------#
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



def goodHealthMeter(currentHealth): #makes a rect for the current health so the player knows how much health they have left
    healthRect = Rect(10, 10, 10+(currentHealth*2), 20)
    return healthRect


def drawScene(badGuys, badGuys2, arrows, back, builds): #actually blits and draws EVERYTHING
    screen.blit(back, (0, 0))   #background
    guy = image.load('Pictures/' + weapon + ' ' + Class + '.png') #pic for guy based on class and weapon
    pic = transform.scale(guy, (50, 50)) #resizes guy so hes not a giant
    turn() #calling function to get teh angle needed for player to face cursor
    pic = transform.rotate(pic, angle)  #rotates guy to the angle gotten from turn()
    screen.blit(pic, (guyx - 17, guyy - 17)) #actually blits the guy after make necessary alterations
    shoot2 = image.load("Pictures/redbullet.png").convert()#the image of the bullet to be shot
    shoot2 = transform.scale(shoot2, (7, 7)) #resizes the bullet so it looks like bullet instead of a giant ball

    for crate in Wcrates: #blits the weapon crates in Wcrates list
        weaponcrate = transform.scale(crat, (40,60))
        screen.blit(weaponcrate, (crate[0], crate[1]))
        checkUpgrade(Wcrates, Mcrates, guyx, guyy)

    for med in Mcrates: #blits all of the med crates in Mcrates list
        medcrate = transform.scale(crat3, (40, 60))
        screen.blit(medcrate, (med[0], med[1]))
        checkUpgrade(Wcrates, Mcrates, guyx, guyy)
    if weapon == 'Shotgun': #if the weapon is shotgun, uses spreadshot and draws 3 bullets for every shot
        for s in shotgunList[:]:
            for shot in s:
                screen.blit(shoot2, (int(shot[X]), int(shot[Y])))
    for shot in shots[:]:   #draws all of the bullets in shots
        screen.blit(shoot2, (int(shot[X]), int(shot[Y])))

    for shot in badshots[:]: #draws all of the shots shot by badGuys3
        screen.blit(shoot2, (int(shot[X]), int(shot[Y])))
    for shot in bossshots[:]: #draws the bossshots
        screen.blit(shoot2, (int(shot[X]), int(shot[Y])))

    for bguy in badGuys: #draws every bguy in teh badGuys list
        moveBadGuys1(bguy, guyx, guyy)
        alien1 = transform.rotate(badguy1, bguy[2]) #rotates the image to face the player
        screen.blit(alien1, bguy[:2])

    for bomb in bombs: #blits the sprites for the bombs, using the frame # and coordinates
        screen.blit(bombPics[bomb[3]], (bomb[X],bomb[Y]))

    if page=='room_3B': #boss is only in room 3B, so this only applies to room 3B
        for b in Boss:
            moveBadGuys1(b,guyx,guyy) #draws the boss and rotates according to angle
            bosss=transform.rotate(boss,b[2])
            screen.blit(bosss, b[:2])
            bossrect= bossRect(b)
            draw.rect(screen,(255,0,0),bossrect,1) #rect to avoid, cuz if you hit it insta death is activated

    for bguy in badGuys2: #draws each of the bguys in badGuys2
        moveBadGuys2(bguy, guyx, guyy)
        alien2= transform.rotate(badguy2, bguy[2])
        screen.blit(alien2, bguy[:2])

    for bguy in badGuys3:
        moveBadGuys3(bguy, guyx, guyy)
        alien3 = transform.rotate(badguy3, bguy[2])
        screen.blit(alien3, bguy[:2])

    for b in builds: #draws the buildings fo that level
        screen.blit(b[0], (b[1], b[2]))

    grect = guyRect(guyx, guyy) #rect around the plater to check if anything hits him
    checkHit(grect) #checks if hit by any enemies
    healthRect = goodHealthMeter(currentHealth)
    draw.rect(screen, (0, 255, 0), healthRect)  #draws the health bar
    healthArea = Rect(10,30,100,100)    #the place to blit "health" and current health/max health
    weaponArea = Rect(900,10,200,50)    #the place to blit current weapon
    weaponText = arialFont2.render("Weapon:"+weapon,True,(255,0,0)) #what will be written
    healthPic = arialFont2.render('Health:%s/%s'%(str(currentHealth),str(maxHealth)),True,(0,255,0))   #what will be written fro health
    screen.blit(healthPic,(healthArea.x+3,healthArea.y+2)) #blitting health words to screen
    screen.blit(weaponText,(weaponArea.x+3,weaponArea.y+2)) #blitting the word for current weapon type

    win = checkWinLevel(badGuys) #only allowed to leave rooom if all enemies are dead
    if win:
        #arrows are where the player walks to in order to move to next room
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

    lose = checkLoseLevel(currentHealth) #if health is 0 you lose the level
    if lose:
        screen.fill((0, 0, 0))
    display.flip()


def fadeIn():
    image=screen.copy().convert()
    for i in range(255):
        screen.fill((0, 0, 0)) #starts with black screen
        image.set_alpha(255-i)#adds back the alpha slowly through the loop and gives fade effect
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
    global Class
    global weapon
    global maxHealth
    global currentHealth
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
            saveFile = open(myFiles[0], 'r')
            save = saveFile.read().split()
            Class = save[0]
            if save[0] == 'Scout':
                maxHealth = 40
            if save[0] == 'Marine':
                maxHealth = 70
            if save[0] == 'Tank':
                maxHealth = 100
            weapon = save[1]
            currentHealth = int(save[2])
            return save[3]
        if save2.collidepoint(mx, my) and mb[0] == 1:
            saveFile = open(myFiles[1], 'r')
            save = saveFile.read().split()
            Class = save[0]
            if save[0] == 'Scout':
                maxHealth = 40
            if save[0] == 'Marine':
                maxHealth = 70
            if save[0] == 'Tank':
                maxHealth = 100
            weapon = save[1]
            currentHealth = int(save[2])
            return save[3]
        if save3.collidepoint(mx, my) and mb[0] == 1:
            saveFile = open(myFiles[2], 'r')
            save = saveFile.read().split()
            Class = save[0]
            if save[0] == 'Scout':
                maxHealth = 40
            if save[0] == 'Marine':
                maxHealth = 70
            if save[0] == 'Tank':
                maxHealth = 100
            weapon = save[1]
            currentHealth = int(save[2])
            return save[3]
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
    global speed
    global Range
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
            Range = 800
            speed = 7
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
            Range = 400
            speed = 5
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
            Range = 200
            speed = 3
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

'''
def endlessMode():
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
    global shots
    global shotgunList
    endlessRunning = True
    shots = []
    badGuys = [[100, 100, 0, 2]]
    badGuys2 = [[]]
    badGuys3 = [[400, 300, 0, 3], [100, 600, 0, 3]]
    Wcrates = []
    arrows = []
    builds = []
    Mcrates = []

    while endlessRunning:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                endlessRunning = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_p:
                    a = pause()
                    if a != None:
                        return a

        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        if mb[0] == 1 and gunHeat <= 0:
            gunHeat = Heat
            if weapon == 'Shotgun':
                shotgunList.append(
                    shotgun(-angle - 90, -angle - (90 + randint(0, 10)), -angle - (90 - randint(0, 10)), power))
            else:
                shots.append(addShot(-angle - 90, power))
        for bguy in badGuys3:
            ang = moveBadGuys3(bguy, guyx, guyy)
            if randint(0, 50) == 1:
                badshots.append(addBadShot(bguy, -ang, 10))
            moveBadShots(bguy, badshots)

        gunHeat -= 1
        boomBombs(bombs)
        moveShots(shots)
        moveShotgun(shotgunList)
        drawScene(badGuys, badGuys2, arrows, back1, builds)
        moveGuy(guyx, guyy)
        myClock.tick(60)
        blockMove([[Rect(50, 300, 250, 400), 50, 300, 300, 700]])
        display.flip()
        win = checkWinLevel(badGuys)

        display.flip()
    return 'menu'
'''

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
        if page != 'endless':
            screen.blit(saveQuit, (375, 325))
        screen.blit(quitButton, (462, 425))
        print(page)
        display.flip()
        '''
        if page == 'endless':
            if resumeRect.collidepoint(mx, my) and mb[0] == 1:
                pauseRunning = False
            if quitRect.collidepoint(mx, my) and mb[0] == 1:
                return 'menu'
        '''
        if resumeRect.collidepoint(mx, my) and mb[0] == 1:
            pauseRunning = False
        if saveQuitRect.collidepoint(mx, my) and mb[0] == 1:
            return 'menu'
        if quitRect.collidepoint(mx, my) and mb[0] == 1:
            return 'menu'


def blockMove(image): #stops guy from walking on space ships and junk pictures so they are like obtacles
    global lastx
    global lasty
    global guyx
    global guyy
    grect = guyRect(guyx, guyy)
    for i in image:
        imageRect = i[0]
        if grect.colliderect(imageRect): #if guy collides with an image
            guyx = lastx #the current positions turn into the old positions, stopping the player from moving over the picture
            guyy = lasty

######============ROOMS==============#####
#all rooms have the same code, just different lists
def room_1():
    fadeIn() #when you enter the room does fade effect
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
    global shots
    global shotgunList
    shots = [] #shots is reset when you enter the room so old shots from the last room dont carry in
    room_1Running = True
    #all enemies are specific to each room so they are defined in each room
    badGuys=[[100,100,0,2]]
    Wcrates=[] #if there are any crates in the room they would be listed in the Wcrates list in each room function
    arrows = [up] #draws an arrow in the specified location(s) and lead to other rooms
    builds = [[ship9, 50, 300]] #list of buildings that need to be drawn. specific to each room
    Mcrates = [] #same a Wcrates

    while room_1Running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
                room_1Running = False
            if evnt.type == KEYDOWN:
                if evnt.key == K_p:
                    a = pause()
                    if a != None:
                        return a

        mb = mouse.get_pressed()
        if mb[0] == 1 and gunHeat <= 0:
            gunHeat = Heat
            if weapon == 'Shotgun': #since shotgun is the only one with spreadshot, if the weapon isnt shotgun
                #the bullets will have to be used with addShot
                shotgunList.append(shotgun(-angle - 90, -angle - (90+randint(0,10)), -angle - (90-randint(0,10)), power))
            else:
                shots.append(addShot(-angle - 90, power))
        for bguy in badGuys3:
            ang = moveBadGuys3(bguy, guyx, guyy)
            if randint(0,100)==1: #has a 1/100 chance every time it loops around to shoot, making it completely random shooting
                badshots.append(addBadShot(bguy,-ang,10))
            moveBadShots(bguy,badshots,10)

        gunHeat -= 1 #since gunheat has to be at least 0 for shot to shoot, subtract 1 everytime it loops around so player can shoot again
        boomBombs(bombs)
        moveShots(shots)
        moveShotgun(shotgunList)
        drawScene(badGuys, badGuys2, arrows, back1, builds)
        moveGuy(guyx, guyy)
        myClock.tick(60)
        blockMove([[Rect(50, 300, 250, 400)]])
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
    global shots
    global shotgunList
    global badguys3
    shots = []
    shotgunList = []
    room_2Running = True
    badGuys=[[100,700,0,2],[10,500,0,2],[200,400,0,2],[500,450,0,2],[300,20,0,2]]
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
                    a = pause()
                    if a != None:
                        return a

        mb = mouse.get_pressed()
        if mb[0] == 1 and gunHeat <= 0:
            gunHeat = Heat
            if weapon == 'Shotgun':
                shotgunList.append(shotgun(-angle - 90, -angle - (90+randint(0,10)), -angle - (90-randint(0,10)), power))
            else:
                shots.append(addShot(-angle - 90, power))
        for bguy in badGuys3:
            ang = moveBadGuys3(bguy, guyx, guyy)
            if randint(0,100)==1:
                badshots.append(addBadShot(bguy,-ang,10))
            moveBadShots(bguy,badshots,10)

        gunHeat -= 1
        boomBombs(bombs)
        moveShots(shots)
        moveShotgun(shotgunList)
        drawScene(badGuys, badGuys2, arrows, back1, builds)
        moveGuy(guyx, guyy)
        blockMove([[Rect(150, 80, 110, 580)]])
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
    global shots
    global shotgunList
    shots = []
    shotgunList = []
    room_3Running = True
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
                    a = pause()
                    if a != None:
                        return a

        mb = mouse.get_pressed()
        if mb[0] == 1 and gunHeat <= 0:
            gunHeat = Heat
            if weapon == 'Shotgun':
                shotgunList.append(shotgun(-angle - 90, -angle - (90+randint(0,10)), -angle - (90-randint(0,10)), power))
            else:
                shots.append(addShot(-angle - 90, power))
        for bguy in badGuys3:
            ang = moveBadGuys3(bguy, guyx, guyy)
            if randint(0,100)==1:
                badshots.append(addBadShot(bguy,-ang,10))
            moveBadShots(bguy,badshots,10)

        gunHeat -= 1
        boomBombs(bombs)
        moveShots(shots)
        moveShotgun(shotgunList)
        drawScene(badGuys, badGuys2, arrows, back1, builds)
        moveGuy(guyx, guyy)
        blockMove([[Rect(675, 60, 190, 280)]])
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
    global shots
    global shotgunList
    shots = []
    shotgunList = []
    room_4Running = True
    badGuys=[[140,600,0,2],[10,250,0,2],[200,400,0,2],[900,320,0,2],[820,350,0,2]]
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
                    a = pause()
                    if a != None:
                        return a

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
            if randint(0,100)==1:
                badshots.append(addBadShot(bguy,-ang,10))
            moveBadShots(bguy,badshots,10)

        gunHeat -= 1
        boomBombs(bombs)
        moveShots(shots)
        moveShotgun(shotgunList)
        drawScene(badGuys, badGuys2, arrows, back1, builds)
        moveGuy(guyx, guyy)
        blockMove([[Rect(185, 155, 60, 140)],
                   [Rect(555, 480, 70, 150)],
                   [Rect(760, 210, 130, 75)]])
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
    global badGuys2
    global Wcrates
    global Mcrates
    global guyx
    global guyy
    global shots
    global shotgunList
    shots = []
    shotgunList = []
    room_5Running = True
    badGuys=[[100,700,0,2],[10,500,0,2],[500,450,0,2]]
    badGuys2 = [[200,200,0],[300,100,0]]
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
                    a = pause()
                    if a != None:
                        return a

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
            if randint(0,100)==1:
                badshots.append(addBadShot(bguy,-ang,10))
            moveBadShots(bguy,badshots,10)

        gunHeat -= 1
        boomBombs(bombs)
        moveShots(shots)
        moveShotgun(shotgunList)
        drawScene(badGuys, badGuys2, arrows, back1, builds)
        moveGuy(guyx, guyy)
        blockMove([[Rect(160, 100, 100, 250)],
                   [Rect(270, 510, 200, 100)],
                   [Rect(610, 160, 80, 160)]])
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
    global badGuys2
    global Wcrates
    global Mcrates
    global guyx
    global guyy
    global shots
    global shotgunList
    shots = []
    shotgunList = []
    room_6Running = True
    badGuys=[[100,700,0,2],[10,500,0,2],[200,400,0,2],[500,450,0,2]]
    badGuys2 = [[300,700,0],[900,100,0]]
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
                    a = pause()
                    if a != None:
                        return a

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
            if randint(0,100)==1:
                badshots.append(addBadShot(bguy,-ang,10))
            moveBadShots(bguy,badshots,10)

        gunHeat -= 1
        boomBombs(bombs)
        moveShots(shots)
        moveShotgun(shotgunList)
        drawScene(badGuys, badGuys2, arrows, back1, builds)
        moveGuy(guyx, guyy)
        blockMove([[Rect(305, 170, 120, 190)],
                   [Rect(310, 380, 170, 200)],
                   [Rect(210, 300, 80, 250)]])
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
    global badGuys2
    global shots
    global shotgunList
    shots = []
    shotgunList = []
    room_7Running = True
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
                    a = pause()
                    if a != None:
                        return a

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
            if randint(0,100)==1:
                badshots.append(addBadShot(bguy,-ang,10))
            moveBadShots(bguy,badshots,10)

        gunHeat -= 1
        boomBombs(bombs)
        moveShots(shots)
        moveShotgun(shotgunList)
        drawScene(badGuys, badGuys2, arrows, back1, builds)
        moveGuy(guyx, guyy)
        blockMove([[Rect(320, 195, 180, 490)]])
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
    global badGuys2
    global Wcrates
    global Mcrates
    global guyx
    global guyy
    global shots
    global shotgunList
    shots = []
    shotgunList = []
    room_8Running = True
    badGuys=[[100,300,0,2],[10,500,0,2],[200,400,0,2],[500,450,0,2]]
    badGuys2 = [[123,342,0],[234,523,0]]
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
                    a = pause()
                    if a != None:
                        return a

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
            if randint(0,100)==1:
                badshots.append(addBadShot(bguy,-ang,10))
            moveBadShots(bguy,badshots,10)

        gunHeat -= 1
        boomBombs(bombs)
        moveShots(shots)
        moveShotgun(shotgunList)
        drawScene(badGuys, badGuys2, arrows, back1, builds)
        moveGuy(guyx, guyy)
        blockMove([[Rect(200, 240, 160, 80)],
                   [Rect(680, 100, 165, 625)]])
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
    global badGuys2
    global Wcrates
    global Mcrates
    global guyx
    global guyy
    global shots
    global shotgunList
    shots = []
    shotgunList = []
    room_9Running = True
    badGuys=[[10,500,0,2],[200,400,0,2],[500,450,0,2]]
    badGuys2 = [[234,453,0],[455,243,0],[543,244,0]]
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
                    a = pause()
                    if a != None:
                        return a

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
            if randint(0,100)==1:
                badshots.append(addBadShot(bguy,-ang,10))
            moveBadShots(bguy,badshots,10)

        gunHeat -= 1
        boomBombs(bombs)
        moveShots(shots)
        moveShotgun(shotgunList)
        drawScene(badGuys, badGuys2, arrows, back1, builds)
        moveGuy(guyx, guyy)
        blockMove([[Rect(280, 115, 440, 420)]])
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
    global badGuys2
    global Wcrates
    global Mcrates
    global guyx
    global guyy
    global shots
    global shotgunList
    shots = []
    shotgunList = []
    room_10Running = True
    badGuys=[[100,700,0,2],[10,500,0,2],[200,400,0,2],[500,450,0,2]]
    badGuys2 = [[randint(0,1024),randint(0,700),0],
                [randint(0,1024),randint(0,700),0],
                [randint(0,1024),randint(0,700),0]]
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
                    a = pause()
                    if a != None:
                        return a

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
            if randint(0,100)==1:
                badshots.append(addBadShot(bguy,-ang,10))
            moveBadShots(bguy,badshots,10)

        gunHeat -= 1
        boomBombs(bombs)
        moveShots(shots)
        moveShotgun(shotgunList)
        boomBombs(bombs)
        drawScene(badGuys, badGuys2, arrows, back1, builds)
        moveGuy(guyx, guyy)
        blockMove([[Rect(140, 170, 100, 80)],
                   [Rect(190, 420, 100, 80)],
                   [Rect(435, 270, 100, 80)],
                   [Rect(615, 200, 100, 80)],
                   [Rect(635, 520, 100, 80)]])
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
    global badGuys2
    global Wcrates
    global Mcrates
    global guyx
    global guyy
    global shots
    global shotgunList
    shots = []
    shotgunList = []
    room_11Running = True
    badGuys2=[[100,600,0,2],[10,500,0,2],[200,400,0,2],[500,450,0,2]]
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
                    a = pause()
                    if a != None:
                        return a

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
            if randint(0,100)==1:
                badshots.append(addBadShot(bguy,-ang,10))
            moveBadShots(bguy,badshots,10)

        gunHeat -= 1
        boomBombs(bombs)
        moveShots(shots)
        moveShotgun(shotgunList)
        drawScene(badGuys, badGuys2, arrows, back1, builds)
        moveGuy(guyx, guyy)
        blockMove([[Rect(220, 165, 100, 270)],
                   [Rect(670, 215, 100, 270)]])
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
    global badGuys2
    global Wcrates
    global Mcrates
    global guyx
    global guyy
    global shots
    global shotgunList
    shots = []
    shotgunList = []
    room_12Running = True
    badGuys2=[[100,700,0,2],[10,500,0,2],[200,400,0,2],[500,450,0,2]]
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
                    a = pause()
                    if a != None:
                        return a

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
            if randint(0,100)==1:
                badshots.append(addBadShot(bguy,-ang,10))
            moveBadShots(bguy,badshots,10)

        gunHeat -= 1
        boomBombs(bombs)
        moveShots(shots)
        moveShotgun(shotgunList)
        drawScene(badGuys, badGuys2, arrows, back1, builds)
        moveGuy(guyx, guyy)
        blockMove([[Rect(215, 320, 100, 80)],
                   [Rect(830, -50, 1024, 900)]])
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
    global badGuys2
    global Wcrates
    global Mcrates
    global guyx
    global guyy
    global shots
    global shotgunList
    shots = []
    shotgunList = []
    room_13Running = True
    badGuys2=[[100,700,0,2],[10,500,0,2],[200,400,0,2],[500,450,0,2]]
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
                    a = pause()
                    if a != None:
                        return a

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
            if randint(0,100)==1:
                badshots.append(addBadShot(bguy,-ang,10))
            moveBadShots(bguy,badshots,10)

        gunHeat -= 1
        boomBombs(bombs)
        moveShots(shots)
        moveShotgun(shotgunList)
        drawScene(badGuys, badGuys2, arrows, back1, builds)
        moveGuy(guyx, guyy)
        blockMove([[Rect(415, 295, 100, 80)],
                   [Rect(0, -50, 200, 900)]])
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
    global badGuys3
    global running
    global Class
    global gunHeat
    global weapon
    global badGuys
    global Wcrates
    global Mcrates
    global guyx
    global guyy
    global shots
    global shotgunList
    shots = []
    shotgunList = []
    room_1BRunning = True
    badGuys=[[100,700,0,2],[10,500,0,2],[200,400,0,2],[500,450,0,2]]
    badGuys2=[[100,100,0],[500,400,0]]
    badGuys3 = [[20,20,0,3],[900,20,0,3]]
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
                    a = pause()
                    if a != None:
                        return a

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
            if randint(0,100)==1:
                badshots.append(addBadShot(bguy,-ang,10))
            moveBadShots(bguy,badshots,10)

        gunHeat -= 1
        boomBombs(bombs)
        moveShots(shots)
        moveShotgun(shotgunList)
        drawScene(badGuys, badGuys2, arrows, back2, builds)
        moveGuy(guyx, guyy)
        blockMove([[Rect(0, -50, 200, 900)],
                   [Rect(800, -50, 1024, 900)]])
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
    global badGuys2
    global badGuys3
    global Wcrates
    global Mcrates
    global guyx
    global guyy
    global shots
    global shotgunList
    shots = []
    shotgunList = []
    room_2BRunning = True
    badGuys=[[100,700,0,2],[10,500,0,2],[200,400,0,2],[500,450,0,2]]
    badGuys2 = [[randint(0,1024),randint(0,700),0],
                [randint(0,1024),randint(0,700),0],
                [randint(0,1024),randint(0,700),0],
                [randint(0,1024),randint(0,700),0]]
    badGuys3 = [[20,20,0,3],[900,20,0,3]]
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
                    a = pause()
                    if a != None:
                        return a

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
            if randint(0,100)==1:
                badshots.append(addBadShot(bguy,-ang,10))
            moveBadShots(bguy,badshots,10)

        gunHeat -= 1
        boomBombs(bombs)
        moveShots(shots)
        moveShotgun(shotgunList)
        drawScene(badGuys, badGuys2, arrows, back2, builds)
        moveGuy(guyx, guyy)
        blockMove([[Rect(0, -50, 200, 900)],
                   [Rect(800, -50, 1024, 900)]])
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
    global badGuys2
    global badGuys3
    global Wcrates
    global Mcrates
    global guyx
    global guyy
    global shots
    global shotgunList
    global Boss
    shots = []
    Boss = [[512, 0, 0, 50]]
    shotgunList = []
    room_3BRunning = True
    badGuys=[[100,700,0,2],[10,500,0,2],[200,400,0,2],[500,450,0,2]]
    badGuys2 = [[randint(0,1024),randint(0,700),0],
                [randint(0,1024),randint(0,700),0],
                [randint(0,1024),randint(0,700),0]]
    badGuys3 = [[20,20,0,3],[900,20,0,3],[20,600,0,3],[900,600,0,3]]
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
                    a = pause()
                    if a != None:
                        return a

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
            if randint(0,100)==1:
                badshots.append(addBadShot(bguy,-ang,10))
            moveBadShots(bguy,badshots,10)
        for b in Boss:
            if randint(0,50)==1:
                bossshots.append(addBadShot(b, -b[2]-90, 10))
            moveBadShots(b ,bossshots,20)
            bossrect = bossRect(b)
            instaDeath(guyx,guyy,bossrect)
        gunHeat -= 1
        boomBombs(bombs)
        moveShots(shots)
        moveShotgun(shotgunList)
        drawScene(badGuys, badGuys2, arrows, back2, builds)
        moveGuy(guyx, guyy)
        blockMove([[Rect(0, -50, 200, 900)],
                   [Rect(800, -50, 1024, 900)]])
        myClock.tick(60)
        display.flip()

        win = checkWinLevel(badGuys)
        if win:
            return 'menu'
    return 'title'


page = 'room_3B'
while page != 'exit':
    mixer.music.set_volume(.7)
    mixer.music.play(-1)
    if page == 'title':
        page = title()
    if page == 'menu':
        page = menu()
    if page == 'gameLoad':
        page = gameLoad()
    if page == 'load':
        page = load()
    #if page == 'endlesss':
        #page == endless()
    if page == 'classSelect':
        page = classSelect()
    #if page == 'endlessMode':
        #page = endlessMode()
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
    if not running:
        page = 'exit'
quit()
