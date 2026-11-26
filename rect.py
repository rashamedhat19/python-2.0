import pgzrun
import random
WIDTH = 300
HEIGHT = 300
TITLE='RECTANGLE PATTERN'
def draw():
    #r = random.randint(0,255)
    #g = random.randint(0,255)
    #b = random.randint(0,255)
    #to draw rect
    

    width = WIDTH-200
    height = HEIGHT-200
    for i in range(20):#20 is the number of circles
      r = random.randint(0,255)
      g = random.randint(0,255)
      b = random.randint(0,255)

      rect = Rect((0,0), (width, height))
      rect.center = 150,150
      screen.draw.rect(rect, (r,g,b))
      width -= 10
      height -= 10
      
      








pgzrun.go()

