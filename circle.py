import pgzrun
import random
WIDTH = 300
HEIGHT = 300

def draw():
    #r = random.randint(0,255)
    #g = random.randint(0,255)
    #b = random.randint(0,255)
    #to draw circle
    radius = 100
    for i in range(20):#20 is the number of circles
      r = random.randint(0,255)
      g = random.randint(0,255)
      b = random.randint(0,255)
      screen.draw.filled_circle((WIDTH//2, HEIGHT//2),radius,(r,g,b))
      r -= 10
      g += 10
      radius -= 5








pgzrun.go()

