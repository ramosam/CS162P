'''
You should define the board in main and pass it to each of the functions that should access it. Note that when you are passing it, you will be passing it using its address and changes made to the board in a function change the board everywhere.
'''

import random

dungeon = []
max_size = 10
player = ' P '
deadly_trap = ' T '
treasure = ' X '
monster = ' M '
floor = ' . '
game_over = False

# Helper function to build a basic dungeon layout
def build_dungeon(dungeon_board):
	''' Creates a basic dungeon layout, populated with the string value " . ".  '''
	# Creates a number of 'rows' based on max_size
	for row in range(max_size):
		row_list = []
		# Creates a number of 'columns' based on max_size
		for column in range(max_size):
			row_list.append(floor) 
		dungeon_board.append(row_list)
	return dungeon_board


def display_dungeon(dungeon_board):
	''' Displays the dungeon in its current state.  Prints board, does not return anything. '''
	# Creates a printable view based on dungeon board
	print("The dungeon:\n")
	board = ''
	# Go through each row
	for row in dungeon_board:
		# Create row view
		row_list_view = ''
		# Iterate through columns
		for column in row:
			# Add column to row view
			row_list_view += column
		# At the end of the row, create a new line
		row_list_view += '\n'
		# Add completed row layout to the board
		board += row_list_view
	# Display completed board
	print(board)


def create_dungeon(dungeon_board, trap_count):
	'''	Creates a dungeon with specified trap count, four monsters, a single treasure and a single player. '''
	# Creates basic dungeon of max_size by max_size in nested lists
	dungeon_board = build_dungeon(dungeon_board)
	# Places number of traps specified
	for item in range(trap_count):
		trap_placed = False
		while (not trap_placed):
			# Generate a random row
			trap_row = random.randrange(max_size)
			# Generate a random column
			trap_col = random.randrange(max_size)
			# Check that the square is not already occupied by trap
			if dungeon_board[trap_row][trap_col] != deadly_trap:
				dungeon_board[trap_row][trap_col] = deadly_trap
				trap_placed = True
	# Places treasure
	treasure_placed = False
	while (not treasure_placed):
		# Create random treasure location
		treasure_row = random.randrange(max_size)
		treasure_col = random.randrange(max_size)
		# Check that square is not already occupied by trap
		if dungeon_board[treasure_row][treasure_col] != deadly_trap:
			dungeon_board[treasure_row][treasure_col] = treasure
			treasure_placed = True
	# Places player
	player_placed = False
	while (not player_placed):
		# Create random treasure location
		player_row = random.randrange(max_size)
		player_col = random.randrange(max_size)
		# Check that square is not already occupied by trap or treasure
		if dungeon_board[player_row][player_col] != deadly_trap and dungeon_board[player_row][player_col] != treasure:
			dungeon_board[player_row][player_col] = player
			player_placed = True
	# Places monsters
	for critter in range(4): # hard coded 4 monsters
		critter_placed = False
		while (not critter_placed):
			critter_row = random.randrange(max_size)
			critter_col = random.randrange(max_size)
			# Check that the square is not already occupied
			if dungeon_board[critter_row][critter_col] != deadly_trap and dungeon_board[critter_row][critter_col] != treasure and dungeon_board[critter_row][critter_col] != player:
				dungeon_board[critter_row][critter_col] = monster
				critter_placed = True
	return dungeon_board

def get_move_from_player():
	''' Get user directional input. '''
	valid_move = False
	while(not valid_move):
		player_move = input("Which direction would you like to move? Left (L), Right (R), Up (U) or Down (D): ")
		if player_move.upper() == "L":
			valid_move = True
			return "L"
		elif player_move.upper() == "R":
			valid_move = True
			return "R"
		elif player_move.upper() == "U":
			valid_move = True
			return "U"
		elif player_move.upper() == "D":
			valid_move = True
			return "D"
		else:
			print("That is not a valid move choice. Where do you think you're going?")


def get_move(dungeon_board):
	''' Move player based upon user input. '''
	# Get move from player
	player_move = get_move_from_player()
	# Find out where the player is currently located
	player_row = -1
	player_col = -1
	# Finding int value of row
	for row in range(len(dungeon_board)):
		if player in dungeon_board[row]:
			player_row = row
			# Finding column by index
			player_col = dungeon_board[row].index(player)

	# If, for some reason, neither the row or column can be found
	if player_row == -1:
		player_row = 0
		print('player_row could not be found.')
	if player_col == -1:
		player_col = 0
		print('player_col could not be found.')
	# Save original location to know which square to revert back to floor
	old_player_position = (player_row, player_col)

	if player_move == 'L':
	# Move left player_col -1
		player_col -= 1
	elif player_move == 'R':
	# Move right player_col + 1
		player_col +=1
	elif player_move == 'U':
	# Move up player_row - 1
		player_row -= 1
	elif player_move == 'D':
	# Move down player_row + 1
		player_row += 1
	# Save player destination
	new_player_position = (player_row, player_col)

	return old_player_position, new_player_position

