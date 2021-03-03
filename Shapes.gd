extends Control

class_name Shapes
var color: Color
var grid: Array
var coords: Array
var cells: GridContainer

# rotate GridContainers
func rotate_left():
	# Access parent node (Node2D), rotate visually
	cells.get_parent().rotate(-PI/2)
	# Counterclockwise rotation
	rotate_grid(1, -1)

func rotate_right():
	# Access parent node (Node2D), rotate visually
	cells.get_parent().rotate(PI/2)
	# Clockwise rotation
	rotate_grid(-1, 1)
	

func rotate_grid(xval, yval):
	# create a copy of the original grid to store rotated values
	var rotated_grid = grid.duplicate(true)
	
	# loop through each cell in grid
	for x in coords:
		for y in coords:
			# store x1 value from initial grid
			var x1 = coords.find(x)
			# store y1 value from initial grid
			var y1 = coords.find(y)
			# modify and store rotated values
			var x2 = coords.find(yval * y)
			var y2 = coords.find(xval * x)
			# update the grid
			rotated_grid[y1][x1] = grid[y2][x2]
	grid = rotated_grid
	
