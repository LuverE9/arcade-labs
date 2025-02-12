import random
import arcade
import math

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.6
SPRITE_SCALING_ENEMY = 0.2
COIN_COUNT = 50
ENEMY_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3

enemy_sound = arcade.load_sound("6DH.wav")
coin_sound = arcade.load_sound("smw_coin.wav")


class Coin(arcade.Sprite):
    def update(self):
        self.center_y -= 100

        if self.center_y < -20:
            self.center_y = random.randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 100)
            self.center_x = random.randrange(SCREEN_WIDTH)

        self.angle += 1

        # If we rotate past 360, reset it back a turn.
        if self.angle > 359:
            self.angle -= 360

class Enemy(arcade.Sprite):
    def update(self):
        self.center_x -= 15

        if self.center_x < -20:
            self.center_y = random.randrange(SCREEN_HEIGHT)
            self.center_x = random.randrange(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100)

class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT, "Sprite Example")

        self.player_list = None
        self.coin_list = None
        self.enemy_list = None

        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.APPLE_GREEN)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()

        self.score = 0

        self.player_sprite = arcade.Sprite(":resources:images/enemies/bee.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        for i in range(COIN_COUNT):
            coin = Coin(":resources:images/topdown_tanks/treeBrown_small.png",SPRITE_SCALING_COIN)

            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            self.coin_list.append(coin)

        for i in range(ENEMY_COUNT):
            enemy = Enemy("dino.jpg",SPRITE_SCALING_ENEMY)

            enemy.center_x = random.randrange(SCREEN_WIDTH)
            enemy.center_y = random.randrange(SCREEN_HEIGHT)

            self.enemy_list.append(enemy)

    def on_draw(self):
        arcade.start_render()

        self.coin_list.draw()
        self.player_list.draw()
        self.enemy_list.draw()

        output = "Score: " + str(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        self.coin_list.update()
        self.enemy_list.update()

        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        for coin in coins_hit_list:
            arcade.play_sound(coin_sound)
            coin.remove_from_sprite_lists()
            self.score += 1

        enemy_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.enemy_list)
        for enemy in enemy_hit_list:
            arcade.play_sound((enemy_sound))
            enemy.remove_from_sprite_lists()
            self.score -= 1


def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()