from pagamento import Pagamento


class BoletoEmpresa(Pagamento):
    def realiza_pagamento(self, data: list):
        print('realiza pagamento boleto emrp')
