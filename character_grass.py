from pico2d import *
import math
open_canvas()

character = load_image('character.png')
grass = load_image('grass.png')

clear_canvas_now()
grass.draw_now(400,30)
character.draw_now(400,90)
delay(1)

def run_circle():
    print('circle')
    r = 200
    for deg in range(0, 360,5):
        x = math.cos(math.radians(deg)) * r
        y = math.sin(math.radians(deg)) * r
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        delay(0.1)
    pass
def run_rect():
    print('rect')
    pass
while (True):
    run_circle()
    run_rect()
    break
    
close_canvas()
