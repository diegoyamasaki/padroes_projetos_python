

from pagamento import Pagamento


class BoletoApplication():

    def __init__(self, pagamento: Pagamento) -> None:
        self._pagamento = pagamento

    @property
    def pagamento(self) -> Pagamento:
        return self._pagamento

    @pagamento.setter
    def pagamento(self, pagamento: Pagamento) -> None:
        self._pagamento = pagamento

    def realiza_pagamentos(self) -> None:
        print("realiza pagamento de boletos")
        result = self._pagamento.realiza_pagamento(["a", "b", "c", "d", "e"])





