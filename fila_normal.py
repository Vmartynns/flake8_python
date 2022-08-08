from fila_base import FilaBase


class FilaNormal(FilaBase):
    def gerasenhatual(self) -> None:
        self.senhatual = "NM{}".format(self.codigo)

    def atualizafila(self) -> None:
        self.reseta_fila()
        self.gerasenhatual()
        self.fila.append(self.senhatual)

    def chamacliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return (f'Cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}')
