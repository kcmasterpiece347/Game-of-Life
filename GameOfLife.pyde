import copy
import time

w = 15
environment = [[0]*50 for n in range(50)]
start_time = time.time()
c = 0
rgb_mode = False
speed = 0.08
    
def setup():
    size(751,751)
    frameRate(30)

def draw():
    x, y = 0, 0
    for row in environment:
        for cell in row:
            if cell > 0:
                fillCol(cell)
            else:
                fill(255)
            rect(x,y,w,w)
            x = x + w
        x = 0
        y = y + w

def fillCol(cell):
    global c
    if c==0:
        fill(180-20*cell)
    elif c==1:
        fill(180,180-20*cell,180-20*cell)
    elif c==2:
        fill(200-20*cell,180,200-20*cell)
    elif c==3:
        fill(180-20*cell,180-20*cell,180)
    elif c==4:
        fill(180,180,180-20*cell)

def mousePressed():
    environment[mouseY/w][mouseX/w]=(environment[mouseY/w][mouseX/w]+1)%2

def keyPressed():
    global environment, c, rgb_mode, start_time, speed
    isPlaying = False
    if key=='n':
        if( (time.time()-start_time)%2 > speed):
            environment = iterate_life(environment)
            start_time = time.time()
        if(rgb_mode == True):
            c = (c+1)%5
    if key=='r':
        environment = [[0]*50 for n in range(50)]
    if key=='R':
        randomize()
    if key=='c':
        c = (c+1)%5
    if key=='C':
        rgb_mode = not rgb_mode
    if key=='f':
        if speed>0:
            speed -= 0.01
            print(speed)
    if key=='s':
        if speed<0.2:
            speed += 0.01
            print(speed)
    
def iterate_life(environment):
    new_environment = copy.deepcopy(environment)
    for i in range(0,len(environment)):
        for j in range(0, len(environment[0])):
            check = count_neighbors(environment, i, j)
            if new_environment[i][j]>0 and (check > 3 or check < 2):
                new_environment[i][j] = 0
            elif check == 3 and environment[i][j]==0:
                new_environment[i][j] = 1
            if environment[i][j] > 0 and new_environment[i][j] > 0 and new_environment[i][j] < 6:
                new_environment[i][j] += 1
    return new_environment

def count_neighbors(environment, x, y):
    neighbor_count = 0
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if (i!=0 or j!=0) and environment[(x+i)%len(environment)][(y+j)%len(environment[0])] > 0:
                neighbor_count += 1
    return neighbor_count

def randomize():
    global environment
    for i in range(50):
        for j in range(50):
            environment[i][j] = int(random(0,2))
    
