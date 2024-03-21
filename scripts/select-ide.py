from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from pynput import keyboard
import numpy as np
import hackMatrix.api as matrix

# Initialize the console
console = Console()
console.clear()

# Define the IDE options
# Define the IDE options
ide_options = ["Vim", "Emacs", "VSCode"]
startPos = np.array((1.5, 1.5, -3.9))
startOrientation = np.array((0,-5,0))
relative_app_positions = np.array([(0,0,0),
                                   (2.5, 1.5, -3.5)-startPos,
                                   (3.3, 1.5, -2.78)-startPos])
relative_app_orientations = np.array([(0, 0, 0), (0, -35, 0), (0, -50, 0)])
selected_index = 0

def move(pos, rotation):
    matrix.player_move(pos, rotation, 2)

def move_to(selected_index):
    global cur_pos
    global cur_orientation

    awayFromScreenPosOffset = np.array((0,-0.35,1.2))
    awayFromScreenOrientationOffset = np.array((2, 0, 0))

    move(
        relative_app_positions[selected_index] +
        startPos +
        awayFromScreenPosOffset,

        relative_app_orientations[selected_index] +
        startOrientation +
        awayFromScreenOrientationOffset
    )

# Function to display the IDE options with the arrow indicating the selected option
def display_options(selected_index):
    options_text = "\n".join([f"[{'bold purple'}]{'->' if i == selected_index else '  '}[/] {option}" for i, option in enumerate(ide_options)])
    header = Text("Select an IDE:", style="bold green")
    console.print(header)
    console.print(options_text)

# Function to handle arrow key presses and update the selected index
def on_press(key):
    global selected_index
    try:
        if key == keyboard.Key.down:
            selected_index = min(selected_index + 1, len(ide_options) - 1)
            console.clear()
            display_options(selected_index)
            move_to(selected_index)
        elif key == keyboard.Key.up:
            selected_index = max(selected_index - 1, 0)
            console.clear()
            display_options(selected_index)
            move_to(selected_index)
    except AttributeError:
        pass



# Start listening for keyboard events
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Hide the cursor
console.show_cursor(False)

# Display the IDE options initially
display_options(selected_index)
move_to(0)

with keyboard.Events() as events:
    # Wait for an Enter keypress
    for event in events:
        if isinstance(event, keyboard.Events.Press) and event.key == keyboard.Key.enter:
            break

## absorb the enter key before exit
console.input()

# Hide the cursor
console.show_cursor(True)
