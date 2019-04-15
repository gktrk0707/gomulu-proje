# Mağazalar için müşteri sayma sistemi

Projeyi kullanabilmeniz için;

Raspberry pi üzerinde yüklü olması gereken programlar

1-)python3

2-)opencv

3-)python dropbox kütüphanesi

Bilgisayarda yüklü olması gereken programlar

1-)python3

2-)python matplotlib kütüphanesi

3-)python numpy kütüphanesi

4-)python dropbox kütüphanesi

Ayrıca bir dropbox hesabı açılmalı ve dropbox hesabının access token'ı alınmalıdır
Bu işlemlerin nasıl yapıldığı gömülü_proje.odt dosyasında detaylarıyla birlikte açıklanmıştır.

NOT : Github desteklemediği için veri klasörü ikiye bölünmüş olup geri kalan dosyalar 'icindeki_dosyalari_veri_klasorune_kopyalayın' klasöründe bulunmaktadır projenin düzgün çalışması için '
icindeki_dosyalari_veri_klasorune_kopyalayın' klasörünün içindeki dosyaların 'veri' klasörüne aktarılması gerekmektedir

NOT2 : Projenin canlı video kamera ile çalıştırılabilmesi için 'proje.py' dosyasında 6.satırın "capture = cv2.VideoCapture(0)" şeklinde değiştirilmesi gerekmektedir ayrıca kamera açısına bağlı olarak 'cizgi_y' değerinin değiştirilmesi ve eğer x ekseniylede işlem yapılacaksa kodların x eksenine görede düzenlenmesi gerekmektedir. (proje.py dosyası videoya göre düzenlenmiş olup sadece düz giriş ve düz çıkış olduğu için y ekseninde işlemler yapılmıştır.)
