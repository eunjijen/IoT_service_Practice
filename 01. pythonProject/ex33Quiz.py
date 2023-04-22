print('---로그인 처리---')
users2 = []
while True:
    menu = input('1.회원가입, 2. 전체회원목록, 3.로그인 4. 종료 ')

    if menu == '1':
        uid = input('아이디를 입력하세요')
        pwd = input('비밀번호를 입력하세요.')
        user = {}           # 입력받은 아이디/ 비번을 dict에 저장한 뒤
        user['userid'] = uid
        user['passwd'] = pwd
        users2.append(user)  # 리스트에 저장
    elif menu == '2':
        print('---------------------------------')
        print('아이디 : 비밀번호')
        print('---------------------------------')

        for user in users2:
            print(f"{user['userid']}")
        print('---------------------------------')
        # break
    elif menu=='3':
        logid=input('아이디: ')
        passwd=input('비밀번호: ')
        isExist, isLogin=False, False
        for user in users2:
            if(user['userid'])==logid:
                isExist=True
                if user['passwd']==passwd:
                    print(logid,'님 환영합니다')
                    isLogin=True
                    break
                else:
                    print('비밀번호가 일치하지 않습니다')
                    continue
        if not isExist:
            print('회원이 아닌것 같습니다.')
        if isLogin:
            print('>>서비스를 이용할 수 있습니다<<')
    elif menu=='4':
        exit(0)