import cv2
import time
import dropbox

backsub = cv2.createBackgroundSubtractorMOG2()
capture = cv2.VideoCapture("example_02.mp4")

sayac=0
cizgi=200
yer_sayacı=0
giren_insan_sayısı=0
simdiki_veri = []
gecmis_veri = []
sayi=0
tarih=time.strftime("%x").replace("/","_")



access_token="sizin Dropbox access_tokeniniz" #****************************************************



def yükle():
    dosya.close()
    dbx = dropbox.Dropbox(access_token)
    capture.release()
    cv2.destroyAllWindows()
    with open("veri/"+tarih+".txt", "rb") as f:
        dbx.files_upload(f.read(),"/"+tarih+".txt", mute = True)

with open("veri/"+tarih+".txt","a") as dosya:
    while True:
        ret, frame = capture.read()

        if capture:
            sayi=1
            fgmask = backsub.apply(frame, None,0.018)
            cv2.line(frame, (0, 200), (400, 200), (0, 255, 0), 2)


            _,contours,_ = cv2.findContours(fgmask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

            for contour in contours :
                (x,y,w,h) = cv2.boundingRect(contour)
                if w>65 and h>65 :
                    simdiki_veri.append([x, y])
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            yer_listesi=[]
            try:
                for i in range (len(simdiki_veri)):
                    mini=1000000
                    for k in range(len(gecmis_veri)):
                        diff_x=simdiki_veri[i][0]-gecmis_veri[k][0]
                        diff_y=simdiki_veri[i][1]-gecmis_veri[k][1]
                        distance = (diff_x*diff_x)+(diff_y * diff_y)
                        if(distance<mini ):
                            mini=distance
                            yer_sayacı=k
                    yer_listesi.append(yer_sayacı)
            except IndexError:
                continue
            try:
                for i in yer_listesi:
                    for k in range(1,len(yer_listesi)):
                        if i==yer_listesi[k]:
                            yer_listesi.pop(k)
                            yer_listesi.insert(k,"pass")
            except IndexError:
                continue
            for i in range (len(simdiki_veri)):
                try:
                    if yer_listesi[i]=="pass":
                        pass
                    else:
                        y_previous=gecmis_veri[yer_listesi[i]][1]
                        if(simdiki_veri[i][1]<cizgi and y_previous> cizgi):
                            giren_insan_sayısı=giren_insan_sayısı+1
                            dosya.write(time.strftime('%X')+"\n")                      

                except IndexError:
                    continue
            gecmis_veri = simdiki_veri
            simdiki_veri = []



            cv2.putText(frame,"giren: "+str(giren_insan_sayısı), (220, 20), cv2.FONT_HERSHEY_SIMPLEX,0.6, (0, 0, 0), 2)

            cv2.imshow("Takip", frame)



            key = cv2.waitKey(60)
            if key == ord('q'):
                yükle()
                break
        else:
            tarih=time.strftime("%x").replace("/","_")
            if sayi==1:
                yükle()
                sayi=0

