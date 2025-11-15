# This class represents a ledger entry for a specific stock symbol. There will likely be multiple
# purchases associated with each ledger entry, and multiple ledger entries in a stock ledger

from linked_deque import LinkedDeque
from stock_purchase import StockPurchase
class LedgerEntry:
    # Constructor initializes a ledger entry for a specific stock symbol
    def __init__(self, stock_symbol):
        self.stock_symbol = stock_symbol
        self.purchases = LinkedDeque()
        

    # Methods to add and remove stock purchases from the front (default) or back of the ledger entry
    def add_purchase(self, new_purchase):
        self.purchases.add_to_back(new_purchase)

    def add_purchase_front(self, new_purchase):
        self.purchases.add_to_front(new_purchase)

    def remove_purchase(self):
        return self.purchases.remove_front()
    
    def remove_purchase_back(self):
        return self.purchases.remove_back()
    

    # Method to check if the ledger entry matches a given stock symbol
    def equals(self, other):
        return self.stock_symbol == other
    
    # Method to display the ledger entry's stock symbol and purchase details
    def display_entry(self):
        if self.purchases.is_empty():
            return f"{self.stock_symbol}: No shares owned\n"
        tally = self.purchases.display()
        display_string = self.stock_symbol + ": "
        for price_info in tally:        # iterates through list to fill return string
            display_string += f"${(price_info[0].cost_per_share):.2f} ({price_info[1]} shares), "
        display_string = display_string[:-2] + "\n"
        return display_string
    
    # Helper method to calculate and return the average cost per share of all purchases in the ledger entry,
    # adding all costs per share and dividing by the total number of shares
    def average_cost(self):
        tally = self.purchases.display()
        total_cost = 0.0
        total_shares = 0
        for price_info in tally:
            total_cost += price_info[0].cost_per_share * price_info[1]
            total_shares += price_info[1]
        if total_shares == 0:
            return 0.0
        return total_cost / total_shares
    
    # Helper method to determine the relative costs per share of the front and back purchases
    def front_is_lower(self):
        return self.purchases.get_front().cost_per_share < self.purchases.get_back().cost_per_share