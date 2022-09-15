from pagamento import Pagamento


class BoletoBancario(Pagamento):

    def realiza_pagamento(self, data: list):
        print("fazendo pagamento boleto bancario")
        return "pagamento realizado"
