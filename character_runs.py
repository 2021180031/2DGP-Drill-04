from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('run_animation.png')

GRASS_LEVEL=90




def draw_character(frame):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, 400, GRASS_LEVEL)
    update_canvas()
    delay(0.05)


def next_frame(frame):
    return (frame + 1) % 8

frame=0
while True:
   draw_character(frame)
   frame=next_frame(frame)

close_canvas()
