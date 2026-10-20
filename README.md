# Hafta 3
Bu depoda, ders kapsamında gerçekleştirilen ağ güvenliği ve sızma testleri uygulamalarının ekran görüntüleri ve açıklamaları yer almaktadır.

Temel Kavramlar:

ARP (Address Resolution Protocol - Adres Çözümleme Protokolü): Yerel ağda (LAN) bir cihazın bildiği IP adresine karşılık gelen fiziksel MAC adresini bulmasını sağlayan ağ protokolüdür. Cihazlar birbirleriyle haberleşmeden önce ARP kullanarak "Bu IP adresine sahip cihazın MAC adresi nedir?" sorusunu ağa sorarlar.

Flooding (Taşkın / Seliçi Saldırı): Bir ağ cihazının veya sistemin kapasitesini aşacak büyüklükte ve hızda veri/istek gönderilerek kilitlenmesini veya normal işlevini yapamaz hale getirilmesini hedefleyen saldırı türüdür.
* **
Bu hafta gerçekleştirilen uygulamada, yerel ağlardaki anahtarlama (Switching) mekanizmasının çalışma mantığı ve güvenlik açıkları incelenmiştir.

Amaç: Switch cihazlarının üzerinde bulunan ve MAC adreslerini portlarla eşleştiren **CAM (Content Addressable Memory) tablosunu** kasıtlı olarak doldurmak ve ağ güvenliğindeki bir zafiyeti gözlemlemek.
Uygulama: Kali Linux işletim sistemi üzerinde `macof` aracı kullanılarak ağa saniyede yüzlerce sahte (random) MAC adresi ve paket gönderilmiştir.
Ekran görüntüsünde yer alan komut satırı (`sudo macof -i ...`) bu yoğun paket akışının üretildiğini ve sistemin trafiğe boğulduğunu göstermektedir.

### Sonuç ve Kazanımlar
1. **Bellek Taşması:** Switch'ler normalde gelen trafiği sadece ilgili hedef cihaza yönlendirir. Ancak `macof` ile tablo sonuna kadar doldurulduğunda switch belleği taşar.
2. **Hub Davranışı (Fail-Open):** Tablo dolunca switch güvenlik önlemi olarak trafiği yönetemez hale gelir ve gelen tüm paketleri bir hub gibi ağdaki herkese (**broadcast**) göndermeye başlar.
3. **Güvenlik Riski:** Bu durum, saldırganın aynı ağdaki diğer bilgisayarların trafiğini dinlemesine (Sniffing) ve Man-in-the-Middle (Ortadaki Adam) saldırılarına zemin hazırlar. Bu lab çalışması ile **Port Security** önlemlerinin neden hayati olduğu uygulamalı olarak kavranmıştır.

----------------------------------------------------------------------------------------------------------------------------------------

# Hafta 4
Basit Hedef Erişim Testi (Ping Script)

Bu proje, **Siber Güvenlik** dersi kapsamında Linux/Bash ortamında temel otomasyon becerileri kazanmak ve ağ üzerindeki hedeflerin erişilebilirliğini test etmek amacıyla geliştirilmiştir.

## Ne Amaçla Yapıldı? (Projenin Amacı)
Siber güvenlik testlerinde, ağ analizlerinde (Penetration Testing) veya günlük sistem yönetiminde hedeflenen bir IP adresinin veya web sitesinin aktif olup olmadığını (ağa yanıt verip vermediğini) hızlıca kontrol etmek kritik bir adımdır. 
Bu ödevin amacı; her defasında terminale uzun komutlar yazmak yerine, kullanıcıdan girdi (`read`) alabilen ve bu girdiyi sistem komutlarıyla (`ping`) otomatik işleyen **ilk temel Bash betiğini (script)** yazmayı öğrenmektir.

## Tam Olarak Ne İşe Yarar? (Çalışma Mantığı)
1. **Dinamik Girdi Alır:** Çalıştırıldığında kullanıcıya *"Saldırılacak websitesi veya IP adresini giriniz"* şeklinde bir komut istemi sunar.
2. **Kullanıcı Girdisini İşler:** Klavyeden girilen hedef adresi (`github.com`, `google.com` veya bir IP) hafızaya kaydeder.
3. **Erişilebilirlik Testi Yapar (Ping):** Alınan hedef adrese ICMP paketleri göndererek hedef sistemin ayakta olup olmadığını ve veri alışverişi yapıp yapamadığını test eder. Böylece hedef sistemin yanıt verip vermediği ekranda raporlanır.

-----------------------------------------------------------------------------------------------------------------------------------------


# Hafta 5

Bu depoda, Siber Güvenlik dersi kapsamında gerçekleştirilen Python ile UDP veri gönderme ve alma uygulamasına ait ekran görüntüleri ve açıklamalar yer almaktadır.

## Temel Kavramlar

**UDP (User Datagram Protocol - Kullanıcı Datagram Protokolü):** Ağ üzerindeki cihazlar arasında veri aktarımını sağlayan, bağlantı kurmadan çalışan bir taşıma katmanı protokolüdür.

**Socket (Soket):** Uygulamaların ağ üzerinden veri gönderip almasını sağlayan yazılım arayüzüdür. Python'da `socket` kütüphanesi kullanılarak ağ iletişimi gerçekleştirilebilir.

**IP Adresi ve Port:** IP adresi hedef cihazı, port numarası ise cihaz üzerindeki uygulamanın iletişim uç noktasını belirtir.

