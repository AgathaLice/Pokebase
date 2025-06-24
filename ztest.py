import tkinter as tk

root = tk.Tk()
root.wm_title("Title:D")

root.columnconfigure([0, 2], weight=1)
root.columnconfigure(1, weight=4)
root.rowconfigure([0, 1, 2], weight=1)

f = tk.Frame(root)
f.grid(row=0, column=0, columnspan=2)

a = tk.Label(f, text='ablulbe')
a.pack(side='top')
ab = tk.Entry(f)
ab.pack(side='right')
root.mainloop()