import requests
from bs4 import BeautifulSoup
import time
import sys

#文章标题：Exact stochastic simulation of coupled chemical

#目前已经收集的条目
Now = 3558

SID = 'W11cbb8iTfiUWhOM8hc'

#基础网址，手动搜索文章标题可得，会变动，同时更改cookie
webUrl = 'http://apps.webofknowledge.com/full_record.do?product=WOS&search_mode=CitedRefIndex&qid=3&SID='

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
}

#停止等待时间
Waittime = 1

#从文章详细页获取想要的信息
def getData(url):
    global Waittime
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
    except BaseException as e:
        print('访问与解析错误，停止等待……')
        time.sleep(Waittime)
        Waittime *= 2
        print('重试……')
        getData(url)
    #获取wos
    wos = soup.select('div > div > p > a')
    wos = str(str(wos).encode('utf-8'))
    index = wos.find('UT=WOS:')
    wos = wos[index+7:index+22]
    #获取标题
    title = soup.select('div.title > value')
    if (len(title) != 0):
        title = title[0].getText()
    else:
        title = 'NULL'
    #获取年份
    year = soup.select('div.block-record-info.block-record-info-source > p')
    year = str(year)[-18:-14]
    #获取doi
    doi = soup.select('div.block-record-info.block-record-info-source > p > value')
    if (len(doi) != 0):
        doi[0] = ''
        final = ''
        for d in doi:
            d = str(d)
            if (len(d) > len(final)):
                final = d
        doi = str(final)[7:-8]
    else:
        doi = 'NULL'
    #获取引用列表连接
    link = soup.find_all('a', title='View this record\'s bibliography')
    if (len(link) != 0):
        link = link[0].get('href')
        link = 'http://apps.webofknowledge.com' + link
    else:
        link = soup.find_all('a', title='查看此记录的题录信息')
        if (len(link) != 0):
            link = link[0].get('href')
            link = 'http://apps.webofknowledge.com' + link
        else:
            link = ''
    
    data = {
        'wos':wos,
        'title':title,
        'year':year,
        'doi':doi,
        'link':link
    }
    return data

#根据b类文章的引用连接，搜寻C类文章
def findC(link,f):
    global Waittime
    if (link == ''):
        print('地址获取失误，程序停止……')
        sys.exit(0)
    try:
        response = requests.get(link, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
    except BaseException as e:
        print('访问与解析错误，停止等待……')
        time.sleep(Waittime)
        Waittime *= 2
        print('重试……')
        findC(link,f)
    links = soup.find_all('a', class_='smallV110')
    if (len(links) == 0):
        print('未知错误，程序停止……')
        sys.exit(0)
    for l in links:
        href = str(l.get('href'))
        if (href[0] == '/' and href[1] == 'C'):
            href = 'http://apps.webofknowledge.com' + href
            data = getData(href)
            saveByFile(data, f)
    #递归寻找下一页
    nexts = soup.find_all('a', class_='paginationNext')
    nexts = nexts[0].get('href')
    if (nexts[0] == 'h'):
        findC(nexts,f)

#保存数据
def saveByFile(d,f):
    if (str(d['wos']) == 'NULL' or str(d['title']) == 'NULL' or str(d['year']) == 'NULL' or str(d['doi']) == 'NULL'):
        print('数据获取失败，程序停止……')
        sys.exit(0)
    with open('articleData.txt', 'a') as file:
        file.write('%s*%s*%s*%s\n' % (str(d['wos']),str(d['title']),str(d['year']),str(d['doi'])))
        print('%s*%s*%s*%s\n' % (str(d['wos']),str(d['title']),str(d['year']),str(d['doi'])))     
    with open('relationalData.txt', 'a') as file:
        if (f == '999999999999999'):
            file.write('%s,%s\n' % (str(d['wos']),f))
        else:
            file.write('%s,%s\n' % (f,str(d['wos']))) 



if __name__ == "__main__":
    for i in range(1, 357):
        for j in range((i - 1) * 10 + 1, i * 10 + 1):
            if (j <= Now):
                continue
            url = webUrl + SID + '&page=' + str(i) + '&doc=' + str(j)
            print('\n\n正在下载数据，第%d条b文章' % j)
            data = getData(url)
            saveByFile(data, '999999999999999')
            findC(data['link'], data['wos'])