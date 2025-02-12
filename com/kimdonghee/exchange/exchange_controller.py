from com.kimdonghee.exchange.exchange_service import ExchangeService
from com.kimdonghee.exchange.exchange_model import ExchangeModel


class ExchangeController:
    def __init__(self,**kwargs):
        self.amount = kwargs.get("amount")


    def getResult(self) -> ExchangeModel:
        exchange = ExchangeModel()
        service = ExchangeService()
        exchange.amount = self.amount

        return service.execute(exchange)


