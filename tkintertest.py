from Tkinter import *

class Program:
    def __init__(self, master):
        main = Frame(master)
        main.pack()
        frame = Frame(main, bg = '#bbbbbb', width = '360', height = '100')
        frame.pack()

        entry_content1 = StringVar()
        entry_content2 = StringVar()
        entry_content3 = StringVar()

        self.textAccountType = Label(frame, bg = '#bbbbbb', text="Account Type")
        self.textAccountType.grid(row=0, column=0, sticky=W, padx=5)

        self.textName = Label(frame, bg = '#bbbbbb', text="Name")
        self.textName.grid(row=0, column=1, sticky=W, padx=5)

        self.textAccount = Label(frame, bg = '#bbbbbb', text="Account Number")
        self.textAccount.grid(row=0, column=2, sticky=W, padx=5)

root = Tk()
application = Program(root)
root.mainloop()
