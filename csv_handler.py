import pandas as pd

def csv_formator():
    roth = pd.read_csv("roth_read.csv")
    broke = pd.read_csv("brokerage.csv")

    roth = roth[["Account Name","Symbol", "Quantity", "Average Cost Basis", "Cost Basis Total" ]].dropna()
    roth['Average Cost Basis'] = roth['Average Cost Basis'].str.replace('$', '').astype(float)
    roth['Cost Basis Total'] = roth['Cost Basis Total'].str.replace('$', '').astype(float)

    broke = broke[["Account Name","Symbol", "Quantity", "Average Cost Basis", "Cost Basis Total" ]].dropna()
    broke['Average Cost Basis'] = broke['Average Cost Basis'].str.replace('$', '').astype(float)
    broke['Cost Basis Total'] = broke['Cost Basis Total'].str.replace('$', '').astype(float)

    port = pd.concat([broke,roth], ignore_index=True)

    
    print(port)

    return port.to_csv(f"./data/portfolio.csv", index=False)


if __name__ == "__main__": 
    csv_formator()