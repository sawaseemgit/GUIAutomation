import pyautogui as pg

# pg.moveTo(60,300,duration=0.2) # moves to the coord
pg.click(60, 300)  # Give coords here to move and click
pg.typewrite(f'\nhello world!!', interval=0.1)

pg.typewrite(['left', 'left', 'Z'], interval=0.2)# only single chars, no words for Z
# py.press('f1')  #press F1 key

