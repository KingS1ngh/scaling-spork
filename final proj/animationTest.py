"""THINGS TO WORK ON
-BE ABLE TO MOVE WHILE BULLET STILL TRAVELS
-GET MELEE ATTACK TO WORK
-ANIMATE ENEMIES
-GET DAMAGE TO WORK
-MAKE ALIENS SHOOT
-AMMO COUNTER?
"""
from pygame import *
from random import *
screen=display.set_mode((800,600))#screen size
running=True
myClock=time.Clock()
screen.fill((211,211,211))#background colour
posx,posy=0,300#initial position of characters and other stuff
name="MTank"#just for testing, starts with melee tank character as default
end=""#variable set to see if sprite should be facing up, down left or right
#based on what end equals(if end="",up. if end="D", down)
eend=""
back1=image.load("Back1.png")
back1=transform.scale(back1,(2000,2000))
screen.blit(back1,(0,0))
screenBuff=screen.copy()
mclock=250#speed set for character movement
eposx,eposy=100,100
while running:#basic setup for running
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
###############################FUNCTIONS############################################
    keys=key.get_pressed()#gets the key that is pressed
    def character():#function to use sprite based on the global variable
        #name(takes name and end to find what sprite should be used at each time)
        global name
        global end
        guy=image.load(name+"\\"+name+end+".png")#loads sprite to be used
        guy=transform.scale(guy,(50,50))#transforms it into desired size
        screen.blit(guy,(posx,posy))#blits sprite at the position of the character
    def enemy(n,size,pos):
        global eend
        enemy=image.load("alien"+str(n)+"//"+"alien"+str(n)+eend+".png")
        enemy=transform.scale(enemy,(size))
        screen.blit(enemy,(pos))
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
            if (eposx,eposy)==(sx,sy):
                break

    def punch():#work in progress still
        global end
        sx,sy=posx,posy
        punch=image.load("stuff//slash.png")
        punch=transform.scale(punch,(20,30))
        screen.blit(punch,(sx+30,sy))
        
#################################MOVEMENT#####################################    
    if keys[K_w]:
        end=""
        screen.blit(screenBuff,(0,0))
        character()
        posy-=1
        myClock.tick(mclock)
        if posy<=0:
            posy=0
    if keys[K_s]:
        end="D"
        screen.blit(screenBuff,(0,0))
        #screen.fill((211,211,211))
        character()
        posy+=1
        myClock.tick(mclock)
        if posy>=560:
            posy=560
    if keys[K_a]:
        end="L"
        screen.blit(screenBuff,(0,0))
        #screen.fill((211,211,211))
        character()
        posx-=1
        myClock.tick(mclock)
        if posx<=0:
            posx=0
    if keys[K_d]:
        end="R"
        screen.blit(screenBuff,(0,0))
        #screen.fill((211,211,211))
        character()
        posx+=1
        myClock.tick(mclock)
        if posx>=760:
            posx=760
###############SWITCHING CHARACTERS#######################
    if keys[K_1]:
        name="MTank"
    if keys[K_2]:
        name="MMarine"
    if keys[K_3]:
        name="CScout"
####################ATTACKS##############################
    if keys[K_SPACE]:
        import time
        start_time=time.time()
        if name=="MTank":
            punch()
        if name=="CScout":
            shoot("cannon",(40,40))
        if name=="MMarine":
            shoot("shot",(20,20))
        
####################ENEMIES##############################
    if keys[K_UP]:
        eend=""
        screen.blit(screenBuff,(0,0))
        enemy(1,(55,55),(eposx,eposy))
        eposy-=1
        myClock.tick(mclock)
    if keys[K_DOWN]:
        eend="D"
        screen.blit(screenBuff,(0,0))
        enemy(1,(55,55),(eposx,eposy))
        eposy+=1
        myClock.tick(mclock)
    if keys[K_LEFT]:
        eend="L"
        screen.blit(screenBuff,(0,0))
        enemy(1,(55,55),(eposx,eposy))
        eposx-=1
        myClock.tick(mclock)
    if keys[K_RIGHT]:
        eend="R"
        screen.blit(screenBuff,(0,0))
        enemy(1,(55,55),(eposx,eposy))
        eposx+=1
        myClock.tick(mclock)
    display.flip()
quit()
