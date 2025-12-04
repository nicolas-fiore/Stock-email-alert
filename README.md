# Stock Email Alert

Automatically monitors my stock portfolio from exported csv's from Fidelity

## Description
This project reads my portfolio data from CSV files and formats it using pandas, fetches live stock prices using the `yfinance` API, calculates total cost, current value, and net profit, and sends an email summary to me at 3:59pm every weekday using cron. It helps by not having to log in to Fidelity everyday and use face id to login which takes around 5 seconds(too long)

## Features
- Reads portfolio data from multiple accounts (CSV files)
- Calculates current value, total cost, and unrealized profit/loss
- uses pandas to format and clean dataframe
- Fetches live stock prices using `yfinance`
- Sends daily email alerts with portfolio summary
- Creates a history of my Portfolio everyday as well


## Example Email Output

```text
Portfolio Value
------------------------------------------
SPYM: 
Total Cost Basis: $799.13 
Current Value: $986.90(+$187.77) 
Shares Owned: 12.255 
Average Cost Basis: $65.21
High Today: $80.64
Low Today: $80.18
------------------------------------------
KVUE: 
Total Cost Basis: $100.0 
Current Value: $104.23(+$4.23) 
Shares Owned: 6.133 
Average Cost Basis: $16.31
High Today: $17.19
Low Today: $14.39
```