import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from modelos.pedido import Pedido
from interfaces.janela_adicionar_pedido import JanelaAdicionarPedido
from interfaces.janela_listar_pedidos import JanelaListarPedidos

class InterfaceAtendente(QMainWindow):
    def __init__(self, gerente_pedidos):
        super().__init__()
        self.gerente_pedidos = gerente_pedidos
        self.proximo_id_pedido = 1
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Gerenciamento de Pedidos - Atendente")
        
        layout = QVBoxLayout()
        
        self.botao_adicionar_pedido = QPushButton("Adicionar Pedido")
        self.botao_adicionar_pedido.clicked.connect(self.abrir_janela_adicionar_pedido)
        layout.addWidget(self.botao_adicionar_pedido)

        self.botao_listar_pedidos = QPushButton("Listar Pedidos")
        self.botao_listar_pedidos.clicked.connect(self.abrir_janela_listar_pedidos)
        layout.addWidget(self.botao_listar_pedidos)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def abrir_janela_adicionar_pedido(self):
        self.janela_adicionar_pedido = JanelaAdicionarPedido(self.gerente_pedidos, self.proximo_id_pedido)
        self.janela_adicionar_pedido.show()
        self.proximo_id_pedido += 1

    def abrir_janela_listar_pedidos(self):
        self.janela_listar_pedidos = JanelaListarPedidos(self.gerente_pedidos)
        self.janela_listar_pedidos.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    from gerentes.gerente_pedidos import GerentePedidos
    gerente_pedidos = GerentePedidos()
    janela = InterfaceAtendente(gerente_pedidos)
    janela.show()
    
    sys.exit(app.exec())
