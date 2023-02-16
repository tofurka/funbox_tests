import schedule
import time
import datetime
import requests

def curl_metric():
    lst = [ "maria.ru", "rose.ru", "sina.ru" ]    
    for server in lst:
        ts = datetime.datetime.now()
        #http://servername/api/count
        url = f"http://{server}/api/count"
        resp = requests.get(url)
        
        for line in resp.text.splitlines():
            if 'count' in line:                
                print(ts.strftime("%Y-%m-%d %H:%M:%S"), server, line.replace("{\"count\":", "" )[:-1:])
                # {"count": 42}
                # 2023-02-16 18:09:00 rose.ru 0

schedule.every().minute.at(":00").do(curl_metric)

while True:
    schedule.run_pending()
    time.sleep(1)