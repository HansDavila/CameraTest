import cv2
import serial
import time
import threading

from Tools.scripts.var_access_benchmark import A



car_cascade = cv2.CascadeClassifier('cars.xml')
cap = cv2.VideoCapture('videoCarro.mp4')
deteccion = cv2.createBackgroundSubtractorMOG2(history=10000, varThreshold=12)

def monitoreo(id):
    while True:
        cont = 0
        _, img = cap.read()
        _,binarizada = cv2.threshold(img,210,255,cv2.THRESH_BINARY)
        # img = cv2.resize(img,(1280,720))
        print("image.shape = ", img.shape)
        #cv2.rectangle(img, (50, 80), (100, 100), (255, 0, 0), -1)

        zona = img[10:900, 25:350]

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, 1.1, 6)

        ActualCont = 0
        # mascara = deteccion.apply(zona)
        for (x, y, w, h) in cars:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            ActualCont = ActualCont + 1
            cv2.putText(img, "" + str(ActualCont), (x - 10, y - 10), 1, 1, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.imshow('img', img)
        #cv2.imshow('binary', binarizada)






        # if(ActualCont >= 4):
        #   print("VERDE")
        #   ser.write(str(ActualCont).encode())
        # elif ActualCont < 4:
        #    ser.write(str(ActualCont).encode())
        #    print("ROJO")

        #time = (ActualCont * 2) + 10;
        print("HILO [" + str(id) + "] -> Cars " + str(ActualCont))
        print("HILO [" + str(id) + "] -> Tiempo " + str(time) + " segundos.")
        # Mando el conteo de carros


        # Mando el tiempo
        #ser.write(str(time).encode('ascii'))

        #cv2.imshow("Zona de interes", zona)
        k = cv2.waitKey(40)

        if k == 27:
            break

    cap.release()

    return

t1 = threading.Thread(name="hilo1", target=monitoreo, args=(1,))
t1.start()
t1.join()


