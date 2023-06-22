''' map= nested list 10*10, 0-9 , y-x
 0 = road, 1 = wall
 t=trap, p = potion, exit
'''
map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 'P', 0, 't', 1, 'e', 1],
    [0, 1, 0, 1, 1, 0, 1, 1, 0, 't'],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 'p', 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 't', 1, 1, 1, 1, 1, 1]
]


playerPos = [7, 2]
moves = 20
temp = True


def lose_moves(nr_of_moves):
    global moves

    moves = moves - nr_of_moves


def add_moves(nr_of_moves):
    global moves

    moves = moves + nr_of_moves


def endgame():
    global temp
    temp = False


def player_move_here(y, x):
    global map
    global playerPos

    if y > -1 and y < 10 and x > -1 and x < 10:  # check we are in map

        if type(map[y][x]) is int:  # check if_int

            if map[y][x] == 0:  # check if_road
                playerPos = [y, x]  # move player
                lose_moves(1)  # cost 1 move to walk

            else:  # a wall
                lose_moves(1)  # cost 1 move to walk
                print('Ouch! I can not walk through walls…')

        else:

            if map[y][x] == 't':  # a trap
                playerPos = [7, 2]  # return to start
                lose_moves(1)  # cost one move 2 walk to trap up
                print('oh no, a trap!')
            elif map[y][x] == 'p':  # powerbar
                playerPos = [y, x]  # move player
                lose_moves(1)  # cost one move 2 walk to power up
                add_moves(15)  # add effect of power bar
                map[y][x] = 0  # chocolate bar is consumed?
                print('A chocolate bar, I feel stronger')

            else:  # mission complete
                print('You survived! Well done adventurer!')
                endgame()

    else:  # map surounded with walls right? traps, wth?
        lose_moves(1)
        playerPos = [7, 2]  # return to start

        print('Oh no, a trap!')


print('You have been placed in a pitch-black labyrinth, \n'
      'without knowing if there is a way out or not. \n'
      'Maybe there are traps?\n'
      'The only option available is to walk in a '
      'random direction and hope for the best, \n'
      'hope that you do not walk into a wall,\n'
      'or even worse,\n'
      'that you walk in circles.\n'
      'But hurry up,\n'
      'you only have so many moves…\n')

print('To move around use:\n'
      'w = up\n'
      'a = left\n'
      's = down\n'
      'd = right')
while(temp):

    direction = input('Enter Direction: ')

    if direction == 'w':
        player_move_here((playerPos[0]-1), playerPos[1])

    elif direction == 's':
        player_move_here((playerPos[0]+1), playerPos[1])

    elif direction == 'd':
        player_move_here(playerPos[0], (playerPos[1]+1))

    elif direction == 'a':
        player_move_here(playerPos[0], (playerPos[1]-1))

    if moves <= 0:
        print('Game over! You did not reach the exit in time.')
        endgame()
