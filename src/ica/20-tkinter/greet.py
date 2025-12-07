import tkinter as tk

class BasicGui:
    def __init__(self):
        # Create the main window
        self.mainWin = tk.Tk()
        self.mainWin.title("Greetings")

        # Create the widgets
        # The 'self.message_label' is an instance variable to be accessed by callbacks
        self.message_label = tk.Label(self.mainWin, text="Welcome", width=20, font=("Helvetica", 16))

        quit_button = tk.Button(self.mainWin, text="Quit", command=self.quit_callback)
        hello_button = tk.Button(self.mainWin, text="Hello", command=self.hello_callback)
        goodbye_button = tk.Button(self.mainWin, text="Goodbye", command=self.goodbye_callback)

        # Place the widgets in the grid
        quit_button.grid(row=0, column=0, padx=10, pady=5)
        hello_button.grid(row=1, column=0, padx=10, pady=5)
        goodbye_button.grid(row=2, column=0, padx=10, pady=5)
        self.message_label.grid(row=1, column=1, padx=10, pady=5)

    def run(self):
        """Starts the tkinter event loop."""
        self.mainWin.mainloop()

    def quit_callback(self):
        """Callback function for the Quit button."""
        self.mainWin.destroy()

    def hello_callback(self):
        """Callback function for the Hello button."""
        self.message_label['text'] = "Hello"

    def goodbye_callback(self):
        """Callback function for the Goodbye button."""
        self.message_label['text'] = "Goodbye"


# ----- Main program -----
if __name__ == "__main__":
    myGui = BasicGui()
    myGui.run()