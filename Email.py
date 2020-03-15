from tkinter import*
from random import*


def Scree1():
    
    label1 = Label(root ,fg = "white", width = 20,bg = "red", padx = 30 ,pady = 10, text = "Welcome to Math Quiz", font=("Times", "24","bold italic"))
    label1.pack()
    
    label2 = Label (root ,text ="Name",width = 20,font=("Time","14","bold italic"))
    label2.pack()
    
    textbox1 = Entry (root,width = 20)
    textbox1.pack()
    
    label3 = Label (root,text ="Age",width = 20,font=("Time","14","bold italic"))
    label3.pack()
    
    textbox2 = Entry (root,width = 20)
    textbox2.pack(padx = 2, pady = 10)
    
    rb1 = Radiobutton(root,width = 20,value = 1,text = "Easy", anchor = W)
    rb1.pack()
    rb2 = Radiobutton(root,width = 20,value = 2,text ="Medium", anchor = W)
    rb2.pack()
    rb3 = Radiobutton(root,width = 20,value = 3,text ="Hard", anchor = W)
    rb3.pack()
    button1 = Button(root,text = "Next",)
    button1.pack()

#Main routine
root = Tk()
root.title("Screenl")
root.geometry("400x300+850+0")   

root.mainloop()
