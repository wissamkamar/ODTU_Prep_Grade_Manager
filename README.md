Student-Grade-Manager – Öğrenci Not ve Devamsızlık Takip Sistemi
Sistemimiz, ODTÜ İngilizce Hazırlık öğrencilerinin dönem notlarını, devamsızlıklarını ve EPE sınavına girme haklarını takip edebilmeleri için geliştirilmiştir.

Uygulama Python ve Streamlit kullanılarak geliştirilmiştir.

1. Dönem ve kur seçimi
Öğrenci öncelikle uygulamaya girerek hangi dönemde olduğunu seçer:

*Fall (Güz)

*Spring (Bahar)

Daha sonra mevcut kurunu seçer:

*DBE101

*DBE102

*DBE103

*DBE104

*DBE105

Seçilen kura göre öğrencinin devamsızlık hakkı sistem tarafından belirlenir.

2. Devamsızlık takibi
Öğrenci, seçtiği kur için tanımlanan devamsızlık hakkını görür.

Daha sonra o dönemde toplam kaç saat derse katılmadığını sisteme girer ve ekle butonuna basar.

Sistem girilen devamsızlık saatlerini hesaplamaya dahil eder ve öğrencinin:

*Toplam devamsızlık hakkını,

*Kullandığı devamsızlık saatini,

*Kalan devamsızlık saatini,

*Devamsızlık ortalamasını ve durumunu

gösterir.

3. Sınav notu ekleme sistemi
Öğrenci daha sonra sınav notlarını sisteme girebilir.

Not ekleme işlemi üç aşamadan oluşur:

1.Sınav türünü seçer.

2.Sınav numarasını seçer.

3.Aldığı notu girer.

Son olarak Ekle butonuna basar.

Girilen sınav notu ekranın altındaki not listesine eklenir. Öğrenci aynı işlemi istediği kadar tekrarlayarak bütün sınav notlarını sisteme kaydedebilir.

4. Otomatik not hesaplama sistemi
Sistemin en önemli özelliklerinden biri, sınav notlarını otomatik olarak hesaplamasıdır.

Öğrenci not ekledikçe sistem arka planda:

*Aynı sınav türüne ait notları bir araya getirir.

*Aynı döneme ait sınavları dikkate alır.

*İlgili sınav türlerinin ortalamalarını hesaplar.

*DBE değerlendirme kurallarına göre genel ortalamayı belirler.

Hesaplanan sonuçlar uygulamanın en üst bölümünde görüntülenir.

5. Öğrencinin akademik durumunun gösterilmesi
Sistem bütün hesaplamaları tamamladıktan sonra öğrencinin durumunu en üst bölümde gösterir.




Sistemin genel çalışma sırası
1. Dönem seçimi
   Fall veya Spring.
   
2. Kur seçimi
   DBE101, DBE102, DBE103, DBE104 veya DBE105.
   
3. Devamsızlık bilgisi
   Gelinmeyen toplam ders saatini girme.
   
4. Sınav notlarını ekleme
   Sınav türü, numarası ve puanını girme.
   
5. Otomatik hesaplama
   Aynı tür ve döneme ait sınavların DBE kurallarına göre hesaplanması.

6. Sonuç ekranı
   EPE hakkı, genel not ortalaması ve devamsızlık durumunun görüntülenmesi.

Kısacası: Öğrenci yalnızca dönemini, kurunu, devamsızlık saatlerini ve sınav notlarını sisteme girer. Geri kalan hesaplamaları sistem otomatik olarak gerçekleştirir ve öğrencinin EPE sınavına girme hakkı olup olmadığını gösterir.



sonra siteye yolandirecek seni
Sistemi nasıl çalıştırıyoruz?
Uygulamayı çalıştırmak için aşağıdaki adımları takip ediyoruz.

1. Streamlit kütüphanesini yükleme
Öncelikle bilgisayarımıza Python'un Streamlit kütüphanesini indiriyoruz.

Terminali açıp şu komutu yazıyoruz:

pip install streamlit

2. Proje klasörüne girme
Terminal üzerinden projemizin bulunduğu klasöre gidiyoruz:

cd Student-Grade-Manager

4. Dosyaları kontrol etme
Proje klasöründeki dosyaları görmek için:

ls

4. Uygulamayı başlatma
Son olarak şu komutu çalıştırıyoruz:

streamlit run app.py

5. Uygulamayı açma
Bu komutu çalıştırdıktan sonra Streamlit uygulamayı başlatır ve terminalde yerel site adresini gösterir.
Genellikle:http://localhost:8501

Bu bağlantıya tıkladığımızda veya tarayıcıya yazdığımızda öğrenci not takip sistemi açılır.


Kısaca bütün komutlar:
pip install streamlit
cd Student-Grade-Manager
ls
streamlit run app.py

Artık tarayıcı üzerinden sistemimizi kullanabiliriz!