def check_out_of_bounds(player_position):
	''' Checks if player has fallen outside the dungeon border. Immediate death if true.	'''
	player_row, player_col = player_position
	if player_row < 0 or player_row >= max_size:
		return True
	elif player_col < 0 or player_col >= max_size:
		return True 
	else:
		return False

def check_move(dungeon_board, player_position, trigger_item):
	''' Checks if player has triggered a trap or treasure. '''
	player_row, player_col = player_position
	if dungeon_board[player_row][player_col] == trigger_item:
		return True
	return False
		 
def update_dungeon(dungeon_board, orig_pos, dest_pos):
	''' Checks boundaries, traps, treasure before updating player location. '''
	orig_row, orig_col = orig_pos
	dest_row, dest_col = dest_pos

	if check_out_of_bounds(dest_pos):
		print("Game Over. You have banged your head against the wall one too many times.")
		dungeon_board[orig_row][orig_col] = player
		game_over = True
	elif check_move(dungeon_board, dest_pos, deadly_trap):
		print("Game Over. You stepped in poo.")
		dungeon_board[dest_row][dest_col] = player
		dungeon_board[orig_row][orig_col] = floor
		game_over = True
	elif check_move(dungeon_board, dest_pos, treasure):
		print("You win! You found the thing!")
		dungeon_board[dest_row][dest_col] = player
		dungeon_board[orig_row][orig_col] = floor
		game_over = True
	elif check_move(dungeon_board, dest_pos, monster):
		print("You were a delicious snack. The monster is happy.")
		dungeon_board[dest_row][dest_col] = monster
		dungeon_board[orig_row][orig_col] = floor
		game_over = True
	else:
		dungeon_board[dest_row][dest_col] = player
		dungeon_board[orig_row][orig_col] = floor
		game_over = False

	return game_over, dungeon_board



def play_game(dungeon_board, game_over = False):
	'''	Runs the game cycle as long as the player would like. '''
	trap_count = input('How many traps would you like to avoid? ')
	count = 1
	try: 
		count = int(trap_count)
		if count >= (max_size * max_size / 2):
			print("You're nuts. I'm taking away your privileges.")
			count = 10
		elif count < 0:
			print("You're trapping the dungeon?")
			count = 1
	
	except ValueError:
		print("I'll just decide for you.")
		
	create_dungeon(dungeon_board, count)
	display_dungeon(dungeon_board)
	while (not game_over):
		player_origin_pos, player_dest_pos = get_move(dungeon_board)
		make_monsters_move(dungeon_board)
		game_over, dungeon_board = update_dungeon(dungeon_board, player_origin_pos, player_dest_pos)
		display_dungeon(dungeon_board)
	replay = input('Would you like to try again? Y/y to continue, or any other character to quit. ')
	if replay.upper() == "Y":
		new_dungeon = []
		# game_over = False
		play_game(new_dungeon)
	else: 
		print("Ta ta for now.")


def make_monsters_move(dungeon_board):
	''' Gathers locations of monsters and attempts a random move. '''
	list_of_monster_pos = []  # Expecting tuples for monster at row, col
	for row in range(len(dungeon_board)):
		for col in range(len(dungeon_board[row])):
			if dungeon_board[row][col] == monster:
				# Save monster's position
				m_pos = (row, col)
				list_of_monster_pos.append(m_pos)				
	print(list_of_monster_pos)

	move_options = ['L', 'R', 'U', 'D']
	for i in range(len(list_of_monster_pos)):
		# Get original row and column and copy for replacing old position
		m_row, m_col = list_of_monster_pos[i]
		orig_m_row, orig_m_col = list_of_monster_pos[i]
		valid_move = False
		while (not valid_move):
			# Get random direction
			random_index = random.randrange(len(move_options))
			random_direction = move_options[random_index]
			# Attempt move within bounds and not occupied, else try random direction
			if random_direction == 'L' and m_col > 0 and dungeon_board[m_row][m_col - 1] == floor:
			# Move left player_col -1
				m_col -= 1
				valid_move = True
			elif random_direction == 'R' and  m_col < max_size - 2 and dungeon_board[m_row][m_col + 1] == floor:
			# Move right player_col + 1
				m_col +=1
				valid_move = True
			elif random_direction == 'U' and m_row > 0 and dungeon_board[m_row - 1][m_col] == floor:
			# Move up player_row - 1
				m_row -= 1
				valid_move = True
			elif random_direction == 'D' and m_row < max_size - 2 and dungeon_board[m_row + 1][m_col] == floor:
			# Move down player_row + 1
				m_row += 1
				valid_move = True
			else:
				valid = move = False
		# Save monster destination
		new_m_position = (m_row, m_col)

		# Update 'old' position back to floor
		dungeon_board[m_row][m_col] = monster
		dungeon_board[orig_m_row][orig_m_col] = floor

		
	

play_game(dungeon)
