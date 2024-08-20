from tkinter import *
import random
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
simulator_window = None
class Main(Frame):
    def __init__(self, master, days):
        super().__init__(master, bg="#1C1C1C") 
       
        self.grid(sticky=N + S + E + W)
        self.days = int(days) + 1
        self.money = 1000
        self.normFont = ("Cambria", 16)
        self.createWidgets()
        self.updateDay()

    def createWidgets(self):
        self.tFrame = Frame(self, bg="white")
        self.tFrame.grid(columnspan=2, sticky=N, pady=15)
        self.title = Label(self.tFrame, text="CUBICLE: The Trading Simulator", font=("Cambria", 24, "bold"), bg="white", fg="#1C1C1C")
        self.title.grid(sticky=W + E, padx=20, pady=10)
        self.mLabel = Label(self.tFrame, text=f"Your money: {self.money}", font=self.normFont, bg="white", fg="#1C1C1C")
        self.mLabel.grid(padx=2)
        self.daysLabel = Label(self.tFrame, font=self.normFont, bg="white", fg="#1C1C1C")
        self.daysLabel.grid()
        self.nextDay = Button(self.tFrame, text="Next Day", command=self.updateDay, font=("Cambria", 16, "bold"), bg="#1C1C1C", fg="white")
        self.nextDay.grid(pady=8)
        self.menu = BuyMenu(self)
        self.menu.grid(row=2, column=0, pady=15, sticky=E + W + N + S)
        self.inv = Inventory(self)
        self.inv.grid(row=2, column=1, pady=15, sticky=E + W + N + S)

    def updateDay(self):
        self.days -= 1
        if self.days == 5:
            messagebox.showwarning("Message", "You have 5 days left!")
        elif self.days == 0:
            
             messagebox.showinfo("Congratulations!", f"You completed the stock broker dealer challenge with {self.money} dollars")
             mydb = mysql.connector.connect(
       host='localhost',
     port=3306,
     user='root',
     password='root@123',
     database='mms')
             cursor = mydb.cursor()
             name=namev.get()
             days=Daysv.get()

             cursor.execute('insert into person(Name, Days,Money) values (%s, %s, %s)',
            (name, days,self.money))
             mydb.commit()
             
             self.acknowldge()
             self.deactivate()
            

        self.daysLabel['text'] = f"Days Left: {self.days}"
        self.menu.updatePrices()

    def purchase(self, stockI, amount, cost):
        self.inv.userInv[stockI] += amount
        self.money -= cost
        self.mLabel['text'] = f"Your money: {self.money}"
        self.inv.amounts.delete(stockI)

        self.inv.amounts.insert(stockI, self.inv.userInv[stockI])


    def sell(self, stockI, amount):
        cost = self.menu.prices[stockI] * amount
        self.money += cost
        self.mLabel['text'] = f"Your money: {self.money}"

    def deactivate(self):
        self.menu.buy['state'] = DISABLED
        self.inv.sell['state'] = DISABLED
        self.nextDay['state'] = DISABLED

    def acknowldge(self):
        
        self.ap=Toplevel()
        self.ap.geometry('900x600')
        self.ap.title('Acknowledgement')
        self.a1=Image.open('1393720.jpg').resize((900,600))
        self.a2=ImageTk.PhotoImage(self.a1)
       
        
        Label(self.ap,image=self.a2,background='white').place(x=0,y=0)
        Label(self.ap,text='Congratualtions You SuccesFully Completed Challenge',font='cambria 23 ',background='black',foreground='white').pack(pady=20)
        Label(self.ap,text=f'your money : {self.money}.',font='cambria 16 ',background='black',foreground='white').pack(pady=20)
        Label(self.ap,text='Outcomes::',font='cambria 16 ',background='black',foreground='white').pack(pady=5)
        Label(self.ap,text='Investment Strategies, Risk And Reward,Budget Management,',font='cambria 16 ',background='black',foreground='white').pack(pady=5)
        Label(self.ap,text='Market Volatility, Economic Litracy ',font='cambria 16 ',background='black',foreground='white').pack(pady=5)
        Label(self.ap,text="Thanks for Visiting Us Visit Again!",font='cambria 16 ',background='black',foreground='white').pack(pady=(10,5))
        Label(self.ap,text='Mail us on tejasbankar58@gmail.com',font='cambria 16 ',background='black',foreground='white').pack(pady=5)
    
 

