import sys
import pandas as pd
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QTextEdit, QWidget, QVBoxLayout, QHBoxLayout, QLabel,QLineEdit, QPushButton, QMessageBox
import GetTabela

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Get de Tabelas")
        self.setFixedHeight(700)
        self.setFixedWidth(700)

        self.url_label = QLabel("URL:")
        self.url_label.setFixedWidth(80)
        self.url_input = QLineEdit()
        self.url_input.setFixedWidth(500)
        self.url_input.setAlignment(Qt.AlignCenter)

        self.extract_button = QPushButton("Extrair Tabelas")
        self.extract_button.setFixedWidth(100)
        self.extract_button.clicked.connect(self.extract_tables)
        
        url_layout = QHBoxLayout()
        url_layout.addWidget(self.url_label)
        url_layout.addWidget(self.url_input)

        self.log_label = QLabel("Log do Processo:")
        self.log_label.setAlignment(Qt.AlignBottom)
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        self.log_text.setFixedHeight(200)
        self.log_text.setFixedWidth(650)

        log_layout = QVBoxLayout()
        log_layout.addWidget(self.log_label)
        log_layout.addWidget(self.log_text)

        layout = QVBoxLayout()
        layout.addLayout(url_layout)
        layout.addWidget(self.extract_button)
        layout.addLayout(log_layout)
        layout.setAlignment(Qt.AlignCenter)

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
