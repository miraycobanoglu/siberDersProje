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
