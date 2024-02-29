import arcade
import random

music = arcade.load_sound("C:/Users/luver/Desktop/cosos del antiguo SSD/Descargas/X19 - Trophy Mode.mp3")

# le dibujo

def draw_background():
    arcade.draw_lrtb_rectangle_filled(0,800,180,0,arcade.color.EERIE_BLACK)
    arcade.draw_circle_filled(70,50,250,arcade.color.EERIE_BLACK)
    arcade.draw_rectangle_filled(300,180,50,120,arcade.color.EERIE_BLACK)
    arcade.draw_rectangle_filled(370, 180, 80, 100, arcade.color.EERIE_BLACK)
    arcade.draw_rectangle_filled(400, 180, 40, 120, arcade.color.EERIE_BLACK)

    arcade.draw_circle_filled(400,120,40,arcade.color.RED)
    arcade.draw_rectangle_filled(400,80,80,70,arcade.color.RED)
    arcade.draw_rectangle_filled(390, 90, 100, 60, arcade.color.RED)
    arcade.draw_rectangle_filled(375,40,30,20,arcade.color.RED)
    arcade.draw_rectangle_filled(425, 40, 30, 20, arcade.color.RED)
    arcade.draw_rectangle_filled(420,110,60,40,arcade.color.LIGHT_BLUE)
def draw_star(x,y):
    arcade.draw_point(x,y,arcade.color.WHITE,10)
def on_draw(delta_time):
    arcade.start_render()
    for i in range(0,300):
        draw_star(random.randint(0,800), random.randint(100,600))
    on_draw.star_x += 1
    draw_background()


on_draw.star_x = random.randint(0,800)
on_draw.star_y = random.randint(400,600)

def main():
    arcade.open_window(800, 600, 'dibujinho')
    arcade.set_background_color(arcade.color.CATALINA_BLUE)
    arcade.schedule(on_draw,1/60)
    arcade.play_sound(music)
    arcade.run()

# le no dibujo
main()

