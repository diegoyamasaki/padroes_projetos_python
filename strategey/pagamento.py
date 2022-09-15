from abc import ABC, abstractmethod


class Pagamento(ABC):

    @abstractmethod
    def realiza_pagamento(self, data: list):
        pass