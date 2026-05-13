# Stock Portfolio Tracker

stock_prices = {
    'AAPL': 150.00,
    'GOOGL': 2800.00,
    'AMZN': 3400.00,
    'MSFT': 300.00
}

print("Available Stocks:")
for stock in stock_prices:
    print(stock)

stock_name = input("\nEnter the stock name: ").upper()
quantity = int(input("Enter the quantity of stocks: "))

if stock_name in stock_prices:
    price = stock_prices[stock_name]
    total_value = price * quantity

    print("\nInvestment Details")
    print("Stock Name:", stock_name)
    print("Price per Share: $", price)
    print("Quantity:", quantity)
    print("Total Investment Value: $", total_value)

else:
    print("Stock not found in portfolio.")