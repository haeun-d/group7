
# 알찬소<br>
## 알찬 소비를 나누는 소비자 커뮤니티

<br><br><br>
# 😎 개발팀원 소개 
| <center> 김은서  </center> | <center>여지원 </center> | <center>장다연</center> | 
| --- | --- | --- |
| <center> <img width="150px" src="https://avatars.githubusercontent.com/u/128278212?v=4" /></center> | <center><img width="150px" src="https://soopool.art/image/acnh/animal/Flurry.png" /></center> | <center><img width="150px" src="https://soopool.art/image/acnh/animal/Apple.png" /></center> | 
| <center>로그인, 금융, 지도 </center> | <center> 커뮤니티 </center> | <center> 중고거래 </center> |
| [@7beunseo](https://github.com/7beunseo)  | [@yjwon6621](https://github.com/yjwon6621) |  [@noeyadd](https://github.com/noeyadd) |

| <center>정하은 </center> | <center>한리안 </center> | <center>. </center> | 
| --- | --- | --- |
| <center> <img width="150px" src="https://soopool.art/image/acnh/animal/Molly.png" /></center> | <center><img width="150px" src="https://soopool.art/image/acnh/animal/Bree.png" /></center> | <center><img width="150px" src="https://soopool.art/image/acnh/animal/Graham.png" /></center> | 
| <center>커뮤니티 </center> | <center> 중고거래 </center> | <center>  </center> |
| [@haeun-d](https://github.com/haeun-d)  | [@agigongju](https://github.com/agigongju) |   |

<br><br><br>
# 📙 프로젝트 소개<br><br>


### ✨ 서비스 핵심 기능<br>

#### 금융 기록 
  - 금융 기록을 작성, 조회, 수정, 삭제하며 자신의 소비 기록을 남길 수 있다
  - 금융 기록을 작성할 때 공개를 해제하면 다른 사용자들에게 해당 기록은 보이지 않는다
  - 사용자의 닉네임, 혹은 아이디를 검색해서 사용자 간 팔로우, 언팔로우를 한다
  - 팔로잉한 사람들에 한해 다른 사용자들의 소비 기록을 보며 좋아요를 남길 수 있다
  - 자신의 소비를 기반으로 카테고리별 월별 소비 통계를 그래프르 확인할 수 있다
 

#### 제휴 정보 확인
  - 학교 제휴 정보를 지도로 한눈에 보며 스크랩으로 내가 원하는 정보를 저장할 수 있다
  - 스크랩 정보는 마이페이지에서 확인한다
  - 기한이 지난 제휴 정보는 더이상 보이지 않는다
    
#### 중고 거래
  - 중고 상품을 올리고 수정 삭제할 수 있다
  - 소비자는 원하는 중고거래를 찜할 수 있다
  - 중고 거래 희망을 원하는 사용자는 1:1 채팅 기능을 통해 판매자와 연락을 주고받는다
  - 소비자의 경우 마이페이지에서 내가 요청한 채팅을 모두 조회할 수 있다
  - 판매자의 경우 올린 상품에서 요청받은 채팅을 확인할 수 있다
  - 거래가 완료된 경우 판매자는 구매한 사용자의 닉네임을 입력하여 판매 완료 표시를 한다
  - 판매자가 소비자를 정상 등록한다면 해당 중고 상품의 리뷰를 남길 수 있다
  - 거래가 완료되면 진행했던 1:1 채팅방을 나갈 수 있다

#### 커뮤니티  
  - 




### ✨ 기술 스택<br>

- 기획디자인 : 피그마
- 프론트엔드 : Bootstap, Kakao map API
- 백엔드 : python, django
- ETC : git


### ✨ 폴더 구조<br>


  ```
  📂 
  └─ aalchanso
   ├─ my_project
   │  ├─ __init__.py
   │  ├─ asgi.py
   │  ├─ settings.py
   │  ├─ urls.py
   │  └─ wsgi.py
   ├─ myapp/
   │  ├─ __init__.py
   │  ├─ admin.py
   │  ├─ apps.py
   │  ├─ models.py
   │  ├─ tests.py
   │  └─ views.py
   └─ manage.py
  ```

### ✨ 개발환경에서의 실행 방법<br>
  ```
  $ cd group7
  $ source venv/Scripts/activate 
  $ python manage.py makemigrations
  $ python manage.py migrate
  $ python manage.py migrate --run-syncdb
  $ python manage.py runserver
  ```


