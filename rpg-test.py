rooms = {
          "Hall" : { "south" : "Kitchen",
                     "east"  : "Dining Room",
                     "item"  : "key"
                   },

          "Kitchen" : { "north" : "Hall",
                        "item"  : "monster"
                      },

          "Dining Room" : { "west"  : "Hall",
                            "south" : "Garden",
                            "item"  : "potion"
                          },

          "Garden" : { "north" : "Dining Room" }
        }


inventory = ["key"]


for room, room_dict in rooms.items():
    for key, value in room_dict.items():
        if key == "item":
            if value in inventory:
                rooms[room][key] = ""


print(rooms["Hall"]["item"])
print(rooms)