class BuyMenu(Frame):
    def __init__(self, master):
        super().__init__(master, bg="white")
        self.master = master
        self.grid(padx=50)
        self.stockList = ["Bitcoin", "Apple", "Microsoft", "Tesla", "Google", "Facebook", "Snapchat", "Amazon"]
        self.createWidgets()

    def createWidgets(self):
        self.menuFont = ("Cambria", 13)
        self.menuTitle = Label(self, text="TODAY'S MENU", font=("Cambria", 15, "underline"), bg="white", fg="black")
        self.menuTitle.grid(row=0, column=0)
        self.stockMenu = Listbox(self, height=8, selectmode=SINGLE, activestyle="none", font=self.menuFont, width=19, bg="white", fg="black")
        self.stockMenu.grid(row=1, column=0, padx=5, pady=(12, 12))
        for d in self.stockList:
            self.stockMenu.insert(END, d)
        self.pTitle = Label(self, text="PRICES", font=("Cambria", 15, "underline"), bg="white", fg="black")
        self.pTitle.grid(row=0, column=1)
        self.priceList = Listbox(self, activestyle="none", height=8, selectbackground="#ffffff", selectforeground="black", takefocus=0, font=self.menuFont, width=10, bg="white", fg="black")
        self.priceList.grid(row=1, column=1, pady=(12, 12))
        self.buy = Button(self, text="Buy it!", command=self.buystocks, font='Cambria 17', bg="#1C1C1C", fg="white")
        self.buy.grid(row=2, column=0, columnspan=2)

    def updatePrices(self):
        self.prices = self.generatePrices()
        self.priceList.delete(0, END)
        for price in self.prices:
            self.priceList.insert(END, price)

    def generatePrices(self):
        return [random.randint(200, 700), random.randint(400, 1000), random.randint(2013, 7692),
                random.randint(10234, 18290), random.randint(3500, 7690), random.randint(567, 1403),
                random.randint(3251, 7882), random.randint(67, 315)]

    def buystocks(self):
        stockI = self.stockMenu.curselection()#return indices
        if not stockI:
            messagebox.showwarning("Error", "Please select a stock to buy")
            return
        stockI = stockI[0]
        stock = self.stockList[stockI]
        stockPrice = self.prices[stockI]
        w = PopupInput(self.master, money=self.master.money, stock=stock, stockPrice=stockPrice, buy=True)
        self.master.wait_window(w.top)
        amount = w.amount
        cost = amount * stockPrice
        self.master.purchase(stockI, amount, cost)

class Inventory(Frame):
    def __init__(self, master):
        super().__init__(master, bg="white")
        self.grid(padx=50)
        self.stockList = ["Bitcoin", "Apple", "Microsoft", "Tesla", "Google", "Facebook", "Snapchat", "Amazon"]
        self.userInv = [0 for _ in range(8)]
        self.menuFont = ("Cambria", 13)
        self.createWidgets()

    def createWidgets(self):
        Label(self, text="Your Inventory", font=("Cambria", 15, "underline")).grid()
        self.inventory = Listbox(self, height=0, font=self.menuFont, width=18, activestyle="none")
        self.inventory.grid(row=1, column=0, padx=5, pady=(12, 12))
        for stock in self.stockList:
            self.inventory.insert(END, stock)
        Label(self, text="Amounts", font=("Cambria", 15, "underline")).grid(row=0, column=1)
        self.amounts = Listbox(self, height=0, font=self.menuFont, width=10, activestyle='none', selectbackground="#ffffff", selectforeground="black")
        self.amounts.grid(row=1, column=1, pady=(12, 12))
        for _ in range(8):
            self.amounts.insert(END, 0)
        self.sell = Button(self, text="Sell it!", command=self.sellstocks, font='cambria 17', bg='#1c1c1c', fg='white')
        self.sell.grid(row=2, column=0, columnspan=2)

    def sellstocks(self):
        stockI = self.inventory.curselection()
        if not stockI:
            messagebox.showerror("Error", "Please select a stock to sell")
            return
        stockI = stockI[0]
        stock = self.stockList[stockI]
        w = PopupInput(self.master, self.master.money, stock, self.master.menu.prices[stockI], buy=False, stockI=stockI)
        self.master.wait_window(w.top)
        numSell = w.amount
        self.master.sell(stockI, numSell)
        self.userInv[stockI] -= numSell
        self.amounts.delete(stockI)
        self.amounts.insert(stockI, self.userInv[stockI])

