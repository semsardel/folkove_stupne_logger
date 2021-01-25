import urllib.request
import time
import datetime

# FILENAME = 'hlasy.txt'
# TIMER = 120    # timer interval [sec], minimum 10 sec

FILENAME = 'hlasy_10s.txt'
TIMER = 10    # timer interval [sec], minimum 10 sec

def get_url(url:str, filename:str):
    try:
        # print("getUrl: {}".format(url))
        fp = urllib.request.urlopen(url, timeout=10)
        # print("read...")
        content = fp.read()
        if filename != None:
            # save data
            # print("write file: {}".format(filename))
            try:
              newFile = open(filename, "wb")
              newFile.write(content)
              newFile.close()
            except Exception as e:
                print('Write file exception: {}'.format(e))
        return content
    except Exception as e:
        print('getUrl exception:')
        print(e)
        return ''


def parse_hlasy():
   try: 
     wc = str(get_url('http://www.countryradio.cz/folkove-stupne/', None)).encode().decode('unicode-escape')
     wc.replace('\t','').replace('\n','')
     d1 = wc.split('<h3 class="nadpis size_18">Folkov')[1].split('</table>')[0]
     d2 = d1.split('<td class="size_11 c">')
     d3 = list(map(lambda x : x.split('</td>')[0], d2[1:]))
     return d3
   except Exception as e:
     print('Exception: parse_hlasy:')
     print(e)
     return ''  


while True:
  try:  
    num = parse_hlasy()
    dt = datetime.datetime.today()
    stamp = '{}-{}-{}_{:02}:{:02}:{:02} '.format(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
    votelog = '{}{}\r\n'.format(stamp, num)
    print(votelog)
    with open(FILENAME, 'a') as file:
      file.write(votelog)
  except Exception as e:
    print('Global Exception:')
    print(e)
  print('Timer: ', end='')
  for i in range(int(TIMER / 10)):
    print('{}'.format(i%10), end='')  
    time.sleep(10)
  print('')
  
      
