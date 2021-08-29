import cv2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 얼굴, 눈 탐지기
face_cascade = cv2.CascadeClassifier('../haarcascade_classifier/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('../haarcascade_classifier/haarcascade_eye.xml')

eyeCnt = 0
cap = cv2.VideoCapture(0)

# Webdriver  실행
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome('../chromedriver.exe', options=options)

# Webdriver에서 임의의 뉴스 기사 페이지 접속
driver.get('https://news.naver.com/main/read.naver?mode=LSD&mid=shm&sid1=105&oid=031&aid=0000621051')

# 웹 스크롤 함수
def doScrollDown() :
    body = driver.execute_script("return document.body")
    for i in range(1) :
        body.send_keys(Keys.PAGE_DOWN)

# 눈과 눈동자 인식 함수
def detectEyesAndPupils() :    
    global eyeCnt

    # 눈 탐색
    eyes = eye_cascade.detectMultiScale(eye_gray)

    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(eye_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)  # 눈 사각형 그리기

        roi_color = eye_color[ey : ey + eh, ex : ex + ew]
        roi_gray = eye_gray[ey : ey + eh, ex : ex + ew]
        rows, cols, _ = roi_color.shape

        roi_gray = cv2.GaussianBlur(roi_gray, (7,7), 0)

        # 홍채 탐색
        _, threshold = cv2.threshold(roi_gray, 40, 255, cv2.THRESH_BINARY_INV)
        contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

        for cnt in contours:
            (x,y,w,h) = cv2.boundingRect(cnt)
            cv2.rectangle(roi_color, (x,y), (x+w, y+h), (255, 0, 0), 2) # 홍채 사각형 그리기
            cv2.line(roi_color, (x+int(w/2), 0), (x+int(w/2), rows), (0, 255, 0), 1)    # 동공 중심을 지나는 눈 세로선
            cv2.line(roi_color, (0, y+int(h/2)), (cols, y+int(h/2)), (0,255,0), 1)  # 동공 중심을 지나는 눈 가로선
            cv2.line(roi_color, (x+int(w/2), y+int(h/2)), (x+int(w/2), y+int(h/2)), (0, 0, 255), 2) # 동공 중심
            
            # 눈 세로길이에 대한 동공부터 눈 하단까지의 비율 
            rat = (rows - (y + int(h/2))) / rows * 100  
            print(f'{rat}%')
            cv2.line(roi_color, (x+int(w/2), y+int(h/2)), (x+int(w/2), rows), (0, 255, 255), 2) # 동공부터 눈 하단까지 세로선

            if(rat < 47) :  # 사용자 맞춤 비율 적용
                eyeCnt += 1
            
            if(eyeCnt >= 7) :   # 사용자의 읽기 속도에 따라 맞춤 적용
                eyeCnt = 0
                doScrollDown()

            break

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        # 인식된 얼굴에 사각형 그리기
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        eye_color = frame[y:y+h, x:x+w]
        eye_gray = gray[y:y+h, x:x+w]

        # 눈과 눈동자 인식
        detectEyesAndPupils()

    cv2.imshow("eye", frame)
    key = cv2.waitKey(30)
    if key == 27:
        break
        
cv2.destroyAllWindows()
