import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QSpinBox, QHBoxLayout

from modelos.item_cardapio import Lanche, Bebida
from modelos.pedido import Pedido

class JanelaAdicionarPedido(QMainWindow):
    def __init__(self, gerente_pedidos, id_pedido):
        super().__init__()
        self.gerente_pedidos = gerente_pedidos
        self.id_pedido = id_pedido
        self.itens_pedido = []
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle(f"Adicionar Pedido #{self.id_pedido}")
        self.resize(400, 300)  # Aumentar o tamanho da janela
        
        layout = QVBoxLayout()

        # Exemplo de itens do cardápio
        self.cardapio = [
            ("Hamburguer", "Lanche", 10.99),
            ("Refrigerante", "Bebida", 5.99),
            ("Batata Frita", "Lanche", 7.99),
            ("Suco", "Bebida", 6.99)
        ]

        for item_nome, item_descricao, item_preco in self.cardapio:
            item_layout = QHBoxLayout()
            label_item = QLabel(f"{item_nome} ({item_descricao}) - R$ {item_preco:.2f}")
            spinbox_quantidade = QSpinBox()
            spinbox_quantidade.setRange(0, 10)
            item_layout.addWidget(label_item)
            item_layout.addWidget(spinbox_quantidade)
            layout.addLayout(item_layout)
            self.itens_pedido.append((item_nome, item_descricao, item_preco, spinbox_quantidade))
        
        self.botao_concluir_pedido = QPushButton("Concluir Pedido")
        self.botao_concluir_pedido.clicked.connect(self.concluir_pedido)
        layout.addWidget(self.botao_concluir_pedido)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def concluir_pedido(self):
        pedido = Pedido(self.id_pedido)
        for item_nome, item_descricao, item_preco, spinbox_quantidade in self.itens_pedido:
            quantidade = spinbox_quantidade.value()
            for _ in range(quantidade):
                if item_descricao == "Lanche":
                    item = Lanche(item_nome, item_descricao, item_preco)
                else:
                    item = Bebida(item_nome, item_descricao, item_preco)
                pedido.adicionar_item(item)
        
        self.gerente_pedidos.adicionar_pedido(pedido)
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    from gerentes.gerente_pedidos import GerentePedidos
    gerente_pedidos = GerentePedidos()
    janela = JanelaAdicionarPedido(gerente_pedidos, 1)
    janela.show()
    
    sys.exit(app.exec())
