class Count: #Count는 앞에만 대문자
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
    
# 셀프는 아무것도 잡아먹지 않은 상태라고 생각해야해/// 파라미터가없음을 나타내는게 .....self
# 파라미터를 안보낼 수 있다는 개념을 존재를 보여주기 위해 self를 작성한다. 파라미터는 함수나 메서드에 값을 전달하기 위한 변수이다.
# 라우터는 함수만 갖고 있으니까,즉, 메소드만 갖고 있으니까(즉, 메소드를 만든게 아니라 갖고 온 것이다.) 객체 지향이 아니에요. 그래서 클래스라는 단어가 아니다. 셀프라는 단어는 클래스에서만 존재한다.
# 셀프는 클래스에서만 존재한다. 셀프는 객체 지향에서만 존재한다.
# 캐글은 데이터 분석 사이트이다...