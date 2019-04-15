import numpy as np
import matplotlib.pyplot as plt
import os
import time
import dropbox

saat=('10.00','10.30','11.00','11.30','12.00','12.30','13.00','13.30','14.00','14.30','15.00','15.30','16.00','16.30','17.00','17,30','18.00')
ay=('01','02','03','04','05','06','07','08','09','10','11','12')
yıl=('14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30')


dbx=dropbox.Dropbox("sizin Dropbox access_tokeniniz") #*******************************************************


os.chdir(os.getcwd()+"/veri/")
veri=os.listdir()
def günlük():
    günlük=[]
    tarih=input("grafikte görmek istediğiniz verinin tarihini aa_gg_yy olarak giriniz :")
    if tarih+".txt" in verii:
        with open(tarih+".txt","r") as dosya:
            veri=dosya.readlines()
            for i in range(10,18):
                ilk=0
                ikinci=0
                for k in veri:
                    if k[:2]==str(i):
                        if 0<=int(k[3:5])<30:
                            ilk+=1
                        elif 30<=int(k[3:5])<60:
                            ikinci+=1
                günlük.append(ilk)
                günlük.append(ikinci)
            günlük.append(0)
            uzunluk=np.arange(len(saat))
            plt.title("{} tarihinin günlük grafiği".format(tarih.replace("_",".")))
            plt.bar(uzunluk,günlük,width=0.95,align='edge')
            plt.xticks(uzunluk,saat)
            plt.show()
    else:
        print("malesef girdiğiniz '{}' tarihli verinin kayıtları yok".format(tarih))
def ay_grafik():
    aylık=[]
    klasör=os.listdir()
    zaman=time.strftime("%y")
    zaman=str(zaman)
    tarih=input("Aylarını görüntülemek istediğiniz yılın son 2 hanesini girin :")
    try:
        if tarih in yıl:
            for i in ay:
                data=[]
                sayac=0
                for k in klasör:
                    if i==k[:2] and k[6:8]==str(tarih):
                        with open(k,"r") as dosya:
                            veri=dosya.readlines()
                            data.append(len(veri))
                for k in data:
                    sayac+=k
                aylık.append(sayac)
            uzunluk=np.arange(len(ay))
            plt.title("{} yılının aylık grafiği".format("20"+tarih))
            plt.bar(uzunluk,aylık,align='center')
            plt.xticks(uzunluk,ay)
            plt.ylim(((min(aylık)/100)*95,(max(aylık)/100)*102))
            plt.show()
        else:
            print("sadece {} yılından {} yılları arası olan veriler bulunmakta lütfen bu iki yılın ve arasındaki yılların son 2 basamağını girin".format("14",zaman))
    except:
        print("Lütfen sayı değeri girdiğinizden emin olun!!!")
def yıl_grafik():
    yıllık=[]
    for i in yıl:
        data=[]
        sayac=0
        for k in verii:
            if i==k[6:8]:
                with open(k,"r") as dosya:
                    veri=dosya.readlines()
                    data.append(len(veri))
        for k in data:
            sayac+=k
        yıllık.append(sayac)
    uzunluk=np.arange(len(yıl))
    plt.title("Yıllık grafik")
    plt.bar(uzunluk,yıllık,width=0.95,align='center')
    plt.xticks(uzunluk,yıl)
    plt.ylim(((min(yıllık)/100)*95,(max(yıllık)/100)*102))
    plt.show()
