# 📈 Cubicle – Stock Market Simulator

Cubicle is a **Python Tkinter–based stock market simulation game** where users can experience real-like trading using virtual money. Players buy and sell stocks, face random price fluctuations, manage risk, and try to maximize profit within a limited number of days.
The application also stores player results in a **MySQL database**.

---

## 🎮 Features

* 💰 Starting balance: **$1000**
* ⏳ User-defined gameplay duration (Days)
* 💹 Random stock price changes every day
* 🛒 Buy & Sell multiple popular stocks
* 📊 Inventory management with live updates
* ⚠️ Smart alerts (warnings & confirmations)
* 🏁 Final performance summary + achievements screen
* 🗄 Stores player data in MySQL:

  * Player Name
  * Days Played
  * Final Money

---

## 🛠 Tech Stack

* **Python**
* **Tkinter** – GUI
* **Pillow** – Images
* **MySQL** – Data storage
* **Random Module** – Stock price variation

---

## 📁 Project Flow

1️⃣ User enters **Name** and **Days to Play**
2️⃣ Reads instructions
3️⃣ Starts simulator
4️⃣ Each day:

* Stock prices refresh
* Player buys/sells
* Balance & inventory update

5️⃣ Game ends → Final summary shown
6️⃣ Results saved to database

---

## 🗄 Database Requirement

Create a database (example):

```
database name: mms
table: person(Name, Days, Money)
```

---

## ▶️ How to Run

### Install Dependencies

```
pip install pillow mysql-connector-python
```

### Configure MySQL

Update in code:

```
host='localhost'
user='root'
password='your_password'
database='mms'
```

### Run Program

```
python main.py
```

---

## 🔮 Future Enhancements

* Live stock market API integration
* Leaderboard
* Graph analytics
* Difficulty levels
* Sound effects & animations

---

## 🙌 Credits

Developed as a stock trading learning simulator to help users understand:
Investment Strategies, Risk vs Reward, Budget Management, Market Volatility, and Economic Literacy.

---

