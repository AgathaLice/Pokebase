import tkinter as tk

root = tk.Tk()
root.wm_title("Title:D")

root.geometry('{}x{}'.format(500, 300))

##photo = PhotoImage(file="spaz.gif")
label = tk.Label(root, text="Label 1")
label.grid(row=1, column=1)

root.grid_columnconfigure(4, weight=1)

w = tk.Label(root, text="This label", fg="red", font=("Helvetica", 16))
w.grid(row=5, column=20)

root.mainloop()