def indir():
    zaman=time.strftime('%x')
    veri2=""
    sayac=0
    for i in range(int(zaman[6:8]),0,-1):
        if sayac==1:
            break
        if len(str(i))==1:
            i="0"+str(i)
        for k in range(12,0,-1):
            if len(str(k))==1:
                k="0"+str(k)
            if sayac==1:
                break       
            for j in range(31,0,-1):
                if len(str(j))==1:
                    j="0"+str(j)
                denek=str(k)+"_"+str(j)+"_"+str(i)+".txt"
                if denek in veri:
                    veri2=denek
                    sayac=1
                    break
    veri3=veri2
    if veri2[0:2]==zaman[0:2] and veri2[6:8]==zaman[6:8]:
        for i in range(int(veri2[3:5])+1,int(zaman[3:5])+1):
            if len(str(i))==1:
                i="0"+str(i)
            veri2=veri2[0:3]+str(i)+veri2[5:]
            try:
                print(veri2)
                dbx.files_download_to_file(os.getcwd()+"/"+veri2,"/"+veri2)
            except (dropbox.exceptions.ApiError):
                continue
    else:

        if int(veri2[0:2])<int(zaman[0:2]):
            for i in range(int(veri2[0:2]),int(zaman[0:2])+1):
                if len(str(i))==1:
                        i="0"+str(i)
                veri2=veri2.replace(veri2[0:2],str(i),1)
                if int(i)==int(veri3[0:2]):
                    for k in range(int(veri2[3:5])+1,32):
                        if len(str(k))==1:
                            k="0"+str(k)
                        veri2=veri2[0:3]+str(k)+veri2[5:]
                        try:
                            print(veri2)
                            dbx.files_download_to_file(os.getcwd()+"/"+veri2,"/"+veri2)
                        except (dropbox.exceptions.ApiError):
                            continue
                elif int(i)==int(zaman[0:2]):
                    for k in range(0,int(zaman[3:5])+1):
                        if len(str(k))==1:
                            k="0"+str(k)
                        veri2=veri2[0:3]+str(k)+veri2[5:]
                        try:
                            print(veri2)
                            dbx.files_download_to_file(os.getcwd()+"/"+veri2,"/"+veri2)
                        except (dropbox.exceptions.ApiError):
                            continue
                else:
                    for k in range(0,32):
                        if len(str(k))==1:
                            k="0"+str(k)
                        veri2=veri2[0:3]+str(k)+veri2[5:]
                        try:
                            print(veri2)
                            dbx.files_download_to_file(os.getcwd()+"/"+veri2,"/"+veri2)
                        except (dropbox.exceptions.ApiError):
                            continue
        else:
            
            for i in range(int(veri2[0:2]),13):
                veri2=veri2.replace(veri2[0:2],str(i),1)


                if int(i)==int(veri3[0:2]):
                    for k in range(int(veri2[3:5])+1,32):
                        if len(str(k))==1:
                            k="0"+str(k)
                        veri2=veri2[0:3]+str(k)+veri2[5:]
                        try:
                            print(veri2)
                            dbx.files_download_to_file(os.getcwd()+"/"+veri2,"/"+veri2)
                        except (dropbox.exceptions.ApiError):
                            continue
                else:
                    for k in range(0,32):
                        if len(str(k))==1:
                            k="0"+str(k)
                        veri2=veri2[0:3]+str(k)+veri2[5:]
                        try:
                            print(veri2)
                            dbx.files_download_to_file(os.getcwd()+"/"+veri2,"/"+veri2)
                        except (dropbox.exceptions.ApiError):
                            continue
            veri2=veri2[0:6]+str(int(veri2[6:8])+1)+veri2[8:]
            for i in range(1,int(zaman[0:2])+1):
                if len(str(i))==1:
                        i="0"+str(i)
                veri2=veri2.replace(veri2[0:2],str(i),1)
                
                if int(i)==int(zaman[0:2]):
                    for k in range(0,int(zaman[3:5])+1):
                        if len(str(k))==1:
                            k="0"+str(k)
                        veri2=veri2[0:3]+str(k)+veri2[5:]
                        try:
                            print(veri2)
                            dbx.files_download_to_file(os.getcwd()+"/"+veri2,"/"+veri2)
                        except (dropbox.exceptions.ApiError):
                            continue
                else:
                    for k in range(0,32):
                        if len(str(k))==1:
                            k="0"+str(k)
                        veri2=veri2[0:3]+str(k)+veri2[5:]
                        try:
                            print(veri2)
                            dbx.files_download_to_file(os.getcwd()+"/"+veri2,"/"+veri2)
                        except (dropbox.exceptions.ApiError):
                            continue
sayı=input("""Merhaba sayın kullanıcı...
Eğer günlük grafiği görmek istiyorsan 'günlük'
Eğer aylık grafiği görmek istiyorsan 'aylık'
Eğer yıllık grafiği görmek istiyorsan 'yıllık'
Eğer 3 grafiği birden görüntülemek istiyorsanız üçlü yazın
(NOT:olmayan verilerin indirilme işleme otomatik olarak başlatılacaktır)
(NOT2:üçlü grafiği seçmeniz halinde pencereler teker teker açılacaktır) :
""")
print("indirme işlemi başlıyor indirilen veriler :")        
indir()
verii=os.listdir()
if sayı=="günlük":                
    günlük()
elif sayı=="aylık":
    ay_grafik()               
elif sayı=="yıllık":
    yıl_grafik()
elif sayı=="üçlü":
    günlük()
    ay_grafik()
    yıl_grafik()
        
