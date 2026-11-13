import tkinter as tk
from tkinter import ttk

'''
root = tk.Tk()
root.title("Widgets Demo")

widgets = [
    tk.Label,
    tk.Checkbutton,
    ttk.Combobox,
    tk.Entry,
    tk.Button,
    tk.Radiobutton,
    tk.Scale,
    tk.Spinbox,
]

for widget in widgets:
    try:
        widget = widget(root, text=widget.__name__)
    except tk.TclError:
        widget = widget(root)
    widget.pack(padx=5, pady=5, fill="x")

root.mainloop()
'''

w = tk.Tk()
w.title('Testing widgets')

# LABEL
label = tk.Label(w, text='label :D', anchor='w')
label.pack()

# CHECK BOX
def show_state():
    checked = "Yes: well done :D" if var.get() else "No: go do it :("
    checkbox.config(text=f"Did u do ur hw? - {checked}")

var = tk.IntVar()
checkbox = tk.Checkbutton(w, text="Did u do ur hw?", variable=var)
checkbox.select()
checkbox.config(command=show_state)
checkbox.pack()

# COMBO BOX
def selection_changed(event):
    label.config(text=f"{event.widget.get()} selected")

combobox = ttk.Combobox(w, values=["Purple", "Purple again", "Purple yet again", "Blue", 'Orange', 'Red'])
combobox.set("Fav colour?")
combobox.bind("<<ComboboxSelected>>", selection_changed)
combobox.pack(padx=5, pady=5, fill="x")

label = tk.Label(w, text="None selected")
label.pack(pady=5, fill="x")

# LIST BOX
def selection_changed(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        label.config(text=f"{event.widget.get(index)} selected")
        event.widget.get(index)

l = tk.Label(w, text='Fav animal?')
l.pack(pady=5)

listbox = tk.Listbox(w)
for item in ["dino", "birb", "mao", "quack", "woof", "piggy", "goose"]:
    listbox.insert(tk.END, item)
listbox.bind("<<ListboxSelect>>", selection_changed)
listbox.pack(padx=5, pady=5, fill="both", expand=True)

label = tk.Label(w, text="none selected")
label.pack(padx=5, pady=5, fill="x")

# SCALE
w2 = tk.Tk()
w2.title('Important Q')

def value_changed(event):
    l3.config(text=event.widget.get())

l2 = tk.Label(w2, text='How much do you like computer science?')
l2.pack()

scale = tk.Scale(w2, from_=0, to=10, orient="horizontal")
scale.bind("<Motion>", value_changed)
scale.pack(padx=5, pady=5, fill="x")

l3 = tk.Label(w2, text='0')
l3.pack()

w.mainloop()

'''
img = tk.Tk()
img.title('Image :3')
otter = tk.PhotoImage(file="otter2.png").subsample(2)
otter_label = tk.Label(img, image=otter)
otter_label.pack(expand=True)

img.mainloop()
'''