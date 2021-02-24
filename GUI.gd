extends PanelContainer

var grid
var next
const CELL_BG1 = Color(.1, .1, .1) # dark grey
const CELL_BG2 = Color(0) # black

func _ready():
	grid = find_node("Grid") # look through scene and find Grid node
	next = find_node("NextShape") # look through scene and find NextShape node
	add_cells(grid, 200)
	clear_cells(grid, CELL_BG1)
	
func add_cells(node, n): # generating cells
	var num_cells = node.get_child_count()
	while num_cells < n: # add cells until hit number specified
		node.add_child(node.get_child(0).duplicate())
		num_cells += 1
	
func clear_cells(node, color): # change color of all cells in specified node
	for cell in node.get_children():
		cell.modulate = color

