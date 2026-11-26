import pgzrun
import random
WIDTH = 300
HEIGHT = 300

def draw():
    r = 255
    g = 0
    b = random.randint(120,255)
    #to draw circle
    radius = 100
    for i in range(20):#20 is the number of circles
      screen.draw.circle((WIDTH//2, HEIGHT//2),radius,(r,g,b))
      r -= 10
      g += 10
      radius -= 5








pgzrun.go()

