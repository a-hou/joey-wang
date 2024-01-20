一个是双色球爬虫，一个是大乐透爬虫  
双色球爬虫中每次爬取一页，大乐透爬虫中每次爬取一期  
双色球爬虫需要在循环中修改页数，将url放到网页中去查询一共多少页，for i in range(1,156,1):  
大乐透需要求改期数，http://datachart.500.com/dlt/history/newinc/history.php?start=07001&end=24008，其中24008为期数  
最后都是随机生成从未出现过的几组号
