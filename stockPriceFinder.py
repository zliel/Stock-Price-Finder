import robin_stocks as robin
import sys

# TODO - find something else to use instead of a global variable
lists = { "movers": "top-movers", "earnings": "upcoming-earnings", "etf": "etf", "tech": "technology", "top100": "100-most-popular", "finance": "finance"}

def main():
    # Login info -- TODO REMOVE IF YOU EVER GO TO UPLOAD IT TO GITHUB
    email = "Your username here"
    password = "Your password here"
    

    robin.login(email, password)

    # stocksearch search /search_item - Searches for stocks with a given name
    if len(sys.argv) == 3 and sys.argv[1] == "search":
        print(f"Searching for stocks with the name {sys.argv[2]}...")
        stocks = robin.find_instrument_data(sys.argv[2])
        defaultTitle()
        printStocks(stocks)

    elif len(sys.argv) >= 2:
        if sys.argv[1] == "list":
            listFunction()
        else:
            printStockLists(sys.argv[1])
        
        if len(sys.argv) > 2 and sys.argv[2]:
            print(f"Searching for stocks with the name {sys.argv[2]}...")
            stocks = robin.find_instrument_data(sys.argv[2])
            defaultTitle()
            printStocks(stocks)

    else:                         # Defaults to searching for Tesla
        print("Searching for Tesla stock...")
        stocks = robin.find_instrument_data("Tesla")
        defaultTitle()
        printStocks(stocks)

# Default header
def defaultTitle():
    print("\n----------------------")
    print("Stock names and prices")
    print("----------------------\n")

# Prints the stocks' names and prices
def printStocks(stocks):

    for stock in stocks:
        # Displays Stock name and latest price
        print(f'Stock name: {stock["name"]}')
        price = float(robin.get_latest_price(stock['symbol'])[0])
        price = "${:,.2f}".format(price)
        print(f'Price: {price}\n')

# Lists stocks with the provided tags
def printStockLists(listName):
    
    # Break up the dictionary text into an array
    listText = lists[listName].split('-')
    # Join the split array with spaces and make it title case
    listText = " ".join(listText).title()
    
    print(f"Pulling up today's {listText}...")
    search = robin.get_all_stocks_from_market_tag(lists[listName])
    searchResultList = []

    for item in search:
        searchResultList.append(item['symbol'])
    searchResultStocks = robin.get_instruments_by_symbols(searchResultList)
    
    print("\n-----------------------")
    print(f"{listText}".center(22))
    print("-----------------------\n")
    printStocks(searchResultStocks)

# Function lists all available commands
def listFunction():
    print("stocksearch usage: stocksearch COMMAND\n")
    for (cmd, tag) in lists.items():
        print(f"{cmd} - Searches for stocks with the {tag} tag\n")
    
    print("list - Lists all available commands\n")
    print("stocksearch search /search_item - searches for stocks with the entered name\n")


main()
# TODO - (COMPLETE) Make the printing of stocks into a function
# TODO - (75% COMPLETE) Make more possible commands for it
# TODO TODO - (COMPLETE) Maybe make a list command 
# TODO TODO - Something to check different watchlists or something
# TODO BUT NOT IMPORTANT RIGHT NOW - Make commands for trading