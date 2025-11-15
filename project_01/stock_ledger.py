# This class represents a stock ledger that tracks stock purchases and sales

from stock_purchase import StockPurchase
from ledger_entry import LedgerEntry

class StockLedger:
    # Constructor initializes an empty stock ledger
    def __init__(self):
        self._ledger_list = []
    
    # Buys shares of a stock at a given price and adds them to the ledger
    def buy(self, stock_symbol, shares_bought, price_per_share):
        target_entry = self.get_entry(stock_symbol)    # Calls helper function to find stock if it exists
        if target_entry is None:                        # Adds stock to ledger if not found 
            target_entry = LedgerEntry(stock_symbol)
            self._ledger_list.append(target_entry)
        for _ in range(shares_bought):                  # Iterates to add each share purchase
            purchase = StockPurchase(stock_symbol, price_per_share)
            target_entry.add_purchase(purchase)

    # Stores new stocks in ledger based on their cost relative to the average of the stock in the ledger
    def buy_optimal(self, stock_symbol, shares_bought, price_per_share):
        target_entry = self.get_entry(stock_symbol)
        if target_entry is None:
            target_entry = LedgerEntry(stock_symbol)
            self._ledger_list.append(target_entry)
        if price_per_share < target_entry.average_cost():   # Buys at front if price is lowwer than average
            for _ in range(shares_bought):
                purchase = StockPurchase(stock_symbol, price_per_share)
                target_entry.add_purchase_front(purchase)
        else:
            for _ in range(shares_bought):
                purchase = StockPurchase(stock_symbol, price_per_share)
                target_entry.add_purchase(purchase)

    # Sells shares of a stock and returns the net profit of the sale
    def sell(self, stock_symbol, shares_sold, price_per_share):
        total_purchace_price = 0.0
        total_sale_price = shares_sold * price_per_share
        sale_target = self.get_entry(stock_symbol)     # Calls helper function to find stock if it exists
        if sale_target is not None:                     # Checks that stock exists in ledger before selling
            for _ in range(shares_sold):
                purchase = sale_target.remove_purchase() # By default, sells from front (FIFO)
                if purchase is not None:
                    total_purchace_price += purchase.cost_per_share # tracks total cost of sold shares
            return str(f"Net prefit of sale : ${total_sale_price - total_purchace_price:.2f}\n")

    # Checks whether to sell from front or back based on cost to maximize profit
    def sell_optimal(self, stock_symbol, shares_sold, price_per_share):
        total_purchace_price = 0.0
        total_sale_price = shares_sold * price_per_share
        sale_target = self.get_entry(stock_symbol)
        if sale_target is not None:
            for _ in range(shares_sold):
                if sale_target.front_is_lower():    # Sells from back if front cost is lower to maximize profit
                    purchase = sale_target.remove_purchase()
                else:
                    purchase = sale_target.remove_purchase_back()
                if purchase is not None:
                    total_purchace_price += purchase.cost_per_share
            return str(f"Net prefit of sale : ${total_sale_price - total_purchace_price:.2f}\n")

    # Displays the entire stock ledger as a formatted string
    def display_ledger(self):
        display_string = "---- Stock Ledger ----\n"
        for entry in self._ledger_list:
            display_string += entry.display_entry()
        return display_string
    
    # Checks the ledeger to see if it contains a specific stock symbol
    def contains(self, stock_symbol):
        for entry in self._ledger_list:
            if entry.equals(stock_symbol):
                return True
        return False
    
    # Similar to contains(), but returns the ledger enttry if found, else None
    def get_entry(self, stock_symbol):
        for entry in self._ledger_list:
            if entry.equals(stock_symbol):
                return entry
        return None
