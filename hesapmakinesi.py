import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("hesapmako_zeynelborandogan")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_883=tk.Button(root)
        GButton_883["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_883["font"] = ft
        GButton_883["fg"] = "#000000"
        GButton_883["justify"] = "center"
        GButton_883["text"] = "+"
        GButton_883.place(x=100,y=270,width=30,height=25)
        GButton_883["command"] = self.GButton_883_command

        GButton_717=tk.Button(root)
        GButton_717["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_717["font"] = ft
        GButton_717["fg"] = "#000000"
        GButton_717["justify"] = "center"
        GButton_717["text"] = "-"
        GButton_717.place(x=210,y=270,width=30,height=25)
        GButton_717["command"] = self.GButton_717_command

        GButton_475=tk.Button(root)
        GButton_475["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_475["font"] = ft
        GButton_475["fg"] = "#000000"
        GButton_475["justify"] = "center"
        GButton_475["text"] = "x"
        GButton_475.place(x=310,y=270,width=30,height=25)
        GButton_475["command"] = self.GButton_475_command

        GButton_453=tk.Button(root)
        GButton_453["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_453["font"] = ft
        GButton_453["fg"] = "#000000"
        GButton_453["justify"] = "center"
        GButton_453["text"] = "/"
        GButton_453.place(x=480,y=270,width=30,height=25)
        GButton_453["command"] = self.GButton_453_command

        GLineEdit_987=tk.Entry(root)
        GLineEdit_987["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_987["font"] = ft
        GLineEdit_987["fg"] = "#333333"
        GLineEdit_987["justify"] = "center"
        GLineEdit_987["text"] = "Entry"
        GLineEdit_987.place(x=110,y=100,width=70,height=25)

        GLineEdit_913=tk.Entry(root)
        GLineEdit_913["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_913["font"] = ft
        GLineEdit_913["fg"] = "#333333"
        GLineEdit_913["justify"] = "center"
        GLineEdit_913["text"] = "Entry"
        GLineEdit_913.place(x=200,y=100,width=70,height=25)

        GLineEdit_123=tk.Entry(root)
        GLineEdit_123["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_123["font"] = ft
        GLineEdit_123["fg"] = "#333333"
        GLineEdit_123["justify"] = "center"
        GLineEdit_123["text"] = "Entry"
        GLineEdit_123.place(x=400,y=100,width=70,height=25)

        GLabel_906=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_906["font"] = ft
        GLabel_906["fg"] = "#333333"
        GLabel_906["justify"] = "center"
        GLabel_906["text"] = "Rakam1"
        GLabel_906.place(x=110,y=50,width=70,height=25)

        GLabel_599=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_599["font"] = ft
        GLabel_599["fg"] = "#333333"
        GLabel_599["justify"] = "center"
        GLabel_599["text"] = "Rakam2"
        GLabel_599.place(x=200,y=50,width=70,height=25)

        GLabel_438=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_438["font"] = ft
        GLabel_438["fg"] = "#333333"
        GLabel_438["justify"] = "center"
        GLabel_438["text"] = "sonuc"
        GLabel_438.place(x=400,y=50,width=70,height=25)

    def GButton_883_command(self):
        print("buton1'e basildi")


    def GButton_717_command(self):
        print("buton2'e basildi")


    def GButton_475_command(self):
        print("buton3'e basildi")


    def GButton_453_command(self):
        print("buton4'e basildi")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    testBoxYazilanlar1 = tk.StringVar()  
    testBoxYazilanlar2 = tk.StringVar()  
    testBoxYazilanlar3 = tk.StringVar()  
    root.mainloop()
