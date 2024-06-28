# Posture-calibration-monitoring-system-
2024 1학기 기말 미니 프로젝트

참여 인원: 2명

작업 기간: 2주 (2024/05/27 - 2024/06/08)

환경: Rasbian Legacy-32bit OS / Python

역할: 가속도 센서 처리 및 각도 계산, SQL 쿼리문 수정, 라즈베리파이간 소켓통신, 모니터링 화면(UI) 마무리 작업

소개
--
- 가속도센서를 사용해 **[1] 앉은 자세로 학습하는 사람의 허리 각도를 계산해 자세교정이 이루어질 수 있도록 하는 디바이스**와 이에 대한 데이터를 **[2] 무선 통신으로 전달받아 나타내는** 통합적인 모니터링 시스템. 
- 기본적으로 여러 사용자를 엄두에 두고 제작하였으며, NFC와 같은 토큰 카드를 이용해 기존의 독서실과 유사한 키를 찍을 시 통과할 수 있는(로그인 할 수 있는) 회원제 기반의 환경을 만들고자 한다.

- **[1]번 라즈베리파이**는 가속도센서와 연결되어 허리 각도를 계산한다. 이 라즈베리파이에선 칼만 필터를 통해 허리 각도를 계산하는 과정이 이루어진다. 이후, 이 데이터를 무선통신을 이용해 [2]번 라즈베리파이로 전송한다.
- **[2]번 라즈베리파이**는 NFC태그와 연결된다. [1]번 라즈베리파이로부터 전달받은 각도 데이터를 회원별로 관리한다.

Blueprint
--

![image](https://github.com/j0gea/Posture-calibration-monitoring-system/assets/137410154/af7ebbe4-9767-4fb1-9646-de97f701bac9)


![image](https://github.com/j0gea/Posture-calibration-monitoring-system/assets/137410154/f27ddbee-23bc-478c-93cd-071e51185650)


- [1] 왼쪽, 디바이스 형태, client -- 가속도 센서와 연결
- [2] 오른쪽, 데이터베이스, Server -- RFID와 연결

Flow chart
--
![image](https://github.com/j0gea/Posture-calibration-monitoring-system/assets/137410154/89ce0bd3-fbaa-4102-b1b1-491cc387f5be)


참고문헌
--
- [상현,<라즈베리파이에서RFID리더기를사용하기>,2022.11.25](https://velog.io/@gemnsh/%EB%9D%BC%EC%A6%88%EB%B2%A0%EB%A6%AC%ED%8C%8C%EC%9D%B4%EC%97%90%EC%84%9C-RFID%EB%A6%AC%EB%8D%94%EA%B8%B0-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0)
- [경걍,<RasberryPi에MySQL설치&workbench연결>,2022.07.29](https://kyumq.tistory.com/6)
- [진의,<라즈베리파이7.MySQLDB설치및접속하기>,2017.12.10](https://blog.naver.com/wlsdml1103/221159758141)
- [C#예제 공부일기, <RasberryPi : 파이썬 MariaDB 서버 커넥션>, 2020.07.30](https://smartfactory121.tistory.com/70)
- [Raspberry Pi KR, <Raspberry Pi 와 함께 RFID 리더를 사용하십시오> , 2019.07](https://raspberry-pi.kr/rfid-raspberry-pi-8/)
- [ZETA7, <라즈베리파이 두 대로 소켓 통신을 해보자, 파이썬 버전>, 2018.05.07](https://blog.naver.com/zeta0807/221269996160)
- [Widgets and Gizmos - Wizmoz](https://wizmoz.blogspot.com/2013/01/simple-accelerometer-data-conversion-to.html?_sm_au_=iVVrPJjs44Sjbntq)


이슈

- 스레드 관리
- 필요없는 코드 삭제
- 새창 여는 것이 아닌 한 UI 안에서 해결(안쪽 객체를 바꾸는 식으로)
