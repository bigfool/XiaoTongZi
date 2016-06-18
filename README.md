#XiaoTongZi
爬虫与数据可视化 (by Python & Highcharts)<br>
Licensed under the Apache License<br>
----------------------------------------------------------------------------------------------<br>
###问题描述：<br>
想在暑假从北京坐飞机至昆明，问：<br>
1.应该提前多少天买票比较合适？<br>
2.票价为多少是可以接受的？<br>
3.上午买和下午买有区别吗？<br>
###数据来源：<br>
1.[阿里旅行国内机票低价日历](https://sjipiao.alitrip.com/flight_search_result.htm?searchBy=1277&tripType=0&depCityName=%B1%B1%BE%A9&depCity=&arrCityName=%C0%A5%C3%F7&arrCity=&depDate=2016-07-24&arrDate=)<br>
2.爬虫每小时采集一次数据，每次60条，为两个月内每天的最低机票价格<br>
3.数据采集自2016年6月15日至6月19日<br>
###方法步骤：<br>
1.用提前日期，机票价格，购票时刻作为三元组绘制三维散点图<br>
2.启动runTongZi.bat，调用getData.py获取数据并保存在flightsData.txt与recordNumber.txt中<br>
3.启动dealWithData.bat，调用processData.py提取数据并保存在chartData.js中<br>
4.使用Highcharts(showData1.html与showData2.html)根据数据绘制图表<br>
###总结与反思：<br>
结论：<br>
1.结论为提前5~15天购票比较合适,700元以下的票可以立即买<br>
2.没有发现机票价格与购买时刻的关系<br>
弊端：<br>
1.机票价格有着一套复杂的算法，受节假日、城市是否为热门城市等各种因素影响，不具一般性<br>
2.三维散点图中绘制了999个点，用的是随机抽样方法选取点。数据处理方法比较简单<br>
3.每天的最低票价所对应的登机时间一般太早或太晚，所以好好挣钱才是王道<br>
4.数据采集受网络中断等影响时间不够连续<br>
----------------------------------------------------------------------------------------------<br>
Copyright © 2016 buaadpy. All Rights Reserved<br>
<br>
<br>
![Version1.0](/release_v1.0.jpg)