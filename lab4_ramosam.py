'''
You should define the board in main and pass it to each of the functions that should access it. Note that when you are passing it, you will be passing it using its address and changes made to the board in a function change the board everywhere.
'''

import random

dungeon = []
max_size = 10
player = ' P '
deadly_trap = ' T '
treasure = ' X '
floor = ' . '

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
	# Creates a printable view based on dungeon matrix
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
	'''	Creates a dungeon with specified traps, a single treasure and a single player. '''
	# Creates basic dungeon of max_size by max_size in nested lists
	dungeon_board = build_dungeon(dungeon_board)
	# Places number of traps specified
	for trap in range(trap_count):
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
		if (dungeon_board[player_row][player_col] != deadly_trap) and (dungeon_board[player_row][player_col] != treasure):
			dungeon_board[player_row][player_col] = player
			player_placed = True
	return dungeon_board

def get_move():
	player_move = input("Which direction would you like to move? Left (L), Right (R), Up (U) or Down (D): ")
	switcher = {
		"L": "L",
		"l": "L",
		"R": "R",
		"r": "R",
		"U": "U",
		"u": "U",
		"D": "D",
		"d": "D",
	}
	return switcher.get(player_move, "That is not a valid direction. Where do you think you're going?")
	

create_dungeon(dungeon, 3)		
display_dungeon(dungeon)
print(get_move())
