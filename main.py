from tkinter import *
from pynput.keyboard import Key,Controller
root = Tk()
root.title('crappy login')
root.resizable(0, 0) #delete this if you want resizable window
keyboard = Controller()
def back():
	keyboard.press(Key.backspace)
	keyboard.release(Key.backspace)
name = Label(root,text= "User ID: ").grid(row=1,column=1)
password = Label(root,text= "password: ").grid(row=2,column=1)

name_in = Entry(root).grid(row=1,column=3,columnspan= 3)
pass_in = Entry(root,show="*").grid(row=2,column=3,columnspan=3)

seven = Button(root,text="7",command= lambda: keyboard.type('7')).grid(row=3,column=3)
eight = Button(root,text="8",command= lambda: keyboard.type('8')).grid(row=3,column=4)
nine  = Button(root,text="9",command= lambda: keyboard.type('9')).grid(row=3,column=5)
four  = Button(root,text="4",command= lambda: keyboard.type('4')).grid(row=4,column=3)
five  = Button(root,text="5",command= lambda: keyboard.type('5')).grid(row=4,column=4)
six   = Button(root,text="6",command= lambda: keyboard.type('6')).grid(row=4,column=5)
one   = Button(root,text="1",command= lambda: keyboard.type('1')).grid(row=5,column=3)
two   = Button(root,text="2",command= lambda: keyboard.type('2')).grid(row=5,column=4)
three = Button(root,text="3",command= lambda: keyboard.type('3')).grid(row=5,column=5)
ok = Button(root,text="ok").grid(row=6,column=3)
zero = Button(root,text="0",command= lambda: keyboard.type('0')).grid(row=6,column=4)
clr = Button(root,text="<-",command= back).grid(row=6,column=5)

root.mainloop()
