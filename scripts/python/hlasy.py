import urllib.request
import time
import datetime

FILENAME = 'hlasy10s.txt'

TIMER = 10    # [sec]

def get_url(url:str, filename:str):
    fp = urllib.request.urlopen(url, timeout=10)
    content = fp.read()
    if filename != None:
        try:
            newFile = open(filename, "wb")
            newFile.write(content)
            newFile.close()
        except Exception as e:
            print('Write file exception: {}'.format(e))
    return content


def parse_hlasy():
    wc = str(get_url('http://www.countryradio.cz/folkove-stupne/', None)).encode().decode('unicode-escape')
    wc.replace('\t','').replace('\n','')
    d1 = wc.split('<h3 class="nadpis size_18">Folkov')[1].split('</table>')[0]
    d2 = d1.split('<td class="size_11 c">')
    d3 = list(map(lambda x : int(x.split('</td>')[0]), d2[1:]))
    return d3


if __name__ == '__main__':
  while True:
    try: 
      try:  
        print('Getting data...')
        num = []
        try:
          num = parse_hlasy()
        except Exception as e:
          print('EXCEPTION: parse exception: ')
          print(e)
          num = []    # if error create empty row
        dt = datetime.datetime.today()
        stamp = '{}-{:02}-{:02}_{:02}:{:02}:{:02}'.format(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
        vote = ';  '.join(map(lambda x: str(x), num))
        votelog = '{};  {}\r\n'.format(stamp, vote)
        print(votelog)
        with open(FILENAME, 'a') as file:
          file.write(votelog)
            
      except KeyboardInterrupt: 
        raise KeyboardInterrupt
        
      except Exception as e:
        print('Exception:')
        print(e)
        
      time.sleep(TIMER)
        
    except KeyboardInterrupt: 
      print("\n\nCtrl+c. FINISH.")
      exit(0) 



