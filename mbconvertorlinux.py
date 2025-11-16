import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
value1 = "kilobytes"
value2 = "megabytes"

IMAGE_PATH = "./images/equal.png"

IMAGE_HEIGHT = 50
IMAGE_WIDTH = 50



root = ctk.CTk()
img = tk.Image('photo', file="./images/icona.png")
root.geometry("600x150")
root.iconphoto(False, img)
root.title("Binary Converter v1.0")
dict = {}
valori = ["bytes","kilobyes","megabytes","gigabyte","terabytes","pentabytes"]
i = 0

#questo ciclo serve per assegnare ad ogni stringa il proprio valore rispetto ai bytes
for valore in valori:
    if i == 0:
        dict[valore] = 1
        i +=10
    else:

        dict[valore] = 2**i
        i += 10

def valuepick(choice):
    global value1
    value1 = str(choice)
def valuepick2(choice):
    global value2
    value2 = str(choice)

def convert():
    global value1, value2
    value1 = firstcombobox.get()
    value2=secondcombobox.get()
    dividendo = int(firstentryvar.get())
    elevamento = dict[value1] / dict[value2]

    risultato = elevamento*dividendo
    risultato = float(risultato)

    output_label.configure(text=f"{risultato} {value2}")


firstentryvar = ctk.StringVar()

firstentry = ctk.CTkEntry(root, width = 200, font=("Helvetica",16),textvariable = firstentryvar)
firstentry.grid(row=0,column = 0)

equal_image = ctk.CTkImage(light_image=Image.open(IMAGE_PATH), size=(IMAGE_WIDTH , IMAGE_HEIGHT))
equal_label = ctk.CTkLabel(root,image=equal_image,text="")
equal_label.grid(row=0,column=1)

firstcombobox = ctk.CTkComboBox(root, values = valori,command=valuepick)
firstcombobox.grid(row=1,column=0)

secondcombobox = ctk.CTkComboBox(root, values = valori,command=valuepick2)
secondcombobox.grid(row=1,column=2)

output_label = ctk.CTkLabel(root,width = 200, font=("helvetica",16),text="output")
output_label.grid(row=0,column=2)

output_button = ctk.CTkButton(root, width = 200, font=("Helvetica",16),command=convert,text="Convert")
output_button.grid(row=2,column=1)

root.mainloop()
