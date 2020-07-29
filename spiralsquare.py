import pyautogui as pg

# print(pg.size()) # screen size
# print(pg.position()) # current position of mouse

# pg.moveTo(625, 589, duration=1)  # takes the duration time to move to specified coords
# pg.moveRel(50,200,duration=1.5)  # moves relative to current position, Y coords dec moving up
# pg.click(955,222) #if no coords=> click at current position
# Draw a square spiral
pg.moveTo(62, 229, duration=0.2)  # takes the duration time to move to specified coords
pg.click()
dis = 300
while dis > 0:
    print(dis, 0)
    pg.dragRel(dis, 0, duration=0.2)# move right
    dis -= 25
    pg.dragRel(0, dis, duration=0.2)
    dis -= 25
    pg.dragRel(-dis, 0, duration=0.2) # move left
    dis -= 25
    pg.dragRel(0, -dis, duration=0.2)
