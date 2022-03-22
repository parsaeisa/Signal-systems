from tkinter import *
import os.path as path
chaneltext=""
window=Tk()
window.title('Digital Radio')

window.resizable(0,0)

image1 = PhotoImage(file="radio1.gif")
w = image1.width()
h = image1.height()
window.geometry("%dx%d+0+0" % (w, h))


panel1 = Label(window, image=image1)
panel1.pack(side='top', fill='both', expand='yes')

panel1.image = image1

# lbl.place(x=30, y=20)
display=Text(window, bg='black',fg='green', font=("DIGITAL-7", 23),height=3.4,width=12,state=DISABLED)

display.place(x=239, y=207)

fileFounded = False
filePath = ""

L1 = Label(window, text="User Name")
L1.pack( side = LEFT)
E1 = Entry(window, bd =5 )
E1.place(x=240, y=177)


def AvaButtonClicked(args):
    if(fileButton(args) != ""):
        chaneltext= "Ava"
        display.config(state=NORMAL, fg = "green")
        display.delete('1.0', END)
        display.insert(INSERT,"\n      " + chaneltext)
        display.config(state=DISABLED)
        return "ava"

def FarhangButtonClicked(args):
    if(fileButton(args) != ""):
        chaneltext="Farhang"
        display.config(state=NORMAL, fg = "green")
        display.delete('1.0', END)
        display.insert(INSERT,"\n    " +chaneltext)
        display.config(state=DISABLED)
    return "Farhang"

def EghtesadButtonClicked(args):
    if(fileButton(args) != ""):
        chaneltext="Eghtesad"
        display.config(state=NORMAL, fg = "green")
        display.delete('1.0', END)
        display.insert(INSERT,"\n   " +chaneltext)
        display.config(state=DISABLED)
        return "Eghtesad"

def GoftogooButtonClicked(args):    
    if(fileButton(args) != ""):
        chaneltext="Goftogoo"
        display.config(state=NORMAL, fg = "green")
        display.delete('1.0', END)
        display.insert(INSERT,"\n   " +chaneltext)
        display.config(state=DISABLED)
        return "Goftogoo"

def fileButton(args):
    fileFounded = False
    filePath = E1.get()
    if(filePath == "" ):
        #error
        display.fg = "red"
        display.config(state=NORMAL, fg = "red")
        display.delete('1.0', END)
        display.insert(INSERT,"\n   enter file " )
        display.config(state=DISABLED)
        return ""

    elif(filePath.endswith(".txt") == False):        
        display.config(state=NORMAL , fg = "red")
        display.delete('1.0', END)
        display.insert(INSERT,"\nwrong format" )
        display.config(state=DISABLED)
        return ""

    elif  (path.exists(filePath) == False ):
        display.fg = "red"
        display.config(state=NORMAL, fg = "red")
        display.delete('1.0', END)
        display.insert(INSERT,"\n no such file" )
        display.config(state=DISABLED)
        return ""

    else :
        fileFounded = True
        display.config(state=NORMAL, fg = "green")
        display.delete('1.0', END)
        display.insert(INSERT,"     select \n     channel" )
        display.config(state=DISABLED)
        return filePath

#ava
btn_Ava=Button(window, text="آوا", bg='#d9d9d9')
btn_Ava.place(x=160, y=185)
btn_Ava.bind('<Button-1>', AvaButtonClicked)


#Farhang
btn_farhang=Button(window, text="فرهنگ", bg='#d9d9d9')
btn_farhang.place(x=460, y=185)
btn_farhang.bind('<Button-1>', FarhangButtonClicked)

#eghtesad
btn_Eghtesad=Button(window, text="اقتصاد", bg='#d9d9d9')
btn_Eghtesad.place(x=510, y=185)
btn_Eghtesad.bind('<Button-1>', EghtesadButtonClicked)


#Goftogoo
btn_Goftogoo=Button(window, text="گفت و گو", bg='#d9d9d9')
btn_Goftogoo.place(x=90, y=185)
btn_Goftogoo.bind('<Button-1>', GoftogooButtonClicked)

#fileButton
btn_Goftogoo=Button(window, text="انتخاب", bg='#d9d9d9')
btn_Goftogoo.place(x=370, y=177)
btn_Goftogoo.bind('<Button-1>', fileButton)


window.mainloop()