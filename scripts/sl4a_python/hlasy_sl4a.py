# import urllib.request
import string
import urllib
import urllib2
import time
import datetime
import android 

droid = android.Android() 
droid.wakeLockAcquirePartial()


FILENAME = '/sdcard/sl4a/scripts/lubyn_stupne/hlasy_sl4a.txt'

WEB_LOG_FOLDER = '/sdcard/sl4a/scripts/lubyn_stupne/weblog/'

TIMER = 120    # [sec], minimum 10 sec

def get_url(url1):
   try: 
     # url = url1 % (urllib.quote(location), hl)
     url = url1
     handler = urllib2.urlopen(url)
     data = handler.read()
     print "get_url: page size: " + str(len(data))
     return data
   except Exception as e:
     print('Exception: get_url:')
     print(e)
     return ''
 
 
def parse_hlasy(webcontent):
   try: 
     
     # wc = str(get_url('http://www.countryradio.cz/folkove-stupne/'))
     wc = webcontent
     
     wc.replace('\t','').replace('\n','')
     # print(wc)
     d1 = wc.split('<h3 class="nadpis size_18">Folkov')[1].split('</table>')[0]
     d2 = d1.split('<td class="size_11 c">')
     
     # d3 = list(map(lambda x : x.split('</td>')[0], d2[1:]))
     d3 = []
     for d in d2[1:]:
         d3.append(d.split('</td>')[0]) 
     
     return d3
   except Exception as e:
     print('Exception: parse_hlasy:')
     print(e)
     return ''  
 
 
if __name__ == '__main__': 
  while True:
    try:  
      try:  
        wc = str(get_url('http://www.countryradio.cz/folkove-stupne/'))
        num = parse_hlasy(wc)
        vote = ';  '.join(map(lambda x: str(x), num))
        ts = time.strftime("%Y-%m-%d_%H:%M:%S;  ")
        votelog = ts + str(vote)
        print(votelog)
        
        try:
          f = open(FILENAME, 'a')
          f.write(votelog + '\r\n')
        finally:  
          f.close()
        
        '''  
        try:
          ts2 = ts.replace(':','')
          fwlog = open(WEB_LOG_FOLDER + ts2 + '.html', 'w')
          fwlog.write(wc)
        finally:  
          fwlog.close()
        '''  
      except KeyboardInterrupt: 
        raise KeyboardInterrupt
    
      except Exception as e:
        print "MAIN EXCEPTION :"
        print e.message   
        time.sleep(TIMER) 
       
      time.sleep(TIMER)   
      
    except KeyboardInterrupt: 
        print("\n\nCtrl+c. FINISH.")
        exit(0)    