**MTU (Maximum Transmission Unit):** Bir ağ bağlantısında tek bir pakette taşınabilecek veri miktarını ifade eder. MTU sınırını aşan IP paketleri parçalanabilir veya iletim sırasında başarısız olabilir.

## Uygulamanın Amacı

Bu hafta gerçekleştirilen uygulamada, Python programlama dili kullanılarak UDP protokolü üzerinden veri gönderme ve alma işlemleri gerçekleştirilmiştir. Ayrıca büyük boyutlu verilerin aktarımı ve IP parçalanmasıyla ilgili ayarlar incelenmiştir.

## UDP Veri Gönderici (Sender)

Gönderici programında Python'un `socket` kütüphanesi kullanılarak bir UDP soketi oluşturulmuştur.

- **Hedef IP adresi:** `172.16.107.22`
- **Hedef port:** `5000`
- **Veri boyutu:** `4000` bayt
- **Protokol:** UDP

`b"A" * 4000` komutuyla 4000 baytlık veri oluşturulmuş ve `sendto()` fonksiyonu kullanılarak hedef IP adresine gönderilmiştir.

Programda ayrıca `IP_MTU_DISCOVER` ve `IP_PMTUDISC_DONT` seçenekleri kullanılarak Linux ortamındaki IPv4 Path MTU Discovery davranışıyla ilgili ayarlar yapılmıştır.

![UDP Veri Gönderici]

## UDP Veri Alıcı (Receiver)

Alıcı programında UDP soketi oluşturulmuş ve `bind()` fonksiyonu ile `0.0.0.0` adresinin `8000` portuna bağlanılmıştır.

- **Dinleme adresi:** `0.0.0.0`
- **Dinleme portu:** `8000`
- **Veri alma fonksiyonu:** `recvfrom()`

Program, gelen UDP verisini beklemekte ve veri ulaştığında gönderen cihazın IP adresini, portunu ve alınan verinin boyutunu ekrana yazdırmaktadır. Ayrıca alınan verinin ilk 40 baytı görüntülenmektedir.

Ekran görüntüsünde 4000 baytlık verinin alındığı ve gönderen adresinin `172.16.107.22` olduğu görülmektedir.

![UDP Veri Alıcı]

## Sonuç ve Kazanımlar

- Python ile UDP soketi oluşturma, veri gönderme ve veri alma işlemleri öğrenilmiştir.
- `sendto()` ve `recvfrom()` fonksiyonlarının kullanımı incelenmiştir.
- IP adresi ve port numaralarının ağ iletişimindeki önemi kavranmıştır.
- MTU ve IP parçalanması kavramları değerlendirilmiştir.
- UDP protokolünün bağlantısız yapısı ve veri teslimatını garanti etmemesi hakkında bilgi edinilmiştir.

Bu uygulama sayesinde Python ile temel ağ programlama becerileri geliştirilmiş ve UDP protokolünün çalışma mantığı uygulamalı olarak incelenmiştir.

-------------------------------------------------------------------------------------------------------------------------

# Hafta 5 (git ve github betiği)

## Otomatik Git ve GitHub Yükleme Betiği

Bu proje, Siber Güvenlik dersi kapsamında Linux/Bash ortamında temel otomasyon, sürüm kontrol süreçlerini komut satırından yönetmek ve GitHub yükleme adımlarını otomatikleştirmek amacıyla geliştirilmiştir

### Ne Amaçla Yapıldı? (Projenin Amacı)
Yazılım geliştirme, siber güvenlik araçları yazımı ve sistem yönetimi süreçlerinde hazırlanan kodların veya analiz raporlarının GitHub gibi uzak depolara (remote repository) düzenli aktarılması gerekir. Normal şartlarda bir dosyayı uzak depoya yüklemek için birden fazla terminal komutunun (`git init`, `git add`, `git commit`, `git branch`, `git remote`, `git push`) her defasında sırayla ve hatasız yazılması gerekir. Bu ödevin amacı; her seferinde bu komutları tek tek elle girmek yerine, kullanıcıdan dinamik girdi (`read`) alarak yeni bir dosya oluşturan ve tüm Git adımlarını arka planda tek seferde tamamlayan bir Bash betiği (`saldiri.sh`) yazılır.

### Tam Olarak Ne İşe Yarar? (Çalışma Mantığı)
1. **Dinamik Girdileri Alır:** Betik çalıştırıldığında kullanıcıdan önce yüklenecek dosya adını (`FILE_NAME`), ardından dosyanın gönderileceği GitHub repo adresini (`REPO_URL`) girmesini ister.
2. **Dosyayı Otomatik Oluşturur:** Kullanıcının girdiği dosya adıyla sistemde sıfırdan bir dosya oluşturur ve içine başlık formatında dosya ismini ekler (`echo "# $FILE_NAME" > "$FILE_NAME"`).
3. **Yerel Git Deposunu Hazırlar:** Bulunulan dizinde `git init` ile Git yapısını başlatır, dosyayı `git add` ile takibe alır, `git commit -m "first commit"` ile ilk kaydı oluşturur ve ana dalı `git branch -M main` olarak ayarlar.
4. **Uzak Depoyu Bağlar ve Yükler (Push):** Varsa çakışan eski remote adresini temizler (`git remote remove origin 2>/dev/null`), kullanıcının verdiği bağlantıyı `git remote add origin "$REPO_URL"` ile ekler ve `git push -u origin main` komutuyla dosyayı doğrudan GitHub repoya aktarır. İşlem başarıyla bittiğinde ekrana tebrik mesajı verir
