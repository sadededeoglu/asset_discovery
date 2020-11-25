# asset Discovery

Proje Amacı: flask ile girilen ip adresinin bulunduğu network ağının  icinde bir nmap taraması başlatıp o ağdaki tüm ip adreslerinin açık portlarını taratıp sonuclarını json veri formatında ekrana çıktı olarak verir.

Control.py

1)Nmap: Bağlantı noktası tarayıcısıdır.

# import nmap

2)Checkcontrol  adinda bir class oluşturulur.

# class checkControl:

2)Nmap i kontrol edecek bir fonksiyon yazıp içine  parametre eklenir.

# def checkNmap(host):

3)Discovery.py da girdi olarak alınan IPAddress i buradaki host a eşitlenir.

# IPAddress = host

4)Girilen ip nin bulunduğu network üzerindeki tüm ip lere erişip portlarını taratıp result a eşitlenir.

# results = nmap.PortScanner().scan()

5)Scan ın içine Girilen ip nin bulunduğu network üzerindeki tüm ip lere erişebilmek için /24 eklenir. Arguments olarak daha hızlı calısması için nmap in komutu olan -T4 verilir.

# hosts=IPAddress+'/24', arguments='-T4'

6)Çıkan sonuçlarin içinden sadece scan in içeriğini bir değişkene atanir.

# end=results['scan']

7)Sadece end değişkeninin dönmesini sağlanır.

# return(end)

Discovery.py

1)Flask :api dir. ‘uygulama programlama arayüzü’
Flask-RESTful :REST API'lerini hızla oluşturmak için destek ekleyen bir Flask uzantısıdır.
2)Flask-RESTful kütüphanesinin içinden resource ve Api import edilir.

3)Control dosyası içinden checkControl class ı import edilir.

# from flask import Flask, request
# from flask_restful import Resource, Api
# from control import checkControl

4)__name__ değişkeni dosyanın (modülünün) hangi yolla çağrıldığını kontrol eder. 

# app = Flask(__name__)
# api = Api(app)

5)İçerisinde resource olan bir class oluşturulur.

# class nmapCheck(Resource):

6)Get metodunu kullanarak fonksiyon oluşturup 2 parametre verilir.

# def get(a, IPAddress):

7)Control dosyasından getirilen checkControl class ının içinden checkNmap fonksiyonunu çağırarak ip adresini döndürülür.

# return(checkControl.checkNmap(IPAddress))

8)Tanımlanmış olan apinin içinden add_resource alınıp , nmapCheck class ının içinde dönecek olan ip adresinin girdisi alınır.

# api.add_resource(nmapCheck, '/nmap/<string:IPAddress>')

9) name == "_ _main_ _" kontrolü dışarıdan import edildiğinde hangi alanların çalıştırılacağının seçimini yapar.

# if _ _name_ _ == '_ _main_ _':

10)hangi ip ve port üstünden bu bilgilere erişebileceğimizi belirlenir.

# app.run(host='127.0.0.1', port='5000', debug=True)


