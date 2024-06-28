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

![image](https://github.com/j0gea/Posture-calibration-monitoring-system-/assets/137410154/48da9327-c1ec-4dc7-aad7-096768cd4b1d)

![image](https://github.com/j0gea/Posture-calibration-monitoring-system-/assets/137410154/b3a3a279-823a-4804-b134-623be4d2e4f7)

- [1] 왼쪽, 디바이스 형태, client -- 가속도 센서와 연결
- [2] 오른쪽, 데이터베이스, Server -- RFID와 연결


Flow chart
--
![image](https://github.com/j0gea/Posture-calibration-monitoring-system-/assets/137410154/cf867ce6-ccf1-4bcb-a594-b8868c68ba40)


