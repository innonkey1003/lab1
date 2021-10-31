# lab1
## test file
### edit your address book   
Menu
1. 친구 리스트 출력
2. 친구 추가
3. 친구 삭제
4. 정보 변경

```
코드 중 일부
# (name, phone) 튜플 입력
 samename = False
        for i in friends:    # i는 튜플  ex) ('황인호', '01048556652')
            if i[0] == name:          # i[0] = 황인호, i[1] = 01048556652
                samename = True
                
        # 이 사이클을 돌고 나면 중복 이름이 있는지 검출된다
        # 같은 이름이 없을 경우 
        
        if samename == False:
            friends.append((name, phone))    
        else:
            print("중복됩니다.") 
```
* * *
<img width="960" alt="20213102-result4" src="https://user-images.githubusercontent.com/93446072/139574823-d4bed97d-5b09-49e0-8948-579e7587aeed.png">

* * * 
### my favorite song
+ Bruno Mars
  * [When I was your man](https://youtu.be/ekzHIouo8Q4)
+ Maroon 5
  * [She will be loved](https://youtu.be/nIjVuRTm-dc)    
