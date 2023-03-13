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
equation=StringVar()
button1=Button (screen,text="1",fg='blue',bg='black',height=1,width=5,command=lambda:run(1)).grid(row=2,column=0)
button2=Button (screen,text="2",fg='blue',bg='black',height=1,width=5,command=lambda:run(2)).grid(row=2,column=1)
button3=Button (screen,text="3",fg='blue',bg='black',height=1,width=5,command=lambda:run(3)).grid(row=2,column=2)
button4=Button (screen,text="4",fg='blue',bg='black',height=1,width=5,command=lambda:run(4)).grid(row=3,column=0)
button5=Button (screen,text="5",fg='blue',bg='black',height=1,width=5,command=lambda:run(5)).grid(row=3,column=1)
button6=Button (screen,text="6",fg='blue',bg='black',height=1,width=5,command=lambda:run(6)).grid(row=3,column=2)
button7=Button (screen,text="7",fg='blue',bg='black',height=1,width=5,command=lambda:run(7)).grid(row=4,column=0)
button8=Button (screen,text="8",fg='blue',bg='black',height=1,width=5,command=lambda:run(8)).grid(row=4,column=1)
button9=Button (screen,text="9",fg='blue',bg='black',height=1,width=5,command=lambda:run(9)).grid(row=4,column=2)
button0=Button (screen,text="0",fg='blue',bg='black',height=1,width=5,command=lambda:run(0)).grid(row=5,column=0,columnspan=2,ipadx=33)
button9=Button (screen,text=".",fg='black',bg='white',height=1,width=5,command=lambda:run(".")).grid(row=5,column=2)
button9=Button (screen,text="*",fg='black',bg='white',height=1,width=5,command=lambda:run("*")).grid(row=1,column=3)
button9=Button (screen,text="-",fg='black',bg='white',height=1,width=5,command=lambda:run("-")).grid(row=2,column=3)
button9=Button (screen,text="+",fg='black',bg='white',height=1,width=5,command=lambda:run("+")).grid(row=3,column=3)
button1=Button (screen,text="=",fg='black',bg='white',height=1,width=5,command=lambda:result()).grid(row=4,column=3,rowspan=2,ipady=15)
button2=Button (screen,text="÷",fg='black',bg='white',height=1,width=5,command=lambda:run("÷")).grid(row=1)
button3=Button (screen,text="AC",fg='black',bg='white',height=1,width=5,command=lambda:clear()).grid(row=1,column=0)
button4=Button (screen,text="√x",fg='black',bg='white',height=1,width=5,command=lambda:run("√x")).grid(row=1,column=1)
button5=Button (screen,text="%",fg='black',bg='white',height=1,width=5,command=lambda:run("%")).grid(row=1,column=2)
answer=Entry(screen,textvariable=equation,width=34).grid(row=0,column=0,columnspan=4)

screen.mainloop()
label("hi")
