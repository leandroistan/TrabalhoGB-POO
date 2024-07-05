class Pedido:
    def __init__(self, id):
        self.id = id
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def mostrar_itens(self):
        print(f"Pedido #{self.id}:")
        for item in self.itens:
            print(f"- {item.get_nome()}: {item.get_descricao()} - R$ {item.get_preco():.2f}")
        print()

    def get_total(self):
        return sum(item.get_preco() for item in self.itens)
    
    def get_id(self):
        return self.id

    def get_itens(self):
        return self.itens
