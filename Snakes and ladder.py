import pygame
import random
import numpy as np
import itertools as itt

pygame.font.init()

gridloc=np.array([(61, 511), (111, 511), (161, 511), (211, 511), (261, 511), (311, 511), (361, 511), (411, 511), (461, 511), (511, 511),
         (511, 461), (461, 461), (411, 461), (361, 461), (311, 461), (261, 461), (211, 461), (161, 461), (111, 461), (61, 461),
         (61, 411), (111, 411), (161, 411), (211, 411), (261, 411), (311, 411), (361, 411), (411, 411), (461, 411), (511, 411),
         (511, 361), (461, 361), (411, 361), (361, 361), (311, 361), (261, 361), (211, 361), (161, 361), (111, 361), (61, 361),
         (61, 311), (111, 311), (161, 311), (211, 311), (261, 311), (311, 311), (361, 311), (411, 311), (461, 311), (511, 311),
         (511, 261), (461, 261), (411, 261), (361, 261), (311, 261), (261, 261), (211, 261), (161, 261), (111, 261), (61, 261),
         (61, 211), (111, 211), (161, 211), (211, 211), (261, 211), (311, 211), (361, 211), (411, 211), (461, 211), (511, 211),
         (511, 161), (461, 161), (411, 161), (361, 161), (311, 161), (261, 161), (211, 161), (161, 161), (111, 161), (61, 161),
         (61, 111), (111, 111), (161, 111), (211, 111), (261, 111), (311, 111), (361, 111), (411, 111), (461, 111), (511, 111),
         (511, 61), (461, 61), (411, 61), (361, 61), (311, 61), (261, 61), (211, 61), (161, 61), (111, 61), (61, 61)])
         
ladders={2: 23, 8: 14, 26: 35, 38: 44, 41: 60, 56: 77, 31: 86, 69: 90, 88: 92, 79: 81}
snakes={99: 78, 96: 47, 94: 73, 63: 59, 64: 37, 70: 49, 42: 22, 33: 27, 29: 10, 25: 4}


r=pygame.image.load("sprites/r.png")
g=pygame.image.load("sprites/g.png")
b=pygame.image.load("sprites/b.png")
y=pygame.image.load("sprites/y.png")
pieces={"r":r,"y":y,"b":b,"g":g}

location={}
lpoints=[]
spoints=[]


def printdie(num,x,y):
    rect=pygame.Rect(x,y,60,60)
    pygame.draw.rect(win,(255,255,255),rect)
    if num==1:
        pygame.draw.circle(win,(0,0,255),(x+30,y+30),4)
    elif num==2:
        pygame.draw.circle(win,(0,0,255),(x+10,y+30),4)
        pygame.draw.circle(win,(0,0,255),(x+50,y+30),4)
    elif num==3:
        pygame.draw.circle(win,(0,0,255),(x+10,y+30),4)
        pygame.draw.circle(win,(0,0,255),(x+50,y+30),4)
        pygame.draw.circle(win,(0,0,255),(x+30,y+30),4)
    elif num==4:
        pygame.draw.circle(win,(0,0,255),(x+10,y+10),4)
        pygame.draw.circle(win,(0,0,255),(x+50,y+10),4)
        pygame.draw.circle(win,(0,0,255),(x+50,y+50),4)
        pygame.draw.circle(win,(0,0,255),(x+10,y+50),4)
    elif num==5:
        pygame.draw.circle(win,(0,0,255),(x+10,y+10),4)
        pygame.draw.circle(win,(0,0,255),(x+50,y+10),4)
        pygame.draw.circle(win,(0,0,255),(x+50,y+50),4)
        pygame.draw.circle(win,(0,0,255),(x+10,y+50),4)
        pygame.draw.circle(win,(0,0,255),(x+30,y+30),4)
    elif num==6:
        pygame.draw.circle(win,(0,0,255),(x+10,y+10),4)
        pygame.draw.circle(win,(0,0,255),(x+50,y+10),4)
        pygame.draw.circle(win,(0,0,255),(x+50,y+50),4)
        pygame.draw.circle(win,(0,0,255),(x+10,y+50),4)
        pygame.draw.circle(win,(0,0,255),(x+50,y+30),4)
        pygame.draw.circle(win,(0,0,255),(x+10,y+30),4)
    pygame.display.update()
    
