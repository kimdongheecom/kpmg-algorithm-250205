from com.kimdonghee.exchange.exchange_service import ExchangeService
from com.kimdonghee.exchange.exchange_model import ExchangeModel


class ExchangeController:
    def __init__(self,**kwargs):
        self.amount = int(kwargs.get("amount"))
        self.currency = kwargs.get("currency")


    def getResult(self) -> ExchangeModel:
        exchange = ExchangeModel()
        service = ExchangeService()
        exchange.amount = self.amount
        exchange.currency = self.currency

        return service.execute(exchange)


