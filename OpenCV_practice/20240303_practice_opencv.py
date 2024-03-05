import cv2
import numpy as np


def main1():
    img = cv2.imread("colorcolor.jpg")
    img = cv2.resize(img, (100,100), fx=0.5, fy=0.5)#改變圖片, resize(圖片img, (像素tuple), fx=長比例, fy=寬比例)
    print(img.shape)
    cv2.imshow("img", img)
    cv2.waitKey(0)

def main2():
    cap = cv2.VideoCapture("thumb.mp4")#讀取影片
    while True:
        ret, frame = cap.read()#ret為讀取成功與否回傳T/F, frame是每一偵的圖片array
        
        if ret:
            frame = cv2.resize(frame, (0,0), fx=0.4, fy=0.4)
            cv2.imshow("video",frame)
        else:
            break
        if cv2.waitKey(10)==ord("q"):
            break

def main3():
    cap = cv2.VideoCapture(0)#讀取外部鏡頭, 1為內建鏡頭再來就是2,3,4....
    while True:
        ret,frame = cap.read()
        if ret:
            frame = cv2.resize(frame, (0,0), fx=0.4, fy=0.4)
            cv2.imshow("video", frame)
        else:
            break
        if cv2.waitKey(10)==ord("q"):
            break

def main4():
    img0 = cv2.imread("colorcolor.jpg")
    print(img0.shape)#(長, 寬, 顏色)
    #顏色順序為[B, G, R]
    img = np.empty((300,300,3), np.uint8)
    for row in range(300):
        for col in range(300):
            img[row][col]=[255,0,0]#將所有array中的元素都改成B()藍色
    cv2.imshow("img", img)
    cv2.waitKey(0)

def main5():#將所有array中的元素都改成隨機顏色
    img = np.empty((300,300,3), np.uint8)
    for row in range(300):
        for col in range(300):
            img[row][col]=[np.random.randint(0,255), np.random.randint(0,255), np.random.randint(0,255)]
    cv2.imshow("img", img)
    cv2.waitKey(0)

def main5():#將所有colorcolor.jpg中長300個像素都改成隨機顏色
    img = cv2.imread("colorcolor.jpg")
    for row in range(300):
        for col in range(img.shape[1]):
            img[row][col]=[np.random.randint(0,255), np.random.randint(0,255), np.random.randint(0,255)]
    cv2.imshow("img", img)
    cv2.waitKey(0)

def main6():#取得局部範圍
    img = cv2.imread("colorcolor.jpg")
    new_img = img[150:400,200:400]#[高度:寬度]
    cv2.imshow("img", img)
    cv2.imshow("new_img", new_img)
    cv2.waitKey(0)

def main7():#影像處理時常用到的功能
    img = cv2.imread("colorcolor.jpg")
    img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#將img轉成灰階COLOR_BGR2GRAY (圖片名, 顏色樣式)
    blur = cv2.GaussianBlur(img, (15,15), 10)#將img做成模糊 (圖片名, (3,3)必須是奇數, 標準差)
    canny = cv2.Canny(img, 150, 200)#抓取圖片中的邊緣 (圖片名, 最低值, 最高值)
    dilate = cv2.dilate(canny, np.ones((3,3), np.uint8), iterations=1)#將邊緣膨脹 (圖片名, 2維陣列, iteration=膨脹次數)
    erode = cv2.erode(dilate, np.ones((3,3), np.uint8), iterations=1)#將邊緣侵蝕 (圖片名, 2維陣列, iteration=侵蝕次數)
    
    cv2.imshow("erode",erode)
    cv2.imshow("dilate",dilate)
    cv2.imshow("canny",canny)
    cv2.imshow("blur",blur)
    cv2.imshow("gray",gray)
    cv2.imshow("img",img)
    cv2.waitKey(0)

