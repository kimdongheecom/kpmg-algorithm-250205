from flask import Flask, render_template, request, redirect, url_for
from com.kimdonghee.exchange.exchange_controller import ExchangeController
from com.kimdonghee.exchange.exchange_model import ExchangeModel

#class 는 함수이다. 함수를 모아 놓은게 클래스이다. 클래스 안에 있는게 메소드이다.인공지능할 때 클래스 만들고, 메소드를 호출할 것이다.

app = Flask(__name__) # 실제이름은 Flask이지만, 인식이 안되기 때문에,,,,app이라는 이름을 준 것이다. 
@app.route('/')
def intro():

    return render_template("/index.html")

@app.route('/exchange_won')
def exchange_won2():

    return render_template("/exchange_won.html")

@app.route('/exchange_dollar')
def exchange_dollar2():

    return render_template("/exchange_dollar.html")

@app.route('/exchange_won', methods=['POST', 'GET'])
def exchange_won():
    print("원화 환전에서 전송된 데이터 방식")
    
    if request.method == "POST":
        print("😎post 방식으로 진입")

        amount = request.form.get('amount')
        # price = request.form.get('price')
        amount = int(amount)
        # total = int(total)
        # price = int(price)
        
        # if price > total :
        #     error_msg = "음수는 허용되지 않는다"

        # else :
        #     amount = total - price
        # print(f"거스름돈: {amount}")

       
        controller = ExchangeController(amount = amount)

        resp : ExchangeModel = controller.getResult()


        render_html = '<h1>결과보기</h1>'
        render_html += resp.result

        return render_template("exchange_won.html", render_html = render_html)
    
    else:
        print("😙get 방식으로 진입")

        return render_template("exchange_won.html") 

@app.route('/exchange_dollar', methods=['POST', 'GET'])
def exchange_dollar():
    print("달러 환전에서 전송된 데이터 방식")
    
    # dollar_500 = dollar_100 = dollar_50 = dollar_5 = 0
    # total = None
    # price = None
    # amount = None
    # error_msg = None



    if request.method == "POST":
        print("😎post 방식으로 진입")

        amount = request.form.get('amount') #exchange_dollar에서 amount를 요청함. amount는 html에서 문자열이기 때문에, int()를 사용해서 변환시켜줌.
        # price = request.form.get('price')
       
        amount = int(amount)  
        # price = int(price)

        # if price > total :
        #     error_msg = "음수는 허용되지 않는다"

        # else :
        #     amount = total - price
        # print(f"거스름돈: {amount}")

        DOLLAR_100 = 100  
        DOLLAR_50 = 50
        DOLLAR_10 = 10
        DOLLAR_5 = 5 
        DOLLAR_1 = 1

        unit_list = [DOLLAR_100, DOLLAR_50, DOLLAR_10, DOLLAR_5, DOLLAR_1]

        unit_count = Count()

        unit_dict = unit_count.get_unit_count(amount, unit_list) 

        for unit, count in unit_dict.items(): 
            print(f"{unit}$: {count}개") 

        render_html = '<h1>결과보기</h1>' 
        for unit, count in unit_dict.items(): 
            render_html += f"{unit}$: {count}개 <br/>" 

        return render_template("exchange_dollar.html", render_html = render_html)
    
    else:
        print("😙get 방식으로 진입")

        return render_template("exchange_dollar.html") 

if __name__ == '__main__':  
   app.run(debug=True)

app.config['TEMPLATES_AUTO_RELOAD'] = True