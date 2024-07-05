import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QHBoxLayout

class JanelaListarPedidos(QMainWindow):
    def __init__(self, gerente_pedidos):
        super().__init__()
        self.gerente_pedidos = gerente_pedidos
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Listar Pedidos")
        self.resize(600, 400)
        
        layout = QVBoxLayout()

        # Listar pedidos na fila de pedidos
        label_pedidos = QLabel("Pedidos na Fila:")
        layout.addWidget(label_pedidos)
        for pedido in self.gerente_pedidos.pedidos:
            layout.addWidget(QLabel(f"Pedido #{pedido.get_id()}"))
            self.adicionar_botoes_status(layout, pedido)

        # Listar pedidos em preparação
        label_em_preparacao = QLabel("Pedidos em Preparação:")
        layout.addWidget(label_em_preparacao)
        for pedido in self.gerente_pedidos.em_preparacao:
            layout.addWidget(QLabel(f"Pedido #{pedido.get_id()}"))
            self.adicionar_botoes_status(layout, pedido)

        # Listar pedidos entregues
        label_entregues = QLabel("Pedidos Entregues:")
        layout.addWidget(label_entregues)
        for pedido in self.gerente_pedidos.entregues:
            layout.addWidget(QLabel(f"Pedido #{pedido.get_id()}"))

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def adicionar_botoes_status(self, layout, pedido):
        botoes_layout = QHBoxLayout()
        botao_iniciar_preparacao = QPushButton("Iniciar Preparação")
        botao_iniciar_preparacao.clicked.connect(lambda: self.iniciar_preparacao(pedido))
        botoes_layout.addWidget(botao_iniciar_preparacao)

        botao_completar_pedido = QPushButton("Completar Pedido")
        botao_completar_pedido.clicked.connect(lambda: self.completar_pedido(pedido))
        botoes_layout.addWidget(botao_completar_pedido)

        layout.addLayout(botoes_layout)

    def iniciar_preparacao(self, pedido):
        self.gerente_pedidos.pedidos.remove(pedido)
        pedido.status = "Em preparação"
        self.gerente_pedidos.em_preparacao.append(pedido)
        self.close()
        self.init_ui()

    def completar_pedido(self, pedido):
        self.gerente_pedidos.em_preparacao.remove(pedido)
        pedido.status = "Entregue"
        self.gerente_pedidos.entregues.append(pedido)
        self.close()
        self.init_ui()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    from gerentes.gerente_pedidos import GerentePedidos
    gerente_pedidos = GerentePedidos()
    janela = JanelaListarPedidos(gerente_pedidos)
    janela.show()
    
    sys.exit(app.exec())
