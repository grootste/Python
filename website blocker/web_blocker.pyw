import time
from datetime import datetime as dt

host_temp="hosts"
#hosts_path="C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["wwww.facebook.com", "facebook.com", "singh.baibhav321@gmail.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,16) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,17):
        print("woking hours")
        with open(host_temp,'r+') as file:
            content=file.read()
            print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write("\n"+redirect+" "+ website+"\n")
    else:
        with open(host_temp,'r+') as file:
            content=file.readline()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()  
        print("Fun Hours")
    time.sleep(1)
