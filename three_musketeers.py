# The Three Musketeers Game
# by David Matuszek and Shuting Sun.

# In all methods,
#   A 'location' is a two-tuple of integers, each in the range 0 to 4.
#        The first integer is the row number, the second is the column number.
#   A 'direction' is one of the strings "up", "down", "left", or "right".
#   A 'board' is a list of 5 lists, each containing 5 strings: "M", "R", or "-".
#        "M" = Musketeer, "R" = Cardinal Richleau's man, "-" = empty.
#        Each list of 5 strings is a "row"
#   A 'player' is one of the strings "M" or "R" (or sometimes "-").
#
# For brevity, Cardinal Richleau's men are referred to as "enemy".
# 'pass' is a do-nothing Python statement. Replace it with actual code.

def create_board():
    global board
    """Creates the initial Three Musketeers board and makes it globally
       available (That is, it doesn't have to be passed around as a
       parameter.) 'M' represents a Musketeer, 'R' represents one of
       Cardinal Richleau's men, and '-' denotes an empty space."""
    m = 'M'
    r = 'R'
    board = [ [r, r, r, r, m],
              [r, r, r, r, r],
              [r, r, m, r, r],
              [r, r, r, r, r],
              [m, r, r, r, r] ]

def set_board(new_board):
    """Replaces the global board with new_board."""
    global board
    board = new_board

def get_board():
    """Just returns the board. Possibly useful for unit tests."""
    return board

def string_to_location(s):
    """Given a two-character string (such as 'A5'), returns the designated
       location as a 2-tuple (such as (0, 4))."""
    """ord(c): given a string of length one, return a interger of representing
       the Unicode code point of the character when the argument is a unicode object.
       For example, ord('A') returns the integer 65, ord('E') returns the integer 69
       ord('1') returns the integer 49, ord('5') returns the integer 53.
       The Unicodes of 'A' to 'E' are sequential, and so are the Unicodes of '1' to '5'.
       using ord('A') - 65 to convert 'A' to 0, and ord('1') - 49 to convert '1' to 0"""
    # assert s[0] >= 'A' and s[0] <= 'E'
    # assert s[1] >= '1' and s[1] <= '5'
    the_location = (ord(s[0]) - 65, ord(s[1]) - 49)
    return the_location

def location_to_string(location):
    """Returns the string representation of a location."""
    """chr(i): Return the string representing a character
       whose Unicode code point is the integer i.
       chr(65) returns 'A', chr(49) returns '1'."""
    # assert location[0] >= 0 and location[0] <= 4
    # assert location[1] >= 0 and location[1] <= 4
    the_string = chr(location[0] + 65) + chr(location[1] + 49)
    return the_string

def at(location):
    """Returns the contents of the board at the given location."""
    return board[location[0]][location[1]]

def all_locations():
    """Returns a list of all 25 locations on the board."""
    # pass # Replace with code
    the_list = []
    for i in range(0, 5):
        for j in range(0, 5):
            the_list.append((i,j))
    return the_list

def adjacent_location(location, direction):
    """Return the location next to the given one, in the given direction.
       Does not check if the location returned is legal on a 5x5 board."""
    (row, column) = location
    if direction == 'up':
        the_location = (row - 1, column)
    if direction == 'down':
        the_location = (row + 1, column)
    if direction == 'left':
        the_location = (row, column - 1)
    if direction == 'right':
        the_location = (row, column + 1)
    return the_location

def is_legal_move_by_musketeer(location, direction):
    """Tests if the Musketeer at the location can move in the direction."""
    # assert at(location) == 'M'
    # need to both make sure the location is legal and at(location) we got the desired token
    if is_within_board(location, direction) and at(adjacent_location(location, direction)) == 'R':
        return True
    else:
        return False

def is_legal_move_by_enemy(location, direction):
    """Tests if the enemy at the location can move in the direction."""
    # assert at(location) == 'R'
    # need to both make sure the location is legal and at(location) we got the desired token
    if is_within_board(location, direction) and at(adjacent_location(location, direction)) == '-':
        return True
    else:
        return False

def is_legal_move(location, direction):
    """Tests whether it is legal to move the piece at the location
       in the given direction."""
    """If there is no piece at that location to begin with, return False.
       Otherwise, determine what kind of piece you are working with,
       determine if it can move to its desired location by calling
       is_legal_move_by_musketeer or is_legal_move_by_enemy, accordingly."""
    if is_legal_location(location):
        if at(location) == '-':
            return False
        if at(location) == 'R':
            return is_legal_move_by_enemy(location, direction)
        if at(location) == 'M':
            return is_legal_move_by_musketeer(location, direction)
    else:
        return False