def newloc(piece,num):
    newloc=[]
    if not location[piece]+num>100:
        for i in range(num):
            newloc.append(location[piece]+i+1)
    if not newloc==[]:   
        if newloc[-1] in ladders:
            newloc.append(ladders[newloc[-1]])

        elif newloc[-1] in snakes:
            newloc.append(snakes[newloc[-1]])
        
    return newloc

def iswon(turn,piece):
    labels={"r":"Red","b":"Blue","g":"Green","y":"Yellow"}
    if location[piece]==100:
        font1=pygame.font.SysFont('comicsans',20)
        won.append(piece)
        num=len(won)
        msg1=font1.render(("#"+str(num)+" "+labels[piece]),1,(255,255,255))
        win.blit(msg1,(600,(50*num)))
        win.blit(pieces[piece],(700,(50*num)))
    
    

def piecestacker():
    at={}
    piece=list(pieces.keys())
    for i in range(len(piece)):
        pos=tuple(gridloc[int(location[piece[i]])-1])
        if pos not in at:
            at[pos]=0
            win.blit(pieces[piece[i]],pos)
        else:
            at[pos]+=1
            win.blit(pieces[piece[i]],(pos[0]-(at[pos]*2.5),pos[1]))

def mover(piece,arr):

    if len(arr)!=0:
        for j in range(len(arr)):
            win.blit(pieces[piece],tuple(gridloc[(arr[j]-1)]))
            pygame.time.delay(100)
            location[piece]=arr[j]
            board()
            pygame.time.delay(10)


