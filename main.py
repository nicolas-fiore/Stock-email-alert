import yfinance as yf
import pandas as pd
from datetime import date
from email_alert import alert
from csv_handler import csv_formator
import sys, schedule, time

def daily():
        write_file()
        alert()

def csv_reader(): 
    tmp_list = []
    try:
        port = pd.read_csv("./data/portfolio.csv").T
    except FileNotFoundError: 
        sys.exit("File was not found or does not exist")

    for i in range(len(port.columns)): 
        tmp_list.append(port[port.columns[i]].to_list()) 
    return tmp_list


def portfolio_values():
    csv_formator()
    stock_list = csv_reader()
    format_string = []
    
    for i in range(len(stock_list)): 
        symbol, shares, avg_cost, total_cost = stock_list[i][1],stock_list[i][2] ,stock_list[i][3], stock_list[i][4]
        dat = yf.Ticker(symbol)
        dat = dat.fast_info

        net_profit = float(f"{((shares * dat['lastPrice']) - total_cost):.2f}")
        unrealized = f"{(dat['lastPrice'] * shares):.2f}"

        if net_profit > 0: 
            unrealized = f"${unrealized}"
            net_profit = f"+${net_profit}"
        else: 
            unrealized = f"${unrealized}"
            net_profit = f"-${abs(net_profit)}"
        
        
        format_string.append(f"""{symbol}: 
Total Cost Basis: ${total_cost} 
Current Value: {unrealized}({net_profit}) 
Shares Owned: {shares} 
Average Cost Basis: ${avg_cost}
High Today: ${dat['dayHigh']:.2f}
Low Today: ${dat['dayLow']:.2f}
------------------------------------------""")

        print(format_string[i])
        
    
    return format_string


def write_file():
    with open("final.txt", "w") as file: 
        file.write("Portfolio Value\n")
        file.write("------------------------------------------\n")
        for i in portfolio_values(): 
            file.write(f"{i}\n")

    with open("final.txt") as orginal: 
        content = orginal.read()
        with open(f"./history/{date.today()}.txt", "w") as copy: 
            copy.write(content)


def main(): 
    schedule.every().monday.at("15:59:00").do(daily)
    schedule.every().tuesday.at("15:59:00").do(daily)
    schedule.every().wednesday.at("15:59:00").do(daily)
    schedule.every().thursday.at("15:59:00").do(daily)
    schedule.every().friday.at("15:59:00").do(daily)

    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__ == "__main__": 
    main()



# with open("test.html", "w") as file:
#     string = f"""<!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Document</title>
# </head>
# <body>
#     <p style="color:red;">YO</p>
# </body>
# </html>
# """
#     file.write(string)
