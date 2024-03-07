import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Ball:
    def __init__(self,position_x,position_y,change_x,change_y,radius,color):
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(self.position_x,self.position_y,
                                  self.radius,self.color)

class MyGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width, height, title) # Parent's class init function

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY) # Background color

        self.ball = Ball(50,50,3,3,15,arcade.color.AUBURN)

    def on_draw(self):
        arcade.start_render()

        self.ball.draw()

    def on_mouse_motion(self,x,y,dx,dy):
        self.ball.position_x = x
        self.ball.position_y = y


def main():
    window = MyGame(SCREEN_WIDTH,SCREEN_HEIGHT,"Drawing Example")
    arcade.run()

main()