
from com.kimdonghee.exchange.exchange_model import ExchangeModel


class ExchangeService:
    def __init__(self):
        pass

    def get_unit_count(self, amount, unit_list): #self만 있고, 어마운트와 유닛리스트가 없으면 파라미터가 아예 없다는 상태를 의미함. 나(메쏘드) 자신만 있다는 뜻이다. 여기서 셀프가 없으면, 어마운트가 파라미터가 2개가 있다.. 셀프가 있으면 파라미터가 없다라는 뜻이다.
        money = amount
        unit_dict ={}
        for unit in unit_list :
            unit_dict[unit] = money // unit 
            money %= unit 
        print(f"{unit}원: {unit_dict[unit]}개") 
        return unit_dict
    
    def sample(self):
        print("sample")

    def execute(self,exchange: ExchangeModel) -> ExchangeModel:

        amount = exchange.amount
     
        
        WON_50000 = 50000  
        WON_10000 = 10000
        WON_5000 = 5000
        WON_1000 = 1000 
        WON_500 = 500
        WON_100 = 100
        WON_50 = 50
        WON_10 = 10

        unit_list = [WON_50000,WON_10000,WON_5000,WON_1000, WON_500, WON_100, WON_50, WON_10]

        unit_dict = self.get_unit_count(amount, unit_list) 
        print("-----------시작------------")

        for unit, count in unit_dict.items(): 
            print(f"{unit}원: {count}개")

        print("-----------끝------------")

        temp = ''
        
        for unit, count in unit_dict.items(): 
            temp += f"{unit}원: {count}개<br/>"
        
        exchange.amount = amount
        exchange.result = temp

        return exchange