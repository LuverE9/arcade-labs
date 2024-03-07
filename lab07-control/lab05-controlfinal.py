import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 4

class Banana: # cambio cambioso
    def __init__(self,position_x,position_y,change_x,change_y,color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.color = color

    def draw(self):
        #banana_list = ((10,0),(15,0),(20,5))
        #arcade.draw_polygon_filled(banana_list,arcade.color.BANANA_YELLOW)
        arcade.draw_arc_filled(self.position_x-5, self.position_y+5, 30, 75,
                               arcade.color.BANANA_YELLOW, 0, 360,30)
        arcade.draw_arc_filled(self.position_x+10, self.position_y-5, 30, 60,
                               arcade.color.BANANA_YELLOW, 0, 360, 45)
        arcade.draw_arc_filled(self.position_x + 22, self.position_y-15, 30, 70,
                               arcade.color.BANANA_YELLOW, 0, 360, 80)

    def update(self):
        self.position_y += self.change_y
        self.position_x += self.change_x

        if self.position_x < 10:
            self.position_x = 10
        if self.position_x > SCREEN_WIDTH - 10:
            self.position_x = SCREEN_WIDTH - 10
        if self.position_y < 5:
            self.position_y = 5
        if self.position_y > SCREEN_WIDTH - 5:
            self.position_y = SCREEN_HEIGHT - 5

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
    def __init__(self):
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT,"Lab 7 - User Control")
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.ALICE_BLUE)
        self.ball = Ball(50, 50, 0, 0, 15, arcade.color.BANANA_YELLOW)
        self.banana = Banana(50,50,0,0,arcade.color.BANANA_YELLOW)

    def on_draw(self):
        arcade.start_render()
        # le dibujo

        arcade.draw_rectangle_filled(420, 100, 45, 65, arcade.color.BLUSH)
        arcade.draw_rectangle_filled(400, 0, 800, 430, arcade.color.CATALINA_BLUE)

        ice_list0 = ((500, 200), (620, 180), (850, 190), (850, 450), (730, 410), (630, 300), (580, 280), (550, 300))
        ice_list1 = ((500, 190), (620, 170), (850, 180))

        arcade.draw_polygon_filled(ice_list0, arcade.color.BLIZZARD_BLUE)
        arcade.draw_polygon_outline(ice_list0, arcade.color.AZURE, 2)
        arcade.draw_line_strip(ice_list1, arcade.color.BABY_BLUE, 2)

        # le no dibujo

        #self.ball.draw()
        self.banana.draw()

    def update(self,delta_time):
        self.ball.update()
        self.banana.update()

    def on_key_press(self,key,modifiers):

        if key == arcade.key.LEFT:
            self.ball.change_x = -MOVEMENT_SPEED
            self.banana.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ball.change_x = MOVEMENT_SPEED
            self.banana.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.ball.change_y = MOVEMENT_SPEED
            self.banana.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ball.change_y = -MOVEMENT_SPEED
            self.banana.change_y = -MOVEMENT_SPEED

    def on_key_release(self,key,modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.change_x = 0
            self.banana.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.change_y = 0
            self.banana.change_y = 0

def main():
    window = MyGame()
    arcade.run()

main()