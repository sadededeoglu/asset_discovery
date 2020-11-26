import nmap 
#Nmap: Bağlantı noktası tarayıcısıdır.

class checkControl: 

    def checkNmap(host):  #Nmap i kontrol edecek bir fonksiyon yazıp içine parametre eklenir.
        IPAddress = host  #Discovery.py da girdi olarak alınan IPAddress i buradaki host a eşitlenir.
        results = nmap.PortScanner().scan(hosts=IPAddress+'/24', arguments='-T4') #Girilen ip nin bulunduğu network üzerindeki tüm ip lere erişip portlarını taratıp result a eşitlenir.
        #Scan ın içine Girilen ip nin bulunduğu network üzerindeki tüm ip lere erişebilmek için /24 eklenir. Arguments olarak daha hızlı calısması için nmap in komutu olan -T4 verilir.
        end=results['scan'] #Çıkan sonuçlarin içinden sadece scan in içeriğini bir değişkene atanir.
        return(end)       #Sadece end değişkeninin dönmesini sağlanır.