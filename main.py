import sys
from PySide6.QtWidgets import QApplication

from gerentes.gerente_pedidos import GerentePedidos
from interfaces.interface_atendente import InterfaceAtendente
from interfaces.interface_cozinha import InterfaceCozinha
from interfaces.interface_relatorio import InterfaceRelatorio
from interfaces.janela_cliente import JanelaCliente  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    gerente_pedidos = GerentePedidos()
    
    janela_atendente = InterfaceAtendente(gerente_pedidos)
    janela_cozinha = InterfaceCozinha(gerente_pedidos)
    janela_relatorio = InterfaceRelatorio(gerente_pedidos)
    janela_cliente = JanelaCliente(gerente_pedidos)
    
    janela_atendente.show()
    janela_cozinha.show()
    janela_relatorio.show()
    janela_cliente.show()
    
    sys.exit(app.exec())
