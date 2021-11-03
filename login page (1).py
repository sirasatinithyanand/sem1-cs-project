from tkinter import *
import mysql.connector
import tkinter as tk
from PIL import ImageTk,Image
import random
import pygame


pygame.mixer.init()
def play():
        pygame.mixer.music.load("C:\\Users\\Nithya\\OneDrive\\Desktop\\cs project\\perfect.mp3")
        pygame.mixer.music.play(loops=100)
play()





# Returns list of digits of a number 
def getDigits(num): 
        return [int(i) for i in str(num)] 


def noDuplicates(num): 
        num_li = getDigits(num) 
        if len(num_li) == len(set(num_li)): 
                return True
        else: 
                return False




# Generates a 4 digit number with no repeated digits	 
def generateNum(): 
        while True: 
                num = random.randint(1000,9999) 
                if noDuplicates(num): 
                        return num 

num = generateNum()
print(num)
#set variables
tries = 10
turn_no = 1
y_var1 = 330
y_var2 = 350
win = 0


def game_page():

        def homepagedisp():
            gamepage.destroy()
            homepage()
        
            
        def backgame():

            def backtogamepage():
                incorrectpass.destroy()
                game_page()
        
            def back():
                incorrectpass.destroy()
                pygame.mixer.music.stop()
                
            incorrectpass=tk.Tk()
            incorrectpass.geometry("325x200")
            f15=tk.Canvas(bg="light blue",height=2190,width=1520).pack()
            incorrectpass.title("ARE YOU SURE??")

            head=tk.Label(incorrectpass,text='ARE YOU SURE??',fg="black",bg="light blue",font=("Courier",10))
            head.place(x=20,y=65)
            btn = tk.Button(f15, text = 'OKAY', command = back, fg = "White" ,bg="Black", width="15")
            btn.place(x=100,y=105)
            btn = tk.Button(f15, text = 'BACK', command = backtogamepage, fg = "White" ,bg="Black", width="15")
            btn.place(x=100,y=135)

        def quitcheck():
            gamepage.destroy()
            backgame()
            
        # Returns list of digits of a number 
        def getDigits(num): 
                return [int(i) for i in str(num)] 
                

        # Returns True if number has no duplicate digits, otherwise False	                
        def noDuplicates(num): 
                num_li = getDigits(num) 
                if len(num_li) == len(set(num_li)): 
                        return True
                else: 
                        return False


        # Generates a 4 digit number with no repeated digits	 
        def generateNum(): 
                while True: 
                        num = random.randint(1000,9999) 
                        if noDuplicates(num): 
                                return num 


        # Returns common digits with exact matches (bulls) and the common digits in wrong position (cows) 
        def numOfBullsCows(num,guess): 
                bull_cow = [0,0] 
                num_li = getDigits(num) 
                guess_li = getDigits(guess) 
                
                for i,j in zip(num_li,guess_li): 
                        
                        # common digit present 
                        if j in num_li: 
                        
                                # common digit exact match 
                                if j == i: 
                                        bull_cow[0] += 1
                                
                                # common digit match but in wrong position 
                                else: 
                                        bull_cow[1] += 1
                                        
                return bull_cow

        # Secret Code 
        num = generateNum()
        print(num)
        #set variables
        tries = 10
        turn_no = 1
        y_var1 = 330
        y_var2 = 350
        win = 0
        # Play game until correct guess or till no tries left
        def PlayGame():
                global tries
                global turn_no
                global y_var1
                global y_var2
                global win
                if tries > 0 and win == 0:
                        guess = int(num_input.get())
                        text20 = Label(gamepage,text=f"\t\t      {tries-1} attempts left\t\t\t\t",fg="black",bg="light blue",font=("Helvetica",12))
                        text20.place(x=32, y=255)
                        
                        if not noDuplicates(guess): 
                                text20 = Label(gamepage,text='Note: Number should not have repeated digits. Try again.',fg="black",bg="light blue",font=("Helvetica",12))
                                text20.place(x=20, y=255)
                
                                
                        elif guess < 1000 or guess > 9999: 
                                text21 = Label(gamepage,text='Note: Enter 4 digit number only. Try again.',fg="black",bg="light blue",font=("Helvetica",12))
                                text21.place(x=20, y=255)
                
                        else:
                                bull_cow = numOfBullsCows(num,guess)
                                text10 = Label(gamepage,text=f"{turn_no}) {guess}",fg="black",bg="light blue",font=("Helvetica",12))
                                text10.place(x=20, y = y_var1)
                                text11 = Label(gamepage,text=f"{bull_cow[1]} bulls, {bull_cow[0]} cows",fg="black",bg="light blue",font=("Helvetica",12))
                                text11.place(x=20, y = y_var2)
                                tries -=1
                                turn_no +=1
                                y_var1 += 40
                                y_var2 += 40
                                
                                if bull_cow[0] == 4: 
                                        text20 = Label(gamepage,text='You guessed right!\t\t\t\t\t',fg="black",bg="light blue",font=("Helvetica",12))
                                        text20.place(x=20, y=255)
                                        win +=1
                                if tries == 0:
                                        text20 = Label(gamepage,text=f"You ran out of tries. Number was {num}",fg="black",bg="light blue",font=("Helvetica",12))
                                        text20.place(x=20, y=255)
                        num_input.delete(0,len(num_input.get()))

        gamepage = Tk()
        gamepage.geometry("500x750")
        #canvas
        Canvas1 = Canvas(bg="light blue",height=2190,width=1520).pack()
        gamepage.title("COW & BULL")
        #title
        title = Label(gamepage,text='COW & BULL GAME',fg="black",bg="light blue",font=("Helvetica",20,"bold"))
        title.place(x=125, y=35)
        #Enter number
        text1 = Label(gamepage,text='ENTER YOUR NUMBER',fg="black",bg="light blue",font=("Helvetica",12))
        text1.place(x=165, y=120)
        #text box
        num_input = Entry(gamepage, width = 35)
        num_input.place(x=148, y = 170)
        #guess button
        action_b1 = Button(gamepage, text = 'GUESS!', command = PlayGame, fg = "White" ,bg="Black", width="20",activebackground="gray")
        action_b1.place(x=178,y=225)
        #your guesses:
        text2 = Label(gamepage,text='Your guesses:',fg="black",bg="light blue",font=("Helvetica",15))
        text2.place(x=20, y=300)
        btn = tk.Button(gamepage, text = '<BACK', command =homepagedisp, fg = "White" ,bg="Black", width="10",activebackground="gray")
        btn.place(x=5,y=10)
        btn = tk.Button(gamepage, text = 'QUIT', command =quitcheck, fg = "White" ,bg="Black", width="10",activebackground="gray")
        btn.place(x=415,y=10)
        
        gamepage.mainloop()








