def main8():#畫圖/寫字
    img = np.zeros((600,600,3), np.uint8)
    cv2.line(img, (0,0), (img.shape[1],img.shape[0]), (255,0,0), 1)#劃一條線在img圖片中 (圖片名, 起始座標, 結束座標, 顏色, 線條寬度)
    cv2.rectangle(img, (0,0), (400,300), (0,0,255), cv2.FILLED)#劃一方形在img圖片中 (圖片名, 起始座標, 結束座標, 顏色, 線條寬度/是否填滿)
    cv2.circle(img, (300,400), 30, (255,0,0), cv2.FILLED)#劃一圓形在img圖片中 (圖片名, 起始座標, 結束座標, 顏色, 線條寬度/是否填滿)
    cv2.putText(img, "Hellow", (100,500), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (255,255,255), 1)#在img圖片中寫字 (圖片名, 文字, 座標, 文字字體, 文字大小, 文字顏色, 文字寬度)

    cv2.imshow("img", img)
    cv2.waitKey(0)

def main9():#偵測圖片中的特定顏色
    def empty(v):
        pass

    #img = cv2.imread(r"D:\Software\ML\GrandmaCan_python_opencv-main\XiWinnie.jpg")
    #img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
    cap = cv2.VideoCapture(0)
    
    cv2.namedWindow("TrackBar")#創建名為"TrackBar"的視窗
    cv2.resizeWindow("TrackBar", 640, 320)#調整名為Trackbar的視窗大小
    cv2.createTrackbar("Hue Min", "TrackBar", 0, 179, empty)#在Trackbar中創建名為"Hue Min"的調整儀
    cv2.createTrackbar("Hue Max", "TrackBar", 179, 179, empty)
    cv2.createTrackbar("Sat Min", "TrackBar", 0, 255, empty)
    cv2.createTrackbar("Sat Max", "TrackBar", 255, 255, empty)
    cv2.createTrackbar("Val Min", "TrackBar", 0, 255, empty)
    cv2.createTrackbar("Val Max", "TrackBar", 255, 255, empty)

    
    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)#將顏色轉換為HSV((色調)Hue, (飽和度)Saturation, (亮度)Value)
        if ret:
            h_min = cv2.getTrackbarPos("Hue Min", "TrackBar")
            h_max = cv2.getTrackbarPos("Hue Max", "TrackBar")
            s_min = cv2.getTrackbarPos("Sat Min", "TrackBar")
            s_max = cv2.getTrackbarPos("Sat Max", "TrackBar")
            v_min = cv2.getTrackbarPos("Val Min", "TrackBar")
            v_max = cv2.getTrackbarPos("Val Max", "TrackBar")
            print(h_min, h_max, s_min, s_max, v_min, v_max)
            lower = np.array([h_min, s_min, v_min])
            upper = np.array([h_max, s_max, v_max])
            mask = cv2.inRange(hsv, lower, upper)
            result = cv2.bitwise_and(frame, frame, mask=mask)

            cv2.imshow("img", frame)
            cv2.imshow("hsv", hsv)
            cv2.imshow("mask", mask)
            cv2.imshow("result", result)
        else:
            break
        if cv2.waitKey(10)==ord(" "):
            break


        cv2.waitKey(1)

def main10():#偵測邊緣

    img = cv2.imread("shape.jpg")
    imgContour = img.copy()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(img, 150, 200)
    contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    #偵測輪廓函式-findContours(要偵測的圖片, 模式, 近似方法), 回傳輪廓與皆層
    for cnt in contours:
        cv2.drawContours(imgContour, cnt, -1, (255,0,0), 4)#畫圖 在imgContour上 (指定圖名(被畫的), 要畫的輪廓, -1, 指定顏色, 線條粗度)
        
        area = cv2.contourArea(cnt)#取得指定輪廓的面積

        if area > 500:
            peri = cv2.arcLength(cnt, True)#取得指定輪廓的周長
            vertices = cv2.approxPolyDP(cnt, peri*0.02, True)#近似值用來改變每個圖形的點量 approxPolyDP(輪廓, 精度參數, 布林直(密合/開放))
            corners = (len(vertices)) 
            
            x ,y, w, h = cv2.boundingRect(vertices)#將vertices的形狀以方形框起來, 回傳四個值(左上座標(x,y), 框高(w,h))
            cv2.rectangle(imgContour, (x,y), (x+w, y+h), (0,255,0),4)#劃一個四邊形 rectangle(被畫的圖, (左上座標), (右下座標), (顏色), 粗度)

            if corners==3:
                cv2.putText(imgContour, "triangle", (x,y-5), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2
                            )#在圖片中寫入文字 putText(被寫的圖片, "要寫的文字", (座標), 字體, 文字大小, (顏色), (粗度))
            elif corners==4:
                cv2.putText(imgContour, "rectangle", (x,y-5), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2
                            )
            elif corners==5:
                cv2.putText(imgContour, "pentagon", (x,y-5), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2
                            )
            elif corners>=6:
                cv2.putText(imgContour, "circle", (x,y-5), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2
                            )

    #cv2.imshow("img", img)
    #cv2.imshow("canny", canny)
    cv2.imshow("imgContour",imgContour)
    cv2.waitKey(0)