class PopupInput(Frame):
    def __init__(self, master, money, stock, stockPrice, buy=True, stockI=None):
        super().__init__(master)
        self.grid()
        self.master = master
        okayCommand = (self.register(self.isOkay), "%S")
        self.stockI = stockI
        self.money = money
        self.stock = stock
        self.stockPrice = stockPrice
        self.defFont = ("Cambria", 15)
        self.bOrS = "buy" if buy else "sell"
        self.top = Toplevel(master)
        self.howMuch = Label(self.top, text=f"How much {stock} stock would you like to {self.bOrS}?", font=self.defFont)
        self.howMuch.grid(padx=20, pady=(5, 0), columnspan=2)
        self.userInp = Entry(self.top, font=self.defFont, validate='key', validatecommand=okayCommand)
        self.userInp.grid(columnspan=2)
        if buy:
            self.userInp.insert(0, money // stockPrice)
        elif not buy:
            self.userInp.insert(0, self.master.inv.userInv[stockI])
        self.ok = Button(self.top, text="Ok", font=self.defFont, command=self.confirmOrder)
        self.ok.grid(ipadx=25)
        self.cancel = Button(self.top, text="Cancel", font=self.defFont, command=self.top.destroy)
        self.cancel.grid(row=2, column=1)

    def confirmOrder(self):
        if self.bOrS == "buy":
            if int(self.userInp.get()) * self.stockPrice > self.master.money:
                messagebox.showerror("Error!", f"You do not have enough money to buy that much {self.stock} stock")
            else:
                self.amount = int(self.userInp.get())
                if messagebox.askokcancel("Are you sure?", f"Do you want to buy {self.amount} {self.stock} stock for {self.amount * self.stockPrice} dollars?"):
                    self.top.destroy()
        elif self.bOrS == "sell":
            if int(self.userInp.get()) > self.master.inv.userInv[self.stockI]:
                messagebox.showerror("Error", f"You do not have that much of {self.stock} stock")
            else:
                self.amount = int(self.userInp.get())
                if messagebox.askokcancel("Are you sure?", f"Do you want to sell {self.amount} {self.stock} stock for {self.amount * self.stockPrice} dollars?"):
                    self.top.destroy()

    def isOkay(self, what):
        try:
            int(what)
            return True
        except:
            self.bell()
            return False

def funcw():
    global next
    next = Toplevel()
    next.configure(bg='black')
    next.title('INSTRUCTIONS')
    next.geometry('700x650')
    headle = Label(next, text=' Welcome to the Cubicle Stock Market Simulator!', font='cambria 23 italic', background='black', foreground='white')
    headle.pack()
    Label(next, text='This is a trading simulation game where you can buy and sell stocks.', font='cambria 15 italic', background='black', foreground='white').pack(pady=20)
    Label(next, text='Instructions:', font='cambria 23 italic', background='black', foreground='white').pack(pady=10)
    Label(next, text='1. You have a starting budget of $1000.', font='cambria 15 italic', background='black', foreground='white').pack(pady=20)
    Label(next, text='2. You can trade stocks on a daily basis.', font='cambria 15 italic', background='black', foreground='white').pack(pady=20)
    Label(next, text='3. The stock prices will change randomly each day.', font='cambria 15 italic', background='black', foreground='white').pack(pady=20)
    Label(next, text='4. You can buy or sell stocks from the available list.', font='cambria 15 italic', background='black', foreground='white').pack(pady=20)
    Label(next, text='5. Try to maximize your profit over the given number of days.', font='cambria 15 italic', background='black', foreground='white').pack(pady=20)
    Label(next, text='  Have fun trading! ', background='black', foreground='white', font='cambria 15 italic').pack()
    am = Button(next, text='continue', width=15, background='white', foreground='black', font='cambria 17', command=continue_to_simulator)
    am.pack(pady=10)
def continue_to_simulator():
    global simulator_window
    if simulator_window is None:
        days_entry = Dayentry.get()
        simulator_window = Tk()
        simulator_window.configure(bg='black')
        simulator_window.title("Simulator")
       # simulator_window.geometry('800x600')
        simulator_window.resizable(width=False, height=False)
        simulator = Main(simulator_window, days_entry)
        simulator_window.mainloop()
        root.destroy()
        next.destroy()
root = Tk()
root.title("Simulator")
root.geometry('800x600')
root.resizable(width=False, height=False)
logoT = Image.open('stc3.jpg').resize((850, 600))
imgtk = ImageTk.PhotoImage(logoT)
Label(root, image=imgtk, bg='white').place(x=0, y=0)
logom = Image.open('stc.jpeg').resize((200, 200))
imgtm = ImageTk.PhotoImage(logom)
Label(root, image=imgtm, bg='white').place(x=40, y=180)
title = Label(root, text='CUBICLE STOCK MARKET SIMULATOR', font='CAMBRIA 22 bold', foreground='white', background='black')
title.pack(pady=10)
frame = Frame(root, bg='white', width='480', height='0', border=2, background='black')
frame.place(x=300, y=90)
namev=StringVar()
name=Label(frame,text='ENTER YOUR NAME',font='CAMBRIA 15 ',foreground='white',background='black')
name.pack(pady=20,padx=70)
nameentry=Entry(frame,font='cambria 15 ',textvariable=namev,foreground='black',background='white')
nameentry.pack(pady=15,padx=70)
Daysv=StringVar()
Day=Label(frame,text='ENTER NO OF DAYS',font='CAMBRIA 15 ',foreground='white',background='black')
Day.pack(pady=20,padx=70)
Dayentry=Entry(frame,font='cambria 15',textvariable=Daysv,foreground='black',background='white')
Dayentry.pack(pady=15,padx=70)
but=Button(frame,text='continue',font='cambria 16',width=10,background='white',command=funcw)
but.pack(pady=30,padx=170)

root.mainloop()