import cv2



nplateCascade = cv2.CascadeClassifier("front/haarcascade_russian_plate_number.xml")
minArea = 1000
count = 0

while True:
    img = img = cv2.imread("image/car1.jpg")
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    numberPlate = nplateCascade.detectMultiScale(img_gray,1.14,8)
    for (x,y,w,h) in numberPlate:
        area = w*h
        if area > minArea:
            cv2.rectangle(img,(x,y-30),(x+w+30,y+h),(0,0,255),2)
            cv2.putText(img,"NUmber Plate",(x,y-35),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,0,0),2)
            
   
        imgRoi = img[y-30:y+h,x:x+w+30]
        cv2.imshow("Roi",imgRoi)
        cv2.imshow("Original",img)
    if cv2.waitKey(1) & 0xFF == ord("e"):
                  count+= 1
                  cv2.imwrite("Imagefortrain/license"+str(count)+".jpg",imgRoi)
                  cv2.putText(img,"SAVE",(50,50),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(0,255,0),2)
                  cv2.waitKey(500)
    