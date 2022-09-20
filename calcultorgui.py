from cProfile import label
from tkinter import *
from turtle import left

expression=""
def run(num):
  global expression
  global equation
  expression=expression+str(num)
  equation.set(expression)

def result():
    equation.set(str(eval(expression)))
def clear():
    global expression
    equation.set("")
    expression=""

screen=Tk()
screen.configure(bg="grey")
screen.title("my graphic windows")
screen.geometry("500x500")
welcome_text=Label(screen,text="CALCULATOR",fg='orange',bg='black')
welcome_text.pack(side=TOP)
equation=StringVar()  
button1=Button (screen,text="1",fg='black',bg='white',height=1,width=5,command=lambda:run(1)).place(x=50,y=60)
button2=Button (screen,text="2",fg='black',bg='white',height=1,width=5,command=lambda:run(2)).place(x=120,y=60)
button3=Button (screen,text="3",fg='black',bg='white',height=1,width=5,command=lambda:run(3)).place(x=190,y=60)
button4=Button (screen,text="4",fg='black',bg='white',height=1,width=5,command=lambda:run(4)).place(x=50,y=90)
button5=Button (screen,text="5",fg='black',bg='white',height=1,width=5,command=lambda:run(5)).place(x=120,y=90)
button6=Button (screen,text="6",fg='black',bg='white',height=1,width=5,command=lambda:run(6)).place(x=190,y=90)
button7=Button (screen,text="7",fg='black',bg='white',height=1,width=5,command=lambda:run(7)).place(x=50,y=120)
button8=Button (screen,text="8",fg='black',bg='white',height=1,width=5,command=lambda:run(8)).place(x=120,y=120)
button9=Button (screen,text="9",fg='black',bg='white',height=1,width=5,command=lambda:run(9)).place(x=190,y=120)
button9=Button (screen,text="*",fg='black',bg='white',height=1,width=5,command=lambda:run("*")).place(x=260,y=60)
button9=Button (screen,text="-",fg='black',bg='white',height=1,width=5,command=lambda:run("-")).place(x=260,y=90)
button9=Button (screen,text="+",fg='black',bg='white',height=1,width=5,command=lambda:run("+")).place(x=260,y=120)
button1=Button (screen,text="=",fg='black',bg='white',height=1,width=5,command=lambda:result()).place(x=260,y=150)
button2=Button (screen,text="÷",fg='black',bg='white',height=1,width=5,command=lambda:run("÷")).place(x=260,y=30)
button3=Button (screen,text="AC",fg='black',bg='white',height=1,width=5,command=lambda:clear()).place(x=190,y=30)
button4=Button (screen,text="√x",fg='black',bg='white',height=1,width=5,command=lambda:run("√x")).place(x=50,y=30)
button5=Button (screen,text="%",fg='black',bg='white',height=1,width=5,command=lambda:run("%")).place(x=120,y=30)
answer=Entry(screen,textvariable=equation,width=34).place(x=50,y=0)

screen.mainloop()
