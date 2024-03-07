import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
MOVEMENT_SPEED = 3

class Ball:
    def __init__(self,position_x,position_y,change_x,change_y,radius,color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(self.position_x,self.position_y,
                                  self.radius,self.color)

    def update(self):
        self.position_y += self.change_y
        self.position_x += self.change_x

        if self.position_x < self.radius:
            self.position_x = self.radius
        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius
        if self.position_y < self.radius:
            self.position_y = self.radius
        if self.position_y > SCREEN_WIDTH - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius

class MyGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width, height, title) # Parent's class init function

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY) # Background color

        self.ball = Ball(50,50,0,0,15,arcade.color.AUBURN)

    def on_draw(self):
        arcade.start_render()
        self.ball.draw()

    def update(self,delta_time):
        self.ball.update()

    def on_key_press(self,key,modifiers):
        if key == arcade.key.LEFT:
            self.ball.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ball.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.ball.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ball.change_y = -MOVEMENT_SPEED

    def on_key_release(self,key,modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.change_y = 0

def main():
    window = MyGame(SCREEN_WIDTH,SCREEN_HEIGHT,"Drawing Example")
    arcade.run()

main()