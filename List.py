from tkinter import *
import random
root=Tk()


root.title("list")
root.geometry("400x600")
root.configure(background="#800237")

randomList=Label(root,fg="blue",bg="#FFD700")
randomSortedList=Label(root,fg="blue",bg="#FFD700")

def list1():
    l=random.sample(range(10,30),5)
    randomList["text"]="random list : "+str(l)
    l.sort()
    randomSortedList["text"]="random sorted list: "+str(l)

btn=Button(root,text="random no.",bg="#800237",fg="white",command=list1)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)
randomList.place(relx=0.5,rely=0.5,anchor=CENTER)
randomSortedList.place(relx=0.5,rely=0.6,anchor=CENTER)
root.mainloop()
