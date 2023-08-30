import requests
import matplotlib.pyplot as plt

api_key = open('api_key.txt', 'r').read()

ticker = input("Please enter a ticker symbol: ").upper()
years = int(input("Please enter desired range in years: "))

income_statement = requests.get(f"https://financialmodelingprep.com/api/v3/income-statement/{ticker}?Limit={years}&apikey={api_key}")
income_statement = income_statement.json()

revenues = list(reversed([income_statement[i]['revenue'] for i in range(len(income_statement))]))
profits = list(reversed([income_statement[i]['grossProfit'] for i in range(len(income_statement))]))

plt.plot(revenues, label="Revenue")
plt.plot(profits, label="Profit")
plt.title(f"${ticker} Revenue & Profit")
plt.legend(loc="upper left")
plt.show()

if __name__ == "__main__":
    data = end_of_day()
    print(data.to_string())