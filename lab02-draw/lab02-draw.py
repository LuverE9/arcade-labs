import arcade

arcade.open_window(800,600,'dibujinho')

arcade.set_background_color(arcade.color.ALICE_BLUE)

arcade.start_render()

# le dibujo

arcade.draw_rectangle_filled(420, 100, 45, 65, arcade.color.BLUSH)
arcade.draw_rectangle_filled(400, 0,800,430,arcade.color.CATALINA_BLUE)

point_list0 = ((350,200),(450,200))
point_list1 = ((450,200),(470,230),(350,230),(350,200))
point_list2 = ((450,200),(460,215),(350,215),(350,200))

#arcade.draw_polygon_filled(point_list1, arcade.color.WHITE)
#arcade.draw_polygon_filled(point_list2, arcade.color.BLACK)
#arcade.draw_polygon_outline(point_list1, arcade.color.BLACK, 2)
#arcade.draw_line_strip(point_list0,arcade.color.BABY_BLUE,3)

ice_list0 = ((500,200),(620,180),(850,190),(850,450),(730,410),(630,300),(580,280),(550,300))
ice_list1 = ((500,190),(620,170),(850,180))

arcade.draw_polygon_filled(ice_list0, arcade.color.BLIZZARD_BLUE)
arcade.draw_polygon_outline(ice_list0, arcade.color.AZURE,2)
arcade.draw_line_strip(ice_list1,arcade.color.BABY_BLUE,2)

# le no dibujo

arcade.finish_render()

arcade.run()