def has_some_legal_move_somewhere(who):
    """Tests whether a legal move exists for player "who" (which must
       be either 'M' or 'R'). Does not provide any information on where
       the legal move is."""
    """use can_move_piece_at(location) in the definition of has_some_legal_move_somewhere(who). """
    if who == 'M':
        for the_location in all_locations():
            if at(the_location) == 'M' and can_move_piece_at(the_location):
                return True
        return False
    if who == 'R':
        for the_location in all_locations():
            if at(the_location) == 'R' and can_move_piece_at(the_location):
                return True
        return False 

def possible_moves_from(location):
    """Returns a list of directions ('left', etc.) in which it is legal
       for the player at location to move. If there is no player at
       location, returns the empty list, []."""
    the_list = []
    if is_legal_location(location):
        if at(location) == '-':
            return the_list
        if at(location) == 'M':
            if is_legal_move_by_musketeer(location, 'up'):
                the_list.append('up')
            if is_legal_move_by_musketeer(location, 'down'):
                the_list.append('down')
            if is_legal_move_by_musketeer(location, 'left'):
                the_list.append('left')
            if is_legal_move_by_musketeer(location, 'right'):
                the_list.append('right')
            return the_list
        if at(location) == 'R':
            if is_legal_move_by_enemy(location, 'up'):
                the_list.append('up')
            if is_legal_move_by_enemy(location, 'down'):
                the_list.append('down')
            if is_legal_move_by_enemy(location, 'left'):
                the_list.append('left')
            if is_legal_move_by_enemy(location, 'right'):
                the_list.append('right')
            return the_list
    else:
        return the_list
     
def can_move_piece_at(location):
    """Tests whether the player at the location has at least one move available."""
    ''' The  following code in comment works, but unnecessary.=_='''
    '''if is_legal_location(location):
        if at(location) == '-':
            return False
        if at(location) == 'M':
            if (is_legal_move_by_musketeer(location, 'up')
                or is_legal_move_by_musketeer(location, 'down')
                or is_legal_move_by_musketeer(location, 'left')
                or is_legal_move_by_musketeer(location, 'right')):
                return True
            else:
                return False
        if at(location) == 'R':
            if (is_legal_move_by_enemy(location, 'up')
                or is_legal_move_by_enemy(location, 'down')
                or is_legal_move_by_enemy(location, 'left')
                or is_legal_move_by_enemy(location, 'right')):
                return True
            else:
                return False
    else:
        return False'''
    if possible_moves_from(location) != []:
        return True
    else:
        return False
    
        
def is_legal_location(location):
    """Tests if the location is legal on a 5x5 board."""
    if (0 <= location[0] <= 4) and (0 <= location[1] <= 4):
        return True
    else:
        return False

def is_within_board(location, direction):
    """Tests if the move stays within the boundaries of the board."""
    (row, column) = adjacent_location(location, direction)
    if (0 <= row <= 4) and (0 <= column <= 4):
           return True
    else:
        return False

def all_possible_moves_for(player):
    """Returns every possible move for the player ('M' or 'R') as a list
       (location, direction) tuples."""
    # Order is important for this function, I use: up, down, left, right
    the_list = []
    if player == 'M':
        for the_location in all_locations():
            if at(the_location) == 'M':
                if is_within_board(the_location, 'up') and at(adjacent_location(the_location, 'up')) == 'R':
                    the_list.append((the_location,'up'))
                if is_within_board(the_location, 'down') and at(adjacent_location(the_location, 'down')) == 'R':
                    the_list.append((the_location,'down'))
                if is_within_board(the_location, 'left') and at(adjacent_location(the_location, 'left')) == 'R':
                    the_list.append((the_location,'left'))
                if is_within_board(the_location, 'right') and at(adjacent_location(the_location, 'right')) == 'R':
                    the_list.append((the_location,'right'))
        return the_list

    if player == 'R':
        for the_location in all_locations():
            if at(the_location) == 'R':
                if is_within_board(the_location, 'up') and at(adjacent_location(the_location, 'up')) == '-':
                    the_list.append((the_location,'up'))
                if is_within_board(the_location, 'down') and at(adjacent_location(the_location, 'down')) == '-':
                    the_list.append((the_location,'down'))
                if is_within_board(the_location, 'left') and at(adjacent_location(the_location, 'left')) == '-':
                    the_list.append((the_location,'left'))
                if is_within_board(the_location, 'right') and at(adjacent_location(the_location, 'right')) == '-':
                    the_list.append((the_location,'right'))
        return the_list

def make_move(location, direction):
    """Moves the piece in location in the indicated direction."""
    if is_legal_move(location, direction):
        if at(location) == 'M':
            board[location[0]][location[1]] = '-'
            board[adjacent_location(location, direction)[0]][adjacent_location(location, direction)[1]] = 'M'
        if at(location) == 'R':
            board[location[0]][location[1]] = '-'
            board[adjacent_location(location, direction)[0]][adjacent_location(location, direction)[1]] = 'R'
        else:
            return
    else:
        return