def inspage():
    def quitpage():
        inspage.destroy()
        pygame.mixer.music.stop()
    def homepagedisp():
        
        inspage.destroy()
        homepage()
    
    inspage=tk.Tk()
    inspage.geometry("500x600")
    f15=tk.Canvas(bg="light blue",height=2190,width=1520).pack()
    
    inspage.title("INSTRUCTIONS PAGE")
    head=tk.Label(inspage,text='INSTRUCTIONS',fg="black",bg="light blue",font=("Helvetica",20,"bold"))
    head.place(x=140,y=45)

    text=tk.Label(inspage,text='All digits in the secret number are different',fg="black",bg="light blue",font=("Courier",10))
    text.place(x=55,y=135)
    text=tk.Label(inspage,text=' The secret number cannot start with zero ',fg="black",bg="light blue",font=("Courier",10))
    text.place(x=65,y=175)
    text=tk.Label(inspage,text='If your try has matching digits on the exact \n places, they are Bulls',fg="black",bg="light blue",font=("Courier",10))
    text.place(x=55,y=215)
    text=tk.Label(inspage,text='If you have digits from the secret number, but \n not on the right places, they are Cows',fg="black",bg="light blue",font=("Courier",10))
    text.place(x=55,y=270)
    text=tk.Label(inspage,text='In the lower text area is added your proposition \nand the number of bulls and cows that match',fg="black",bg="light blue",font=("Courier",10))
    text.place(x=55,y=325)

    btn = tk.Button(f15, text = 'BACK TO HOMEPAGE', command =homepagedisp, fg = "White" ,bg="Black", width="25",activebackground="gray")
    btn.place(x=150,y=410)
    btn = tk.Button(f15, text = 'QUIT', command =quitpage, fg = "White" ,bg="Black", width="25",activebackground="gray")
    btn.place(x=150,y=465)
    
    inspage.mainloop()

















