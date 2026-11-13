import tkinter as tk

'''
class Window():
    def __init__(self):
        self.__window = tk.Tk()
        self.__window.title('Something?')
        self.__window.config(bg='#7748F2')

    def start(self):
        self.__window.mainloop()

    def add_label(self, text, bg, fg):
        label = tk.Label(self.__window, text=text, bg=bg, fg=fg)
        label.pack()

w = Window()
w.start()
w.add_label('idk bro', 'black', 'white')
'''

# setting up window
window = tk.Tk()
window.geometry = (200,200)
window.title('Something?')
window.config(bg='#7748F2')

# variables
answer = tk.StringVar()

# functions
def submit():
    ans = answer.get()
    if ans == 'yes':
        print('stupid')
    elif ans == 'no':
        print('well done')
    answer.set('')

def quit_window():
    global window
    window.quit()

# widgets
label = tk.Label(window, text='this isnt a button', bg='black', fg='red')
label.pack()
ask = tk.Label(window, text='Did you try to press the text above?')
ask.pack()
entry = tk.Entry(window, textvariable=answer)
entry.pack()
enter = tk.Button(window, text='click here to submit answer', command=submit)
enter.pack()
end = tk.Button(window, text='click to exit', command=quit_window)
end.pack()

# shapes
canvas = tk.Canvas(window, width=100,height=100, bg='white')
canvas.pack()
canvas.create_line((0,0),(100,100),width=1,fill='black')
canvas.create_line((100,0),(0,100),width=1,fill='black')
canvas.create_rectangle((20,20), (80,80), outline='green',fill='hotpink')
canvas.create_oval((30,30),(70,70), fill='white')
canvas.create_arc((40,40),(60,60),style=tk.PIESLICE, outline='black')


# actually running window
window.mainloop()