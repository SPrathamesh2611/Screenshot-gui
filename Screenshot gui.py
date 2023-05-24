# Screen shot GUI

import pyautogui
import time
import tkinter as tk

# Define a function to capture a screenshot
def screenshot():
    """
    This function captures a screenshot of the screen and saves it to a file.
    It uses PyAutoGUI library to take the screenshot and tkinter for GUI components.
    """
    # Wait for 5 seconds to allow switching to the desired screen
    time.sleep(5)
    
    # Generate a unique filename based on the current timestamp
    name = time.time()
    name = 'C:/Users/hp/Documents/github/{}.png'.format(name)
    
    # Capture the screenshot using PyAutoGUI
    img = pyautogui.screenshot()
    
    # Save the screenshot to the specified file path
    img.save(name)
    
    # Display the screenshot using the default image viewer
    img.show()

# Create a tkinter GUI window
root = tk.Tk()

# Create a frame within the window
frame = tk.Frame(root)
frame.pack()

# Create a button for capturing a screenshot
button = tk.Button(frame, text="Take Screenshot", command=screenshot)
button.pack(side=tk.LEFT)

# Create a button for quitting the application
close = tk.Button(frame, text="Quit", command=quit)
close.pack(side=tk.LEFT)

# Start the GUI event loop
root.mainloop()
