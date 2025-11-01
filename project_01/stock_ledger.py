from stock_purchase import StockPurchase
from ledger_entry import LedgerEntry

class StockLedger:
    def __init__(self):
        self.ledger_list = []
    
    def buy(self, stock_symbol, shares_bought, price_per_share):
        target_entry = None
        contains_stock_symbol = False
        for entry in self.ledger_list:
            if entry.equals(stock_symbol):
                contains_stock_symbol = True
                target_entry = entry
                break
        if not contains_stock_symbol:
            target_entry = LedgerEntry(stock_symbol)
            self.ledger_list.append(target_entry)
        for _ in range(shares_bought):
            purchase = StockPurchase(stock_symbol, price_per_share)
            target_entry.add_purchase(purchase)

## TODO: Fix the sell method
    def sell(self, stock_symbol, shares_sold, price_per_share):
        total_purchace_price = 0.0
        total_sale_price = shares_sold * price_per_share
        for entry in self.ledger_list:
            if entry.equals(stock_symbol):
                for _ in range(shares_sold):
                    purchase = entry.remove_purchase()
                    if purchase is not None:
                        total_purchace_price += purchase.cost_per_share
                return str(f"Net prefit of sale : ${total_sale_price - total_purchace_price:.2f}\n")

    def display_ledger(self):
        display_string = "---- Stock Ledger ----\n"
        for entry in self.ledger_list:
            display_string += entry.display_entry()
        return display_string
    
    def contains(self, stock_symbol):
        for entry in self.ledger_list:
            if len(self.ledger_list) > 0 and entry.equals(stock_symbol):
                return True
        return False
    
    def get_entry(self, stock_symbol):
        for entry in self.ledger_list:
            if entry.equals(stock_symbol):
                return entry
        return None