def laddermaker():

    brown=(69,39,38)
    for i in (ladders.keys()):
        loc2=ladders[i]
        n=(loc2-i)
        if n <10:
            n=2
        else:
            n=(n//10)*2
        n+=2
        e1=gridloc[i-1]
        e2=gridloc[loc2-1]

        pygame.draw.line(win,brown,(e1[0],e1[1]),(e2[0],e2[1]),2) 
        pygame.draw.line(win,brown,(e1[0]+10,e1[1]),(e2[0]+10,e2[1]),2)

        if lc==0:
            for j in range(1,n):
                k=j/n

                lpoints.append((e1[0]+k*(e2[0]-e1[0]),e1[1]+k*(e2[1]-e1[1])))
        

    for j in lpoints:
        pygame.draw.line(win,brown,(j[0],j[1]),(j[0]+10,j[1]),2)

def snakemaker():
  h=25
  v=20

  for i in (snakes.keys()):

    loc2=snakes[i]
    n=(i-loc2)//2
    if n%2==0:
        n-=1
    else:
      n+=1
    n+=1

    green=(11,135,4)
    e1=gridloc[i-1]
    e2=gridloc[loc2-1]
    
    pygame.draw.rect(win,green,pygame.Rect(e1[0]-h+11,e1[1]-v+5,h,v),0,4)
    pygame.draw.ellipse(win,green,pygame.Rect(e1[0]-h+7,e1[1]-v+5,h,v))
    pygame.draw.ellipse(win,green,pygame.Rect(e1[0]-h+15,e1[1]-v+5,h,v))
    pygame.draw.line(win,(255,255,0),(e1[0]-h+6,e1[1]-v+17),(e1[0]-h+20,e1[1]-v+17),2)
    pygame.draw.circle(win,(255,255,255),(e1[0]-h+20,e1[1]-v+12),4)
    pygame.draw.circle(win,(0,0,0),(e1[0]-h+20,e1[1]-v+12),2)

    spoints=[]
    spoints.append((e1[0],e1[1]))
    for j in range(1,n):
        k=j/n
        spoints.append((int(e1[0]+k*(e2[0]-e1[0])),int(e1[1]+k*(e2[1]-e1[1]))))
    spoints.append((e2[0],e2[1]))
    
    c=0
    pygame.draw.line(win,green,(spoints[0][0],spoints[0][1]),(spoints[0+1][0]+5,spoints[0+1][1]),15)
    i=0

    while i<len(spoints)-2:

      if c==0:
        pygame.draw.line(win,green,(spoints[i][0],spoints[i][1]),(spoints[i+1][0]+5,spoints[i+1][1]),15)
        pygame.draw.line(win,green,(spoints[i+1][0]+5,spoints[i+1][1]),(spoints[i+2][0],spoints[i+2][1]),15)
        c=1

      else:
        pygame.draw.line(win,green,(spoints[i][0],spoints[i][1]),(spoints[i+1][0]-5,spoints[i+1][1]),15)
        pygame.draw.line(win,green,(spoints[i+1][0]-5,spoints[i+1][1]),(spoints[i+2][0],spoints[i+2][1]),15)
        c=0

      i+=2

def buttonpress(buttons,mouse):

    p=False
    for i in range(len(buttons)):
        if mouse[0]>(buttons[i][0]) and mouse[0]<(buttons[i][0]+x) and mouse[1]>(buttons[i][1]) and mouse[1]<(buttons[i][1]+y):
            p=True
            break
    if p:
        return i+1

def board():

    pygame.draw.rect(win,(255,255,255),pygame.Rect(36,36,500,500))
    pygame.draw.rect(win,(255,255,255),pygame.Rect(37,37,498,498))
    font1=pygame.font.SysFont('comicsans',13)
    colour=[(255,125,0),(255,0,125),(125,255,0),(0,125,255),(255,255,255),(125,125,0)]
    x=36
    y=36
    k=0

    for i in range(10):
        pygame.draw.rect(win,colour[k],pygame.Rect(x,y,50,50))
        k+=1
        for j in range(9):
            if not k>=len(colour)-1:
                k+=1
            else:
                k=0
            if i%2==0:
                x+=50
            elif i%2!=0:
                x-=50
            pygame.draw.rect(win,colour[k],pygame.Rect(x,y,50,50)) 
        
        y+=50

    for i in range(1,10):
        blocksize=50
        pygame.draw.line(win,(0,0,0),(36,36+(blocksize*i)),(536,36+(blocksize*i)))
        pygame.draw.line(win,(0,0,0),(36+(blocksize*i),36),(36+(blocksize*i),536))
        
    x=1
    h=37
    v=486
    for i in range(1,11):
        text=font1.render(str(x),1,(0,0,0))
        win.blit(text,(h,v))
        for j in range(1,10):
            x+=1
            text=font1.render(str(x),1,(0,0,0))
            if i%2==0:
                h-=50
            else:
                h+=50
            win.blit(text,(h,v))
        v-=50
        x+=1
    laddermaker()
    snakemaker()
    piecestacker()
            
    pygame.display.update()

pygame.init()
pygame.font.init()
win =pygame.display.set_mode((800,600))
pygame.display.set_caption("Snakes and ladder")

running=True

lc=0 #all static point calculation is done at the first loop and then stored for later 

while running:
    won=[]
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            pygame.quit()
            running=False
            break

    #Entry Screen
    red=255
    blue=0
    run=True
    while run:
        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                pygame.quit()
                running=False
                break
            mouse=pygame.mouse.get_pos()

            if mouse[1]>250 and mouse[1]<350 and mouse[0]>305 and mouse[0]<495:
                red=0
                blue=255
            else:
                red=255
                blue=0
            if event.type==pygame.MOUSEBUTTONDOWN and mouse[1]>250 and mouse[1]<350 and mouse[0]>305 and mouse[0]<495:
                win.fill((0,0,0))
                run=False
                
        font1=pygame.font.SysFont('comicsans',40)
        msg=font1.render('Snakes and ladder',1,(255,255,255))
        msg2=font1.render('Snakes and ladder',1,(0,255,0))
        win.blit(msg,(400- (msg.get_width()//2),200))
        win.blit(msg2,(398- (msg.get_width()//2),198))
        font1=pygame.font.SysFont('comicsans',20)
        msg1=font1.render('Press to start',1,(red,255,blue))
        win.blit(msg1,(400-(msg1.get_width()//2),300))
        pygame.display.update()

    #Player Selection
    win.fill((0,0,0))
    pygame.display.update()
    run=True
    x=60
    y=30
    buttons=[(370,200),(370,300),(370,400)]
    font1=pygame.font.SysFont('comicsans',15)

    while run:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        mouse=pygame.mouse.get_pos()

        for i in range(len(buttons)):
            msg=font1.render(str(i+2)+'P',1,(0,0,0))
            pygame.draw.rect(win,(0,255,0),pygame.Rect(buttons[i][0],buttons[i][1],x,y))
            win.blit(msg,(((buttons[i][0]+x//2)- (msg.get_width()//2)),(buttons[i][1]+5)))

        pygame.time.delay(50)

        if event.type==pygame.MOUSEBUTTONDOWN:
            press=buttonpress(buttons,mouse)
            if type(press)==int:
                win.fill((0,0,0))
                pieces=dict(itt.islice(pieces.items(), press+1))
                break

        pygame.display.update()

    for i in pieces:
        location[i]=1
        
    #GAME
    run=True
    printdie(1,690,520)
    board()
    turn=list(pieces.keys())
    pygame.display.update()
    t=0
    while run:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                running=False
                break
        keys=pygame.key.get_pressed()
        if len(won)==len(turn)-1:
            won.append([x for x in turn if x not in won][0])
            break
                 
        if turn[t] not in won :
            if keys[pygame.K_SPACE]:
                num=random.randint(1,6)
                for i in range(30):
                    printdie(random.randint(1,6),690,520)
                printdie(num,690,520)

                locarr=newloc(turn[t],num)
                mover(turn[t],locarr)
                iswon(turn,turn[t])
                if t!=6:
                    if t==(len(turn)-1):  
                        t=0
                    else:
                        t+=1
                
        pygame.time.delay(50)
        pygame.display.update()
        lc=1 #Now the code will use the stored static points instead of calculating everytime
    pygame.time.delay(1000)
    win.fill((0,0,0))
    #GameOver
    run=True
    x=60
    y=30
    buttons=[(275,400),(425,400)]
    labels={"r":"Red","b":"Blue","g":"Green","y":"Yellow"}
    font1=pygame.font.SysFont('comicsans',15)

    while run:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        font=pygame.font.SysFont('comicsans',30,True)
        msg=font.render("Game Over",1,(255,255,255))
        win.blit(msg,(300,40))
        

        for i in won:
            text=str(won.index(i)+1)+"# "+labels[i]
            msg=font1.render(text,1,(255,255,0))
            y1=100
            win.blit(msg,(350,y1+50*(won.index(i))))
            win.blit(pieces[i],(425,y1+50*(won.index(i))))
        mouse=pygame.mouse.get_pos()

        msg=font1.render("Play again",1,(0,0,0))
        pygame.draw.rect(win,(0,255,0),pygame.Rect(buttons[0][0],buttons[0][1],80,y))
        win.blit(msg,(((buttons[0][0]+x//2)- (msg.get_width()//2)+10),(buttons[0][1]+5)))

        msg=font1.render("Quit",1,(0,0,0))
        pygame.draw.rect(win,(255,0,0),pygame.Rect(buttons[1][0],buttons[1][1],x,y))
        win.blit(msg,(((buttons[1][0]+x//2)- (msg.get_width()//2)),(buttons[1][1]+5)))
        
        if event.type==pygame.MOUSEBUTTONDOWN:

            press=buttonpress(buttons,mouse)
            if type(press)==int:
                if press==0:
                    continue
                else:
                    running=False
                    break

        pygame.display.update()
        pygame.time.delay(10)
        win.fill((0,0,0))
 
pygame.quit()
