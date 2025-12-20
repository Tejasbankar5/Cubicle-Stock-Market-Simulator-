📈 Cubicle – Stock Market Simulator

Cubicle is a Python Tkinter–based stock trading simulation game where players can practice buying and selling virtual stocks, experience price fluctuations, learn risk management, and try to maximize profit within a limited number of days.
The system also stores player results in a MySQL database.

🎮 Features

🎯 Starting balance of $1000

⏳ User selects number of gameplay days

💹 Random stock price fluctuations daily

🛒 Buy & Sell real-world inspired stocks (Bitcoin, Apple, Tesla, Google, etc.)

📊 Track inventory and profits

⚠️ Warnings & confirmations to prevent mistakes

🏁 Final acknowledgement screen with results & learning outcomes

🗄 Saves Player Name, Days Played & Final Money to MySQL

🛠 Tech Stack

Python

Tkinter – GUI

Pillow – Image Support

MySQL – Result Storage

Random Module – Price Variations

📂 Database

Stores:

Player Name

Days Played

Final Money

Table example:

person(Name, Days, Money)

▶️ How to Run

1️⃣ Install required packages

pip install pillow mysql-connector-python


2️⃣ Configure your MySQL credentials in code:

host='localhost'
user='root'
password='yourpassword'
database='mms'


3️⃣ Run the program

python main.py

🔮 Future Enhancements

Live stock price API

Leaderboard

Graph analytics

Difficulty modes

Sound and animation effects
