from data_structures import Queue

def get_overflow_list(grid):
	if grid:
		overflow_list = []
		# go through all grid:
		for row in range(len(grid)):
			for col in range(len(grid[row])):
				# case of corner: max 2
				if (row == 0 or row == len(grid) - 1) and (col == 0 or col == len(grid[row]) - 1):
					items = 2 
				# case of edge: max 3
				elif row == 0 or row == row == len(grid) - 1 or col == 0 or col == len(grid[row]) - 1:
					items = 3
				# case of outside: max 4
				else:
					items = 4

				# push overflowing cell into the list
				if abs(grid[row][col]) >= items:
					overflow_list.append((row,col))

		if overflow_list:
			return overflow_list
		else:
			return None

def signs_not_same(grid):
	if grid:
		positive = False
		negative = False
		# check through all grid, if both positive and negative turn True, stop checking
		for row in range(len(grid)):
			for col in range(len(grid[row])):
				if grid[row][col] > 0:
					positive = True
				elif grid[row][col] < 0:
					negative = True
				if positive and negative:
					break
		if positive and negative:
			return True
		else:
			return False

def overflow(grid, a_queue):
	if grid is not None and a_queue is not None:
		# if signs not all same and cell overflowing, process overflow
		if signs_not_same(grid):
			overflow_list = get_overflow_list(grid)
			if overflow_list:
				# define a new grid to process overflow
				grid_with_correct_sign = [row[:] for row in grid]

				# modify overflow cells
				for row, col in overflow_list:
					grid[row][col] = 0

				# modify neighbors
				for row, col in overflow_list:
					# determin the sign by original grid
					if grid_with_correct_sign[row][col] > 0:
						sign = 1
					elif grid_with_correct_sign[row][col] < 0:
						sign = -1

					# determin all neighbors
					neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]

					# modify all neighbors
					for neighbor_row, neighbor_col in neighbors:
						# only modify neighbor in grid
						if 0 <= neighbor_row < len(grid) and 0 <= neighbor_col < len(grid[row]):
							grid[neighbor_row][neighbor_col] = (abs(grid[neighbor_row][neighbor_col]) + 1) * sign

				# create a deep copy of grid, record persedure to queue
				copy_grid = [row[:] for row in grid]
				a_queue.enqueue(copy_grid)

				return 1 + overflow(grid, a_queue)
	return 0