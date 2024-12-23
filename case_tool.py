import json
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton,
    QLineEdit, QMessageBox, QTreeWidget, QTreeWidgetItem, QTabWidget, QLabel, QFileDialog
)
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
import sys

class CASETool:
    def __init__(self):
        self.shapes = []
        self.arrows = []
        self.data_dict = {}
        self.shape_counter = 1
        self.arrow_counter = 1

    def draw_shape(self, shape_type, name):
        shape = {"id": self.shape_counter, "type": shape_type, "name": name}
        self.shapes.append(shape)
        self.shape_counter += 1
        return f"{shape_type.capitalize()} '{name}' created."

    def draw_arrow(self, start_id, end_id, data_name):
        if not any(shape['id'] == start_id for shape in self.shapes):
            return "Error: Start shape ID does not exist."
        if not any(shape['id'] == end_id for shape in self.shapes):
            return "Error: End shape ID does not exist."
        arrow = {"arrow_id": self.arrow_counter, "start_id": start_id, "end_id": end_id, "data_name": data_name}
        self.arrows.append(arrow)
        self.data_dict[self.arrow_counter] = data_name
        self.arrow_counter += 1
        return f"Arrow from ID {start_id} to ID {end_id} created."

    def delete_item(self, item_id):
        for shape in self.shapes:
            if shape["id"] == item_id:
                self.shapes.remove(shape)
                return f"Shape ID {item_id} deleted."
        for arrow in self.arrows:
            if arrow["arrow_id"] == item_id:
                self.arrows.remove(arrow)
                del self.data_dict[item_id]
                return f"Arrow ID {item_id} deleted."
        return "Item not found."

    def save_design(self, filename):
        design = {"shapes": self.shapes, "arrows": self.arrows, "data_dict": self.data_dict}
        with open(filename, 'w') as f:
            json.dump(design, f, indent=4)

    def load_design(self, filename):
        with open(filename, 'r') as f:
            design = json.load(f)
        self.shapes = design["shapes"]
        self.arrows = design["arrows"]
        self.data_dict = design["data_dict"]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.case_tool = CASETool()
        self.setWindowTitle("Modern CASE Tool")
        self.setGeometry(300, 100, 800, 600)
        self.setWindowIcon(QIcon("icon.png"))  # Add a custom icon

        # Layouts
        main_layout = QVBoxLayout()
        self.tabs = QTabWidget()
        self.create_tabs()

        # Buttons
        button_layout = QHBoxLayout()
        buttons = [
            ("Add Bubble", self.add_bubble),
            ("Add Data Store", self.add_data_store),
            ("Add Entity", self.add_entity),
            ("Add Arrow", self.add_arrow),
            ("Delete Item", self.delete_item),
            ("Save Design", self.save_design),
            ("Load Design", self.load_design)
        ]
        for text, handler in buttons:
            button = QPushButton(text)
            button.clicked.connect(handler)
            button.setStyleSheet("background-color: #444; color: white; font-weight: bold; padding: 5px;")
            button_layout.addWidget(button)

        # Main Layout Setup
        main_layout.addWidget(self.tabs)
        main_layout.addLayout(button_layout)
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def create_tabs(self):
        self.shapes_tab = QWidget()
        self.arrows_tab = QWidget()

        # Shapes Tab
        layout1 = QVBoxLayout()
        self.shapes_tree = QTreeWidget()
        self.shapes_tree.setHeaderLabels(["Shape ID", "Type", "Name"])
        layout1.addWidget(QLabel("Shapes:"))
        layout1.addWidget(self.shapes_tree)
        self.shapes_tab.setLayout(layout1)

        # Arrows Tab
        layout2 = QVBoxLayout()
        self.arrows_tree = QTreeWidget()
        self.arrows_tree.setHeaderLabels(["Arrow ID", "Start ID", "End ID", "Data Name"])
        layout2.addWidget(QLabel("Arrows:"))
        layout2.addWidget(self.arrows_tree)
        self.arrows_tab.setLayout(layout2)

        # Add Tabs
        self.tabs.addTab(self.shapes_tab, "Shapes")
        self.tabs.addTab(self.arrows_tab, "Arrows")

    def refresh_trees(self):
        self.shapes_tree.clear()
        for shape in self.case_tool.shapes:
            QTreeWidgetItem(self.shapes_tree, [str(shape["id"]), shape["type"], shape["name"]])

        self.arrows_tree.clear()
        for arrow in self.case_tool.arrows:
            QTreeWidgetItem(self.arrows_tree, [
                str(arrow["arrow_id"]), str(arrow["start_id"]),
                str(arrow["end_id"]), self.case_tool.data_dict[arrow["arrow_id"]]
            ])

    # Button Handlers
    def add_bubble(self):
        name, ok = QLineEdit.getText(self, "Add Bubble", "Enter bubble name:")
        if ok and name:
            self.case_tool.draw_shape("bubble", name)
            self.refresh_trees()

    def add_data_store(self):
        name, ok = QLineEdit.getText(self, "Add Data Store", "Enter data store name:")
        if ok and name:
            self.case_tool.draw_shape("data_store", name)
            self.refresh_trees()

    def add_entity(self):
        name, ok = QLineEdit.getText(self, "Add Entity", "Enter entity name:")
        if ok and name:
            self.case_tool.draw_shape("entity", name)
            self.refresh_trees()

    def add_arrow(self):
        try:
            start_id = int(QLineEdit.getText(self, "Add Arrow", "Enter start ID:")[0])
            end_id = int(QLineEdit.getText(self, "Add Arrow", "Enter end ID:")[0])
            data_name, ok = QLineEdit.getText(self, "Add Arrow", "Enter data name:")
            if ok:
                self.case_tool.draw_arrow(start_id, end_id, data_name)
                self.refresh_trees()
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Invalid IDs entered!")

    def delete_item(self):
        item_id, ok = QLineEdit.getText(self, "Delete Item", "Enter ID to delete:")
        if ok and item_id.isdigit():
            self.case_tool.delete_item(int(item_id))
            self.refresh_trees()

    def save_design(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save Design", "", "JSON Files (*.json)")
        if filename:
            self.case_tool.save_design(filename)

    def load_design(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Load Design", "", "JSON Files (*.json)")
        if filename:
            self.case_tool.load_design(filename)
            self.refresh_trees()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
