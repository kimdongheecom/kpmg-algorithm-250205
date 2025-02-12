from flask import Flask, render_template, request, redirect, url_for
from com.kimdonghee.exchange.exchange_controller import ExchangeController
from com.kimdonghee.exchange.exchange_model import ExchangeModel

#class 는 함수이다. 함수를 모아 놓은게 클래스이다. 클래스 안에 있는게 메소드이다.인공지능할 때 클래스 만들고, 메소드를 호출할 것이다.

app = Flask(__name__) # 실제이름은 Flask이지만, 인식이 안되기 때문에,,,,app이라는 이름을 준 것이다. 
@app.route('/')
def intro():

    return render_template("/index.html")

@app.route('/won') #html과 같아야 한다.
def exchange_won():
    return render_template("/exchange_won.html")

@app.route('/dollar')
def exchange_dollar():
    return render_template("/exchange_dollar.html")



@app.route('/exchange', methods=['POST', 'GET'])
def exchange():
    print("원화 환전에서 전송된 데이터 방식")
    
    if request.method == "POST":
        print("😎post 방식으로 진입")
        amount = request.form.get('amount')
        currency = request.form.get('currency') #USD, WON 함수
        print("amount: ", amount)
       
       
        controller = ExchangeController(amount = amount, currency = currency)
        resp : ExchangeModel = controller.getResult()

        render_html = '<h1>결과보기</h1>'
        render_html += resp.result

        return render_template(resp.page, render_html = render_html)
    
    else:
        print("😙get 방식으로 진입")

        return render_template("exchange_won.html") 

if __name__ == '__main__':  
   app.run(debug=True)

app.config['TEMPLATES_AUTO_RELOAD'] = True