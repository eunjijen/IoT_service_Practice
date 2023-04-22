import random as rnd

label=["가위","바위","보"]
print(label[0]) #가위  index번호: 0부터 시작
print(label[2]) #보
while True:
    print('''
    --------Game v1.1-------------
    1. 가위  2.바위  3.보  9. 종료
    ------------------------------
    ''')
    #컴퓨터가 랜덤하게 1,2,3 중의 하나를 발생시키자
    com=rnd.randint(1,3)
    num=int(input('\t입력하세요: '))
    # print(num)
    if num==9:
        print("\tBye Bye~~")
        break
    if num<1 or num>3:
        print('\t메뉴에 없는 번호에요 다시 입력하세요')
        continue
    # print("가위바위보 진행>>>")
    result=""
    if num==com:
        result="비겼군요!!"
    elif (num==1 and  com==3) or (num==2 and com==1) or (num==3 and com==2):
        result="당신이 이겼네요^^"
    else:
        result="당신이 졌어요ㅠㅠ"

    print(f'''
    컴퓨터 : {com} [{label[com-1]}]
    당  신 : {num} [{label[num-1]}]
    ***********************
    결  과 : {result}
    ''')