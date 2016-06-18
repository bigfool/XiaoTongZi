import time
import random

red = 0
orange = 0
yellow = 0
green = 0
blue = 0

data = []
price = []
distribute = []
total = int(input('请输入记录个数:'))
record = 0

def getDistribute(p):
    global red
    global orange
    global yellow
    global green
    global blue
    p = int(p)
    if p > 1000:
        red += 1
        return
    if p > 850:
        orange += 1
        return
    if p > 700:
        yellow += 1
        return
    if p > 550:
        green += 1
        return
    blue += 1

def priceToColor(p):
    p = int(p)
    if p > 1000:
        return '#FF0000'
    if p > 850:
        return '#FF7F00'
    if p > 700:
        return '#FFFF00'
    if p > 550:
        return '#00FF00'
    return '#6dcff6' 

if __name__ == "__main__":
    with open('flightsData.txt', 'r') as file:
        for i in range(total):
            linedata = file.readline()
            lis = linedata.split(',')
            getDistribute(lis[-2])
            if record > 998:
                continue
            if random.randint(0 , total) > 1000:
                continue
            record += 1
            d = '[' + lis[-1][:-1] + ',' + lis[-2] + ',' + lis[1] + ']'
            price.append(lis[-2])
            data.append(d)
        print('数据读取完成！\n共加载%d条记录，抽取了其中%d条样本' % (total, record))

    with open('chartData.js', 'w') as file:
        file.write('var chartData = [')
        for i in range(record - 1):
            file.write(data[i] + ',')
        file.write(data[record-1] + '];\n')
        file.write('var colorData = [')
        for i in range(record - 1):
            file.write('\'%s\',' % priceToColor(price[i]))
        file.write('\'%s\'];\n' % priceToColor(price[record-1]))
        file.write('var distribute = [[\'>1000\',%d],[\'1000-850\',%d],[\'850-700\',%d],[\'700-550\',%d],[\'<550\',%d]];\n' % (red, orange, yellow, green, blue))
        print('数据写入完成！')

    print('绘制图表中……')
    print('3……')
    time.sleep(1)
    print('2……')
    time.sleep(1)
    print('1……')
    time.sleep(1)