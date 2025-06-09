from customtkinter import *
from PIL import ImageTk, Image
root = CTk()

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
geometry = str(width) + "x" + str(height)
root.geometry(geometry)
background = CTkImage(light_image=Image.open("BackgroundClaro.png"),
                      dark_image=Image.open("BackgroundClaro.png"),
                      size=(width, height))
bgLabel = CTkLabel(root,
                   image=background,)
bgLabel.place(x=0,
              y=0)



root.mainloop()