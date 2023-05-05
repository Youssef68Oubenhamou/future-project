from tkinter import *
import os
import random


def get_conditions():

    class PasswordGeneratorOneT:

        alphabets1 = [
            'a' , 'b' , 'c' , 'd' ,
            'e' , 'f' , 'c' , 'i' ,
            'j' , 'k' , 'l' , 'm' ,
            'n' , 'o' , 'p' , 'q' ,
            'r' , 's' , 't' , 'u' ,
            'v' , 'w' , 'x' , 'y' ,
            'z'
        ]

        numbers = [
            '1' , '2' , '3' , '4' , '5' ,
            '6' , '7' , '8' , '9' , '0'
        ]

        FILE_PATH = "./passwords.txt"

        def __init__(self):
            self.password = ""

        def make_pass(self):
            self.type1 = ent1.get() or ent2.get()
            self.length1 = int(ent3.get())
            self.size = ent4.get()
            nothing1 = ""
            if self.type1 == "letters" :
                if self.size == "UPPER" :
                    for i in range(self.length1):
                        nothing1 += random.choice(PasswordGeneratorOneT.alphabets1).upper()
                    self.password = nothing1
                elif self.size == "lower" :
                    for i in range(self.length1):
                        nothing1 += random.choice(PasswordGeneratorOneT.alphabets1).lower()
                    self.password = nothing1
            elif self.type1 == "numbers":
                for j in range(self.length1):
                    nothing1 += random.choice(PasswordGeneratorOneT.numbers)
                self.password = nothing1
            else :
                ent1.delete("0" , "end")
                ent2.delete("0" , "end")
                ent3.delete("0" , "end")
                ent4.delete("0" , "end")
                ent6.delete("0" , "end")
            
                
            return f"{self.password}"
	
    class GenerateOneT(PasswordGeneratorOneT):

        def __init__(self):
            super()

        def save(self , hide:bool):
            self.AccountName = ent6.get()
            self.hide = hide
            with open(PasswordGeneratorOneT.FILE_PATH, "a") as file:
                file.writelines(f"[{self.AccountName}] {self.password}\n")

    ent5 = Entry(win1 ,
                bg="yellow" ,
                fg="black" ,
                font=("Times" , 20 , "bold") ,
                width=30
            )
    ent5.place(x=140 , y=560)
    if ent1.get() != True or ent2.get() != True :
        c1 = GenerateOneT()
        ent5.insert(0 , c1.make_pass())

win1 = Tk()

win1.geometry("700x700")

win1.config(background="#36454F")

win1.title("Password Generator by YoussefOubenhamou")
    
lab = Label(win1 ,
           text="Password Generator" ,
           background="#36454F" ,
           foreground="orange" ,
           font=("Helvetica" , 35 , "bold") 
            )

lab1 = Label(win1 ,
            text="Enter the first type : " ,
            background="#36454F" ,
            fg="black" ,
            font=("Times" , 15 , "bold")
            )

lab2 = Label(win1 ,
            text="Enter the second type : " ,
            background="#36454F" ,
            fg="black" ,
            font=("Times" , 15 , "bold")
            )

lab3 = Label(win1 ,
            text="Enter the length of \nyour password : " ,
            background="#36454F" ,
            fg="black" ,
            font=("Times" , 15 , "bold")
            )

lab4 = Label(win1 ,
            text="Enter the size of it \nUPPER/lower : " ,
            background="#36454F" ,
            fg="black" ,
            font=("Times" , 15 , "bold")
            )

lab6 = Label(win1 ,
            text="Enter the name of \nthe Account : " ,
            bg="#36454F" ,
            fg="black" ,
            font=("Times" , 15 , "bold")
            )

ent1 = Entry(win1 , 
            foreground="black" ,
            background="cyan" ,
            font=("Times" , 20 , "bold") ,
            )

ent2 = Entry(win1 , 
            foreground="black" ,
            background="cyan" ,
            font=("Times" , 20 , "bold") ,
            )

ent3 = Entry(win1 , 
            foreground="black" ,
            background="cyan" ,
            font=("Times" , 20 , "bold") ,
            )

ent4 = Entry(win1 , 
            fg="black" ,
            bg="cyan" ,
            font=("Times" , 20 , "bold") ,
            )

ent6 = Entry(win1 ,
            fg="black" ,
            bg="cyan" ,
            font=("Times" , 20 , "bold")
            )

but_on = Button(win1 ,
               font=("Arial" , 15 , "bold") ,
               text="Generate The Password" ,
               background="burlywood" ,
               foreground="black" ,
               activebackground="burlywood" ,
               activeforeground="black" ,
               width=20 ,
               relief=RAISED ,
               bd=10 ,
               command=get_conditions ,
            )

lab.place(x=130 , y=40)
lab1.place(x=50 , y=205)
lab2.place(x=50 , y=275)
lab3.place(x=50 , y=330)
lab4.place(x=50 , y=400)
lab6.place(x=50 , y=470)

ent1.place(x=260 , y=200)
ent2.place(x=260 , y=270)
ent3.place(x=260 , y=340)
ent4.place(x=260 , y=410)
ent6.place(x=260 , y=480)

but_on.place(x=220 , y=620)

win1.mainloop()