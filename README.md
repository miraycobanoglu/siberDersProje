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
