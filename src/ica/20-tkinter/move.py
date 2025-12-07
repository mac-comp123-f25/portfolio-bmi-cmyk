import tkinter as tk

class MoveGui:
    def __init__(self):
        self.mainWin = tk.Tk()
        self.mainWin.title("Move the Text")

        # Create a Canvas widget
        self.canvas = tk.Canvas(self.mainWin, width=400, height=300, bg='lightgray')
        self.canvas.pack(padx=10, pady=10)

        # Create a Text object on the canvas
        # The ID returned by create_text is stored to move the object later
        self.text_id = self.canvas.create_text(200, 150, text="My Name", fill="darkblue", font=("Arial", 16))

        # Bind key presses on the main window to the callback method
        self.mainWin.bind('<KeyPress>', self.move_callback)

    def move_callback(self, event):
        """
        Callback for key press events. Moves the text object based on the key pressed.
        """
        key = event.keysym  # Get the string name of the key that was pressed

        # Check which key was pressed and move the text object accordingly
        if key == 'w' or key == 'Up':
            self.canvas.move(self.text_id, 0, -10)  # Move up
        elif key == 's' or key == 'Down':
            self.canvas.move(self.text_id, 0, 10)   # Move down
        elif key == 'a' or key == 'Left':
            self.canvas.move(self.text_id, -10, 0)  # Move left
        elif key == 'd' or key == 'Right':
            self.canvas.move(self.text_id, 10, 0)   # Move right

    def run(self):
        self.mainWin.mainloop()


# ----- Main program -----
if __name__ == "__main__":
    myGui = MoveGui()
    myGui.run()