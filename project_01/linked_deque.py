# LinkedDeque and sub-class DLNode. The linked deque is a double-ended queue using doubly linked nodes.
# Insertion and removal of nodes can be done at both the front and back of the deque, though still not 
# from the middle.
class LinkedDeque:
    # Constructor for linked deque
    def __init__(self):
        self._front = None
        self._back = None
        self._size = 0

    # Adds new entry to back of deque
    def add_to_back(self, new_entry):
        new_node = DLNode(_previous_node=self._back, data_portion=new_entry, next_node=None)
        if self.is_empty():             # If deque is empty, adds new node to front
            self._front = new_node
        else:
            self._back.set_next_node(new_node)  # If deque not empty, links old back node to new node
        self._back = new_node                   # and sets new node as back of deque
        self._size += 1                         # Increases size of deque by 1

    # Adds new entry to front of deque
    def add_to_front(self, new_entry):
        new_node = DLNode(_previous_node=None, data_portion=new_entry, next_node=self._front)
        if self.is_empty():                         # If deque is empty, sets new node as back  
            self._back = new_node
        else:
            self._front.set_previous_node(new_node) # If deque not empty, links old front node to new node
        self._front = new_node                      # and sets new node as front of deque
        self._size += 1                             # Increases size of deque by 1
    
    # Returns data from back of deque
    def get_back(self):
        if self.is_empty():     # Checks if deque is empty before attempting to get data
            return None
        return self._back.get_data()
    
    # Returns data from front of deque
    def get_front(self):
        if self.is_empty():     # Checks if deque is empty before attempting to get data
            return None
        return self._front.get_data()
    
    # Removes and returns data from front of deque
    def remove_front(self):
        if self.is_empty():     # Checks if deque is empty before attempting to remove data
            return None
        # reassigns pointers and returns data
        old_front = self._front
        self._front = old_front.get_next_node()
        if self._front is None:
            self._back = None
        else:
            self._front.set_previous_node(None)
        self._size -= 1         # Decreases size of deque by 1
        return old_front.get_data()
    
    # Removes and returns data from back of deque
    def remove_back(self):
        if self.is_empty():     # Checks if deque is empty before attempting to remove data
            return None
        # reassigns pointers and returns data
        old_back = self._back
        self._back = old_back.get_previous_node()
        if self._back is None:
            self._front = None
        else:
            self._back.set_next_node(None)
        self._size -= 1         # Decreases size of deque by 1
        return old_back.get_data()
    
    # Sets pointers to None and size to 0, effectively clearing the deque
    def clear(self):
        self._front = None
        self._back = None
        self._size = 0

    # Returns boolean indicating if deque is empty
    def is_empty(self):
        return self._size == 0
    
    # Returns a list of tuples representing the data in the deque and their counts
    def display(self):
        current_node = self._front  # Starts at front of deque
        display = []                # List to hold tuples of (data, count)
        while current_node is not None:
            this_data = current_node.get_data()
            found_index = -1        # Index of data in display list, defaulting to -1 if not found
            # Iterates through display list to check if data already exists
            for i, (_data, count) in enumerate(display):
                if _data.cost_per_share == this_data.cost_per_share:
                    found_index = i
                    break           # Breaks loop if data is found
            # If data is found, increments count; if not, appends new tuple to list
            if found_index != -1:
                display[found_index] = (this_data, display[found_index][1] + 1)
            else:
                display.append((this_data, 1))
 
            current_node = current_node.get_next_node()
        return display              # Returns list of tuples indicating unique values and their counts

        


class DLNode:
    # Constructor for doubly linked node
    def __init__(self, _previous_node=None, data_portion=None, next_node=None):
        self._previous = _previous_node
        self._data = data_portion
        self._next = next_node
    
    # Returns data from node
    def get_data(self):
        return self._data
    
    # Sets or changes data for node
    def set_data(self, new_data):
        self._data = new_data
    
    # Returns next node
    def get_next_node(self):
        return self._next
    
    # Sets pointer to next node
    def set_next_node(self, next_node):
        self._next = next_node

    # Returns previous node
    def get_previous_node(self):
        return self._previous
    
    # Sets pointer to previous node
    def set_previous_node(self, _previous_node):
        self._previous = _previous_node