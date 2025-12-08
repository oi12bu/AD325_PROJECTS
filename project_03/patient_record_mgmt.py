import binary_search_tree as BST
import csv
import graphviz

class PatientRecord:
    # Initializing a patient record with relevant data
    def __init__(self, patient_id, name, age, diagnosis, blood_pressure, pulse, body_temperature):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        self.blood_pressure = blood_pressure
        self.pulse = pulse
        self.body_temperature = body_temperature

    # Overriding the string representation for easy display
    def __str__(self):
        return (f"Patient ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, "
                f"Diagnosis: {self.diagnosis}, Blood Pressure: {self.blood_pressure}, "
                f"Pulse: {self.pulse}, Body Temperature: {self.body_temperature}")


class PatientRecordManagementSystem:
    # Initializing the patient record management system with a binary search tree
    def __init__(self):
        self.bst = BST.BinarySearchTree()

    # Adding a new patient record to the system
    def add_patient_record(self, patient_id, name, age, diagnosis, blood_pressure, pulse, body_temperature):
        # Creating a new patient record
        record = PatientRecord(patient_id, name, age, diagnosis, blood_pressure, pulse, body_temperature)
        # Creating a new node for the binary search tree with the newly created record
        node = BST.Node(patient_id, record)
        # Adding the new node to the binary search tree
        self.bst.insert(node)

    # Searching for a patient record by patient ID
    def search_patient_record(self, patient_id):
        # Calling the binary search tree's search method
        node = self.bst.search(patient_id)
        # Returning the patient record if found, else None
        if node:
            return node
        else:
            return None
    
    # Removing a patient record by patient ID
    def delete_patient_record(self, patient_id):
        # Calling the binary search tree's remove method
        self.bst.remove(patient_id)
    
    # Displaying all patient records in order
    def display_all_records(self):
        # Using the newly written inorder_traversal method to get all nodes in order
        all_elements = self.bst.inorder_traversal(self.bst.root)
        for element in all_elements:
            record = element.value
            print(f"Patient ID: {record.patient_id}, Name: {record.name}, Age: {record.age}, "
                  f"Diagnosis: {record.diagnosis}, Blood Pressure: {record.blood_pressure}, "
                  f"Pulse: {record.pulse}, Body Temperature: {record.body_temperature}")
            
    def build_tree_from_csv(self, file_path):
        # Reading patient records from a CSV file and adding them to the BST
        # Checking if the file exists and handling exceptions
        try:
            with open(file_path, 'r', newline='') as csvfile:
                # Creating iterator to read CSV file
                csv_reader = csv.reader(csvfile)
                # Skip header row
                next(csv_reader)  
                for row in csv_reader:
                    patient_id = int(row[0])
                    name = row[1]
                    age = int(row[2])
                    diagnosis = row[3]
                    blood_pressure = row[4]
                    pulse = int(row[5])
                    body_temperature = float(row[6])
                    self.add_patient_record(patient_id, name, age, diagnosis, blood_pressure, pulse, body_temperature)
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
        
    # Creating a graphviz digraph to visualize the BST
    def visualize_tree(self):
        dot = graphviz.Digraph()
        self._add_nodes(dot, self.bst.root)
        return dot
    
    # Helper method to add nodes to the graphviz digraph
    def _add_nodes(self, dot, node):
        if node:
            dot.node(str(node.key), f"{node.key}: {node.value.name}")
            if node.left:
                dot.edge(str(node.key), str(node.left.key))
                self._add_nodes(dot, node.left)
            if node.right:
                dot.edge(str(node.key), str(node.right.key))
                self._add_nodes(dot, node.right)
