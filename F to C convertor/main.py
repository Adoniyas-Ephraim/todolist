import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
from datetime import datetime, time

print("""\n-_-_-_-_- F to C -_-_-_-_-
By Adoniyas Ephraim
github: https://github.com/Adoniyas-Ephraim \n""")

# root window
root = tk.Tk()
root.title('F to C converter')
root.iconbitmap("icon.ico")
window_width = 355
window_height = 90

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry('{0}x{1}+{2}+{3}'.format(window_width, window_height, center_x, center_y))
root.resizable(False, False)


def fahrenheit_to_celsius(f):
    """ Convert fahrenheit to celsius
    """
    answer = (f - 32) / 1.8
    answer = round(answer, 1)
    return answer


# frame
frame = ttk.Frame(root)


# field options
options = {'padx': 5, 'pady': 5}

# temperature label
temperature_label = ttk.Label(frame, text='Fahrenheit')
temperature_label.grid(column=0, row=0, sticky='W', **options)

# temperature entry
temperature = tk.StringVar()
temperature_entry = ttk.Entry(frame, textvariable=temperature)
temperature_entry.grid(column=1, row=0, **options)
temperature_entry.focus()

# convert button


def convert_button_clicked():
    """  Handle convert button click event 
    """
    try:
        global f
        f = float(temperature.get())
        global c
        c = fahrenheit_to_celsius(f)
        result = '{0} Fahrenheit = {1} Celsius'.format(f, c)
        result_label.config(text=result)
        result_label.grid(column=0, row=1, sticky='W', **options)
    except ValueError as error:
        showerror(title='Error', message='Please put a value first')


convert_button = ttk.Button(frame, text='Convert')
convert_button.grid(column=2, row=0, sticky='W', **options)
convert_button.configure(command=convert_button_clicked)

# Save button

def save_button_clicked():
    """  Handle saving button click event 
    """
    try:
        date = datetime.now()
        year = date.year
        hour = date.hour
        if hour > 12:
            change = hour - 12
            hour = hour - change
        minute = date.minute
        today = '{0} - {1}:{2} ---'.format(year, hour, minute)
        save = open('results.txt','a')
        save.write('\n{0} {1}F to {2}C\n'.format(today, f, c))
    except ValueError as error:
        showerror(title='Error', message=error)
    except NameError as error:
        showerror(title='Error', message='please put a value first')


convert_button = ttk.Button(frame, text='save')
convert_button.grid(column=2, row=1, sticky='W', **options)
convert_button.configure(command=save_button_clicked)

# result label
result_label = ttk.Label(frame)
result_label.grid(row=1, columnspan=3, **options)

# add padding to the frame and show it
frame.grid(padx=10, pady=10)


# start the app
root.mainloop()
