from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def intro():

    return render_template("/index.html")

@app.route('/exchange_won')
def exchange_won2():

    return render_template("/exchange_won.html")

@app.route('/exchange_dollar')
def exchange_dollar2():

    return render_template("/exchange_dollar.html")


def get_unit_count(amount, unit_list): # get_unit_count(중첩함수)는 unit(예를 들어, 원화, 엔화, 달러 등을 의미함), count는 갯수,,,,즉, 단위와 갯수를 의미함.
    unit_dict = {} # ....count는 갯수,,,,즉, 단위와 갯수를 의미함. 즉, 단위에 맞고, 갯수를 맞추기 위해 이러한 함수를 설정함.
    money = amount 
    
    for unit in unit_list :
        unit_dict[unit] = money // unit 
        money %= unit 
        print(f"{unit}원: {unit_dict[unit]}개") 
    return unit_dict


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

        WON_50000 = 50000  
        WON_10000 = 10000
        WON_5000 = 5000
        WON_1000 = 1000 
        WON_500 = 500
        WON_100 = 100
        WON_50 = 50
        WON_10 = 10

        unit_list = [WON_50000,WON_10000,WON_5000,WON_1000, WON_500, WON_100, WON_50, WON_10]

        unit_dict = get_unit_count(amount, unit_list) 

        for unit, count in unit_dict.items(): 
            print(f"{unit}원: {count}개") 

        render_html = '<h1>결과보기</h1>' 
        for unit, count in unit_dict.items(): 
            render_html += f"{unit}원: {count}개 <br/>" 

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

        unit_dict = get_unit_count(amount, unit_list) 

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