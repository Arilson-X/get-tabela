import sys
import time
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import GetTabela

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Get de Tabelas")
        
        self.url_label = QLabel("URL:")
        self.url_input = QLineEdit()
        
        self.extract_button = QPushButton("Extrair Tabelas")
        self.extract_button.clicked.connect(self.extract_tables)
        
        layout = QVBoxLayout()
        layout.addWidget(self.url_label)
        layout.addWidget(self.url_input)
        layout.addWidget(self.extract_button)
        
        self.setLayout(layout)
    
    def extract_tables(self):
        url = self.url_input.text()
        if not url:
            QMessageBox.warning(self, "Aviso", "Por favor, insira uma URL.")
            return
        try:
            tabelas, titulo = GetTabela.getTabela(url)
            if tabelas.items():
                QMessageBox.information(self, "Sucesso", f"Tabelas extraídas e salvas em '{titulo}'.")
            else: 
                QMessageBox.critical(self, "Erro", "Não foram encontradas tabelas.")
        except:
            QMessageBox.critical(self, "Erro", "Não foi possível extrair as tabelas.")


        # tables = extract_tables_from_site(url)
        # if tables:
        #     output_file = "tabelas.xlsx"
        #     save_tables_to_excel(tables, output_file)
        #     QMessageBox.information(self, "Sucesso", f"Tabelas extraídas e salvas em '{output_file}'.")
        # else:
        #     QMessageBox.critical(self, "Erro", "Não foi possível extrair as tabelas.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
