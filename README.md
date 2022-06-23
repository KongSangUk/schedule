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

#### 3. Calendar 동기화
   * [ main Calendar ] [ second Calendar ] 동기화 구현
   * 제목, 일시, 날짜, 인원, 세부내용 동기화 구현
   * 메모 발생 시 일정 표시 동기화 구현 


<br/>

#### [modal 기능]
-----------------------------
#### 1. popup
   * modal 사용하여 상태바, 주소창 제거
   * 자연스러운 popup 움직임 구현
   * popup 창 밖 클릭시 닫힘 구현

#### 2. popup Record
   * 제목, 구성원, 세부내용 text 방식 구현
   * 일시, 시간 목록 list에서 [ date | time ] 방식 구현
   * 확인 popup 내용 Calendar에 저장
   * 닫기 popup 내용 취소


<br/>

#### [memo 기능]
-----------------------------
#### 1.memo 기록  
   * text 타입으로 입력받아 기록 구현


<br/>


# 사용 영상
-----------------------------
https://youtu.be/qOVEDQxcb4A



# 와이어프레임
-----------------------------
##### [전체]
[스크린샷 2022-06-23 오후 2 26 23](https://user-images.githubusercontent.com/100742282/175222004-a09bfb0f-ea29-487c-952d-74e25b4f655d.png)

##### [1] 로그인 페이지 : 로그인, 회원가입
![스크린샷 2022-06-23 오후 2 26 35](https://user-images.githubusercontent.com/100742282/175222065-a0e6aef1-fe0f-4cc5-a7a0-608372da8389.png)

##### [2] 메인 페이지
![스크린샷 2022-06-23 오후 2 26 46](https://user-images.githubusercontent.com/100742282/175222084-de3ebb6f-e7ec-40f2-be5c-ae65d725f49b.png)

##### [3] 작성 페이지 : 제목, 날짜, 시간, 구성원, 세부내용
![스크린샷 2022-06-23 오후 2 27 03](https://user-images.githubusercontent.com/100742282/175222100-65381183-192b-4537-bc43-e1678968ad92.png)


