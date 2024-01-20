import random
import numpy as np
import requests
import pandas as pd
from lxml import etree
import csv

times = []
times_num = []
numbers = []
for i in range(1,156,1):
    url = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_{}.html'.format(i)

    headers = {

        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
        'cookie':'ck_RegFromUrl=https%3A//cn.bing.com/; seo_key=bing%7C%7Chttps://cn.bing.com/; _jzqx=1.1689777833.1690772890.1.jzqsr=cn%2Ebing%2Ecom|jzqct=/.-; __utmz=63332592.1690772891.5.2.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _jzqckmp=1; tgw_l7_route=6f87741a760244b10ae54436fccac88e; WT_FPC=id=undefined:lv=1691037677818:ss=1691037677818; sdc_session=1691037677820; sdc_userflag=1691037677820::1691037677820::1; _jzqa=1.568345894516795600.1689777833.1691027208.1691037678.12; _jzqc=1; _qzja=1.220434213.1689780279535.1691027208323.1691037677854.1691027296253.1691037677854.0.0.0.22.10; _qzjc=1; _qzjto=13.5.0; Hm_lvt_4f816d475bb0b9ed640ae412d6b42cab=1691025589,1691026008,1691027208,1691037678; Hm_lpvt_4f816d475bb0b9ed640ae412d6b42cab=1691037678; _jzqb=1.1.10.1691037678.1; _qzjb=1.1691037677854.1.0.0.0; __utma=63332592.1893224645.1689777834.1691025591.1691037679.10; __utmc=63332592; __utmt=1; __utmb=63332592.1.10.1691037679; CLICKSTRN_ID=118.73.61.234-1689777831.439777::3B858C5798A8EF0118598E9B0827883F;'
    }

    response = requests.get(url,headers=headers)

    content = response.content.decode('utf8')
    html = etree.HTML(content)

#    time = html.xpath('/html/body/table/tr/td[1]/text()')
    time_num = html.xpath('/html/body/table/tr/td[2]/text()')
    number = html.xpath('//td[@align="center"]/em/text()')
#    for j in time:
#       times.append(j)
    for j in time_num:
        times_num.append(j)
    for j in range(0, len(number), 7):
        numbers.append(number[j:j + 7])
    print('第{}页已经爬取'.format(i))


file =open('C:\\Users\\33628\\Desktop\\双色球.csv','w',encoding='utf-8-sig',newline='')

csv_write = csv.writer(file)

csv_write.writerow(['期号','号码1','号码2','号码3','号码4','号码5','号码6','号码7'])
for t_n,num in zip(times_num,numbers):
    a = []
    a.append(t_n)
    a.append(num[0])
    a.append(num[1])
    a.append(num[2])
    a.append(num[3])
    a.append(num[4])
    a.append(num[5])
    a.append(num[6])
    csv_write.writerow(a)
file.close()

#随机选取号，并分析
x = pd.read_csv('C:\\Users\\33628\\Desktop\\双色球.csv')
c = x.loc[:,['号码1','号码2','号码3','号码4','号码5','号码6','号码7']]

for i in range(3):
    a = random.sample(range(1,34),6)
    sorted_num_red = sorted(a)
    b = random.sample(range(1,17),1)
    sorted_num_blue = sorted(b)

    sorted_num_red.append(sorted_num_blue[0])
    sorted_num = sorted_num_red

    sorted_num = np.array(sorted_num)

    isIn = np.any(np.all(sorted_num == c, axis=1))
    if(isIn == False):
        print(sorted_num)
