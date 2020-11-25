# asset_discovery

Control.py

1)Nmap: Bağlantı noktası tarayıcısıdır.

#import nmap

2)Checkcontrol  adinda bir class oluşturuyorum.

#class checkControl:

2)Nmap i kontrol edecek bir fonksiyon yazıp içine  parametre ekliyorum.

#def checkNmap(host):

3)Discovery.py da girdi olarak alınan IPAddress i buradaki host a eşitliyorum.

#IPAddress = host

4)Girilen ip nin bulunduğu network üzerindeki tüm ip lere erişip portlarını taratıp result a eşitliyorum.

#results = nmap.PortScanner().scan()

5)Scan ın içine Girilen ip nin bulunduğu network üzerindeki tüm ip lere erişebilmek için /24 ekliyorum. Arguments olarak daha hızlı calısması için nmap in komutu olan -T4 veriyorum.

#hosts=IPAddress+'/24', arguments='-T4'

6)Çıkan sonuçlarin içinden sadece scan in içeriğini bir değişkene atıyorum.

#end=results['scan']

7)Sadece end değişkeninin dönmesini sağlıyorum.

#return(end)