def main11():
    img = cv2.imread("qq.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faceCascade = cv2.CascadeClassifier("face_detect.xml")
    faceRect = faceCascade.detectMultiScale(gray, 1.1, 5)

    for (x,y,w,h) in faceRect:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

    cv2.imshow("img", img)
    cv2.waitKey(0)

def main12():
    
    cap = cv2.VideoCapture(0)
    
    SmileCascade = cv2.CascadeClassifier("haarcascade_smile.xml")
    faceCascade = cv2.CascadeClassifier("face_detect.xml")
    
    while True:
        ret, frame = cap.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faceRect = faceCascade.detectMultiScale(gray, 1.2, 5)

            for (x,y,w,h) in faceRect:
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

            cv2.imshow("videos", frame)
            cv2.imshow("gray", gray)
        else:
            break
        if cv2.waitKey(10)==ord("q"):
            break

def main13():

    cap = cv2.VideoCapture(0)
    
    PenColorHSV = [ 
                    [91, 110, 158, 255, 181, 255],
                    [169, 179, 110, 204, 132, 255],
                                                ]

    PenColorBGR = [[255,0,0],[0,0,255]]

    DrawPoints = []

    def findPen(img):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)#將顏色轉換為HSV((色調)Hue, (飽和度)Saturation, (亮度)Value)
        
        for i in range(len(PenColorHSV)):
            lower = np.array(PenColorHSV[i][:3])
            upper = np.array(PenColorHSV[i][3:6])
            mask = cv2.inRange(hsv, lower, upper)
            result = cv2.bitwise_and(img, img, mask=mask)
            penx, peny = findContour(mask)
            cv2.circle(imgContour, (penx,peny), 10,PenColorBGR[i],cv2.FILLED)
            #cv2.imshow("result", result)
            if peny!=-1:
                DrawPoints.append([penx,peny,i])


    def findContour(img):
        contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        #偵測輪廓函式-findContours(要偵測的圖片, 模式, 近似方法), 回傳輪廓與皆層
        x,y,w,h = -1,-1,-1,-1
        for cnt in contours:
            #cv2.drawContours(imgContour, cnt, -1, (255,0,0), 4)#畫圖 在imgContour上 (指定圖名(被畫的), 要畫的輪廓, -1, 指定顏色, 線條粗度)
            area = cv2.contourArea(cnt)#取得指定輪廓的面積
            if area > 0:
                peri = cv2.arcLength(cnt, True)#取得指定輪廓的周長
                vertices = cv2.approxPolyDP(cnt, peri*0.02, True)#近似值用來改變每個圖形的點量 approxPolyDP(輪廓, 精度參數, 布林直(密合/開放))
                x ,y, w, h = cv2.boundingRect(vertices)#將vertices的形狀以方形框起來, 回傳四個值(左上座標(x,y), 框高(w,h))

        return x+w//2,y

    def Draw(DrawPoints):
        for point in DrawPoints:
            cv2.circle(imgContour, (point[0], point[1], 10, PenColorBGR[point[2]], cv2.FILLED))


    while True:
        ret, frame = cap.read()
       
        if ret:
            imgContour = frame.copy()
            #cv2.imshow("video",frame)
            findPen(frame)
            Draw(DrawPoints)
            cv2.imshow("contour", imgContour)
        else:
            break
        if cv2.waitKey(10)==ord(" "):
            break

if __name__=="__main__":
    #main9()
    main13()
    91, 110, 158, 255, 181, 255
    169, 179, 110, 204, 132, 255