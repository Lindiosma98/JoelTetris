extends CenterContainer

# enumeration for game states
enum { STOPPED, STOP, PLAY, PLAYING }

# vars for button states
const DISABLED = true
const ENABLED = false

var gui
var state = STOPPED

func _ready():
	gui = $GUI
	gui.connect("button_pressed", self, "_button_pressed")
	gui.set_button_states(ENABLED)
	
func _button_pressed(button_name):
	# control state of the game based on button pressed
	match button_name:
		"Button_Play":
			gui.set_button_state(DISABLED)
			_start_game()
			
		"Button_About":
			gui.set_button_state("About", DISABLED)
			
func _start_game():
	print("Playing...")
	state = PLAYING
	
