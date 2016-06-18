import requests
from bs4 import BeautifulSoup
import json
import time
from datetime import datetime
from datetime import date
import pymysql

webUrl = ['https://sjipiao.alitrip.com/search/common_cheapest_calendar.htm?_ksTS=1465955381682_4337&callback=jsonp_trip_1681&calType=MonthCalendar&depCity=BJS&arrCity=KMG&searchDay=2016-06-01',
'https://sjipiao.alitrip.com/search/common_cheapest_calendar.htm?_ksTS=1465955381682_4337&callback=jsonp_trip_1681&calType=MonthCalendar&depCity=BJS&arrCity=KMG&searchDay=2016-07-01',
'https://sjipiao.alitrip.com/search/common_cheapest_calendar.htm?_ksTS=1465955381682_4337&callback=jsonp_trip_1681&calType=MonthCalendar&depCity=BJS&arrCity=KMG&searchDay=2016-08-01',
'https://sjipiao.alitrip.com/search/common_cheapest_calendar.htm?_ksTS=1465955381682_4337&callback=jsonp_trip_1681&calType=MonthCalendar&depCity=BJS&arrCity=KMG&searchDay=2016-09-01']

if __name__ == "__main__":
    with open('recordNumber.txt', 'r') as file:
        total = int(file.read())
        total1 = total
    while True:
        today = str(date.today())
        hour = int(datetime.today().hour)
        minute = int(datetime.today().minute)
        print('*********************')
        print('正在下载数据……')
        for url in webUrl:
            response = requests.get(url)
            #soup = BeautifulSoup(response.text, 'lxml')
            jsonData =  json.loads('{' + response.text[(response.text.find('data') - 1):-3])
            data = []
            for flight in jsonData['data']:
                d = {
                    'searchDay' : today,
                    'searchHour' : hour,
                    'dep' : flight['dep'],
                    'arr' : flight['arr'],
                    'date' : flight['date'],
                    'price' : flight['price'],
                    'interval' : (date(int(flight['date'][0:4]), int(flight['date'][5:7]), int(flight['date'][8:])) - date(int(today[0:4]), int(today[5:7]), int(today[8:]))).days
                }
                if (d['price'] == 0) or (d['interval'] > 60):
                    continue
                data.append(d)
            flag = False
            with open('flightsData.txt', 'a') as file:
                for d in data:
                    total1 += 1
                    file.write('%s,%s,%s,%s,%s,%s,%s\n' % (str(d['searchDay']),str(d['searchHour']),str(d['dep']),str(d['arr']),str(d['date']),str(d['price']),str(d['interval'])))           
                with open('recordNumber.txt', 'w') as file:
                    file.write(str(total1))
                    print('写入数据文件成功')
                    flag = True
            if flag != True:
                print('写入数据文件失败')
            try:
                conn = pymysql.connect(user='root', passwd='password', host='localhost', db='dpydb')
                cursor = conn.cursor()
                for d in data:
                    total += 1
                    cursor.execute('INSERT INTO Flights VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',(str(total),str(d['searchDay']),str(d['searchHour']),str(d['dep']),str(d['arr']),str(d['date']),str(d['price']),str(d['interval'])))
                print('写入数据库成功')
            except BaseException as e:
                print('写入数据库失败' + str(e))
            finally:
                cursor.close()
                conn.commit()
                conn.close()
        print('（更新于' + today + ' ' + str(hour) + '时' + str(minute) + '分）')
        print('*********************')
        time.sleep(3600)