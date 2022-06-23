# 항해 3조 
-----------------------------
- 공상욱 조장 
- 권유경 팀원 
- 사상원 팀원 
- 전인호 팀원
<br/><br/>

-----------------------------
# Schedule Calendar Project
-----------------------------

## 프로젝트 기획 내용
>바쁜 현대사회에서 스케줄관리는 매우 중요한 일이다.<br/>
>업무부터 약속의 부분까지, 금일의 일정부터 올해까지 우리는 매우 많은 Schedule 잡혀있다.
>우리 팀은 Schedule을 관리하는 서비스가 증가하고 있다는 것을 확인하였다.
>하지만 서비스를 이용하는 연령대는 10대 ~ 40대가 많았다. 그 이유는 서비스 사용성이 더욱 화려하고 많은 기능을 구현해야 사용자들이 모이기 때문이다.
>그로 인해 화려하며 복잡한 사용성을 따라가지 못한 인원들은 많이들 포기하며 개인 수첩, 달력을 이용하여 손수 기록하고 있었다.<br/><br/>
>우리 팀은 이런 문제로 소외된 인원을 위해 사용성이 용이한 Schedule Calendar Project 진행하기로 하였다. 
>우리는 Project를 진행하면서 사용성이 용이하며 전 연령이 어려움 없이 사용할 수 있는 Schedule Calendar를 서비스한다는 마음으로 진행하겠다.  

<br/>

## Schedule Calendar 기능 설명
-----------------------------
#### [membership and login 기능]
-----------------------------
#### 1. 회원 가입
   * [ ID = username ]
   * [ PW = password, password2 ]

#### 2. 회원 가입 ID 중복 검사<br/>
   * ID 입력 받아 [db = username] 확인
   * true 확인 시 ID 사용
   * false 확인 시 재입력
   
#### 3. 회원 가입 PW 이중 검사<br/>
   * PW 입력 받아 [db = password, password2 ] 확인
   * true 확인시 사용
   * false 확인시 [ 비밀번호가 일치합니다. ] 문구 출력
   
#### 4. 로그인 
   * ID | PW 입력 받아 [ db = username, password ] 확인
   * true 확인 시 main page 이동.
   * false 확인 시 main page 이동 불가.


<br/>

#### [main page 기능]
-----------------------------
#### 1. main Calendar
   * main Calendar로 큰 사이즈로 중앙에 위치
   * 년, 월, 일 표준 달력으로 이동 및 사용 가능
   * 특정 날짜 선택 시 메모 기능 구현
   * 메모 발생 시 일정 표시 구현
   * 등록 및 삭제 구현 

#### 2. second Calendar
   * 년, 월, 일 표준 달력으로 이동 및 사용 가능
   * 특정 날짜 선택 시 메모 기능 구현
   * 메모 발생 시 일정 표시 구현
   * 좌측 상단 작은 사이즈로 구현
   * 등록 및 삭제 구현 

<br/>

#### [modal 기능]
-----------------------------
#### 1. popup
   * modal 사용하여 상태바, 주소창 제거
   * 자연스러운 popup 움직임 구현
   * poppu창 밖 클릭시 닫힘 구현

#### 2. popup Record
   * 
   * 

<br/>

-----------------------------
# 와이어프레임
-----------------------------
##### [전체]
![스크린샷 2022-06-20 오후 5 21 55](https://user-images.githubusercontent.com/100742282/174559800-b9b4f758-a225-4606-9f78-56c122f8002c.png)

##### [1] 로그인 페이지 : 로그인, 회원가입

![스크린샷 2022-06-20 오후 4 06 57](https://user-images.githubusercontent.com/100742282/174559858-9ec5c2a5-4eb9-4d1c-a535-8f2d4bb6c6c6.png)

##### [2] 메인 페이지

![스크린샷 2022-06-20 오후 4 07 18](https://user-images.githubusercontent.com/100742282/174559878-5c7a1a11-2003-42ee-9f03-6e6467e815fa.png)

##### [3] 작성 페이지 : 제목, 날짜, 시간, 구성원, 세부내용

![스크린샷 2022-06-20 오후 4 07 33](https://user-images.githubusercontent.com/100742282/174559923-016f4849-bd93-4d5f-ac3f-8204390fed96.png)
<br/>

-----------------------------
# API 설계
-----------------------------
![스크린샷 2022-06-20 오후 5 15 25](https://user-images.githubusercontent.com/100742282/174559998-872f79b6-f9f0-4dd7-9e55-ab56141135e6.png)
![스크린샷 2022-06-20 오후 5 15 48](https://user-images.githubusercontent.com/100742282/174560024-904b7b89-3c4b-4ac6-9917-6613b2b293dc.png)
![스크린샷 2022-06-20 오후 5 16 19](https://user-images.githubusercontent.com/100742282/174560085-5d73964e-5217-46db-8fe6-db19d510818f.png)

