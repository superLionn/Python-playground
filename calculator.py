from tkinter import *

#Create Event Methods attached to the button
#Get value from number button
expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)
#Get result from equal button
def equalPress():
     try:
         global expression
         total = str(eval(expression))
         equation.set(total)
         expression = ""
     except:
         equation.set(" error ")
         expression = "" 

#Reset the value in expression
def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":


    #Create a window
    MyWindow = Tk()
    MyWindow.title("Calculator GUI")
    MyWindow.configure(background='light blue')
    MyWindow.geometry('340x450')


    # StringVar() is the variable class
    # Create an instance of this class
    equation = StringVar()

    # create the text entry box for
    # showing the expression .
    expression_field = Entry(MyWindow, textvariable=equation)
    expression_field.grid(columnspan=5, ipadx = 40)
    #Create the GUI Component but dont display or add them to the window yet
    button1 = Button(MyWindow,text = ' 1 ', fg='black', bg='red', command=lambda: press(1), height=5,width=5)
    button1.grid(column=0, row=4)

    button2 = Button(MyWindow,text = ' 2 ', fg='black', bg='red', command=lambda: press(2), height=5,width=5)
    button2.grid(column=1,row=4)
    button3 = Button(MyWindow,text = ' 3 ', fg='black', bg='red', command=lambda: press(3), height=5,width=5)
    button3.grid(column=2,row=4)
    button4 = Button(MyWindow,text = ' 4 ', fg='black', bg='red', command=lambda: press(4), height=5,width=5)
    button4.grid(column=0,row=3)
    button5 = Button(MyWindow,text = ' 5 ', fg='black', bg='red', command=lambda: press(5), height=5,width=5)
    button5.grid(column=1,row=3)
    button6 = Button(MyWindow,text = ' 6 ', fg='black', bg='red', command=lambda: press(6), height=5,width=5)
    button6.grid(column=2,row=3)
    button7 = Button(MyWindow,text = ' 7 ', fg='black', bg='red', command=lambda: press(7), height=5,width=5)
    button7.grid(column=0,row=2)
    button8 = Button(MyWindow,text = ' 8 ', fg='black', bg='red', command=lambda: press(8), height=5,width=5)
    button8.grid(column=1,row=2)
    button9 = Button(MyWindow,text = ' 9 ', fg='black', bg='red', command=lambda: press(9), height=5,width=5)
    button9.grid(column=2,row=2)
    button0 = Button(MyWindow,text = ' 0 ', fg='black', bg='red', command=lambda: press(0), height=5,width=5)
    button0.grid(column=1,row=5)

    blank = Button(MyWindow,text = '  ', fg='black', bg='red', height=5,width=5)
    blank.grid(column=0,row=5)



    plus = Button(MyWindow,text = ' + ', fg='black', bg='red', command=lambda: press("+"), height=5,width=5)
    plus.grid(column=3,row=5)
    minus = Button(MyWindow,text = ' - ', fg='black', bg='red', command=lambda: press("-"), height=5,width=5)
    minus.grid(column=3,row=4)
    multiply = Button(MyWindow,text = ' * ', fg='black', bg='red', command=lambda: press("*"), height=5,width=5)
    multiply.grid(column=3,row=3)
    divide = Button(MyWindow,text = ' / ', fg='black', bg='red', command=lambda: press("/"), height=5,width=5)
    divide.grid(column=3,row=2)
    equal = Button(MyWindow,text = ' = ', fg='black', bg='red', command=equalPress, height=5,width=5)
    equal.grid(column=3,row=1)
    Decimal = Button(MyWindow,text = ' . ', fg='black', bg='red', command=lambda: press("."), height=5,width=5)
    Decimal.grid(column=2,row=5)
    Reset = Button(MyWindow,text = " AC ", fg='black', bg='red', command=clear, height=5,width=5)
    Reset.grid(column=0,row=1)
    MyWindow.mainloop()













