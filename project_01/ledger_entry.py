from linked_deque import LinkedDeque
from stock_purchase import StockPurchase
## TODO: Fill in the LedgerEntry class methods
class LedgerEntry:
    def __init__(self, stock_symbol):
        self.stock_symbol = stock_symbol
        self.purchases = LinkedDeque()

    def add_purchase(self, new_purchase):
        self.purchases.add_to_back(new_purchase)

    def remove_purchase(self):
        return self.purchases.remove_front()

    def equals(self, other):
        return self.stock_symbol == other
    
    def display_entry(self):
        tally = self.purchases.display()
        display_string = self.stock_symbol + ": "
        for price_info in tally:
            display_string += f"${(price_info[0].cost_per_share):.2f} ({price_info[1]} shares), "
        display_string = display_string[:-2] + "\n"
        return display_string