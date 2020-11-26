from flask import Flask, request
#Flask :api dir. ‘uygulama programlama arayüzü’ Flask-RESTful :REST API'lerini hızla oluşturmak için destek ekleyen bir Flask uzantısıdır.
#Flask-RESTful kütüphanesinin içinden resource ve Api import edilir.
from flask_restful import Resource, Api
from control import checkControl #Control dosyası içinden checkControl class ı import edilir.

app = Flask(__name__) #_ name _ değişkeni dosyanın (modülünün) hangi yolla çağrıldığını kontrol eder.
api = Api(app)

class nmapCheck(Resource): #İçerisinde resource olan bir class oluşturulur.
    def get(a, IPAddress): #Get metodunu kullanarak fonksiyon oluşturup 2 parametre verilir.
       return(checkControl.checkNmap(IPAddress)) #Control dosyasından getirilen checkControl class ının içinden checkNmap fonksiyonunu çağırarak ip adresini döndürülür.

api.add_resource(nmapCheck, '/nmap/<string:IPAddress>')#Tanımlanmış olan apinin içinden add_resource alınıp , nmapCheck class ının içinde dönecek olan ip adresinin girdisi alınır.

if __name__ == '__main__': # kontrolü dışarıdan import edildiğinde hangi alanların çalıştırılacağının seçimini yapar.
    app.run(host='127.0.0.1', port='5000', debug=True) #Hangi ip ve port üstünden bu bilgilere erişebileceğimizi belirlenir.
