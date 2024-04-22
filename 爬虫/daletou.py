import numpy as np
import pandas as pd
import requests
from lxml import etree
import csv
from matplotlib  import pyplot as plt
import random

#大乐透url，通过修改最后的最近一期的期号（即24***）来爬取所有期的号
url = 'http://datachart.500.com/dlt/history/newinc/history.php?start=07001&end=24044'

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188",
    "cookie":'bid=WS7lyzjUPWQ; _pk_id.100001.4cf6=4ce9a055cdfa056e.1683627924.; __utmz=30149280.1684989866.2.2.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmz=223695111.1684989866.2.2.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __yadk_uid=ADSl2QbUG3WHjlzUnJpYOuGTRydS1puw; ll="108257"; trc_cookie_storage=taboola%2520global%253Auser-id%3D9e8d4c75-2328-445d-9a00-d515ed74590e-tuctbba6989; _vwo_uuid_v2=D1379487087695CF9449490FB52A00BC8|aa12a52fb9b5b11d672a8567986cf837; cto_bundle=LBre0180MVE0ZFc3NHFET0F0UzBYb2t6YyUyRkJRNUJUSVF1QUduaFp0ZENnc3drc01jWWFWektyQXBDVEZQcU5pVnZ6ekszNXlQdHVkRlYlMkZrUTJOemx2djdTY1Z6YXRHWE1sdmJ2d3hVNGRsZVVCc1NPJTJGV1B0N3FKQXFITlAyUGxCbEFaMTVIbWplZ0UlMkJGRTExRmMxaWZ3WCUyRkhnJTNEJTNE; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1690727443%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses.100001.4cf6=1; ap_v=0,6.0; __utma=30149280.994620429.1683627926.1690362873.1690727443.4; __utmc=30149280; __utmt_douban=1; __utmb=30149280.1.10.1690727443; __utma=223695111.1209347815.1683627926.1690362873.1690727443.4; __utmb=223695111.0.10.1690727443; __utmc=223695111; __gads=ID=2bf5fcd85cd4ac31-22a3ce1995df00af:T=1683627930:RT=1690727444:S=ALNI_MYfSp3KeQrbpLFDTGUsInZUeprzhg; __gpi=UID=00000bead65f2824:T=1683627930:RT=1690727444:S=ALNI_MZNH-TRp3wWThFA7yIbJlKbIbtZ8Q',
}
resp = requests.get(url,headers=headers)
content = resp.content.decode('utf-8')

#使用lxml的etree解析html文件
html = etree.HTML(content)
#红球
red = html.xpath('//tbody[@id="tdata"]//td[@class="cfont2"]/text()')
#蓝球
blue =html.xpath('//tbody[@id="tdata"]//td[@class="cfont4"]/text()')
#期号
time = html.xpath('//*[@id="tdata"]/tr/td[1]/text()')
reds = []
blues = []
for i in range(0,len(red),5):
    reds.append(red[i:i+5])
for i in range(0,len(blue),2):
    blues.append(blue[i:i+2])
#在本地创建'大乐透.csv'
file =open('大乐透.csv','w',encoding='utf-8-sig',newline='')
csv_write=csv.writer(file)
csv_write.writerow(['期号','号码1', '号码2', '号码3', '号码4', '号码5', '号码6', '号码7'])


#将红球与蓝球组合
for i,j,k in zip(time,reds,blues):
    a = []
    a.append(i)
    a.append(j[0])
    a.append(j[1])
    a.append(j[2])
    a.append(j[3])
    a.append(j[4])
    a.append(k[0])
    a.append(k[1])
    csv_write.writerow(a)
file.close()
#存到本地文件
x = pd.read_csv('大乐透.csv')
c = x.loc[:,['号码1','号码2','号码3','号码4','号码5','号码6','号码7']]

#此部分为统计近50期中的各个数字出现次数并画图展示
# a = c.head(50)
# red = pd.DataFrame(a,columns=['号码1','号码2','号码3','号码4','号码5'])
# haoma = pd.DataFrame(red.to_numpy().reshape(-1, 1, order='F'), columns=['count'])
# redcounts = haoma['count'].value_counts()
# print(redcounts.sort_values())
# # plt.figure()
# # plt.xlabel('red numbers')
# # plt.ylabel('Count')
# # plt.bar(redcounts.index, redcounts.values)
# # plt.title('rednumbers Count50')
#
# b = c.head(50)
# blue = pd.DataFrame(a,columns=['号码6','号码7'])
# haoma = pd.DataFrame(blue.to_numpy().reshape(-1, 1, order='F'), columns=['count'])
# bluecounts = haoma['count'].value_counts()
# print(bluecounts.sort_values())
# # plt.figure()
# # plt.xlabel('blue numbers')
# # plt.ylabel('Count')
# # plt.bar(bluecounts.index, bluecounts.values)
# # plt.title('bluenumbers Count50')
# # plt.plot()
# # plt.show()

#随机产生3组从未出现过的号
for i in range(3):
    a = random.sample(range(1,35),5)
    sorted_num_red = sorted(a)
    b = random.sample(range(1,12),2)
    sorted_num_blue = sorted(b)

    sorted_num_red.append(sorted_num_blue[0])
    sorted_num_red.append(sorted_num_blue[1])
    sorted_num = sorted_num_red

    sorted_num = np.array(sorted_num)

    isIn = np.any(np.all(sorted_num == c, axis=1))
    if(isIn == False):
        print(sorted_num)








