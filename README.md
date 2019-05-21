# Rasperry Pi Kullanarak Mağazaya Giren İnsan Sayısını Sayma ve Grafik Olarak Yansıtma

Bu proje mağazalara giren insanları sayan bir tasarımdır. Raspberry pi ve bir web kamera kullanarak görüntü işleme ile mağazaya giren insanları sayan ardından sayma işlemini bitirdiktan sonra verileri bulut sistemine gönderen bir düzenek haline getirilmiştir. Bu proje, mağaza yöneticileri için yapacakları indirimlerin veya ne zaman mal sevkiyatı yapmaları gerektiğine dair bir referans olabilir. Bu projede Raspberry pi, USB web kamera, görüntü işleme ve bulut servisi kullanılmıştır.

Projede, üzerinden canlı video yayını alacağımız bir web kamerası bulunmaktadır. Projeyi oluşturan temel dört kısım bulunmaktadır.

Bunlar :

1-)Belirlenen zaman aralığında mağazaya giren insanların girdikleri zamanı veri olarak kaydetmek

2-)Elde edilen verileri görüntü alma işlemi bitirildikten sonra bulut sistemine yüklemek

3-)Bulut sisteminde bulunan verilerin grafik olarak görüntülenmek istenen bilgisayarda bulunan verilerden farklı olması halinde indirilmesi

4-)Verilerin günlük, aylık ve yıllık olarak grafikte gösterilmesi

Projede donanım olarak Raspberry pi ve USB web kamera, yazılım olarak opencv, python ve python kütüphaneleri kullanılmıştır. Raspberry Pi kurulumumuzda Raspbian Jessie OS var.

**Gerekli Donanım Bileşenleri**

**1.** 1 adet Rasperry pi

**2.** 1 adet  Web Kamera

**Gerekli Yazılım Bileşenleri**

 1. Raspbian Jessie OS (www.raspbian.org)
 2. Opencv (https://opencv.org/)
 3. Python 3 ([https://www.python.org](https://www.python.org/))
 4. Matplotlib ([https://matplotlib.org/](https://matplotlib.org/))
 5. Numpy ([http://www.numpy.org/](http://www.numpy.org/))
 6. Dropbox hesabı (https://www.dropbox.com)

**Kullanılan Bileşenlerin Özellikleri**

 1. Rasperry pi :Raspberry pi İngiltere’de pi vakfı tarafından geliştirilen kredi kartı boyutlarında bir cep bilgisayardır.

Projede Raspberry pi 3 model B kullanılmıştır.

Raspberry pi 3 model B [https://www.robotistan.com/raspberry-pi-3](https://www.robotistan.com/raspberry-pi-3) adresinden temin edilmiştir.

 2. USB Web Kamera :Web kamera, bilgisayara bağlanan ve gerçek hayattaki görüntüleri bilgisayara tıpkı bir video kayıt aygıtı gibi aktarmanıza olanak sağlayan aygıtların adıdır.

Kullanılan USB Web Kamera [https://www.hepsiburada.com/everest-sc-301-5-2mp-usb-isik-ayarli-mikrofonlu-tak-pc-kamera-p-BDUCZLKPC-2530](https://www.hepsiburada.com/everest-sc-301-5-2mp-usb-isik-ayarli-mikrofonlu-tak-pc-kamera-p-BDUCZLKPC-2530) adresiden temin edilmiştir.

Ayrıca bir dropbox hesabı açılmalı ve dropbox hesabının access token'ı alınmalıdır
Bu işlemlerin nasıl yapıldığı gömülü_proje.odt dosyasında detaylarıyla birlikte açıklanmıştır.

**NOT** : Github desteklemediği için veri klasörü ikiye bölünmüş olup geri kalan dosyalar 'icindeki_dosyalari_veri_klasorune_kopyalayın' klasöründe bulunmaktadır projenin düzgün çalışması için '
icindeki_dosyalari_veri_klasorune_kopyalayın' klasörünün içindeki dosyaların 'veri' klasörüne aktarılması gerekmektedir

**NOT2** : Projenin canlı video kamera ile çalıştırılabilmesi için 'proje.py' dosyasında 6.satırın "capture = cv2.VideoCapture(0)" şeklinde değiştirilmesi gerekmektedir ayrıca kamera açısına bağlı olarak 'cizgi_y' değerinin değiştirilmesi ve eğer x ekseniylede işlem yapılacaksa kodların x eksenine görede düzenlenmesi gerekmektedir. (proje.py dosyası videoya göre düzenlenmiş olup sadece düz giriş ve düz çıkış olduğu için y ekseninde işlemler yapılmıştır.)
