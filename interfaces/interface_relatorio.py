import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTextEdit

class InterfaceRelatorio(QMainWindow):
    def __init__(self, gerente_pedidos):
        super().__init__()
        self.gerente_pedidos = gerente_pedidos
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Relatório de Faturamento")
        self.resize(300, 200)
        
        layout = QVBoxLayout()
        
        self.botao_gerar_relatorio = QPushButton("Gerar Relatório")
        self.botao_gerar_relatorio.clicked.connect(self.gerar_relatorio)
        layout.addWidget(self.botao_gerar_relatorio)
        
        self.texto_relatorio = QTextEdit()
        layout.addWidget(self.texto_relatorio)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def gerar_relatorio(self):
        faturamento_total, contagem_itens = self.gerente_pedidos.gerar_relatorio()
        relatorio = f"Faturamento Total: R${faturamento_total:.2f}\n\n"
        relatorio += "Quantidade de Itens Vendidos:\n"
        for item, quantidade in contagem_itens.items():
            relatorio += f"{item}: {quantidade}\n"
        self.texto_relatorio.setText(relatorio)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    from gerentes.gerente_pedidos import GerentePedidos
    gerente_pedidos = GerentePedidos()
    janela = InterfaceRelatorio(gerente_pedidos)
    janela.show()
    
    sys.exit(app.exec())
