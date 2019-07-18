'''
You should define the board in main and pass it to each of the functions that should access it. Note that when you are passing it, you will be passing it using its address and changes made to the board in a function change the board everywhere.
'''

import random

dungeon = []
max_size = 5

# Helper function to build a basic dungeon layout
def build_dungeon(dungeon_board):
	''' Creates a basic dungeon layout, populated with the string value " . ".  '''
	# Creates a number of 'rows' based on max_size
	for row in range(max_size):
		row_list = []
		# Creates a number of 'columns' based on max_size
		for column in range(max_size):
			row_list.append(' . ') # intentional spaces for easier viewing
		dungeon_board.append(row_list)
	return dungeon_board


def display_dungeon(dungeon_board):
	''' Displays the dungeon in its current state.  Prints board, does not return anything. '''
	# Creates a printable view based on dungeon matrix
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
	# Creates basic dungeon of max_size by max_size in nested lists
	dungeon_board = build_dungeon(dungeon_board)
	for trap in range(trap_count):
		trap_row = random.randrange(max_size)
		trap_col = random.randrange(max_size)
		print(trap, trap_row)
		print(trap, trap_col)

	return dungeon_board

create_dungeon(dungeon, 3)		
display_dungeon(dungeon)

