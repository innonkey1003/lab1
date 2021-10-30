# 연락처 관리 코드의 확장 

# (이름, 핸드폰 번호)를 튜플로 구성. 연락처는 튜플로 구성된 리스트를 사용한다. 
# 리스트의 예제 data_list = [(홍길동, 010-1234-5678), (김철수, 010-2321-2321),...]

# 친구 추가할 경우 먼저 같은 이름이 있는지 확인. 
# 없을 경우, name및 phone을 문자열로 입력받은 뒤, data_list.append((name, phone))로 리스트에 추가 가능.
# 출력 시 for name, phone in data_list: print(name) print(phone) 형태로 표현 가능.

menu = 0 
friends = []
while menu != 9:
    print("-------연락처 관리----------------")
    print("1. 친구 리스트 출력")
    print("2. 친구 추가")
    print("3. 친구 삭제")
    print("4. 정보 변경")
    print("9. 종료")

    menu = int(input("메뉴를 선택하시오: "))
    if menu == 1:
        print("for name, phone in friends: ", friends)
        
    elif menu == 2:
        name = input("이름을 입력하세요: ")
        phone = input("전화번호를 입력하세요: ")
       
        samename = False
        for i in friends:    # i는 튜플  ex) ('황인호', '01048556652')
            if i[0] == name:          # i[0] = 황인호, i[1] = 01048556652
                samename = True
        
        #이 사이클을 돌고 나면 중복 이름이 있는지 검출된다

        #같은 이름이 없을 경우 
        if samename == False:
            friends.append((name, phone))    
        else:
            print("중복됩니다.")

    elif menu == 3:
        del_name = input("삭제하고 싶은 친구의 이름을 입력하세요: ")

        wrong = False
        for i in friends:
            if i[0] == del_name:
                del_name = (i[0], i[1])
                wrong = True

        if wrong == False:
            print("이름이 발견되지 않았음")
        else:
            friends.remove(del_name)
        

    elif menu == 4:
        wrong_name = input("정보를 수정하고 싶은 이름을 입력하세요: ")

        wrong = False
        for i in friends:
            if i[0] == wrong_name:
                wrong_name = (i[0], i[1])
                wrong = True

        if wrong == False:
            print("이름이 발견되지 않았음")
        else:
            friends.remove(wrong_name)
            new_name = input("수정한 이름을 입력하세요: ")
            new_number = input("수정한 번호를 입력하세요: ")
            
        # 수정한 이름이 중복되지 않게 
            samename = False
            for i in friends:   
                if i[0] == new_name:          
                    samename = True
        
         
            if samename == False:
                friends.append((new_name, new_number))    
            else:
                print("이름이 중복됩니다.")
                friends.append(wrong_name)
                

    elif menu == 9:
        print("종료합니다.")

    else:
        print("메뉴에 없는 번호입니다.")
