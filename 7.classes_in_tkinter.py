from tkinter import *

class testButtons:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="tekstjakis", command = self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="tekstklita", command =frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("wow, uhuhuh, dziala ")


root = Tk()
b = testButtons(root)
root.mainloop()