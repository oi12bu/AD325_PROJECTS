import binary_search_tree as BST
import csv
import graphviz

class PatientRecord:
    def __init__(self, patient_id, name, age, diagnosis, blood_pressure, pulse, body_temperature):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        self.blood_pressure = blood_pressure
        self.pulse = pulse
        self.body_temperature = body_temperature

    def __str__(self):
        return (f"Patient ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, "
                f"Diagnosis: {self.diagnosis}, Blood Pressure: {self.blood_pressure}, "
                f"Pulse: {self.pulse}, Body Temperature: {self.body_temperature}")


class PatientRecordManagementSystem:
    def __init__(self):
        self.bst = BST.BinarySearchTree()

    def add_patient_record(self, patient_id, name, age, diagnosis, blood_pressure, pulse, body_temperature):
        record = PatientRecord(patient_id, name, age, diagnosis, blood_pressure, pulse, body_temperature)
        node = BST.Node(patient_id, record)
        self.bst.insert(node)

    def search_patient_record(self, patient_id):
        node = self.bst.search(patient_id)
        if node:
            return node
        else:
            return None
    
    def delete_patient_record(self, patient_id):
        self.bst.remove(patient_id)
    
    def display_all_records(self):
        all_elements = self.bst.inorder_traversal(self.bst.root)
        for element in all_elements:
            record = element.value
            print(f"Patient ID: {record.patient_id}, Name: {record.name}, Age: {record.age}, "
                  f"Diagnosis: {record.diagnosis}, Blood Pressure: {record.blood_pressure}, "
                  f"Pulse: {record.pulse}, Body Temperature: {record.body_temperature}")
            
    def build_tree_from_csv(self, file_path):
        try:
            with open(file_path, 'r', newline='') as csvfile:
                csv_reader = csv.reader(csvfile)
                next(csv_reader)  # Skip header row
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
        
    def visualize_tree(self):
        dot = graphviz.Digraph()
        self._add_nodes(dot, self.bst.root)
        return dot
    
    def _add_nodes(self, dot, node):
        if node:
            dot.node(str(node.key), f"{node.key}: {node.value.name}")
            if node.left:
                dot.edge(str(node.key), str(node.left.key))
                self._add_nodes(dot, node.left)
            if node.right:
                dot.edge(str(node.key), str(node.right.key))
                self._add_nodes(dot, node.right)
