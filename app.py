from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    print("전송된 데이터 방식")

    coin_500 = coin_100 = coin_50 = coin_5 = 0
    total = None
    price = None
    amount = None
    error_msg = None


    if request.method == "POST":
        print("😎post 방식으로 진입")

        total = request.form.get('total')
        price = request.form.get('price')

        total = int(total)
        price = int(price)

        if price > total :
            error_msg = "음수는 허용되지 않는다"

        else :
            amount = total - price
        
        COIN_500 = 500 #COIN_500,100, 50, 10 : 상수
        COIN_100 = 100
        COIN_50 = 50
        COIN_10 = 10
        
        coin500 = amount // COIN_500  # // : 나눗셈을 의미함 
        coin500_nmg = amount % COIN_500 # coin500_nmg : 500으로 나눈 나머지, amount : 변수

        coin100 = coin500_nmg // COIN_100
        coin100_nmg = coin500_nmg % COIN_100

        coin50 = coin100_nmg // COIN_50
        coin50_nmg = coin100_nmg % COIN_50

        coin10 = coin50_nmg // COIN_10
        coin10_nmg = coin50_nmg % COIN_10


        return render_template("index.html", coin500 = coin500, coin100 = coin100, coin50 = coin50, coin10 = coin10) # index파일에 coin500, coin100, coin50, coin10 이 없으니까 보낸다는 의미이다. 
    else:
        print("😙get 방식으로 진입")

        return render_template("index.html") #get방식을 사용해야하니까 template에서 index파일을 가지고 옴
    

if __name__ == '__main__':  
   app.run(debug=True)

app.config['TEMPLATES_AUTO_RELOAD'] = True