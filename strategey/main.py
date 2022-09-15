from boleto import BoletoApplication
from boleto_bancario import BoletoBancario
from boleto_empresa import BoletoEmpresa

if __name__ == '__main__':
    application = BoletoApplication(BoletoBancario())
    application.realiza_pagamentos()
    print()
    application = BoletoApplication(BoletoEmpresa())
    application.realiza_pagamentos()