def homepage():
    def gamepagedisp():
        root.destroy()
        game_page()
    
    def loginpagedisp():
        root.destroy()
        login_page()
        
    def quitpage():
        root.destroy()
        pygame.mixer.music.stop()

    def popupmsg():
        root.destroy()
        inspage()

        
    root=Tk()
    myCanvas=Canvas(root,bg='lightblue',height=600,width=500)
    myCanvas.create_text(250,30,text='cows and bulls')


    btn=Button(root,text='HOW TO PLAY',command=popupmsg,bg='black',fg='white',width='25',activebackground="gray")
    btn.place(x=158,y=375)
    btn=Button(root,text='START GAME',command=gamepagedisp,bg='black',fg='white',width='25',activebackground="gray")
    btn.place(x=158,y=325)
    btn = tk.Button(myCanvas, text = 'LOGOUT', command =loginpagedisp, fg = "White" ,bg="Black", width="25",activebackground="gray")
    btn.place(x=158,y=425)
    btn = tk.Button(myCanvas, text = 'QUIT', command =quitpage, fg = "White" ,bg="Black", width="25",activebackground="gray")
    btn.place(x=158,y=475)

    bgg15=Image.open("logo.png")
    resized=bgg15.resize((375,225),Image.ANTIALIAS)
    new_pic=ImageTk.PhotoImage(resized)
    bg15=tk.Label(myCanvas,bg='black',image=new_pic)
    bg15.place(x=65,y=25)



    myCanvas.pack()
    root.mainloop()















































def register_page():

    def success_register():
        def gotologin():
            successregister.destroy()
            login_page()
        
        successregister=tk.Tk()
        successregister.geometry("325x200")
        f15=tk.Canvas(bg="light blue",height=2190,width=1520).grid()
        successregister.title("SUCCESSFULLY REGISTERED!!")

        head=tk.Label(successregister,text='YOU HAVE SUCCESSFULLY REGISTERED!!!',fg="black",bg="light blue",font=("Courier",10))
        head.place(x=20,y=65)
        btn = tk.Button(f15, text = '<BACK TO LOGIN', command = gotologin, fg = "White" ,bg="Black", width="15")
        btn.place(x=100,y=105)

    def registeredd():
        registerpage.destroy()
        success_register()


    
    def func():
        nameval=name.get()
        usernameval=username.get()
        passwordval=password.get()
        repasswordval=repassword.get()


        if(passwordval==repasswordval):
            
            db=mysql.connector.MySQLConnection(
            host="127.0.0.1",
            user="root",
            passwd="Nith@2002",
            database="game",
            charset="utf8")
            
            mycursor=db.cursor()
            sql = "insert into gametable values (%s,%s,%s)"

        
            
            val=(nameval,usernameval,passwordval)
            mycursor.execute(sql,val)
            db.commit()

            registeredd()
            


            
        else:
            disp="YOUR PASSWORD AND RE-ENTER PASSWORD VALUES DON'T MATCH!!!"
            head=tk.Label(registerpage,text=disp,fg="black",bg="light blue",font=("Courier",10))
            head.place(x=20,y=500)


            
    def quitpage():
        registerpage.destroy()
        pygame.mixer.music.stop()
    def gotologin():
        registerpage.destroy()
        login_page()
    
    def clearfunc():
            namecon=name.get()
            len1=len(namecon)
            name.delete(0,len1)

            namecon=username.get()
            len1=len(namecon)
            username.delete(0,len1)

            namecon=password.get()
            len1=len(namecon)
            password.delete(0,len1)

            namecon=repassword.get()
            len1=len(namecon)
            repassword.delete(0,len1)
            
    
    registerpage=tk.Tk()
    registerpage.geometry("500x600")
    f15=tk.Canvas(bg="light blue",height=2190,width=1520).grid()

    registerpage.title("REGISTER PAGE")
    head=tk.Label(registerpage,text='REGISTER',fg="black",bg="light blue",font=("Helvetica",20,"bold"))
    head.place(x=175,y=60)
    head=tk.Label(registerpage,text='NAME-',fg="black",bg="light blue",font=("Courier",15))
    head.place(x=20,y=135)
    head=tk.Label(registerpage,text='USERNAME-',fg="black",bg="light blue",font=("Courier",15))
    head.place(x=20,y=195)
    head=tk.Label(registerpage,text='PASSWORD-',fg="black",bg="light blue",font=("Courier",15))
    head.place(x=20,y=255)
    head=tk.Label(registerpage,text='RE-ENTER PASSWORD-',fg="black",bg="light blue",font=("Courier",15))
    head.place(x=20,y=315)

    btn = tk.Button(f15, text = 'REGISTER', command =func, fg = "White" ,bg="Black", width="25",activebackground="gray")
    btn.place(x=40,y=400)
    btn = tk.Button(f15, text = 'CLEAR', command =clearfunc, fg = "White" ,bg="Black", width="25",activebackground="gray")
    btn.place(x=270,y=400)
    btn = tk.Button(f15, text = 'QUIT', command =quitpage, fg = "White" ,bg="Black", width="25",activebackground="gray")
    btn.place(x=155,y=450)
    
    name=tk.Entry(f15,text="",width=35)
    name.place(x=280,y=140)
    username=tk.Entry(f15,text="",width=35)
    username.place(x=280,y=200)
    password=tk.Entry(f15,text="",width=35)
    password.place(x=280,y=260)
    repassword=tk.Entry(f15,text="",width=35)
    repassword.place(x=280,y=320)
    
    btn = tk.Button(f15, text = '<BACK TO LOGIN', command = gotologin, fg = "White" ,bg="Black", width="15")
    btn.place(x=20,y=15)

    registerpage.mainloop()


