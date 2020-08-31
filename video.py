import os
import time
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, timedelta

# 현재 시간 기준으로 동영상 저장 날짜와 1일 이상 차이나면 삭제!
# 해야할 일 목록
# 1. 현재 시간 구하기
# 2. 현재 폴더 내 파일의 저장 날짜 구하기
# 3. 현재 폴더 내 파일 목록 구하기
# 4. 1일 이상 차이나면 삭제 

def del_video():
    # 1. 현재 시간 구하기 
    currentTime = time.time()  #현재 시간 가져오기. type : float
    date = time.gmtime(currentTime) #현재 시간이 제대로 나오는지 확인용
    print(date)
    
    #3. 현재 폴더 내 파일 목록
    folder = os.getcwd() #현재 폴더(디렉토리) 경로

    #  filename : 삭제할 파일을 담은 리스트. .py 확장자인지 확인해서 만약 그렇다면 filename에서 배제.
    filename = [file_name for file_name in os.listdir(folder) if os.path.splitext(file_name)[-1] != '.py'] 
    
    # 파일 이름을 
    for File in filename:
        # 2. 
        saveTime = os.path.getctime(File)   # 파일 저장 시간
        date1 = time.localtime(saveTime)    # 파일 저장시간 확인용
        print("savetime : ",date1)
        
        # 현재 시간과 파일 저장시간 차이
        time_lapse = currentTime - saveTime # 파일 저장시간 차이. type : float

        hour, rest = divmod(time_lapse, 3600)
        minuate, second = divmod(rest, 60)
        
        print("타임랩스 \n\n\nhour : %f, minuate : %f, second : %f" % (hour,minuate,second)) # 시간 차이 확인

        #4.
        # hour이 24 이상이면 해당 파일 삭제
        if hour >= 24.0:
            #해당 파일 삭제 코드
            os.remove(File)
            print(File, "파일을 삭제했습니다.\n\n\n")
            
        else:
             print(File, " 파일을 삭제하지 않았습니다.\n\n####\n")
             

schedule = BlockingScheduler()
schedule.add_job(del_video, 'interval', seconds=5)
#schedule.add_job(del_video, 'interval', hours=1)    #스케줄링 예약 : interval 방식

#스케줄링 시작
schedule.start()