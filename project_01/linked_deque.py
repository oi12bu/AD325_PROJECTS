# LinkedDeque and the sub-class DLNode go here
class LinkedDeque:
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def add_to_back(self, new_entry):
        new_node = DLNode(previous_node=self.back, data_portion=new_entry, next_node=None)
        if self.is_empty():
            self.front = new_node
        else:
            self.back.set_next_node(new_node)
        self.back = new_node
        self.size += 1

    def add_to_front(self, new_entry):
        new_node = DLNode(previous_node=None, data_portion=new_entry, next_node=self.front)
        if self.is_empty():
            self.back = new_node
        else:
            self.front.set_previous_node(new_node)
        self.front = new_node
        self.size += 1
    
    def get_back(self):
        if self.is_empty():
            return None
        return self.back.get_data()
    
    def get_front(self):
        if self.is_empty():
            return None
        return self.front.get_data()
    
    def remove_front(self):
        if self.is_empty():
            return None
        old_front = self.front
        self.front = old_front.get_next_node()
        if self.front is None:
            self.back = None
        else:
            self.front.set_previous_node(None)
        self.size -= 1
        return old_front.get_data()
    
    def remove_back(self):
        if self.is_empty():
            return None
        old_back = self.back
        self.back = old_back.get_previous_node()
        if self.back is None:
            self.front = None
        else:
            self.back.set_next_node(None)
        self.size -= 1
        return old_back.get_data()
    
    def clear(self):
        self.front = None
        self.back = None
        self.size = 0

    def is_empty(self):
        return self.size == 0
    
    def display(self):
        current_node = self.front
        tally = []
        while current_node is not None:
            found_index = -1
            for i, (data, count) in enumerate(tally):
                if data == current_node.get_data():
                    found_index = i
                    break
            if found_index != -1:
                tally[found_index] = (current_node.get_data(), tally[found_index][1] + 1)
            else:
                tally.append((current_node.get_data(), 1))
 
            current_node = current_node.get_next_node()
        return tally

        


class DLNode:
    def __init__(self, previous_node=None, data_portion=None, next_node=None):
        self.previous = previous_node
        self.data = data_portion
        self.next = next_node
    
    def get_data(self):
        return self.data
    
    def set_data(self, new_data):
        self.data = new_data
    
    def get_next_node(self):
        return self.next
    
    def set_next_node(self, next_node):
        self.next = next_node

    def get_previous_node(self):
        return self.previous
    
    def set_previous_node(self, previous_node):
        self.previous = previous_node