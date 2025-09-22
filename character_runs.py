from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet_final_final.png')





#correction: "forth" animation works when y=400
def draw_character(frame,Clipped_height):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 120, Clipped_height, 120, 120, 400, 250,400,400)
    update_canvas()
    delay(0.05)


def next_frame(frame):
    return (frame + 1) % 10

frame=0
while True:
   draw_character(frame,0)
   frame=next_frame(frame)

close_canvas()
