import tkinter as tk
from tkinter import *
import socket
import threading
import time
import pymysql
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
GPIO.setwarnings(False) 

# 서버 연결 부분 

global stop
global con
stop = 0
con = 1

# socket connection 
HOST = '0.0.0.0' 
PORT = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')

try:
    s.bind((HOST, PORT))
except socket.error:
    print ('Bind failed ')

def connection_socket():
    
    def warningGUI(data):
        
        # close funtion 
        def conison():
            # wait 
            global con
            con = 1
            warningGUI.destroy()
    
        warningGUI =tk.Tk()
        warningGUI.geometry("330x400") #창사이즈
        warningGUI.resizable(width=False,height=False) #창움직임XX

        warningGUI.title("SC:StudyCafe") #창제목
        warningGUI_Label = tk.Label(warningGUI,text='현재 허리의 각도는 기준치 보다 \n\n %.2f도 벗어나있습니다.(기준치: 90도). \n \n \n 자세가 좋지 않습니다.' %(90 - (float(data))))
        warningGUI2_Label= tk.Label(warningGUI,text='자세를 고쳐앉으세요.')
        # continue btn
        warningBT= tk.Button(warningGUI,text='계속하기',width=20,height=3,command=conison)
        warningGUI_Label.place(x=50,y=100)
        warningBT.place(x=50,y=255)
    
        warningGUI.mainloop()  
  


    # soket connection 2 
    s.listen(5)
    print ('연결을 기다리고 있습니다.')
    (conn, addr) = s.accept()
    print ('연결완료')

    while True:
        global con
        global stop
            
        # if user select to stop 
        if stop == 1:
            stop = 0
            print("측정을 종료합니다.")
            break
        
        # recive and print 
        data = conn.recv(1024).decode()
        print ('각도: ' , data)
        reply = ''
        
        # if data is more then 75 and stop
        if float(data) < 75:
            warningGUI(data)
            while True:
                data = conn.recv(1024).decode()
                
                # if user closed the warningUI
                # then, continue 
                if con == 1:
                    con = 0
                    break
                print("wait")


    # connection closed
    conn.close()


###회원일경우GUI
#DB접속
db=pymysql.connect(host='localhost',user='root',password='1234',db='NFC_DB',charset='utf8')
#NFC 태그 및 DB에서 확인



#메인시작GUI

def mainGUI():
    def Tag():

        reader=SimpleMFRC522()
        print(reader.read())
    
        try:
            tagid, text = reader.read()
        finally:
            GPIO.cleanup()


        cur=db.cursor()

        try:
            cur.execute("SELECT * FROM NFC_DB.USERS WHERE id = " + str(tagid));

            rows=cur.fetchall()
            user1=list(rows[0])
            user1_id=user1[0]
            user1_name=user1[1]
   
    
            if (tagid==user1_id):
                mainGUI.destroy()
                userGUI(user1_name)

        except:
            mainGUI_Label.config(text='등록된 사용자가 아닙니다.'
            +'\n \n \n등록하시려면 관리자에게 문의하세요. '
            +'\n \n \n 다시 시도해 주세요.')
            Tag()
        

        
        
    mainGUI=tk.Tk()
    mainGUI.geometry("330x400") #창사이즈
    mainGUI.resizable(width=False,height=False) #창움직임XX

    mainGUI.title("SC:StudyCafe") #창제목
    mainGUI_Label = tk.Label(mainGUI,text='회원카드를 태그하세요.') #NFC태그 창
    mainGUI_Label.place(x=100,y=100)
    
    thread_2 = threading.Thread(target=Tag)
    thread_2.daemon = True
    thread_2.start()

    mainGUI.mainloop()
   

#함수 1 scstart : 자세측정 창

def scstartGUI():

    # when user select to stop 
    def stop():
        global stop
        stop = 1
        scstartGUI.destroy()
        

    
    scstartGUI =tk.Tk()
    scstartGUI.geometry("330x400") #창사이즈
    scstartGUI.resizable (width=False,height=False) #창움직임XX

    scstartGUI.title("SC:StudyCafe") 
    scstartGUI_Label =tk.Label(scstartGUI,text='자세를 측정 중입니다.')
    scstartGUI_Button= tk.Button(scstartGUI,text='종료하기',width=20,height=3,command=stop) 
    scstartGUI_Label.place(x=100,y=100)

    scstartGUI_Button.place(x=80,y=255)
    
    thread_1 = threading.Thread(target=connection_socket)
    thread_1.daemon = True
    thread_1.start()
    
    scstartGUI.mainloop()
    
def userGUI(username):
    
    userGUI=tk.Tk()
    userGUI.geometry("330x400") #창사이즈
    userGUI.resizable(width=False,height=False) #창움직임XX

    userGUI.title("SC:StudyCafe") #창제목
    userGUI_Label = tk.Label(userGUI,text='환영합니다. %s \n \n \n자세 측정을 시작하려면 아래 시작버튼을 누르세요.' % username) #NFC태그 창
    userGUI_Label.place(x=20,y=20)

        
    #버튼생성
    startBT= tk.Button(userGUI,text='시작하기',width=20,height=3,command=scstartGUI) #시작하기 버튼 함수:scstart
    quitBT= tk.Button(userGUI,text='종료하기',width=20,height=3,command=userGUI.destroy) 
    
    #버튼배치
    startBT.place(x=70,y=155)
    quitBT.place(x=70,y=235)
    
    
    userGUI.mainloop() 
    

mainGUI()









