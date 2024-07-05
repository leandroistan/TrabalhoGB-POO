from collections import deque

class GerentePedidos:
    def __init__(self):
        self.pedidos = []
        self.pedidos = deque()
        self.em_preparacao = deque()
        self.entregues = deque()
    
    def adicionar_pedido(self, pedido, origem):
        pedido.id = f"Pedido {origem.capitalize()} #{pedido.id} - Mesa {pedido.numero_mesa}"
        self.pedidos.append(pedido)

    def obter_pedidos(self):
        return self.pedidos
    
    def iniciar_preparacao(self):
        if self.pedidos:
            pedido = self.pedidos.popleft()
            pedido.status = "Em preparação"
            self.em_preparacao.append(pedido)
    
    def completar_pedido(self):
        if self.em_preparacao:
            pedido = self.em_preparacao.popleft()
            pedido.status = "Entregue"
            self.entregues.append(pedido)
    
    def gerar_relatorio(self):
        faturamento_total = sum(pedido.get_total() for pedido in self.entregues)
        contagem_itens = {}
        for pedido in self.entregues:
            for item in pedido.get_itens():
                if item.get_nome() in contagem_itens:
                    contagem_itens[item.get_nome()] += 1
                else:
                    contagem_itens[item.get_nome()] = 1
        return faturamento_total, contagem_itens
