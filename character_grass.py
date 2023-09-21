from pico2d import *
import math
open_canvas()

character = load_image('character.png')
grass = load_image('grass.png')

def render_frame(x,y):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    delay(0.1)

def run_circle():
    print('circle')
    cx, cy, r = 400, 300, 200
    for deg in range(0, 360,5):
        x = cx + math.cos(math.radians(deg)) * r
        y = cy + math.sin(math.radians(deg)) * r
        render_frame(x,y)

def run_rect():
    print('rect')

    # bottom line
    for x in range(50, 750 + 1, 5):
        render_frame(x,90) #x,y 위치에 화면을 그려주는 함수
while (True):
    run_circle()
    run_rect()
    break
    
close_canvas()
