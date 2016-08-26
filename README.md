#XiaoTongZi
爬虫与数据可视化 (by Python & Highcharts)<br>
Licensed under the Apache License<br>
Copyright © 2016 buaadpy. All Rights Reserved<br>
##WebofScience<br>
寻找“王子”课题——从Web of Science获取数据:<br>
1.Exact stochastic simulation of coupled chemical，这篇文章称之为a<br>
2.找引用了a的文章，称之为b类文章<br>
3.找每篇b类文章的引用的文章，称之为c类文章<br>
4.对abc三类文章建表，存每篇文章的wos号，文章名，发表年，doi<br>
5.建引用关系表，每条记录都是id1-id2，表示id1文章引用了id2<br>
操作方法:<br>
0.多次访问会被网站锁定，需要手动清空cookie<br>
1.进入数据库搜索文章，搜出所有引用该文章的文章列表<br>
2.点击进入任意一篇文章，找到网址中的SID，并将其写入代码<br>
3.更新已经收集的条目数，开始执行代码<br>
4.一旦失败，则需要删除数据文件中的失败数据，重新执行上述步骤<br>
最终总文章数为9w6左右，数据存在以下几个问题：<br>
1.有文章信息出现分隔符*，会导致条目被错误分隔，预计有0.1%数据存在以上问题<br>
2.有0.2%的数据没有获得正确的id，原因未知，已全部手动修复<br>
3.有部分文章并不存在DOI号，于是其DOI信息是错的，数量未知<br>
4.预计存在1%的数据遗漏<br>
##AliFlight<br>
问题:想在暑假从北京坐飞机至昆明<br>
1.应该提前多少天买票比较合适？2.票价为多少是可以接受的？3.上午买和下午买有区别吗？<br>
数据来源：<br>
1.阿里旅行国内机票低价日历（2016年6月15日至7月1日，北京至昆明）<br>
2.爬虫每小时采集一次数据，每次60条，为两个月内每天的最低机票价格<br>
方法步骤：<br>
1.用提前日期，机票价格，购票时刻作为三元组绘制三维散点图<br>
2.启动runTongZi.bat，调用getData.py获取数据并保存在flightsData.txt与recordNumber.txt中<br>
3.启动dealWithData.bat，调用processData.py提取数据并保存在chartData.js中<br>
4.使用Highcharts(showData1.html与showData2.html)根据数据绘制图表<br>
总结与反思：<br>
1.一共采集了16000条数据<br>
2.结论为提前5~15天购票比较合适，800元以下的票可以立即买，没有发现机票价格与购买时刻的关系<br>
3.机票价格有着一套复杂的算法，受节假日、城市是否为热门城市等各种因素影响，不具一般性<br>
4.三维散点图中绘制了999个点，用的是随机抽样方法选取点。数据处理方法比较简单<br>
5.每天的最低票价所对应的登机时间一般太早或太晚，所以好好挣钱才是王道<br>
6.数据采集受网络中断等影响时间不够连续<br>
7.实验后期发现票价受暑假影响很大，失去有效性<br>
![Version1.0](/release_v1.0.jpg)