def login_page():
    def gotohomepage():
        loginpage.destroy()
        homepage()
        
    def incorrectpassword():
        loginpage.destroy()
        incorrect_pass()
    def incorrect_pass():
        def back():
            incorrectpass.destroy()
            login_page()
        incorrectpass=tk.Tk()
        incorrectpass.geometry("325x200")
        f15=tk.Canvas(bg="light blue",height=2190,width=1520).grid()
        incorrectpass.title("INCORRECT PASSWORD!!")

        head=tk.Label(incorrectpass,text='INCORRECT PASSWORD!!!',fg="black",bg="light blue",font=("Courier",10))
        head.place(x=20,y=65)
        btn = tk.Button(f15, text = 'OKAY', command = back, fg = "White" ,bg="Black", width="15")
        btn.place(x=100,y=105)
    
    def func():
        
        usernameval=username.get()
        passwordval=password.get()
    
        if usernameval and passwordval:    
            db=mysql.connector.MySQLConnection(
                host="127.0.0.1",
                user="root",
                passwd="Nith@2002",
                database="game",
                charset="utf8")
            mycursor=db.cursor()
            sql="Select username,password from gametable"
            mycursor.execute(sql)
            username_found=False
            for i in mycursor.fetchall():
                if(i[0]==usernameval):
                    username_found=True
                    if(i[1]==passwordval):
                        gotohomepage()
                        break
                    else:
                        incorrectpassword()
                        break
            if(username_found==False):
                disp="YOU HAVEN'T REGISTERED... PLEASE REGISTER!!!"
                head=tk.Label(loginpage,text=disp,fg="black",bg="light blue",font=("Courier",10))
                head.place(x=20,y=575)
        else:
            disp="FEILD(S) EMPTY!!!"
            head=tk.Label(loginpage,text=disp,fg="black",bg="light blue",font=("Courier",10))
            head.place(x=20,y=575)


        

    def quitpage():
        loginpage.destroy()
        pygame.mixer.music.stop()
    def gotoregister():
        loginpage.destroy()
        register_page()
    def clearfunc():
        namecon=username.get()
        len1=len(namecon)
        username.delete(0,len1)

        namecon=password.get()
        len1=len(namecon)
        password.delete(0,len1)
        
    
    loginpage=tk.Tk()
    loginpage.geometry("500x600")
    f15=tk.Canvas(bg="light blue",height=2190,width=1520).grid()

    loginpage.title("LOGIN PAGE")
    head=tk.Label(loginpage,text='LOGIN',fg="black",bg="light blue",font=("Helvetica",20,"bold"))
    head.place(x=200,y=25)

    head=tk.Label(loginpage,text='USERNAME-',fg="black",bg="light blue",font=("Courier",15))
    head.place(x=85,y=300)
    head=tk.Label(loginpage,text='PASSWORD-',fg="black",bg="light blue",font=("Courier",15))
    head.place(x=85,y=360)

    btn = tk.Button(f15, text = 'login', command =func, fg = "White" ,bg="Black", width="25",activebackground="gray")
    btn.place(x=50,y=425)
    btn = tk.Button(f15, text = 'CLEAR', command =clearfunc, fg = "White" ,bg="Black", width="25",activebackground="gray")
    btn.place(x=280,y=425)
    btn = tk.Button(f15, text = 'REGISTER', command =gotoregister, fg = "White" ,bg="Black", width="25",activebackground="gray")
    btn.place(x=163,y=485)
    btn = tk.Button(f15, text = 'QUIT', command =quitpage, fg = "White" ,bg="Black", width="25",activebackground="gray")
    btn.place(x=163,y=540)

    username=tk.Entry(f15,text="",width=35)
    username.place(x=240,y=305)
    password=tk.Entry(f15,text="",width=35)
    password.place(x=240,y=365)

    bgg15=Image.open("logo.png")
    resized=bgg15.resize((375,225),Image.ANTIALIAS)
    new_pic=ImageTk.PhotoImage(resized)
    bg15=tk.Label(f15,bg='black',image=new_pic)
    bg15.place(x=65,y=25)

    loginpage.mainloop()
login_page()














