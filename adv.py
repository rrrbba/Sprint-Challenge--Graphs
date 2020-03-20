from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

#for the path that's been traversed
traversal_path = []

#dict for all rooms visited
visited = {}

#path needed for keeping track of going back if get stuck
back_path = []

#we need to be able to go in the opposite direction if we run into a dead end and need to go back so we can keep exploring
opp_dir = {'n':'s', 's':'n', 'w': 'e', 'e':'w'}

#get current room id and the exits available
#prints {0: ['n', 's', 'w', 'e']}
visited[player.current_room.id] = player.current_room.get_exits()

print("Starting search!")

#1) Find shortest path to an unexplored room
#run while loop to check if visited is less than rooms available 
while len(visited) < len(room_graph) - 1:

    #check if the current room the player is in hasn't been added to visited
    if player.current_room.id not in visited:

        #add exits of the current room to rooms
        visited[player.current_room.id] = player.current_room.get_exits()

        #grab the last direction that was traveled 
        last_direction = back_path[-1]

        #remove the last available directions from previous roo, so that new ones can be added with each room visit
        visited[player.current_room.id].remove(last_direction)
        print(f"Available directions: {visited[player.current_room.id]}")
        print(f"Current room id: {player.current_room.id} \n")



    #2) Then find more available rooms 

    #check if no more available rooms to visit or no more directions to go in (could be because of hitting dead end)
    while len(visited[player.current_room.id]) < 1:
        print(f"Available directions: {visited[player.current_room.id]}")
        #if so, then go back by popping it from the path 
        print("\nGoing back!")
        back_dir = back_path.pop()

        print(f"Current room id: {player.current_room.id}")

        #append the back direction to traversal_path so it can travel in that direction (we're able to find room with an available direction to travel)
        traversal_path.append(back_dir)
        print(f"Traveling {traversal_path[-1]} to take you back a room")

        #now we need to give the player the ability to travel in that direction
        player.travel(back_dir)



    #while there are avail. directions, go in the first direction avail. in room
    find_exit = visited[player.current_room.id].pop(0)

    # print(f"Current room id: {player.current_room.id}")
    print(f"Current room: {player.current_room.id} Going in this direction to find an exit :{find_exit}")

    #add these directions to traversal path
    traversal_path.append(find_exit)

    #append the opposite direction to the path used for back tracking
    back_path.append(opp_dir[find_exit])
    print(f"Opposite direction of current direction: {opp_dir[find_exit]} \n")

    #move the player to find the exit
    player.travel(find_exit)


# print(world.print_rooms())
print("Congratulations, you're done!\n\n")



#Write algo that picks random unexplored direction from current_room
#travels and logs that direction
#loop
#should cause player to walk in dft(?)

#Can find the path to shortest unexplored room by using bfs for a room with ? for an exit
#If using bfs from homework make modifications
#Instead of searching for target vertex, search for an exit with a ? as the value
#If exit has been explored, 
    #can put it in bfs queue like normal
#Bfs will return the path as a list of room IDs
    #Will need to convert this to a list of n/s/e/w directions before you can add it to your traversal path
#If all paths explored, done

#DFT until a dead end is reached
#BFS to the nearest unexplored room






# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