def choose_computer_move(who):
    """The computer chooses a move for a Musketeer (who = 'M') or an
       enemy (who = 'R') and returns it as the tuple (location, direction),
       where a location is a (row, column) tuple as usual."""
    if (who == 'M'):
        if len(all_possible_moves_for('M')) > 4:
            return all_possible_moves_for('M')[4]
        else:
            return all_possible_moves_for('M')[0]
        # The three Musketeers should try to stay as far away from one another as possible.
     
    if (who == 'R'):
        # Cardinal Richelieu's men should try to all move in the same direction.
        if len(all_possible_moves_for('R')) > 5:
            return all_possible_moves_for('R')[5]
        else:
            return all_possible_moves_for('R')[0]
        
def is_enemy_win():
    """Returns True if all 3 Musketeers are in the same row or column."""
    for the_location in all_locations():
        if (at(the_location) == 'M'):
            (row, column) = the_location
            count = 0
            for look_row in range(0, 5):
                if board[look_row][column] == 'M':
                    count = count + 1
            if count == 3:
                return True
            else:
                count = 0
                for look_column in range(0, 5):
                    if board[row][look_column] == 'M':
                        count = count + 1
                if count == 3:
                    return True
                else:
                    return False

#---------- Communicating with the user ----------

def print_board():
    print("    1  2  3  4  5")
    print("  ---------------")
    ch = "A"
    for i in range(0, 5):
        print(ch, "|", end = " ") 
        for j in range(0, 5):
            print(board[i][j] + " ", end = " ")
        print()
        ch = chr(ord(ch) + 1)
    print()

def print_instructions():
    print()
    print("""To make a move, enter the location of the piece you want to move,
and the direction you want it to move. Locations are indicated as a
letter (A, B, C, D, or E) followed by an integer (1, 2, 3, 4, or 5).
Directions are indicated as left, right, up, or down (or simply L, R,
U, or D). For example, to move the Musketeer from the top right-hand
corner to the row below, enter 'A5 left' (without quotes).
For convenience in typing, you may use lowercase letters.""")
    print()

def choose_users_side():
    """Returns 'M' if user is playing Musketeers, 'R' otherwise."""
    user = ""
    while user != 'M' and user != 'R':
        answer = input("Would you like to play Musketeer (M) or enemy (R)? ")
        answer = answer.strip() # white spaces stripped from the beginning and the end.
        if answer != "":
            user = answer.upper()[0]
    return user

def get_users_move():
    """Gets a legal move from the user, and returns it as a
       (location, direction) tuple."""    
    directions = {'L':'left', 'R':'right', 'U':'up', 'D':'down'}
    move = input("Your move? ").upper().replace(' ', '')
    if (len(move) >= 3
            and move[0] in 'ABCDE'
            and move[1] in '12345'
            and move[2] in 'LRUD'):
        location = string_to_location(move[0:2])
        direction = directions[move[2]]
        if is_legal_move(location, direction):
            return (location, direction)
    print("Illegal move--'" + move + "'")
    return get_users_move()

def move_musketeer(users_side):
    """Gets the Musketeer's move (from either the user or the computer)
       and makes it."""
    if users_side == 'M':
        (location, direction) = get_users_move()
        if at(location) == 'M':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Musketeer", location, direction)
        else:
            print("You can't move there!")
            return move_musketeer(users_side)
    else: # Computer plays Musketeer
        (location, direction) = choose_computer_move('M')         
        make_move(location, direction)
        describe_move("Musketeer", location, direction)
        
def move_enemy(users_side):
    """Gets the enemy's move (from either the user or the computer)
       and makes it."""
    if users_side == 'R':
        (location, direction) = get_users_move()
        if at(location) == 'R':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Enemy", location, direction)
        else:
            print("You can't move there!")
            return move_enemy(users_side)
    else: # Computer plays enemy
        (location, direction) = choose_computer_move('R')         
        make_move(location, direction)
        describe_move("Enemy", location, direction)
        return board

def describe_move(who, location, direction):
    """Prints a sentence describing the given move."""
    new_location = adjacent_location(location, direction)
    print(who, 'moves', direction, 'from',\
          location_to_string(location), 'to',\
          location_to_string(new_location) + ".\n")

def start():
    """Plays the Three Musketeers Game."""
    users_side = choose_users_side()
    board = create_board()
    print_instructions()
    print_board()
    while True:
        if has_some_legal_move_somewhere('M'):
            board = move_musketeer(users_side)
            print_board()
            if is_enemy_win():
                print("Cardinal Richleau's men win!")
                break
        else:
            print("The Musketeers win!")
            break
        if has_some_legal_move_somewhere('R'):
            board = move_enemy(users_side)
            print_board()
        else:
            print("The Musketeers win!")
            break

if __name__ == "__main__":
    start()
