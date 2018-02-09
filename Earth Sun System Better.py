from pygame import *
from math import *

#S = '1-(0.01672*cos(0.9856*(x-4)))'

def main():
    init()
    size = [800, 800]
    screen = display.set_mode(size)
    clock = time.Clock()
    
    o = [0,0,0,0,0,0,0,0] # Relative Orbital Velocity
    
    while True:
        clock.tick(59)
        screen.fill((0, 0, 0))
        
        for x in range(0, 360):
            screen.fill((0, 0, 0))
            # Sun (Size Not to scale)
            draw.circle(screen, (245, 227, 101), [400, 400], 20)
            #Mercury (To Scale Size, Distance from Sun)
            draw.circle(screen, (255, 255, 255), [400+int(30*cos((x+o[0])/57.3)),  400+int(30*sin((x+o[0])/57.3))], 1)
            #Venus (To Scale Size, Distance from Sun)
            draw.circle(screen, (255, 255, 255), [400+int(40*cos((x+o[1])/57.3)),  400+int(40*sin((x+o[1])/57.3))], 8)
            #Earth (To Scale Size, Distance from Sun)
            draw.circle(screen, (0, 0, 255), [400+int(80*cos((x+o[2])/57.3)),  400+int(80*sin((x+o[2])/57.3))], 10)
            #Mars (To Scale Size, Distance from Sun)
            draw.circle(screen, (255, 0, 0), [400+int(120*cos((x+o[3])/57.3)),  400+int(120*sin((x+o[3])/57.3))], 1)
            #Jupiter (To Scale Size, Distance from Sun)
            draw.circle(screen, (239, 211, 98), [400+int(190*cos((x+o[4])/57.3)),  400+int(190*sin((x+o[4])/57.3))], 50)
            # Saturn (To Scale Size, Distance from Sun)
            draw.circle(screen, (205, 204, 141), [400+int(270*cos((x+o[5])/57.3)),  400+int(270*sin((x+o[5])/57.3))], 25)
            #Uranus (To Scale Size, Distance from Sun)
            draw.circle(screen, (107, 193, 239), [400+int(320*cos((x+o[6])/57.3)),  400+int(320*sin((x+o[6])/57.3))], 15)
            #Neptune (To Scale Size, Distance from Sun)
            draw.circle(screen, (120, 225, 215), [400+int(360*cos((x+o[7])/57.3)),  400+int(360*sin((x+o[7])/57.3))], 12)
            display.update()

            o[0] += 1.59
            o[1] += 1.18
            o[2] += 1
            o[3] += 0.808
            o[4] += 0.439
            o[5] += 0.325
            o[6] += 0.228
            o[7] += 0.182
                
            
        display.update()
        
        for E in event.get():
            if E.type == QUIT:
                quit()

    
    

main()
