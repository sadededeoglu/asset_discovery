import sys, ipaddress,nmap

class checkConn:
    def checkNmap(host):
       IPAddress = host
       hostscan = nmap.PortScanner()
       parsed_ip = IPAddress[0:10]
       
       x=0
       while x < 256:
        s=parsed_ip+str(x)
        results = hostscan.scan(hosts=s, arguments='-T4')
        x+=1
        cikti=results['scan']
        return(cikti)
