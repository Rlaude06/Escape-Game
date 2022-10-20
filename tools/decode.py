import tkinter
import tkinter.ttk as ttk

app = tkinter.Tk()
 
app.title("Escape Game")
app.geometry("500x500")
s=ttk.Style()
s.theme_use('clam')

 
def decode_cesar(code):
    shift = 3
 
    code = code.upper()
 
    plain_text = ""
 
    for c in code:
        c_unicode = ord(c)
        c_index = ord(c) - ord("A")
        new_index = (c_index - shift) % 26
        new_unicode = new_index + ord("A")
        new_character = chr(new_unicode)
        plain_text = plain_text + new_character
    return plain_text

print(decode_cesar("abc"))

 
def action():
    code = entry_input_code.get()
    if not(code.isnumeric()):
        label_error.config(text="Veuillez rentrer un nombre")
        return
 
 
    decode = int(code,2)
    select = listbox.curselection()
    decode = str(select[0]) + str(decode)
    entry_output_code.delete(0, tkinter.END)
    entry_output_code.insert(0,decode)
 
 
 
label_input_code = tkinter.Label(app, text="Entrée")
entry_input_code = tkinter.Entry(app)
 
label_output_code = tkinter.Label(app, text="Sortie")
entry_output_code = tkinter.Entry(app)
 
label_error = tkinter.Label(app, text="", fg="red")
 
button_enter=tkinter.Button(app, text="Entrer", command=action)
 
 
 
values=["Binaire","Héxa", "César"]
 
var = tkinter.Variable(value=values)
 
listbox = tkinter.Listbox(
    app,
    listvariable=var,
    height=6,
    selectmode=tkinter.SINGLE
)
 
 
 
 
 
 
 
 
 
 
 
entry_input_code.place(x=100,y=100)
label_input_code.place(x=0,y=100)
entry_output_code.place(x=150,y=150)
label_output_code.place(x=0,y=150)
label_error.place(x=0,y=300)
button_enter.place(x=0, y=200)

listbox.pack(expand=False)
entry_input_code.pack()
label_input_code.pack()
entry_output_code.pack()
label_output_code.pack()
label_error.pack()
button_enter.pack()



app.mainloop()