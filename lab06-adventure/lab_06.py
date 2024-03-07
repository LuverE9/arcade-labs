class Room:
    """
    Room base
    """
    def __init__(self,description,north,east,south,west):
        """ Constructor """
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west

def main():
    """ er coso eteh """
    room_list = []
    current_room = 0
    done = False
    room = Room("Inicio. Hay un camino al norte y otro al sur. Además, hay una puerta en dirección oeste",2,None,4,1) # 0
    room_list.append(room)
    room = Room("Habitación de la lejía",None,None,None,0) # 1
    room_list.append(room)
    room = Room("Hall A",None,3,0,None) # 2
    room_list.append(room)
    room = Room("Congelador",None,None,None,2) # 3
    room_list.append(room)
    room = Room("Hall B",0,None,None,5) # 4
    room_list.append(room)
    room = Room("Ente misterioso",6,None,None,4) # 5
    room_list.append(room)
    room = Room("Pasillo0",None,7,5,None) # 6
    room_list.append(room)
    room = Room("Pasillo1",None,6,None,8) # 7
    room_list.append(room)
    room = Room("Guarda",10,None,9,7) # 8
    room_list.append(room)
    room = Room("Final A",8,None,None,None) # 9
    room_list.append(room)
    room = Room("Final B",None,None,8,None) # 10
    room_list.append(room)
    print("")
    while done != True:
        print()
        print(room_list[current_room].description)
        text = input("¿En qué dirección irás? ")

        if text.lower() == "n" or text.lower() == "norte" or text.lower() == "north":
            next_room = room_list[current_room].north
        elif text.lower() == "s" or text.lower() == "sur" or text.lower() == "south":
            next_room = room_list[current_room].south
        elif text.lower() == "e" or text.lower() == "este" or text.lower() == "east":
            next_room = room_list[current_room].east
        elif text.lower() == "o" or text.lower() == "oeste" or text.lower() == "w" or text.lower() == "west":
            next_room = room_list[current_room].west
        elif text.lower() == "kanye":
            print("Se abren las puertas del infierno y caes al fuego eterno. Gilipollas.")
            print("\nFin.")
            break
        else:
            print("No sabes a donde ir y un plátano te empuja contra el suelo. Te rompes la cabeza y te mueres por el traumatismo craneoncefálico.")
            print("\nFin.")
            break

        if next_room == None:
            print("Intentas dirigirte hacia una pared, te chocas y procedes a quedarte pensando momentáneamente por qué has hecho eso. Continuas pensando hacia dónde ir.")
        else:
            current_room = next_room

main()