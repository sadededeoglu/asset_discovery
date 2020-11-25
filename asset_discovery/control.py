import nmap 

class checkControl: 

    def checkNmap(host): 
        IPAddress = host 
        hostscan = nmap.PortScanner() 
        results = hostscan.scan(hosts=IPAddress+'/24', arguments='-T4') 
        end=results['scan'] 
        return(end) 