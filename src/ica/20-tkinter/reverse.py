import tkinter as tk

# ----- GUI class and methods -----
class ReverseGui:
    def __init__(self):
        self.mainWin = tk.Tk()
        self.mainWin.title("String Reverser")

        # Create widgets
        instruction_label = tk.Label(self.mainWin, text="Enter a phrase and press Return:")
        self.input_entry = tk.Entry(self.mainWin, width=30)
        # The output label needs to be an instance variable to be changed by the callback
        self.output_label = tk.Label(self.mainWin, text="Reversed phrase will appear here", fg="blue")
        quit_button = tk.Button(self.mainWin, text="Quit", command=self.mainWin.destroy)

        # Place widgets in the grid
        instruction_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5)
        self.input_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=5)
        self.output_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        quit_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Bind the <Return> event on the Entry widget to the callback method
        self.input_entry.bind('<Return>', self.entry_response)

    def entry_response(self, event):
        """
        Callback for the Entry widget. Reverses the input string and updates the output label.
        The 'event' parameter is required by tkinter for bind callbacks.
        """
        # Get the text from the entry widget
        original_text = self.input_entry.get()

        # Reverse the string using slicing
        reversed_text = original_text[::-1]

        # Update the output label's text
        self.output_label.config(text=reversed_text)

    def run(self):
        self.mainWin.mainloop()


# ----- Main program -----
if __name__ == "__main__":
    myGui = ReverseGui()
    myGui.run()