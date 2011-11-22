#!/usr/bin/python
#
# Problem 11
# Compute greatest product of four adjacent numbers in 20x20 grid

# Obtain grid
grid = []
f = open('data/data_11.txt')
for line in f:
	grid.append(map(int, line.strip().split()))
f.close()

# Compute max product
maximum_product = 0
for row in range(20):
	for col in range(20):
		# Initialize products calculations
		south, east, southwest, southeast = 1,1,1,1
		
		# Multiply vertical/horizontal
		south = reduce(lambda x, y: x * y, 
					map(lambda x: grid[x][col], 
						range(row, min(row + 4, 20)))
				)	
		east = reduce(lambda x, y: x * y,
					map(lambda x: grid[row][x], 
						range(col, min(col + 4, 20)))
				)

		# Multiply on diagonals
		count = 0
		while count < 4:
			# Update southeast diagonal product
			if row + count < 20 and col + count < 20:
				southeast *= grid[row + count][col + count]
			
			# Update southwest diagonal product
			if row + count < 20 and col - count >= 0:
				southwest *= grid[row + count][col - count] 
			
			# Update count
			count += 1		

		# Recompute maximum product
		maximum_product = max(maximum_product, \
			south, east, southwest, southeast)

print "Maximum product:",maximum_product
