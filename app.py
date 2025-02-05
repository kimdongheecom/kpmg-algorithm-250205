from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    print("전송된 데이터 방식")
    
    #초기값으로 설정
    won_500 = won_100 = won_50 = won_5 = 0
    total = None
    price = None
    amount = None
    error_msg = None


    if request.method == "POST":
        print("😎post 방식으로 진입")

        total = request.form.get('total')
        price = request.form.get('price')
        #문자를 상수로 변환하기 위해 int를 붙임
        total = int(total)
        price = int(price)

        if price > total :
            error_msg = "음수는 허용되지 않는다"

        else :
            amount = total - price
        print(f"거스름돈: {amount}")

        WON_50000 = 50000
        WON_10000 = 10000
        WON_5000 = 5000
        WON_1000 = 1000 
        WON_500 = 500
        WON_100 = 100
        WON_50 = 50
        WON_10 = 10

        won_list = [WON_50000,WON_10000,WON_5000,WON_1000, WON_500, WON_100, WON_50, WON_10]
        # money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
        # 50000 = 0번 index, 10000 = 1번 index,,,,,즉, money_list[1] =10000
       
        won50000 = amount // won_list[0]   
        won50000_nmg = amount % won_list[0]

        won10000 = won50000_nmg // won_list[1]   
        won10000_nmg = won50000_nmg % won_list[1]

        won5000 = won10000_nmg // won_list[2]   
        won5000_nmg = won10000_nmg % won_list[2]

        won1000 = won5000_nmg // won_list[3]   
        won1000_nmg = won5000_nmg % won_list[3]
        
        won500 = won1000_nmg // won_list[4]   
        won500_nmg = won1000_nmg % won_list[4]

        won100 = won500_nmg // won_list[5]
        won100_nmg = won500_nmg % won_list[5]

        won50 = won100_nmg // won_list[6]
        won50_nmg = won100_nmg % won_list[6]

        won10 = won50_nmg // won_list[7]
        won10_nmg = won50_nmg % won_list[7]

        print(won_list[0])
        print(won_list[1])
        print(won_list[2])
        print(won_list[3])
        print(won_list[4])
        print(won_list[5])
        print(won_list[6])
        print(won_list[7])
        
        #위에 프린터들은 아래 for구문 won_list

        for won in won_list:
            print(won)

        return render_template("index.html", won50000 = won50000, won10000 = won10000, won5000 = won5000, 
                               won1000 = won1000, won500 = won500, won100 = won100, won50 = won50, 
                               won10 = won10, amount = amount)  
    else:
        print("😙get 방식으로 진입")

        return render_template("index.html") 
    

if __name__ == '__main__':  
   app.run(debug=True)

app.config['TEMPLATES_AUTO_RELOAD'] = True