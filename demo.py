from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
top = Tk()
image=Image.open("C:\\Users\\ysaty\\PycharmProjects\\RPS\\1.jpg")
image=image.resize((200,200),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
l1=Label(top,image=photo)
l1.pack()
l2=Label(top,text="Helo")
l2.place(x=20,y=100)
top.mainloop()