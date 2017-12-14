from tkinter import *
from daily_rate import *

def getRates():
    label2.pack(expand=YES, fill=BOTH)

root = Tk()
frame = Frame(root)
label = Label(frame, text="Current Exchange Rates")
label2 = Label(text = currentRates())
button1 = Button(frame, text = "Get Rates",command=getRates)

frame.pack()
label.pack()
button1.pack()

root.mainloop()
