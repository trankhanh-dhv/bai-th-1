import math
pos=[0,0]
while True:
    s=imput()
    if not s:
        break
    movement=s.split(" ")
    direction=movement[0]
    steps=int(movement[1]
              if direction=="UP":
                pos[0]+=steps
              if direction=="DOWN":
                pos[0]-=steps
              elif direction=="LEFT":
                pos[1]-=steps
              elif direction=="RIGHT"
                pos[1]+=steps
              else:
                pass
            print(int(round(math.sprt(pos[1]**2+pos[0]**2))))
                  
              
