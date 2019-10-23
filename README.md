# README

# 기록 GIROK

## 1. 제공 서비스

```
a. 매일 자신의 하루 생활을 간단한 상자 하나로 체크(기록) - Github mypage 모내기 clone  
자신이 설정한 목표(헬스, 공부)를 모두 달성하면 체크 
진행상황 상세 설정을 통해 통계분석 페이지 뷰 - Github insights page 
	
b. 개인정보(건강 데이터 등) 제공에 대해 정보의 가치를 돈으로 환산하여 보여줌 
(혹은 자신의 선택 하에 포인트로 환산 가능)

c. 이미지 / 영상 위주의 커뮤니티 기능 - instagram clone 
```

## 2. 제공 가치 

a. 모내기 - 기록과 성취감  (Life tracking)

```
- 여러가지 *주제/항목* 별로 세분화된 목표를 통합관리
1. 운동
2. 학습
3. 업무
4. 취미(자기발전)

세부 기능: 블로그 태깅(사이드 바)
```

b. 개인정보 - 정보의 가치, 공익성 

c. 블로깅 - 커뮤니티 (사진 및 영상 저장, 게시, 공유) 

## 3. 구현

### 목표

- GIROK: CRU
- BLOG: CRUD
- M:N DB
- Social Media tagging 

### 세부구현

```
1. 최대한 무료 SaaS 사용해서 만들어보자 
2. 우선 핵심기능부터 구현하고 새로운 기능을 추가해보자

디자인
https://www.figma.com/

CSS 라이브러리
https://tailwindcss.com
https://bulma.io

클라이언트
https://insomnia.rest  (REST)
https://altair.sirmuel.design (GraphQL)

유저 비밀번호 관리
https://auth0.com/
https://aws.amazon.com/ko/cognito/

에러 리포팅
https://sentry.io

푸쉬알림
https://onesignal.com/
.
피드
getstream.io
```

#### Frontend

- HTML
- CSS
- Bootstrap

#### Backend

- Django 
- SQLite 

서버는 AWS - docker? 

## How to use

## 경쟁앱

- 데이그램
- 하루노트
- 에버노트
- Momento 모멘토
- 트렐로
- Moves
- Dayone
- timetracker

## 유사기능

- A year in pixels : 무드 트래커, 하루에 픽셀 하나, 해당 날짜의 기분을 표시하는 것 



