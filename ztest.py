import tkinter as tk

window = tk.Tk()

# Configure window to expand
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

# Create a frame to hold the grid
frame = tk.Frame(window)
frame.grid(row=0, column=0, sticky='nsew')

# Configure frame to expand
frame.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)

# Create widgets within the grid
label = tk.Label(frame, text="This label will expand to fill the window")
label.grid(row=0, column=0, sticky='nsew')

# Run the Tkinter event loop
window.mainloop()