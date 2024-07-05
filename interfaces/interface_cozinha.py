import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class InterfaceCozinha(QMainWindow):
    def __init__(self, gerente_pedidos):
        super().__init__()
        self.gerente_pedidos = gerente_pedidos
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Gerenciamento de Pedidos - Cozinha")
        self.resize(300, 200)
        
        layout = QVBoxLayout()
        
        self.botao_iniciar_preparacao = QPushButton("Iniciar Preparação")
        self.botao_iniciar_preparacao.clicked.connect(self.iniciar_preparacao)
        layout.addWidget(self.botao_iniciar_preparacao)
        
        self.botao_completar_pedido = QPushButton("Completar Pedido")
        self.botao_completar_pedido.clicked.connect(self.completar_pedido)
        layout.addWidget(self.botao_completar_pedido)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def iniciar_preparacao(self):
        self.gerente_pedidos.iniciar_preparacao()
    
    def completar_pedido(self):
        self.gerente_pedidos.completar_pedido()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    from gerentes.gerente_pedidos import GerentePedidos
    gerente_pedidos = GerentePedidos()
    janela = InterfaceCozinha(gerente_pedidos)
    janela.show()
    
    sys.exit(app.exec())
