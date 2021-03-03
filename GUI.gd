extends CenterContainer

signal button_pressed(button)

var grid
var next

func _ready():
	grid = find_node("Grid") # look through scene and find Grid node
	next = find_node("NextShape") # look through scene and find NextShape node
	add_cells(grid, 200)
	clear_cells(grid)
	clear_cells(next)
	
func add_cells(node, n): # generating cells
	var num_cells = node.get_child_count()
	while num_cells < n: # add cells until hit number specified
		node.add_child(node.get_child(0).duplicate())
		num_cells += 1
	
func clear_cells(node): # change color of all cells in specified node
	for cell in node.get_children():
		cell.modulate = Color(0)
		


func _on_Button_About_button_down():
	$AboutDialog.popup_centered()
	emit_signal("button_pressed", "About")


func _on_Button_Play_button_down():
	emit_signal("button_pressed", "Play")
	


func _on_Button_Quit_button_down():
	emit_signal("button_pressed", "Quit")


func set_button_state(button, state):
	find_node(button).set_disabled(state)


func set_button_text(button, text):
	find_node(button).set_text(text)

func _on_AboutDialog_popup_hide():
	set_button_state("Button_About", false)
	
func set_button_states(playing):
	set_button_state("Button_Play", playing)
	set_button_state("Button_About", playing)
	set_button_state("Button_Quit", !playing)
	
	
	
