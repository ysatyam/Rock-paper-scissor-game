from tkinter import *
from tkinter import messagebox
import random
from PIL import ImageTk,Image
root=Tk()
root.title('Rock paper Scissor')

root.geometry('650x350')
image=Image.open("C:\\Users\\ysaty\\PycharmProjects\\RPS\\1.jpg")
image=image.resize((650,350),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
pic=Label(root,image=photo)
pic.pack()

root.resizable(width=FALSE,height=FALSE)
l=Label(root,text="Rock paper Scissor",font=("Algerian",18,"bold"))
l.place(x=200,y=15)
l1=Label(root,text="Score:",font=("Times New Roman",18,"bold"))
l1.place(x=20,y=150)
l2=Label(root,text="Your Selected:",font=("Times New Roman",16,"bold"))
l2.place(x=120,y=200)
l2=Label(root,text="Your Score:",font=("Times New Roman",16,"bold"))
l2.place(x=400,y=200)
l3=Label(root,text="Computer Selected:",font=("Times New Roman",16,"bold"))
l3.place(x=80,y=240)
l3=Label(root,text="Computer Selected:",font=("Times New Roman",16,"bold"))
l3.place(x=380,y=240)
selected_label=Label(root,text="----")
selected_label.place(x=270,y=200,width=50,height=30)
c_selected_label=Label(root,text="----")
c_selected_label.place(x=270,y=240,width=50,height=30)
y_score_label=Label(root,text="----")
y_score_label.place(x=530,y=200,width=50,height=30)
c_score_label=Label(root,text="----")
c_score_label.place(x=570,y=240,width=50,height=30)
updateslabel=Label(root,text="Lets start!",font=("Times new Roman",15),fg="red")
updateslabel.place(x=280,y=56)


y_score=0
c_score=0
y_select=""
c_select=""
i=1
def Computer():
    global i
    i+=1
    if i<11:
        global c_selected_label
        global c_select
        c_selected_label.destroy()
        c_select=random.randint(1,3)
        if c_select==1:
            c_selected_label=Label(root,text="Rock",font=("bold",15))
            c_selected_label.place(x=270,y=240,width=50,height=30)
            c_select='Rock'

        elif c_select==2:
            c_selected_label = Label(root, text="Paper", font=("bold", 15))
            c_selected_label.place(x=270, y=240, width=50, height=30)
            c_select = 'Paper'
        else :
            c_selected_label = Label(root, text="Scissor", font=("bold", 15))
            c_selected_label.place(x=270, y=240, width=50, height=30)
            c_select = 'Scissor'
        score()
    else:
        i=1
        result()





def rock():
    global selected_label
    global y_select
    selected_label.destroy()
    selected_label=Label(root,text="Rock",font=("bold",15))
    selected_label.place(x=270,y=200,width=50,height=30)
    y_select="Rock"
    Computer()

def paper():
    global selected_label
    global y_select
    selected_label.destroy()
    selected_label = Label(root, text="Paper", font=("bold", 15))
    selected_label.place(x=270, y=200, width=50, height=30)
    y_select = "Paper"
    Computer()
def scissor():
    global selected_label
    global y_select
    selected_label.destroy()
    selected_label = Label(root, text="Scissor", font=("bold", 15))
    selected_label.place(x=270, y=200, width=50, height=30)
    y_select = "Scissor"
    Computer()
def score():
    global y_score
    global c_score
    global y_select
    global c_select
    global y_score_label
    global c_score_label
    global updateslabel

    y_score_label.destroy()
    c_score_label.destroy()
    updateslabel.destroy()

    if y_select=="Rock":
        if c_select=="Rock":
            y_score_label=Label(root,text=str(y_score),font=("bold",15))
            y_score_label.place(x=530,y=200,width=50,height=30)
            c_score_label=Label(root,text=str(c_score),font=("bold",15))
            c_score_label.place(x=570, y=240, width=50, height=30)
            updateslabel=Label(root,text='Oops its a tie!!!!! ',font=("Times new Roman",15),fg="red")
            updateslabel.place(x=280,y=56)
        elif c_select=="Paper":
            y_score_label = Label(root, text=str(y_score), font=("bold", 15))
            y_score_label.place(x=530, y=200, width=50, height=30)
            c_score+=1
            c_score_label = Label(root, text=str(c_score), font=("bold", 15))
            c_score_label.place(x=570, y=240, width=50, height=30)
            updateslabel = Label(root, text='Computer Wins!!!! ', font=("Times new Roman", 15), fg="red")
            updateslabel.place(x=280, y=56)
        elif c_select=="Scissor":
            c_score_label = Label(root, text=str(c_score), font=("bold", 15))
            c_score_label.place(x=570, y=240, width=50, height=30)
            y_score += 1
            y_score_label = Label(root, text=str(y_score), font=("bold", 15))
            y_score_label.place(x=530, y=200, width=50, height=30)
            updateslabel = Label(root, text='YOU  WIN!!!! ', font=("Times new Roman", 15), fg="red")
            updateslabel.place(x=280, y=56)
    elif y_select=="Paper":
        if c_select=="Rock":
            c_score_label = Label(root, text=str(c_score), font=("bold", 15))
            c_score_label.place(x=570, y=240, width=100, height=30)
            y_score += 1
            y_score_label = Label(root, text=str(y_score), font=("bold", 15))
            y_score_label.place(x=530, y=200, width=100, height=30)
            updateslabel = Label(root, text="You Win...", font=("Times new Roman", 15), fg="red")
            updateslabel.place(x=280, y=56)
        elif c_select=="Paper":
            y_score_label = Label(root, text=str(y_score), font=("bold", 15))
            y_score_label.place(x=530, y=200, width=100, height=30)
            c_score_label = Label(root, text=str(c_score), font=("bold", 15))
            c_score_label.place(x=570, y=240, width=100, height=30)
            updateslabel = Label(root, text="Oops!Its a Tie..", font=("Times new Roman", 15), fg="red")
            updateslabel.place(x=280, y=56)
        elif c_select=="Scissor":
            y_score_label = Label(root, text=str(y_score), font=("bold", 15))
            y_score_label.place(x=530, y=200, width=100, height=30)
            c_score += 1
            c_score_label = Label(root, text=str(c_score), font=("bold", 15))
            c_score_label.place(x=570, y=240, width=100, height=30)
            updateslabel = Label(root, text="Computer Wins...", font=("Times new Roman", 15), fg="red")
            updateslabel.place(x=280, y=56)
    elif y_select=="Scissor":
        if c_select=="Rock":
            y_score_label = Label(root, text=str(y_score), font=("bold", 15))
            y_score_label.place(x=530, y=200, width=100, height=30)
            c_score += 1
            c_score_label = Label(root, text=str(c_score), font=("bold", 15))
            c_score_label.place(x=570, y=240, width=100, height=30)
            updateslabel = Label(root, text="Computer Wins...", font=("Times new Roman", 15), fg="red")
            updateslabel.place(x=280, y=56)
        elif c_select=="Paper":
            c_score_label = Label(root, text=str(c_score), font=("bold", 15))
            c_score_label.place(x=570, y=240, width=100, height=30)
            y_score += 1
            y_score_label = Label(root, text=str(y_score), font=("bold", 15))
            y_score_label.place(x=530, y=200, width=100, height=30)
            updateslabel = Label(root, text="You Win...", font=("Times new Roman", 15), fg="red")
            updateslabel.place(x=280, y=56)
        elif c_select=="Scissor":
            y_score_label = Label(root, text=str(y_score), font=("bold", 15))
            y_score_label.place(x=530, y=200, width=100, height=30)
            c_score_label = Label(root, text=str(c_score), font=("bold", 15))
            c_score_label.place(x=570, y=240, width=100, height=30)
            updateslabel = Label(root, text="Oops!Its a Tie..", font=("Times new Roman", 15), fg="red")
            updateslabel.place(x=280, y=56)




def result():
    n_win=Tk()
    n_win.title("Rock paper scissor!!!!!")
    n_win.geometry('400x350')
    resultlabel=Label(n_win,text="Rock Paper Scissor",font=("Algerian",20,'bold'))
    resultlabel.pack(side=TOP)
    if y_score<c_score:
        resultlabel1=Label(n_win,text="Results :   Computer Won!!!!!",font=("Times New Roman",20))
        resultlabel1.place(x=80,y=55)
    elif y_score>c_score:
        resultlabel2 = Label(n_win, text="Results :   You  Won!!!!!", font=("Times New Roman", 20))
        resultlabel2.place(x=80, y=55)
    else:
        resultlabel3 = Label(n_win, text="Results :   ITs a tie!!!!!", font=("Times New Roman", 20))
        resultlabel3.place(x=80, y=55)


    resultlabel4=Label(n_win,text="Your_Score:  "+str(y_score),font=("Italic",20))
    resultlabel4.place(x=100,y=150)
    resultlabel=Label(n_win,text="Computer_Score:  "+str(c_score),font=("Italic",20))
    resultlabel.place(x=80,y=250)



    n_win.mainloop()

r_button=Button(root,text="Paper",bg='brown',font=("Algerian",12,"bold"),command=paper)
r_button.place(x=46,y=100,width=150,height=40)

p_button=Button(root,text="Scissor",bg='white',font=("Algerian",12,"bold"),command=scissor)
p_button.place(x=250,y=100,width=150,height=40)

r_button=Button(root,text="Rock",bg='yellow',font=("Algerian",12,"bold"),command=rock)
r_button.place(x=460,y=100,width=150,height=40)


root.mainloop()