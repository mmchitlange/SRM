from Tkinter import Tk, W, E, Label
from ttk import Frame, Button, Style
from PIL import ImageTk,Image
from ttk import Entry
import ttk
import Image
from PIL import ImageTk

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)   

        self.parent = parent
        self.initUI()


    def initUI(self):



        self.parent.title("Snack Ladder")

        Style().configure("TButton", padding=(0, 5, 0, 5), 
            font='serif 10')

        label=Label(self, compound='center')        

        for i in range(10):
            label.columnconfigure(i, pad=3)
            label.rowconfigure(i, pad=3)

        #self.rowconfigure(1, pad=3)
        #self.rowconfigure(2, pad=3)
        #self.rowconfigure(3, pad=3)
        #self.rowconfigure(4, pad=3)

        # list declaration for filling the boxes and defining their id
        #
        #
        Box_Id_list = []
        Box_Text_list = []
        for i in range(100):
            Box_Id_list.append('label_'+str(i))
            Box_Text_list.append(str(i+1))

        #frame_1 = Frame(self)
        pos=0
        value=99
        print Box_Id_list
        for row in range(10):
            for col in range(10):
                Box_Id_list[pos] = Label(label, text=Box_Text_list[value],anchor='center',bd=20, height=1, width=2,bg="lightgreen")
                Box_Id_list[pos].grid(row=row, column=col)
                pos = pos+1
                value = value-1

        self.place(x=0,y=0,height=4020,width=4020)
        player_box = Label(self,text="",bg="#940504",font=("Courier", 15))
        player_box.place(x=950,y=50,height=350,width=500)
        player_turn = Label(player_box,text="Leader Board",bg="#940504",font=("Courier", 20, "bold italic"))
        player_turn.place(x=10,y=10,height=50,width=200)

        name = Label(player_box,text="Name of Player",bg="blue",font=("Courier", 15))
        name.place(x=30,y=70,height=50,width=200)
        score = Label(player_box,text="Score",bg="blue",font=("Courier", 15))
        score.place(x=290,y=70,height=50,width=200)
        # plaers name
        player1 = Label(player_box,text="Rahul Gupta",bg="#940504",font=("Courier", 15))
        player1.place(x=12,y=130,height=50,width=200)
        player2 = Label(player_box,text="Rahul Gupta",bg="#940504",font=("Courier", 15))
        player2.place(x=12,y=180,height=50,width=200)
        player3 = Label(player_box,text="Rahul Gupta",bg="#940504",font=("Courier", 15))
        player3.place(x=12,y=230,height=50,width=200)
        player4 = Label(player_box,text="Rahul Gupta",bg="#940504",font=("Courier", 15))
        player4.place(x=12,y=280,height=50,width=200)

        #players score
        score1 = Label(player_box,text="65",bg="#940504",font=("Courier", 15))
        score1.place(x=280,y=130,height=50,width=200)
        score2 = Label(player_box,text="65",bg="#940504",font=("Courier", 15))
        score2.place(x=280,y=180,height=50,width=200)
        score3 = Label(player_box,text="65",bg="#940504",font=("Courier", 15))
        score3.place(x=280,y=230,height=50,width=200)
        score4 = Label(player_box,text="65",bg="#940504",font=("Courier", 15))
        score4.place(x=280,y=280,height=50,width=200)

        dice_box = Label(self,text="",bg="#940504",font=("Courier", 15))
        dice_box.place(x=950,y=500,height=220,width=500)
        player_turn = Label(dice_box,text="Players Turn",bg="#940504",font=("Courier", 20,"bold italic"))
        player_turn.place(x=10,y=30,height=50,width=200)
        player_name = Label(dice_box,text="Rahul Gupta",bg="pink",font=("Courier", 15))
        player_name.place(x=270,y=30,height=50,width=200)
        imag =Image.open('dice.png')
        background_image = ImageTk.PhotoImage(imag)
        dice_button =Button(dice_box,text="Dice")
        dice_button.place(x=250,y=120,height=50,width=100)
        label.place(x=12,y=47,height=2020,width=1000)


def main():

    root = Tk()
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()
