# asset Discovery

Proje Amacı: flask ile girilen ip adresinin bulunduğu network ağının  iceride bir nmap taraması başlatıp o ağdaki tüm ip adreslerinin açık portlarını taratıp sonuclarını json veri formatında ekrana çıktı olarak verir.

Control.py

1)Nmap: Bağlantı noktası tarayıcısıdır.

# import nmap

2)Checkcontrol  adinda bir class oluşturuyor.

# class checkControl:

2)Nmap i kontrol edecek bir fonksiyon yazıp içine  parametre ekliyor.

# def checkNmap(host):

3)Discovery.py da girdi olarak alınan IPAddress i buradaki host a eşitliyor.

# IPAddress = host

4)Girilen ip nin bulunduğu network üzerindeki tüm ip lere erişip portlarını taratıp result a eşitliyor.

# results = nmap.PortScanner().scan()

5)Scan ın içine Girilen ip nin bulunduğu network üzerindeki tüm ip lere erişebilmek için /24 ekliyorum. Arguments olarak daha hızlı calısması için nmap in komutu olan -T4 veriyor.

# hosts=IPAddress+'/24', arguments='-T4'

6)Çıkan sonuçlarin içinden sadece scan in içeriğini bir değişkene atar.

# end=results['scan']

7)Sadece end değişkeninin dönmesini sağlar.

# return(end)

Discovery.py

1)Flask :api dir. ‘uygulama programlama arayüzü’
Flask-RESTful :REST API'lerini hızla oluşturmak için destek ekleyen bir Flask uzantısıdır. Mevcut ORM / kütüphanelerinizle çalışan hafif bir soyutlamadır. Flask-RESTful, minimum kurulumla en iyi uygulamaları teşvik eder.
2)Flask-RESTful kütüphanesinin içinden resource ve Api import ediliyor
3)Control dosyası içinden checkControl class ı import ediliyor 

# from flask import Flask, request
# from flask_restful import Resource, Api
# from control import checkControl

4)
