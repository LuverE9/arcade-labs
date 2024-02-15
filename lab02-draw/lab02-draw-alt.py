import arcade

arcade.open_window(800,600,'dibujinho')

arcade.set_background_color(arcade.color.BOSTON_UNIVERSITY_RED)

arcade.start_render()

# le dibujo

arcade.draw_circle_outline(400,300,250,arcade.color.CHROME_YELLOW,5)
arcade.draw_circle_filled(400,300,250,arcade.color.SAE)

arcade.draw_circle_outline(400,300,244,arcade.color.PEACH_ORANGE,2)
arcade.draw_arc_filled(400,300,500,500,arcade.color.SAE,0,300,330)
arcade.draw_arc_filled(400,300,500,500,arcade.color.SAE,0,5,320)

arcade.draw_circle_outline(400,300,250,arcade.color.DEEP_SAFFRON,3)

star_list_a = ((350,320),(380,300),(370,265),(400,285),(430,265),(420,300),(450,320),(415,320),(400,350),(385,320))
star_list_b = ((300,340),(360,300),(330,230),(400,270),(460,230),(440,300),(500,340),(430,340),(400,400),(370,340))
arcade.draw_polygon_filled(star_list_b,arcade.color.KU_CRIMSON)

arcade.draw_ellipse_filled(230,280,130,90,(255,188,119),270)
arcade.draw_arc_filled(230,250,150,100,arcade.color.PEACH_ORANGE,0,205,95)

# le no dibujo

arcade.finish_render()

arcade.run()