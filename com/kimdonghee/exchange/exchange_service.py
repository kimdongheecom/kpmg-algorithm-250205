
from com.kimdonghee.exchange.exchange_model import ExchangeModel


class ExchangeService:
    def __init__(self):
        pass

    def execute(self,exchange: ExchangeModel) -> ExchangeModel: #execute가 실행하는 함수....선언하는 함수를 통합해서 실행하는 함수이고, 최종적으로 컨트롤러에 보낸다.........
        currency_list = []
        currency_unit = ''
        page = ''

         #amount = 총 금액, currency = 달러, 원.
        print('🚓exchange won', exchange.currency)
        if exchange.currency == 'USD':
            page = "exchange_dollar.html"
            currency_list = self.get_dollar_list()
            currency_unit = '달러'
        elif exchange.currency == 'WON':
            page = "exchange_won.html"
            currency_list = self.get_won_list()
            currency_unit = '원'
        else:
            print("잘못된 화폐단위입니다.")

        currency_dict = self.get_currency_dict(exchange.amount, currency_list)
        self.print_currency_dict(currency_dict)
        exchange.result = self.format_currency_counts(currency_dict,currency_unit)
        exchange.page = page
        return exchange

    

    def get_currency_dict(self, amount, currency_list): #self만 있고, 어마운트와 유닛리스트가 없으면 파라미터가 아예 없다는 상태를 의미함. 나(메쏘드) 자신만 있다는 뜻이다. 여기서 셀프가 없으면, 어마운트가 파라미터가 2개가 있다.. 셀프가 있으면 파라미터가 없다라는 뜻이다.
        money = amount
        print('🚓money = amount', money)
        currency_dict ={}
        for currency in currency_list :
            print('🍔money', type(money))
            print('🍔currency', type(currency))
            currency_dict[currency] = money // currency 
            money %= currency
        return currency_dict


    def print_currency_dict(self, currency_dict):
        print("-----------시작------------")
        for currency, count in currency_dict.items(): 
            print(f"{currency}원: {count}개")
        print("-----------끝------------")

    def get_won_list(self):
        WON_50000 = 50000  
        WON_10000 = 10000
        WON_5000 = 5000
        WON_1000 = 1000 
        WON_500 = 500
        WON_100 = 100
        WON_50 = 50
        WON_10 = 10
        won_list = [WON_50000,WON_10000,WON_5000,WON_1000, WON_500, WON_100, WON_50, WON_10]
        return won_list
    
    def get_dollar_list(self):
        DOLLAR_100 = 100
        DOLLAR_50 = 50
        DOLLAR_20 = 20
        DOLLAR_10 = 10
        DOLLAR_5 = 5
        DOLLAR_2 = 2
        DOLLAR_1 = 1
        dollar_list = [DOLLAR_100, DOLLAR_50, DOLLAR_20, DOLLAR_10, DOLLAR_5, DOLLAR_2, DOLLAR_1]
        return dollar_list

    def format_currency_counts(self, currency_dict, currency_unit):
        temp = ''   
        for currency, count in currency_dict.items(): 
            temp += f"{currency}{currency_unit}: {count}개<br/>"
        return temp