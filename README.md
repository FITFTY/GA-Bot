### 실행하기

$ python -m venv venv

$ . venv/bin/activate


$ pip install -r ./requirements.txt 

$ date # utc 인 경우 바꿔줘야 함

$ sudo ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime 

$ date # kst 확인

$ nohup python3 GA.py 1>/dev/null 2>&1 &
