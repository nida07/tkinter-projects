from tkinter import *
import parser
root=Tk()
root.title("calculator")
# Adjust size
root.geometry("400x400")

display=Entry(root)
display.grid(row=1,columnspan=6,sticky=W+E)
# getting numbers as input
i=0
def get_variable(num):
    global i
    display.insert(i,num)
    i+=1

def clr():
    display.delete(0,END)
# it delete up to end
def undo():
    fstr=display.get()
    if len(fstr):
        nstr=fstr[:-1]
        clr()
        display.insert(0,nstr)
    else:
        clr()
        display.inser(0,"ERROR")
def operation(opr):
    global i
    length=len(opr)
    display.insert(i,opr)
    i+=length
def cal():
    estr=display.get()
    try:
        a=parser.expr(estr).compile()
        res=eval(a)
        clr()
        display.insert(0,res)
    except Exception:
        clr()
        display.insert(0,"ERROR")




Button(root,text="1",command=lambda :get_variable(1)).grid(row=2,column=0)
Button(root,text="2",command=lambda :get_variable(2)).grid(row=2,column=1)
Button(root,text="3",command=lambda :get_variable(3)).grid(row=2,column=2)
Button(root,text="4",command=lambda :get_variable(4)).grid(row=3,column=0)
Button(root,text="5",command=lambda :get_variable(5)).grid(row=3,column=1)
Button(root,text="6",command=lambda :get_variable(6)).grid(row=3,column=2)
Button(root,text="7",command=lambda :get_variable(7)).grid(row=4,column=0)
Button(root,text="8",command=lambda :get_variable(8)).grid(row=4,column=1)
Button(root,text="9",command=lambda :get_variable(9)).grid(row=4,column=2)
Button(root,text="0",command=lambda :get_variable(0)).grid(row=5,column=1)
# adding operators
Button(root,text="UNDO",bg="#00cc99",command=lambda :undo()).grid(row=5,column=0)
Button(root,text="=",bg="grey",command=lambda :cal()).grid(row=5,column=2)
Button(root,text="+",bg="grey",command=lambda :operation('+')).grid(row=2,column=3)
Button(root,text="-",bg="grey",command=lambda :operation('-')).grid(row=3,column=3)
Button(root,text="*",bg="grey",command=lambda :operation('*')).grid(row=4,column=3)
Button(root,text="/",bg="grey",command=lambda :operation('/')).grid(row=5,column=3)
Button(root,text="AC",bg="red",command=lambda :clr()).grid(row=2,column=4)
Button(root,text="(",bg="grey",command=lambda :operation('(')).grid(row=3,column=4)
Button(root,text=")",bg="grey",command=lambda :operation(')')).grid(row=4,column=4)
Button(root,text="%",bg="grey",command=lambda :operation('%')).grid(row=5,column=4)
Button(root,text="π",bg="grey",command=lambda :operation('*3.14')).grid(row=2,column=5)
Button(root,text="^2",bg="grey",command=lambda :operation('**2')).grid(row=3,column=5)
Button(root,text=".",bg="grey",command=lambda :operation('.')).grid(row=4,column=5)
Button(root,text="exp",bg="grey",command=lambda :operation('**')).grid(row=5,column=5)



root.mainloop()




