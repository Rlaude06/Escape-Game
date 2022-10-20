import tkinter as tk
import winsound
from PIL import Image, ImageTk


win = tk.Tk()

image = Image.open("radio.png")
image = image.resize((561*2,444*2), Image.ANTIALIAS)

img = ImageTk.PhotoImage(image)

img1 = tk.PhotoImage(file="radio.png")
width, height = img1.width(), img1.height()
print(width, height)
canvas = tk.Canvas(win,  width=width*2, height=height*2,bg="#add123", bd=0, highlightthickness=0, relief='ridge')

canvas.pack(padx=720, pady=200)
canvas.create_image(0, 0, image=img, anchor=tk.NW)
win.config(bg = '#add123')

    




win.wm_attributes('-transparentcolor', '#add123')
win.overrideredirect(True) 

quit_button = tk.Button(win, text = "X", command = win.quit, anchor = 'w', activebackground = "red")
canvas.create_window(450*2, 100*2, anchor='nw', window=quit_button) 


def playSound():
    code = float(entry_number.get())
    print(code)
    if code == 152.4:
        winsound.PlaySound('la404.wav', winsound.SND_FILENAME)
    else:
        winsound.PlaySound('interference.wav', winsound.SND_FILENAME)


    


var_d = tk.DoubleVar(value=107.7)
entry_number = tk.Spinbox(win, from_= .0, to = 200.0,width=5, increment=.1,
    textvariable=var_d, bg="#C9BCAC", bd=0, highlightthickness=0, relief='ridge')

mhz = tk.Label(text="MHz :", bg="#C9BCAC")
canvas.create_window(360*2, 210*2, anchor='nw', window=mhz) 

canvas.create_window(400*2,210*2, anchor="nw", window=entry_number)

play = tk.Button(win, text = "►", command = playSound, anchor = 'w', activebackground = "red", bd=0, highlightthickness=0, relief='ridge', bg="#B1A184", font=("bold", 15), fg="white")
canvas.create_window(385*2, 230*2, anchor='nw', window=play) 
win.mainloop()