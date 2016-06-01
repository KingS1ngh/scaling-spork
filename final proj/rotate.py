from pygame import *
from math import *
screen=display.set_mode((800,600))
posx,posy=400,300
godX,godY=0,0
guy=image.load("MTank/MTank.png")
guy2 = image.load("MTank/MTankD.png")
guy2=transform.scale(guy2,(200,200))
angle=0
def turn():
    mx,my=mouse.get_pos()
    angle = degrees(atan2(mx-400,my-300))-180
    screen.fill((100,200,200))
    rotPic = transform.rotate(guy,angle)
    screen.blit(rotPic, (400-rotPic.get_width()//2,300-rotPic.get_height()//2))
    display.flip()

    
    
def distance(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

    
running=True    
while running:
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
    turn()
quit()
