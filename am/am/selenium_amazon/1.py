# d = ['婴儿用品商品里排第41名', '(查看婴儿用品商品销售排行榜)\n.zg_hrsr', '{', 'margin:', '0;', 'padding:', '0;', 'list-style-type:', 'none;',
#      '}', '.zg_hrsr_item', '{', 'margin:', '0', '0', '0', '10px;', '}', '.zg_hrsr_rank', '{', 'display:',
#      'inline-block;', 'width:', '80px;', 'text-align:', 'right;', '}\n第1位', '-\xa0婴儿包被']


#
# d1 = ['婴儿用品商品里排第43名', '(查看婴儿用品商品销售排行榜)\n.zg_hrsr']
# d2 = (str(i) for i in d1)
# print("".join(d2))
#



# ls1 = ['a', 1, 'b', 2]
# ls2 = [str(i) for i in ls1]
# ['a', '1', 'b', '2']
# ls3 = ''.join(ls2)


#
# import xlwt
#
# # 创建工作workbook
# workbook = xlwt.Workbook()
#
# # 创建工作表worksheet,填入表名
# worksheet = workbook.add_sheet('表名')
#
# worksheet.write(0, 0, '商品名称')
# worksheet.write(0, 1, '商品价格')
# worksheet.write(0, 2, '评价数量')
# worksheet.write(0, 3, '评价星级')
# worksheet.write(0, 4, '商品url')
# worksheet.write(0, 5, 'ASIN码')
# worksheet.write(0, 6, '排行')
# worksheet.write(0, 7, '店家名称')
# worksheet.write(0, 8, '包装尺寸')
# worksheet.write(0, 9, '重量')
#
# j = [{'price': '$11129.95', 'commit': '2,421', 'name': 'Love To Dream Swaddle UP, Dramatically Better Sleep, Allow Baby to Sleep in Their Preferred arms up Position for self-Soothing', 'icon': '4.3 out of 5 stars', 'name_url': 'https://www.amazon.com/Love-Dream-Swaddle-Original-13-18-5/dp/B005MATQNK/ref=zg_bsnr_3206325011_1?_encoding=UTF8&psc=1&refRID=G21Z82JHF5R0Y20YYMCN', 'ASIN': 'B005MATQNK', 'BestSellersRank': '#38in', 'PackageDimensions': '4.8 ounces', 'ItemWeight': '[<td.value>]','Manufacturer': 'Love to Dream', 'reviews': '2,421 customer reviews'}
# ,{'price': '$29222.95', 'commit': '2,421', 'name': 'Love To Dream Swaddle UP, Dramatically Better Sleep, Allow Baby to Sleep in Their Preferred arms up Position for self-Soothing', 'icon': '4.3 out of 5 stars', 'name_url': 'https://www.amazon.com/Love-Dream-Swaddle-Original-13-18-5/dp/B005MATQNK/ref=zg_bsnr_3206325011_1?_encoding=UTF8&psc=1&refRID=G21Z82JHF5R0Y20YYMCN', 'ASIN': 'B005MATQNK', 'BestSellersRank': '#38in', 'PackageDimensions': '4.8 ounces', 'ItemWeight': '[<td.value>]','Manufacturer': 'Love to Dream', 'reviews': '2,421 customer reviews'}
# ,{'price': '$29.95', 'commit': '2,421', 'name': 'Love To Dream Swaddle UP, Dramatically Better Sleep, Allow Baby to Sleep in Their Preferred arms up Position for self-Soothing', 'icon': '4.3 out of 5 stars', 'name_url': 'https://www.amazon.com/Love-Dream-Swaddle-Original-13-18-5/dp/B005MATQNK/ref=zg_bsnr_3206325011_1?_encoding=UTF8&psc=1&refRID=G21Z82JHF5R0Y20YYMCN', 'ASIN': 'B005MATQNK', 'BestSellersRank': '#38in', 'PackageDimensions': '4.8 ounces', 'ItemWeight': '[<td.value>]','Manufacturer': 'Love to Dream', 'reviews': '2,421 customer reviews'}
# ]
#
# for a in range(len(j)):
#     # print(a)
#     c = 0
#     d = j[a]
#     print(d)
#
#     # 在表中写入相应的数据
#     worksheet.col(c).width = 256 * 30
#     # 1,0
#     a += 1
#     print(a)
#     worksheet.write(a,c,d['name'])
#     worksheet.col(c).width = 256 * 30
#     c += 1
#     # print(a)
#     worksheet.write(a,c,d['price'])
#     worksheet.col(c).width = 256 * 30
#     c += 1
#     worksheet.write(a,c,d['commit'])
#     worksheet.col(c).width = 256 * 30
#     c += 1
#     worksheet.write(a,c,d['icon'])
#     worksheet.col(c).width = 256 * 30
#     c += 1
#     worksheet.write(a,c,d['name_url'])
#     worksheet.col(c).width = 256 * 30
#     c += 1
#     worksheet.write(a,c,d['ASIN'])
#     worksheet.col(c).width = 256 * 30
#     c += 1
#     worksheet.write(a,c,d['BestSellersRank'])
#     worksheet.col(c).width = 256 * 30
#     c += 1
#     worksheet.write(a,c,d['Manufacturer'])
#     worksheet.col(c).width = 256 * 30
#     c += 1
#     worksheet.write(a,c,d['PackageDimensions'])
#     worksheet.col(c).width = 256 * 30
#     c += 1
#     worksheet.write(a,c,d['ItemWeight'])
#     worksheet.col(c).width = 256 * 30
#
#
# #
# # 保存表
#
#     workbook.save('2q11111q21.xls')
#

# d = {'price': '$29.95', 'commit': '2,421', 'name': 'Love To Dream Swaddle UP, Dramatically Better Sleep, Allow Baby to Sleep in Their Preferred arms up Position for self-Soothing', 'icon': '4.3 out of 5 stars', 'name_url': 'https://www.amazon.com/Love-Dream-Swaddle-Original-13-18-5/dp/B005MATQNK/ref=zg_bsnr_3206325011_1?_encoding=UTF8&psc=1&refRID=G21Z82JHF5R0Y20YYMCN', 'ASIN': 'B005MATQNK', 'BestSellersRank': '#38in', 'PackageDimensions': '4.8 ounces', 'ItemWeight': '[<td.value>]','Manufacturer': 'Love to Dream', 'reviews': '2,421 customer reviews'}


#
# j = [{'price': '$11129.95', 'commit': '2,421', 'name': 'Love To Dream Swaddle UP, Dramatically Better Sleep, Allow Baby to Sleep in Their Preferred arms up Position for self-Soothing', 'icon': '4.3 out of 5 stars', 'name_url': 'https://www.amazon.com/Love-Dream-Swaddle-Original-13-18-5/dp/B005MATQNK/ref=zg_bsnr_3206325011_1?_encoding=UTF8&psc=1&refRID=G21Z82JHF5R0Y20YYMCN', 'ASIN': 'B005MATQNK', 'BestSellersRank': '#38in', 'PackageDimensions': '4.8 ounces', 'ItemWeight': '[<td.value>]','Manufacturer': 'Love to Dream', 'reviews': '2,421 customer reviews'}
# ,{'price': '$29222.95', 'commit': '2,421', 'name': 'Love To Dream Swaddle UP, Dramatically Better Sleep, Allow Baby to Sleep in Their Preferred arms up Position for self-Soothing', 'icon': '4.3 out of 5 stars', 'name_url': 'https://www.amazon.com/Love-Dream-Swaddle-Original-13-18-5/dp/B005MATQNK/ref=zg_bsnr_3206325011_1?_encoding=UTF8&psc=1&refRID=G21Z82JHF5R0Y20YYMCN', 'ASIN': 'B005MATQNK', 'BestSellersRank': '#38in', 'PackageDimensions': '4.8 ounces', 'ItemWeight': '[<td.value>]','Manufacturer': 'Love to Dream', 'reviews': '2,421 customer reviews'}
# ,{'price': '$29.95', 'commit': '2,421', 'name': 'Love To Dream Swaddle UP, Dramatically Better Sleep, Allow Baby to Sleep in Their Preferred arms up Position for self-Soothing', 'icon': '4.3 out of 5 stars', 'name_url': 'https://www.amazon.com/Love-Dream-Swaddle-Original-13-18-5/dp/B005MATQNK/ref=zg_bsnr_3206325011_1?_encoding=UTF8&psc=1&refRID=G21Z82JHF5R0Y20YYMCN', 'ASIN': 'B005MATQNK', 'BestSellersRank': '#38in', 'PackageDimensions': '4.8 ounces', 'ItemWeight': '[<td.value>]','Manufacturer': 'Love to Dream', 'reviews': '2,421 customer reviews'}
# ]
#
#
# l = len(j)
# print(l)
# for i in range(l):
#     print(i)
#     print(j[i])
#
# {'price': '$8.49', 'commit': '511', 'name': 'Flamingo P Memory Foam Luxury Bath Rugs Anti-Slip Striped Pattern One Pack', 'icon': '4.3 out of 5 stars', 'name_url': 'https://www.amazon.com/Non-Slip-Bathroom-Absorbent-Comfortable-Stylish/dp/B07R4X9RGZ/ref=zg_bsnr_3206325011_15?_encoding=UTF8&psc=1&refRID=YW06SJ6A6XMJ3BGPKDWS', 'ASIN': 'B07R4X9RGZ', 'BestSellersRank': "#4,772 in Home & Kitchen (See Top 100 in Home & Kitchen)\n#2 in Kids' Bath Rugs\n#25 in Bath Rugs", 'PackageDimensions': '16.8 x 11.8 x 1.4 inches', 'ItemWeight': [], 'Manufacturer': 'Flamingo P'}
#
#
#
# {'price': '$28.99', 'commit': '3,225', 'name': 'BreathableBaby Classic Breathable Mesh Crib Liner - White', 'icon': '4.3 out of 5 stars', 'name_url': 'https://www.amazon.com/Breathable-Endorsed-Prevents-Getting-Slatted/dp/B0013FGWD0/ref=zg_bsnr_3206325011_16?_encoding=UTF8&psc=1&refRID=YW06SJ6A6XMJ3BGPKDWS', 'ASIN': 'B0013FGWD0', 'BestSellersRank': '#769 in Baby (See Top 100 in Baby)\n.zg_hrsr { margin: 0; padding: 0; list-style-type: none; } .zg_hrsr_item { margin: 0 0 0 10px; } .zg_hrsr_rank { display: inline-block; width: 80px; text-align: right; }\n#2 in\xa0Crib Bedding Bumpers', 'PackageDimensions': '111 x 11 inches', 'ItemWeight':'[<td.value>]' , 'Manufacturer': 'BreathableBaby'}
#
#
# s = 'B01MTA00AX'
# print(len(s))
# https://www.amazon.com/gp/new-releases/home-garden/3206325011/ref=zg_bsnr_pg_2?ie=UTF8&pg=2

from urllib.parse import urlencode

# start_urls = []
# keyword = ['3206325011', '284507', '1063252', '1063236', '1063306', '1063278', '3736081', '13679381', '3206324011',
#            '510240', '510106', '3610841', '10802561']
# for kw in keyword:
#     for pg in range(1, 2):
#         # 转换格式
#         pg = str(pg)
#         next_page_url = 'https://www.amazon.com/gp/new-releases/home-garden/' + kw  + '/ref=zg_bsnr_pg_' + pg + '?ie=UTF8&pg=' + pg
#         start_urls.append(next_page_url)
#
#
# print(start_urls)
# print(len(start_urls))


from selenium import webdriver



#!/usr/bin/env python
# -*- coding:utf8 -*-

# import redis
# import requests
# from selenium.webdriver.support.ui import WebDriverWait
#
# '''
# 这种连接是连接一次就断了，耗资源.端口默认6379，就不用写
# r = redis.Redis(host='127.0.0.1',port=6379,password='tianxuroot')
# r.set('name','root')
#
# print(r.get('name').decode('utf8'))
# '''
# '''
# 连接池：
# 当程序创建数据源实例时，系统会一次性创建多个数据库连接，并把这些数据库连接保存在连接池中，当程序需要进行数据库访问时，
# 无需重新新建数据库连接，而是从连接池中取出一个空闲的数据库连接
# '''
# # pool = redis.ConnectionPool(host='127.0.0.1')   #实现一个连接池
# pool = redis.ConnectionPool(host='192.168.5.5')   #实现一个连接池
# ip_pool = redis.Redis(connection_pool=pool)
# a =0
# while True:
#     a += 1
#     l = ip_pool.srandmember('china_ip', 1)
#     # l = ip_pool.spop('ip1', 1)
#     print(ip_pool.scard('ip1'))
#
#     for i in l:
#         j = eval(i.decode())
#         ip = j['ip']+":"+j['port']
#         print(ip)
#
#         import re
#         import requests
#
#         url = "www.baidu.com"
#
#         headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
#         }
#         proxies = {
#             "https": "https://" + 'ip'
#         }
#         response = requests.get(url, headers=headers, proxies=proxies).content.decode()
#
#         print(requests.status_codes)
#


    #     chromeOptions = webdriver.ChromeOptions()
    #
    #     # 设置代理
    #     # chromeOptions.add_argument("--proxy-server=http://202.20.16.82:10152")
    #     chromeOptions.add_argument("--proxy-server=http://" + ip)
    #     # 设置UA
        # chromeOptions.add_argument('User-Agent = Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36')

        # 设置无头浏览器
        # chromeOptions.add_argument("--headless")

        # 设置默认编码为 utf-8
        # chromeOptions.add_argument('lang=zh_CN.UTF-8')

        # print(a)
        # browser = webdriver.Chrome(chrome_options=chromeOptions)
        # # 打开指定网页
        # browser.get("https:www.amazon.com")
        # # 显示等待
        # wait = WebDriverWait(browser, 10)
        #
        # # 退出，清除浏览器缓存
        # browser.quit()


#
# def checkip(ip_port):
#     ip_port = eval(ip_port)
#     ip = ip_port['ip']
#     port = ip_port['port']
#     proxies = {"http": "http://"+ ip + ':' + port, "https": "https://"+ ip + ':' + port} # 代理ip
#     print(proxies)
#     try:
#     response=requests.get(url=url,proxies=proxies,headers=headers,timeout=20)
#     print(response.status_code)
#     response = response.status_code
#     print(type(response))
#     if response == 200 :
#     return ip_port
#     else:
#     return False
#     except:
#     return False


#
# s = ['\n                \n                    \n                    \n                \n\n                \n                    \n                    \nleadtimes 双人床 / 双人床 / 大号双人床花卉轻质印花图案超细纤维羽绒被罩，柔软床上用品套装2个枕头套和1个羽绒被套, 微纤维, 两个\n                    \n\n\n                \n                    \n                    \n                \n            ']
#
# s = ''.join(s)
# s = s.split()
# print(s)
# s = ' '.join(s)
# # s = s[1:]
# print(s)

import json

#
#BestSellersRank = '#101 in Home & Kitchen (See Top 100 in Home & Kitchen)\n#1 in Commercial Wet Mops\n#4 in Household Mops, Buckets & Accessories'

#BestSellersRank = "Amazon Best Sellers Rank: #126 in Health & Household (See Top 100 in Health & Household)\n.zg_hrsr { margin: 0; padding: 0; list-style-type: none; } .zg_hrsr_item { margin: 0 0 0 10px; } .zg_hrsr_rank { display: inline-block; width: 80px; text-align: right; }\n#53 in\xa0Sales & Deals\n#2 in\xa0Commercial Bathroom Cleaners\n#3 in\xa0Household Toilet Cleaners', 'PackageDimensions'"

#BestSellersRank = '/* * Fix for UDP-1061. Average customer reviews has a small extra line on hover * https://omni-grok.amazon.com/xref/src/appgroup/websiteTemplates/retail/SoftlinesDetailPageAssets/udp-intl-lock/src/legacy.css?indexName=WebsiteTemplates#40 */ .noUnderline a:hover { text-decoration: none; }\n4.4 out of 5 stars 5,299 customer reviews P.when(\'A\', \'ready\').execute(function(A) { A.declarative(\'acrLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrLinkClickCount", (ue.count("acrLinkClickCount") || 0) + 1); } }); }); P.when(\'A\', \'cf\').execute(function(A) { A.declarative(\'acrStarsLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrStarsLinkWithPopoverClickCount", (ue.count("acrStarsLinkWithPopoverClickCount") || 0) + 1); } }); });\n\n4.4 out of 5 stars'


# if BestSellersRank[0:4] == '/* *':
#     BestSellersRank1 = ""
#     BestSellersRank2 = ""
#
# if BestSellersRank[0:4] != '/* *':
#
#     BestSellersRank = BestSellersRank.split('\n')
#     BestSellersRank1 = BestSellersRank[0:1]
#     for i in BestSellersRank1:
#         BestSellersRank1 = i.split('(')[0:1]
#         BestSellersRank1 = ''.join(BestSellersRank1)
#
#     BestSellersRank2 = BestSellersRank[1:]
#     BestSellersRank2 = ''.join(BestSellersRank2)
#     BestSellersRank2 = BestSellersRank2.split('#')
#
#     if len(BestSellersRank2) >= 3:
#         BestSellersRank2 = BestSellersRank2[-2:]
#         BestSellersRank2 = ''.join(BestSellersRank2)
#
#     if len(BestSellersRank2) < 3:
#         BestSellersRank2 = BestSellersRank2[-1:]
#         BestSellersRank2 = ''.join(BestSellersRank2)
#
# print("--------------")
# print(BestSellersRank1)
# print(BestSellersRank2)



# s1 = s.split("\n")
# print(s1)
# print(s1)
# print("==========")
# print(s1[0:1])
# s2 = s1[1:]
# print(s2)
#
# print(''.join(s2))
# s2 = s1[0:1]
# for i in s2:
#     i1 = i.split('(')[0:1]
#     for j in i1:
#         pass



# s = '.zg_hrsr { margin: 0; padding: 0; list-style-type: none; } .zg_hrsr_item { margin: 0 0 0 10px; } .zg_hrsr_rank { display: inline-block; width: 80px; text-align: right; }#555 in Sales & Deals#7 in Household Cleaning Sponges'
#
# s1 = s.split('#')
# print(s1[-2:])

# s = " "
# for i in s:
#     print(i, 'dd')

# s = 'New (1) from $19.90 & FREE shipping on orders over $25.00. Details'
# print(s[:-9])



# title = doc("#detail-bullets > table > tbody > tr > td > div.content > ul").text()
# if title == "":
#     title = doc("#productDetails_techSpec_section_1 > tbody").text()
#     if title == "":
#         title = doc("#productDetails_detailBullets_sections1 > tbody").text()
#         if title == "":
#             title = doc("#prodDetails > div").text()
#             if title == "":
#                 title = doc("#prodDetails > div.wrapper.USlocale").text()
#                 if title == "":
#                     title = doc("#detailBulletsWrapper_feature_div").text()
#
# print(title.split('\n'))


a= ['Product Dimensions', '16 x 12 x 35 inches', 'Item Weight', '1.55 pounds', 'Shipping Weight', '1.55 pounds (View shipping rates and policies)', 'Manufacturer', 'Big Joe', 'ASIN', 'B0055DXQS0', 'Item model number', '9999999', 'Customer Reviews', '/* * Fix for UDP-1061. Average customer reviews has a small extra line on hover * https://omni-grok.amazon.com/xref/src/appgroup/websiteTemplates/retail/SoftlinesDetailPageAssets/udp-intl-lock/src/legacy.css?indexName=WebsiteTemplates#40 */ .noUnderline a:hover { text-decoration: none; }', '4.0 out of 5 stars 2,365 customer reviews P.when(\'A\', \'ready\').execute(function(A) { A.declarative(\'acrLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrLinkClickCount", (ue.count("acrLinkClickCount") || 0) + 1); } }); }); P.when(\'A\', \'cf\').execute(function(A) { A.declarative(\'acrStarsLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrStarsLinkWithPopoverClickCount", (ue.count("acrStarsLinkWithPopoverClickCount") || 0) + 1); } }); });', '', '4.0 out of 5 stars', 'Best Sellers Rank', '#504 in Home & Kitchen (See Top 100 in Home & Kitchen)', "#1 in Kids' Chairs", '#1 in Bean Bag Chairs']

a1 = ['Product Dimensions', '18 x 14 x 4 inches', 'Item Weight', '13.6 ounces', 'Shipping Weight', '13.6 ounces (View shipping rates and policies)', 'Manufacturer', 'CASOFU', 'ASIN', 'B07QVHQ8KD', 'Customer Reviews', '/* * Fix for UDP-1061. Average customer reviews has a small extra line on hover * https://omni-grok.amazon.com/xref/src/appgroup/websiteTemplates/retail/SoftlinesDetailPageAssets/udp-intl-lock/src/legacy.css?indexName=WebsiteTemplates#40 */ .noUnderline a:hover { text-decoration: none; }', '4.8 out of 5 stars 244 customer reviews P.when(\'A\', \'ready\').execute(function(A) { A.declarative(\'acrLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrLinkClickCount", (ue.count("acrLinkClickCount") || 0) + 1); } }); }); P.when(\'A\', \'cf\').execute(function(A) { A.declarative(\'acrStarsLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrStarsLinkWithPopoverClickCount", (ue.count("acrStarsLinkWithPopoverClickCount") || 0) + 1); } }); });', '', '4.8 out of 5 stars', 'Best Sellers Rank', '#927 in Home & Kitchen (See Top 100 in Home & Kitchen)', "#1 in Kids' Bed Blankets", '#4 in Bed Throws']

a2 = ['Package Dimensions', '13.7 x 12.6 x 1.3 inches', 'Item Weight', '13.1 ounces', 'Shipping Weight', '13.1 ounces (View shipping rates and policies)', 'Manufacturer', 'YnM', 'ASIN', 'B07RGG4R13', 'Item model number', 'feirenmian122', 'Customer Reviews', '/* * Fix for UDP-1061. Average customer reviews has a small extra line on hover * https://omni-grok.amazon.com/xref/src/appgroup/websiteTemplates/retail/SoftlinesDetailPageAssets/udp-intl-lock/src/legacy.css?indexName=WebsiteTemplates#40 */ .noUnderline a:hover { text-decoration: none; }', '4.2 out of 5 stars 667 customer reviews P.when(\'A\', \'ready\').execute(function(A) { A.declarative(\'acrLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrLinkClickCount", (ue.count("acrLinkClickCount") || 0) + 1); } }); }); P.when(\'A\', \'cf\').execute(function(A) { A.declarative(\'acrStarsLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrStarsLinkWithPopoverClickCount", (ue.count("acrStarsLinkWithPopoverClickCount") || 0) + 1); } }); });', '', '4.2 out of 5 stars', 'Best Sellers Rank', '#1,131 in Home & Kitchen (See Top 100 in Home & Kitchen)', "#4 in Kids' Blankets & Throws", '#7 in Bed Blankets']

a3 = ['Package Dimensions', '17.7 x 1.2 x 1 inches', 'Item Weight', '9.6 ounces', 'Shipping Weight', '9.6 ounces (View shipping rates and policies)', 'Manufacturer', 'KESPEN', 'ASIN', 'B07P7FKW8X', 'Customer Reviews', '/* * Fix for UDP-1061. Average customer reviews has a small extra line on hover * https://omni-grok.amazon.com/xref/src/appgroup/websiteTemplates/retail/SoftlinesDetailPageAssets/udp-intl-lock/src/legacy.css?indexName=WebsiteTemplates#40 */ .noUnderline a:hover { text-decoration: none; }', '4.3 out of 5 stars 159 customer reviews P.when(\'A\', \'ready\').execute(function(A) { A.declarative(\'acrLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrLinkClickCount", (ue.count("acrLinkClickCount") || 0) + 1); } }); }); P.when(\'A\', \'cf\').execute(function(A) { A.declarative(\'acrStarsLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrStarsLinkWithPopoverClickCount", (ue.count("acrStarsLinkWithPopoverClickCount") || 0) + 1); } }); });', '', '4.3 out of 5 stars', 'Best Sellers Rank', '#1,243 in Home & Kitchen (See Top 100 in Home & Kitchen)', '#3 in Window Films']

a4 = ['Product Dimensions', '23.6 x 1.8 x 1.8 inches', 'Item Weight', '1.65 pounds', 'Shipping Weight', '1.65 pounds (View shipping rates and policies)', 'Manufacturer', 'HIDBEA', 'ASIN', 'B07CK1FH6K', 'Item model number', 'WM-BLSI-60-400', 'Customer Reviews', '/* * Fix for UDP-1061. Average customer reviews has a small extra line on hover * https://omni-grok.amazon.com/xref/src/appgroup/websiteTemplates/retail/SoftlinesDetailPageAssets/udp-intl-lock/src/legacy.css?indexName=WebsiteTemplates#40 */ .noUnderline a:hover { text-decoration: none; }', '4.1 out of 5 stars 147 customer reviews P.when(\'A\', \'ready\').execute(function(A) { A.declarative(\'acrLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrLinkClickCount", (ue.count("acrLinkClickCount") || 0) + 1); } }); }); P.when(\'A\', \'cf\').execute(function(A) { A.declarative(\'acrStarsLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrStarsLinkWithPopoverClickCount", (ue.count("acrStarsLinkWithPopoverClickCount") || 0) + 1); } }); });', '', '4.1 out of 5 stars', 'Best Sellers Rank', '#1,705 in Home & Kitchen (See Top 100 in Home & Kitchen)', '#5 in Window Films']

a5 = ['Product Dimensions', '16.8 x 11.3 x 2 inches', 'Item Weight', '8.8 ounces', 'Shipping Weight', '8.8 ounces (View shipping rates and policies)', 'Manufacturer', 'Flamingo P', 'ASIN', 'B01A0O9YBG', 'Item model number', 'RUGS-11017', 'Customer Reviews', '/* * Fix for UDP-1061. Average customer reviews has a small extra line on hover * https://omni-grok.amazon.com/xref/src/appgroup/websiteTemplates/retail/SoftlinesDetailPageAssets/udp-intl-lock/src/legacy.css?indexName=WebsiteTemplates#40 */ .noUnderline a:hover { text-decoration: none; }', '4.3 out of 5 stars 524 customer reviews P.when(\'A\', \'ready\').execute(function(A) { A.declarative(\'acrLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrLinkClickCount", (ue.count("acrLinkClickCount") || 0) + 1); } }); }); P.when(\'A\', \'cf\').execute(function(A) { A.declarative(\'acrStarsLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrStarsLinkWithPopoverClickCount", (ue.count("acrStarsLinkWithPopoverClickCount") || 0) + 1); } }); });', '', '4.3 out of 5 stars', 'Best Sellers Rank', '#1,773 in Home & Kitchen (See Top 100 in Home & Kitchen)', "#1 in Kids' Bath Rugs", '#11 in Bath Rugs']

a6 = ['Style: Slatted & Solid-Back Crib\xa0|\xa0Color: White Technical Details', 'Item Weight', '1 pounds', 'Product Dimensions', '111 x 11 inches', 'UPC', '811283020001 811283021343 885366969600 885468211263 094922799647 885682351967', 'Item model number', '110111', 'Material Type', 'Phthalate Free, Latex Free, Lead Free, BPA Free', 'Number of items', '1', 'Style', 'Slatted & Solid-Back Crib', 'Batteries required', 'No', 'Additional Information', 'ASIN', 'B0013FGWD0', 'Customer Reviews', '4.3 out of 5 stars 3,243 customer reviews', 'Amazon Best Sellers Rank', '#270 in Baby (See Top 100 in Baby)', '.zg_hrsr { margin: 0; padding: 0; list-style-type: none; } .zg_hrsr_item { margin: 0 0 0 10px; } .zg_hrsr_rank { display: inline-block; width: 80px; text-align: right; }', '#1 in\xa0Crib Bedding Bumpers', 'Shipping Weight', '1 pounds (View shipping rates and policies)', 'Domestic Shipping', 'Item can be shipped within U.S.', 'International Shipping', 'This item can be shipped to select countries outside of the U.S. Learn More', 'Warranty & Support', '', 'Manufacturer’s warranty can be requested from customer service. Click here to make a request to customer service.', 'Feedback', 'P.now("A","tellMeMoreLinkData").execute(function(A,tellMeMoreLinkData){ if(typeof tellMeMoreLinkData !== \'undefined\'){ A.state(\'lowerPricePopoverData\',{"trigger":"ns_T0EJFDVKJXVXY76V11DB_11938_1_hmd_pricing_feedback_trigger_product-details","destination":"/gp/pdp/pf/pricingFeedbackForm.html/ref=zg_bsnr_baby-products_2?ie=UTF8&ASIN=B0013FGWD0&PREFIX=ns_T0EJFDVKJXVXY76V11DB_11938_2_&WDG=baby_product_display_on_website&dpRequestId=T0EJFDVKJXVXY76V11DB&from=product-details&psc=1&refRID=QDXH5Y52T7BDCQWS49PY&storeID=baby-productsencodeURI(\'&originalURI=\' + window.location.pathname)","url":"/gp/pdp/pf/pricingFeedbackForm.html/ref=zg_bsnr_baby-products_2?ie=UTF8&ASIN=B0013FGWD0&PREFIX=ns_T0EJFDVKJXVXY76V11DB_11938_2_&WDG=baby_product_display_on_website&dpRequestId=T0EJFDVKJXVXY76V11DB&from=product-details&psc=1&refRID=QDXH5Y52T7BDCQWS49PY&storeID=baby-products","nsPrefix":"ns_T0EJFDVKJXVXY76V11DB_11938_2_","path":"encodeURI(\'&originalURI=\' + window.location.pathname)","title":"Tell Us About a Lower Price"}); return { key:"pricing-fbW", method: function(){ return {"trigger":"ns_T0EJFDVKJXVXY76V11DB_11938_1_hmd_pricing_feedback_trigger_product-details","destination":"/gp/pdp/pf/pricingFeedbackForm.html/ref=zg_bsnr_baby-products_2?ie=UTF8&ASIN=B0013FGWD0&PREFIX=ns_T0EJFDVKJXVXY76V11DB_11938_2_&WDG=baby_product_display_on_website&dpRequestId=T0EJFDVKJXVXY76V11DB&from=product-details&psc=1&refRID=QDXH5Y52T7BDCQWS49PY&storeID=baby-productsencodeURI(\'&originalURI=\' + window.location.pathname)","url":"/gp/pdp/pf/pricingFeedbackForm.html/ref=zg_bsnr_baby-products_2?ie=UTF8&ASIN=B0013FGWD0&PREFIX=ns_T0EJFDVKJXVXY76V11DB_11938_2_&WDG=baby_product_display_on_website&dpRequestId=T0EJFDVKJXVXY76V11DB&from=product-details&psc=1&refRID=QDXH5Y52T7BDCQWS49PY&storeID=baby-products","nsPrefix":"ns_T0EJFDVKJXVXY76V11DB_11938_2_","path":"encodeURI(\'&originalURI=\' + window.location.pathname)","title":"Tell Us About a Lower Price"}; } } } else{ P.when("A").register("tellMeMoreLinkData",function(A){ A.state(\'lowerPricePopoverData\',{"trigger":"ns_T0EJFDVKJXVXY76V11DB_11938_1_hmd_pricing_feedback_trigger_product-details","destination":"/gp/pdp/pf/pricingFeedbackForm.html/ref=zg_bsnr_baby-products_2?ie=UTF8&ASIN=B0013FGWD0&PREFIX=ns_T0EJFDVKJXVXY76V11DB_11938_2_&WDG=baby_product_display_on_website&dpRequestId=T0EJFDVKJXVXY76V11DB&from=product-details&psc=1&refRID=QDXH5Y52T7BDCQWS49PY&storeID=baby-productsencodeURI(\'&originalURI=\' + window.location.pathname)","url":"/gp/pdp/pf/pricingFeedbackForm.html/ref=zg_bsnr_baby-products_2?ie=UTF8&ASIN=B0013FGWD0&PREFIX=ns_T0EJFDVKJXVXY76V11DB_11938_2_&WDG=baby_product_display_on_website&dpRequestId=T0EJFDVKJXVXY76V11DB&from=product-details&psc=1&refRID=QDXH5Y52T7BDCQWS49PY&storeID=baby-products","nsPrefix":"ns_T0EJFDVKJXVXY76V11DB_11938_2_","path":"encodeURI(\'&originalURI=\' + window.location.pathname)","title":"Tell Us About a Lower Price"}); return { key:"pricing-fbW", method: function(){ return {"trigger":"ns_T0EJFDVKJXVXY76V11DB_11938_1_hmd_pricing_feedback_trigger_product-details","destination":"/gp/pdp/pf/pricingFeedbackForm.html/ref=zg_bsnr_baby-products_2?ie=UTF8&ASIN=B0013FGWD0&PREFIX=ns_T0EJFDVKJXVXY76V11DB_11938_2_&WDG=baby_product_display_on_website&dpRequestId=T0EJFDVKJXVXY76V11DB&from=product-details&psc=1&refRID=QDXH5Y52T7BDCQWS49PY&storeID=baby-productsencodeURI(\'&originalURI=\' + window.location.pathname)","url":"/gp/pdp/pf/pricingFeedbackForm.html/ref=zg_bsnr_baby-products_2?ie=UTF8&ASIN=B0013FGWD0&PREFIX=ns_T0EJFDVKJXVXY76V11DB_11938_2_&WDG=baby_product_display_on_website&dpRequestId=T0EJFDVKJXVXY76V11DB&from=product-details&psc=1&refRID=QDXH5Y52T7BDCQWS49PY&storeID=baby-products","nsPrefix":"ns_T0EJFDVKJXVXY76V11DB_11938_2_","path":"encodeURI(\'&originalURI=\' + window.location.pathname)","title":"Tell Us About a Lower Price"}; } } }); } }); Would you like to tell us about a lower price?']

a7 = ['Package Dimensions', '7.8 x 7 x 3.5 inches', 'Item Weight', '14.4 ounces', 'Shipping Weight', '14.4 ounces (View shipping rates and policies)', 'Manufacturer', 'mermaker', 'ASIN', 'B07QTHTDST', 'Customer Reviews', '/* * Fix for UDP-1061. Average customer reviews has a small extra line on hover * https://omni-grok.amazon.com/xref/src/appgroup/websiteTemplates/retail/SoftlinesDetailPageAssets/udp-intl-lock/src/legacy.css?indexName=WebsiteTemplates#40 */ .noUnderline a:hover { text-decoration: none; }', '4.8 out of 5 stars 135 customer reviews P.when(\'A\', \'ready\').execute(function(A) { A.declarative(\'acrLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrLinkClickCount", (ue.count("acrLinkClickCount") || 0) + 1); } }); }); P.when(\'A\', \'cf\').execute(function(A) { A.declarative(\'acrStarsLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrStarsLinkWithPopoverClickCount", (ue.count("acrStarsLinkWithPopoverClickCount") || 0) + 1); } }); });', '', '4.8 out of 5 stars', 'Best Sellers Rank', '#2,334 in Home & Kitchen (See Top 100 in Home & Kitchen)', "#1 in Kids' Throw Blankets"]

a8 = ['Product Dimensions', '17.9 x 1.9 x 1.3 inches', 'Item Weight', '5 ounces', 'Shipping Weight', '7.8 ounces (View shipping rates and policies)', 'Manufacturer', 'Rabbitgoo', 'ASIN', 'B01MTA00AX', 'Item model number', 'FBA_A023W-45', 'Customer Reviews', '/* * Fix for UDP-1061. Average customer reviews has a small extra line on hover * https://omni-grok.amazon.com/xref/src/appgroup/websiteTemplates/retail/SoftlinesDetailPageAssets/udp-intl-lock/src/legacy.css?indexName=WebsiteTemplates#40 */ .noUnderline a:hover { text-decoration: none; }', '4.1 out of 5 stars 1,189 customer reviews P.when(\'A\', \'ready\').execute(function(A) { A.declarative(\'acrLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrLinkClickCount", (ue.count("acrLinkClickCount") || 0) + 1); } }); }); P.when(\'A\', \'cf\').execute(function(A) { A.declarative(\'acrStarsLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrStarsLinkWithPopoverClickCount", (ue.count("acrStarsLinkWithPopoverClickCount") || 0) + 1); } }); });', '', '4.1 out of 5 stars', 'Best Sellers Rank', '#2,351 in Home & Kitchen (See Top 100 in Home & Kitchen)', '#7 in Window Films']

a9 = ['Part Number', 'CB-SOT-30-1/5-1', 'Item Weight', '9.91 pounds', 'Product Dimensions', '15 x 12 x 25.4 inches', 'Item model number', 'CB-SOT-30-1', 'Size', '8 Gal & 1.3 Gal', 'Color', 'Stainless Steel', 'Material', 'Stainless Steel', 'Shape', 'round', 'Item Package Quantity', '1', 'Included Components', 'Trashcan', 'Batteries Included?', 'No', 'Batteries Required?', 'No']

a10 = ['Product Dimensions', '90 x 68 x 1 inches', 'Item Weight', '6.95 pounds', 'Shipping Weight', '6.95 pounds (View shipping rates and policies)', 'Manufacturer', 'Intelligent Design', 'ASIN', 'B072MM5RHL', 'Item model number', 'ID10-1240', 'Customer Reviews', '/* * Fix for UDP-1061. Average customer reviews has a small extra line on hover * https://omni-grok.amazon.com/xref/src/appgroup/websiteTemplates/retail/SoftlinesDetailPageAssets/udp-intl-lock/src/legacy.css?indexName=WebsiteTemplates#40 */ .noUnderline a:hover { text-decoration: none; }', '4.5 out of 5 stars 261 customer reviews P.when(\'A\', \'ready\').execute(function(A) { A.declarative(\'acrLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrLinkClickCount", (ue.count("acrLinkClickCount") || 0) + 1); } }); }); P.when(\'A\', \'cf\').execute(function(A) { A.declarative(\'acrStarsLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrStarsLinkWithPopoverClickCount", (ue.count("acrStarsLinkWithPopoverClickCount") || 0) + 1); } }); });', '', '4.5 out of 5 stars', 'Best Sellers Rank', '#3,061 in Home & Kitchen (See Top 100 in Home & Kitchen)', "#1 in Kids' Comforter Sets"]

a11 = ['Product Dimensions', '20 x 12 x 0.4 inches', 'Item Weight', '7.7 ounces', 'Shipping Weight', '7.7 ounces (View shipping rates and policies)', 'Manufacturer', 'MIULEE', 'ASIN', 'B07PHPQ5NJ', 'Customer Reviews', '/* * Fix for UDP-1061. Average customer reviews has a small extra line on hover * https://omni-grok.amazon.com/xref/src/appgroup/websiteTemplates/retail/SoftlinesDetailPageAssets/udp-intl-lock/src/legacy.css?indexName=WebsiteTemplates#40 */ .noUnderline a:hover { text-decoration: none; }', '4.4 out of 5 stars 505 customer reviews P.when(\'A\', \'ready\').execute(function(A) { A.declarative(\'acrLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrLinkClickCount", (ue.count("acrLinkClickCount") || 0) + 1); } }); }); P.when(\'A\', \'cf\').execute(function(A) { A.declarative(\'acrStarsLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrStarsLinkWithPopoverClickCount", (ue.count("acrStarsLinkWithPopoverClickCount") || 0) + 1); } }); });', '', '4.4 out of 5 stars', 'Best Sellers Rank', '#3,164 in Home & Kitchen (See Top 100 in Home & Kitchen)', "#1 in Kids' Throw Pillows", '#16 in Throw Pillow Covers']

a12 = ['Product Dimensions', '2 x 0.5 inches', 'Item Weight', '2.4 ounces', 'Shipping Weight', '8.8 ounces (View shipping rates and policies)', 'Manufacturer', 'DHHX', 'ASIN', 'B01DPF5B5K', 'Customer Reviews', '/* * Fix for UDP-1061. Average customer reviews has a small extra line on hover * https://omni-grok.amazon.com/xref/src/appgroup/websiteTemplates/retail/SoftlinesDetailPageAssets/udp-intl-lock/src/legacy.css?indexName=WebsiteTemplates#40 */ .noUnderline a:hover { text-decoration: none; }', '4.2 out of 5 stars 562 customer reviews P.when(\'A\', \'ready\').execute(function(A) { A.declarative(\'acrLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrLinkClickCount", (ue.count("acrLinkClickCount") || 0) + 1); } }); }); P.when(\'A\', \'cf\').execute(function(A) { A.declarative(\'acrStarsLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrStarsLinkWithPopoverClickCount", (ue.count("acrStarsLinkWithPopoverClickCount") || 0) + 1); } }); });', '', '4.2 out of 5 stars', 'Best Sellers Rank', '#3,680 in Home & Kitchen (See Top 100 in Home & Kitchen)', '#1 in Window Stickers', '#8 in Window Films']

a13 = ['Product Dimensions', '2.5 x 2.5 x 3.8 inches', 'Item Weight', '4.8 ounces', 'Shipping Weight', '5 ounces (View shipping rates and policies)', 'ASIN', 'B07N5XG38M', 'Item model number', '38535', 'Manufacturer recommended age', '6 - 8 years', 'Best Sellers Rank', '#786 in Toys & Games (See Top 100 in Toys & Games)', "#135 in Kids' Home Store", '', 'Customer Reviews', '/* * Fix for UDP-1061. Average customer reviews has a small extra line on hover * https://omni-grok.amazon.com/xref/src/appgroup/websiteTemplates/retail/SoftlinesDetailPageAssets/udp-intl-lock/src/legacy.css?indexName=WebsiteTemplates#40 */ .noUnderline a:hover { text-decoration: none; }', '5.0 out of 5 stars 2 customer reviews P.when(\'A\', \'ready\').execute(function(A) { A.declarative(\'acrLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrLinkClickCount", (ue.count("acrLinkClickCount") || 0) + 1); } }); }); P.when(\'A\', \'cf\').execute(function(A) { A.declarative(\'acrStarsLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrStarsLinkWithPopoverClickCount", (ue.count("acrStarsLinkWithPopoverClickCount") || 0) + 1); } }); });', '', '5.0 out of 5 stars']

a14 = ['Product Dimensions', '13.3 x 12 x 1.7 inches', 'Item Weight', '1.65 pounds', 'Shipping Weight', '1.65 pounds (View shipping rates and policies)', 'Manufacturer', 'Leadtimes', 'ASIN', 'B073B9MDK6', 'Item model number', 'L026T2', 'Customer Reviews', '/* * Fix for UDP-1061. Average customer reviews has a small extra line on hover * https://omni-grok.amazon.com/xref/src/appgroup/websiteTemplates/retail/SoftlinesDetailPageAssets/udp-intl-lock/src/legacy.css?indexName=WebsiteTemplates#40 */ .noUnderline a:hover { text-decoration: none; }', '4.4 out of 5 stars 841 customer reviews P.when(\'A\', \'ready\').execute(function(A) { A.declarative(\'acrLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrLinkClickCount", (ue.count("acrLinkClickCount") || 0) + 1); } }); }); P.when(\'A\', \'cf\').execute(function(A) { A.declarative(\'acrStarsLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrStarsLinkWithPopoverClickCount", (ue.count("acrStarsLinkWithPopoverClickCount") || 0) + 1); } }); });', '', '4.4 out of 5 stars', 'Best Sellers Rank', '#4,215 in Home & Kitchen (See Top 100 in Home & Kitchen)', "#1 in Kids' Duvet Covers", '#14 in Bedding Duvet Cover Sets']

a15 = ['Product Dimensions', '15.5 x 42 x 31 inches', 'Item Weight', '26.9 pounds', 'Shipping Weight', '26.9 pounds (View shipping rates and policies)', 'Manufacturer', 'Humble Crew', 'ASIN', 'B07KKZ8K5C', 'Item model number', 'WO142', 'Customer Reviews', '/* * Fix for UDP-1061. Average customer reviews has a small extra line on hover * https://omni-grok.amazon.com/xref/src/appgroup/websiteTemplates/retail/SoftlinesDetailPageAssets/udp-intl-lock/src/legacy.css?indexName=WebsiteTemplates#40 */ .noUnderline a:hover { text-decoration: none; }', '4.3 out of 5 stars 142 customer reviews P.when(\'A\', \'ready\').execute(function(A) { A.declarative(\'acrLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrLinkClickCount", (ue.count("acrLinkClickCount") || 0) + 1); } }); }); P.when(\'A\', \'cf\').execute(function(A) { A.declarative(\'acrStarsLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrStarsLinkWithPopoverClickCount", (ue.count("acrStarsLinkWithPopoverClickCount") || 0) + 1); } }); });', '', '4.3 out of 5 stars', 'Best Sellers Rank', '#4,259 in Home & Kitchen (See Top 100 in Home & Kitchen)', "#3 in Kids' Bookcases, Cabinets & Shelves"]

a16 = ['Product Dimensions', '63 x 52 x 0.2 inches', 'Item Weight', '1.21 pounds', 'Shipping Weight', '1.46 pounds (View shipping rates and policies)', 'Manufacturer', 'NICETOWN', 'ASIN', 'B071VS2YFG', 'Item model number', 'Nicetown_Blackout', 'Customer Reviews', '/* * Fix for UDP-1061. Average customer reviews has a small extra line on hover * https://omni-grok.amazon.com/xref/src/appgroup/websiteTemplates/retail/SoftlinesDetailPageAssets/udp-intl-lock/src/legacy.css?indexName=WebsiteTemplates#40 */ .noUnderline a:hover { text-decoration: none; }', '4.8 out of 5 stars 1,024 customer reviews P.when(\'A\', \'ready\').execute(function(A) { A.declarative(\'acrLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrLinkClickCount", (ue.count("acrLinkClickCount") || 0) + 1); } }); }); P.when(\'A\', \'cf\').execute(function(A) { A.declarative(\'acrStarsLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrStarsLinkWithPopoverClickCount", (ue.count("acrStarsLinkWithPopoverClickCount") || 0) + 1); } }); });', '', '4.8 out of 5 stars', 'Best Sellers Rank', '#4,732 in Home & Kitchen (See Top 100 in Home & Kitchen)', '#1 in Nursery Curtain Panels']

a17 = ['Product Dimensions', '12 x 17 x 20.5 inches', 'Item Weight', '1 pounds', 'Shipping Weight', '2.6 pounds (View shipping rates and policies)', 'ASIN', 'B01N9KR1YF', 'Item model number', '6038505-6038453-6038493', 'Manufacturer recommended age', '18 months - 4 years', 'Best Sellers Rank', '#1,483 in Toys & Games (See Top 100 in Toys & Games)', "#2 in Kids' Sofas", '', 'Customer Reviews', '/* * Fix for UDP-1061. Average customer reviews has a small extra line on hover * https://omni-grok.amazon.com/xref/src/appgroup/websiteTemplates/retail/SoftlinesDetailPageAssets/udp-intl-lock/src/legacy.css?indexName=WebsiteTemplates#40 */ .noUnderline a:hover { text-decoration: none; }', '4.6 out of 5 stars 338 customer reviews P.when(\'A\', \'ready\').execute(function(A) { A.declarative(\'acrLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrLinkClickCount", (ue.count("acrLinkClickCount") || 0) + 1); } }); }); P.when(\'A\', \'cf\').execute(function(A) { A.declarative(\'acrStarsLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrStarsLinkWithPopoverClickCount", (ue.count("acrStarsLinkWithPopoverClickCount") || 0) + 1); } }); });', '', '4.6 out of 5 stars']

a18 = ['Package Dimensions', '14.4 x 12.6 x 3.6 inches', 'Item Weight', '1.19 pounds', 'Shipping Weight', '1.19 pounds', 'Manufacturer', 'OJIA', 'ASIN', 'B07NVDZRCR', 'Customer Reviews', '/* * Fix for UDP-1061. Average customer reviews has a small extra line on hover * https://omni-grok.amazon.com/xref/src/appgroup/websiteTemplates/retail/SoftlinesDetailPageAssets/udp-intl-lock/src/legacy.css?indexName=WebsiteTemplates#40 */ .noUnderline a:hover { text-decoration: none; }', '5.0 out of 5 stars 5 customer reviews P.when(\'A\', \'ready\').execute(function(A) { A.declarative(\'acrLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrLinkClickCount", (ue.count("acrLinkClickCount") || 0) + 1); } }); }); P.when(\'A\', \'cf\').execute(function(A) { A.declarative(\'acrStarsLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrStarsLinkWithPopoverClickCount", (ue.count("acrStarsLinkWithPopoverClickCount") || 0) + 1); } }); });', '', '5.0 out of 5 stars', 'Best Sellers Rank', '#2,032 in Kitchen & Dining (See Top 100 in Kitchen & Dining)', "#3 in Kids' Rugs", '', 'Date first listed on Amazon', 'April 9, 2019']

a19 = ['Item Weight', '5.6 ounces', 'Package Dimensions', '9.7 x 3.3 x 1.3 inches', 'Item model number', 'HS0089BI']

a20 = ['Technical Details', 'Item Weight', '3.2 pounds', 'Product Dimensions', '15.1 x 15.5 x 10.5 inches', 'UPC', '863861000448', 'Item model number', 'STL301', 'Best uses', 'Potty Training, Step Stool for Kids', 'Batteries required', 'No', 'Additional Information', 'ASIN', 'B07MR5DLYZ', 'Customer Reviews', '4.9 out of 5 stars 16 customer reviews', 'Amazon Best Sellers Rank', '#1,076 in Baby (See Top 100 in Baby)', '.zg_hrsr { margin: 0; padding: 0; list-style-type: none; } .zg_hrsr_item { margin: 0 0 0 10px; } .zg_hrsr_rank { display: inline-block; width: 80px; text-align: right; }', '#5 in\xa0Nursery Step Stools', 'Shipping Weight', '3.2 pounds (View shipping rates and policies)', 'Warranty & Support', '', 'Product Warranty: For warranty information about this product, please click here', 'Feedback', 'P.now("A","tellMeMoreLinkData").execute(function(A,tellMeMoreLinkData){ if(typeof tellMeMoreLinkData !== \'undefined\'){ A.state(\'lowerPricePopoverData\',{"trigger":"ns_DK59BWNKQD50ERQZMVAZ_32870_1_hmd_pricing_feedback_trigger_product-details","destination":"/gp/pdp/pf/pricingFeedbackForm.html/ref=zg_bsnr_baby-products_11?ie=UTF8&ASIN=B07MR5DLYZ&PREFIX=ns_DK59BWNKQD50ERQZMVAZ_32870_2_&WDG=baby_product_display_on_website&dpRequestId=DK59BWNKQD50ERQZMVAZ&from=product-details&psc=1&refRID=YX5GGHQ1X7YJMVVW6D93&storeID=baby-productsencodeURI(\'&originalURI=\' + window.location.pathname)","url":"/gp/pdp/pf/pricingFeedbackForm.html/ref=zg_bsnr_baby-products_11?ie=UTF8&ASIN=B07MR5DLYZ&PREFIX=ns_DK59BWNKQD50ERQZMVAZ_32870_2_&WDG=baby_product_display_on_website&dpRequestId=DK59BWNKQD50ERQZMVAZ&from=product-details&psc=1&refRID=YX5GGHQ1X7YJMVVW6D93&storeID=baby-products","nsPrefix":"ns_DK59BWNKQD50ERQZMVAZ_32870_2_","path":"encodeURI(\'&originalURI=\' + window.location.pathname)","title":"Tell Us About a Lower Price"}); return { key:"pricing-fbW", method: function(){ return {"trigger":"ns_DK59BWNKQD50ERQZMVAZ_32870_1_hmd_pricing_feedback_trigger_product-details","destination":"/gp/pdp/pf/pricingFeedbackForm.html/ref=zg_bsnr_baby-products_11?ie=UTF8&ASIN=B07MR5DLYZ&PREFIX=ns_DK59BWNKQD50ERQZMVAZ_32870_2_&WDG=baby_product_display_on_website&dpRequestId=DK59BWNKQD50ERQZMVAZ&from=product-details&psc=1&refRID=YX5GGHQ1X7YJMVVW6D93&storeID=baby-productsencodeURI(\'&originalURI=\' + window.location.pathname)","url":"/gp/pdp/pf/pricingFeedbackForm.html/ref=zg_bsnr_baby-products_11?ie=UTF8&ASIN=B07MR5DLYZ&PREFIX=ns_DK59BWNKQD50ERQZMVAZ_32870_2_&WDG=baby_product_display_on_website&dpRequestId=DK59BWNKQD50ERQZMVAZ&from=product-details&psc=1&refRID=YX5GGHQ1X7YJMVVW6D93&storeID=baby-products","nsPrefix":"ns_DK59BWNKQD50ERQZMVAZ_32870_2_","path":"encodeURI(\'&originalURI=\' + window.location.pathname)","title":"Tell Us About a Lower Price"}; } } } else{ P.when("A").register("tellMeMoreLinkData",function(A){ A.state(\'lowerPricePopoverData\',{"trigger":"ns_DK59BWNKQD50ERQZMVAZ_32870_1_hmd_pricing_feedback_trigger_product-details","destination":"/gp/pdp/pf/pricingFeedbackForm.html/ref=zg_bsnr_baby-products_11?ie=UTF8&ASIN=B07MR5DLYZ&PREFIX=ns_DK59BWNKQD50ERQZMVAZ_32870_2_&WDG=baby_product_display_on_website&dpRequestId=DK59BWNKQD50ERQZMVAZ&from=product-details&psc=1&refRID=YX5GGHQ1X7YJMVVW6D93&storeID=baby-productsencodeURI(\'&originalURI=\' + window.location.pathname)","url":"/gp/pdp/pf/pricingFeedbackForm.html/ref=zg_bsnr_baby-products_11?ie=UTF8&ASIN=B07MR5DLYZ&PREFIX=ns_DK59BWNKQD50ERQZMVAZ_32870_2_&WDG=baby_product_display_on_website&dpRequestId=DK59BWNKQD50ERQZMVAZ&from=product-details&psc=1&refRID=YX5GGHQ1X7YJMVVW6D93&storeID=baby-products","nsPrefix":"ns_DK59BWNKQD50ERQZMVAZ_32870_2_","path":"encodeURI(\'&originalURI=\' + window.location.pathname)","title":"Tell Us About a Lower Price"}); return { key:"pricing-fbW", method: function(){ return {"trigger":"ns_DK59BWNKQD50ERQZMVAZ_32870_1_hmd_pricing_feedback_trigger_product-details","destination":"/gp/pdp/pf/pricingFeedbackForm.html/ref=zg_bsnr_baby-products_11?ie=UTF8&ASIN=B07MR5DLYZ&PREFIX=ns_DK59BWNKQD50ERQZMVAZ_32870_2_&WDG=baby_product_display_on_website&dpRequestId=DK59BWNKQD50ERQZMVAZ&from=product-details&psc=1&refRID=YX5GGHQ1X7YJMVVW6D93&storeID=baby-productsencodeURI(\'&originalURI=\' + window.location.pathname)","url":"/gp/pdp/pf/pricingFeedbackForm.html/ref=zg_bsnr_baby-products_11?ie=UTF8&ASIN=B07MR5DLYZ&PREFIX=ns_DK59BWNKQD50ERQZMVAZ_32870_2_&WDG=baby_product_display_on_website&dpRequestId=DK59BWNKQD50ERQZMVAZ&from=product-details&psc=1&refRID=YX5GGHQ1X7YJMVVW6D93&storeID=baby-products","nsPrefix":"ns_DK59BWNKQD50ERQZMVAZ_32870_2_","path":"encodeURI(\'&originalURI=\' + window.location.pathname)","title":"Tell Us About a Lower Price"}; } } }); } }); Would you like to tell us about a lower price?']

a21 = ['Technical Details', 'Item Weight', '8 ounces', 'Package Dimensions', '8.2 x 4.5 x 1.6 inches', 'UPC', '605749060195', 'Material Type', 'Jersey', 'Style', 'Bassinet Fitted Sheet', 'Batteries required', 'No', 'Additional Information', 'ASIN', 'B07K8FMDFS', 'Customer Reviews', '4.6 out of 5 stars 85 customer reviews', 'Amazon Best Sellers Rank', '#1,090 in Baby (See Top 100 in Baby)', '.zg_hrsr { margin: 0; padding: 0; list-style-type: none; } .zg_hrsr_item { margin: 0 0 0 10px; } .zg_hrsr_rank { display: inline-block; width: 80px; text-align: right; }', '#1 in\xa0Bassinet Sheets', 'Shipping Weight', '8 ounces (View shipping rates and policies)', 'Feedback', 'P.now("A","tellMeMoreLinkData").execute(function(A,tellMeMoreLinkData){ if(typeof tellMeMoreLinkData !== \'undefined\'){ A.state(\'lowerPricePopoverData\',{"trigger":"ns_A0KX4P1X0ZHGC1EYTS2A_35502_1_hmd_pricing_feedback_trigger_product-details","destination":"/gp/pdp/pf/pricingFeedbackForm.html/ref=zg_bsnr_baby-products_13?ie=UTF8&ASIN=B07K8FMDFS&PREFIX=ns_A0KX4P1X0ZHGC1EYTS2A_35502_2_&WDG=baby_product_display_on_website&dpRequestId=A0KX4P1X0ZHGC1EYTS2A&from=product-details&psc=1&refRID=YX5GGHQ1X7YJMVVW6D93&storeID=baby-productsencodeURI(\'&originalURI=\' + window.location.pathname)","url":"/gp/pdp/pf/pricingFeedbackForm.html/ref=zg_bsnr_baby-products_13?ie=UTF8&ASIN=B07K8FMDFS&PREFIX=ns_A0KX4P1X0ZHGC1EYTS2A_35502_2_&WDG=baby_product_display_on_website&dpRequestId=A0KX4P1X0ZHGC1EYTS2A&from=product-details&psc=1&refRID=YX5GGHQ1X7YJMVVW6D93&storeID=baby-products","nsPrefix":"ns_A0KX4P1X0ZHGC1EYTS2A_35502_2_","path":"encodeURI(\'&originalURI=\' + window.location.pathname)","title":"Tell Us About a Lower Price"}); return { key:"pricing-fbW", method: function(){ return {"trigger":"ns_A0KX4P1X0ZHGC1EYTS2A_35502_1_hmd_pricing_feedback_trigger_product-details","destination":"/gp/pdp/pf/pricingFeedbackForm.html/ref=zg_bsnr_baby-products_13?ie=UTF8&ASIN=B07K8FMDFS&PREFIX=ns_A0KX4P1X0ZHGC1EYTS2A_35502_2_&WDG=baby_product_display_on_website&dpRequestId=A0KX4P1X0ZHGC1EYTS2A&from=product-details&psc=1&refRID=YX5GGHQ1X7YJMVVW6D93&storeID=baby-productsencodeURI(\'&originalURI=\' + window.location.pathname)","url":"/gp/pdp/pf/pricingFeedbackForm.html/ref=zg_bsnr_baby-products_13?ie=UTF8&ASIN=B07K8FMDFS&PREFIX=ns_A0KX4P1X0ZHGC1EYTS2A_35502_2_&WDG=baby_product_display_on_website&dpRequestId=A0KX4P1X0ZHGC1EYTS2A&from=product-details&psc=1&refRID=YX5GGHQ1X7YJMVVW6D93&storeID=baby-products","nsPrefix":"ns_A0KX4P1X0ZHGC1EYTS2A_35502_2_","path":"encodeURI(\'&originalURI=\' + window.location.pathname)","title":"Tell Us About a Lower Price"}; } } } else{ P.when("A").register("tellMeMoreLinkData",function(A){ A.state(\'lowerPricePopoverData\',{"trigger":"ns_A0KX4P1X0ZHGC1EYTS2A_35502_1_hmd_pricing_feedback_trigger_product-details","destination":"/gp/pdp/pf/pricingFeedbackForm.html/ref=zg_bsnr_baby-products_13?ie=UTF8&ASIN=B07K8FMDFS&PREFIX=ns_A0KX4P1X0ZHGC1EYTS2A_35502_2_&WDG=baby_product_display_on_website&dpRequestId=A0KX4P1X0ZHGC1EYTS2A&from=product-details&psc=1&refRID=YX5GGHQ1X7YJMVVW6D93&storeID=baby-productsencodeURI(\'&originalURI=\' + window.location.pathname)","url":"/gp/pdp/pf/pricingFeedbackForm.html/ref=zg_bsnr_baby-products_13?ie=UTF8&ASIN=B07K8FMDFS&PREFIX=ns_A0KX4P1X0ZHGC1EYTS2A_35502_2_&WDG=baby_product_display_on_website&dpRequestId=A0KX4P1X0ZHGC1EYTS2A&from=product-details&psc=1&refRID=YX5GGHQ1X7YJMVVW6D93&storeID=baby-products","nsPrefix":"ns_A0KX4P1X0ZHGC1EYTS2A_35502_2_","path":"encodeURI(\'&originalURI=\' + window.location.pathname)","title":"Tell Us About a Lower Price"}); return { key:"pricing-fbW", method: function(){ return {"trigger":"ns_A0KX4P1X0ZHGC1EYTS2A_35502_1_hmd_pricing_feedback_trigger_product-details","destination":"/gp/pdp/pf/pricingFeedbackForm.html/ref=zg_bsnr_baby-products_13?ie=UTF8&ASIN=B07K8FMDFS&PREFIX=ns_A0KX4P1X0ZHGC1EYTS2A_35502_2_&WDG=baby_product_display_on_website&dpRequestId=A0KX4P1X0ZHGC1EYTS2A&from=product-details&psc=1&refRID=YX5GGHQ1X7YJMVVW6D93&storeID=baby-productsencodeURI(\'&originalURI=\' + window.location.pathname)","url":"/gp/pdp/pf/pricingFeedbackForm.html/ref=zg_bsnr_baby-products_13?ie=UTF8&ASIN=B07K8FMDFS&PREFIX=ns_A0KX4P1X0ZHGC1EYTS2A_35502_2_&WDG=baby_product_display_on_website&dpRequestId=A0KX4P1X0ZHGC1EYTS2A&from=product-details&psc=1&refRID=YX5GGHQ1X7YJMVVW6D93&storeID=baby-products","nsPrefix":"ns_A0KX4P1X0ZHGC1EYTS2A_35502_2_","path":"encodeURI(\'&originalURI=\' + window.location.pathname)","title":"Tell Us About a Lower Price"}; } } }); } }); Would you like to tell us about a lower price?']

a22 = ['Package Dimensions', '12.3 x 12 x 1.9 inches', 'Item Weight', '8 ounces', 'Shipping Weight', '8 ounces (View shipping rates and policies)', 'Manufacturer', 'Hethrone', 'ASIN', 'B07TBBS4C1', 'Customer Reviews', '/* * Fix for UDP-1061. Average customer reviews has a small extra line on hover * https://omni-grok.amazon.com/xref/src/appgroup/websiteTemplates/retail/SoftlinesDetailPageAssets/udp-intl-lock/src/legacy.css?indexName=WebsiteTemplates#40 */ .noUnderline a:hover { text-decoration: none; }', '4.5 out of 5 stars 44 customer reviews P.when(\'A\', \'ready\').execute(function(A) { A.declarative(\'acrLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrLinkClickCount", (ue.count("acrLinkClickCount") || 0) + 1); } }); }); P.when(\'A\', \'cf\').execute(function(A) { A.declarative(\'acrStarsLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrStarsLinkWithPopoverClickCount", (ue.count("acrStarsLinkWithPopoverClickCount") || 0) + 1); } }); });', '', '4.5 out of 5 stars']

a23 = ['Technical Details', 'Item Weight', '9.6 ounces', 'Package Dimensions', '9.8 x 9.6 x 1.4 inches', 'UPC', '761272116980', 'Material Type', 'Memory Foam, Cotton', 'Material free', 'BPA Free', 'Care instructions', 'Do not Wash, Replace A New One Every 3 Months', 'Batteries required', 'No', 'Additional Information', 'ASIN', 'B07RW3XMSK', 'Customer Reviews', '5.0 out of 5 stars 15 customer reviews', 'Amazon Best Sellers Rank', '#1,150 in Baby (See Top 100 in Baby)', '.zg_hrsr { margin: 0; padding: 0; list-style-type: none; } .zg_hrsr_item { margin: 0 0 0 10px; } .zg_hrsr_rank { display: inline-block; width: 80px; text-align: right; }', '#6 in\xa0Nursery Pillows', '#63 in\xa0Nursery Bedding', 'Shipping Weight', '9.6 ounces (View shipping rates and policies)', 'Feedback', 'P.now("A","tellMeMoreLinkData").execute(function(A,tellMeMoreLinkData){ if(typeof tellMeMoreLinkData !== \'undefined\'){ A.state(\'lowerPricePopoverData\',{"trigger":"ns_6H0J4M8BKF6RQTH1SETY_38162_1_hmd_pricing_feedback_trigger_product-details","destination":"/gp/pdp/pf/pricingFeedbackForm.html/ref=?ie=UTF8&%2AVersion%2A=1&%2Aentries%2A=0&ASIN=B07RW3XMSK&PREFIX=ns_6H0J4M8BKF6RQTH1SETY_38162_2_&WDG=baby_product_display_on_website&dpRequestId=6H0J4M8BKF6RQTH1SETY&from=product-details&storeID=baby-productsencodeURI(\'&originalURI=\' + window.location.pathname)","url":"/gp/pdp/pf/pricingFeedbackForm.html/ref=?ie=UTF8&%2AVersion%2A=1&%2Aentries%2A=0&ASIN=B07RW3XMSK&PREFIX=ns_6H0J4M8BKF6RQTH1SETY_38162_2_&WDG=baby_product_display_on_website&dpRequestId=6H0J4M8BKF6RQTH1SETY&from=product-details&storeID=baby-products","nsPrefix":"ns_6H0J4M8BKF6RQTH1SETY_38162_2_","path":"encodeURI(\'&originalURI=\' + window.location.pathname)","title":"Tell Us About a Lower Price"}); return { key:"pricing-fbW", method: function(){ return {"trigger":"ns_6H0J4M8BKF6RQTH1SETY_38162_1_hmd_pricing_feedback_trigger_product-details","destination":"/gp/pdp/pf/pricingFeedbackForm.html/ref=?ie=UTF8&%2AVersion%2A=1&%2Aentries%2A=0&ASIN=B07RW3XMSK&PREFIX=ns_6H0J4M8BKF6RQTH1SETY_38162_2_&WDG=baby_product_display_on_website&dpRequestId=6H0J4M8BKF6RQTH1SETY&from=product-details&storeID=baby-productsencodeURI(\'&originalURI=\' + window.location.pathname)","url":"/gp/pdp/pf/pricingFeedbackForm.html/ref=?ie=UTF8&%2AVersion%2A=1&%2Aentries%2A=0&ASIN=B07RW3XMSK&PREFIX=ns_6H0J4M8BKF6RQTH1SETY_38162_2_&WDG=baby_product_display_on_website&dpRequestId=6H0J4M8BKF6RQTH1SETY&from=product-details&storeID=baby-products","nsPrefix":"ns_6H0J4M8BKF6RQTH1SETY_38162_2_","path":"encodeURI(\'&originalURI=\' + window.location.pathname)","title":"Tell Us About a Lower Price"}; } } } else{ P.when("A").register("tellMeMoreLinkData",function(A){ A.state(\'lowerPricePopoverData\',{"trigger":"ns_6H0J4M8BKF6RQTH1SETY_38162_1_hmd_pricing_feedback_trigger_product-details","destination":"/gp/pdp/pf/pricingFeedbackForm.html/ref=?ie=UTF8&%2AVersion%2A=1&%2Aentries%2A=0&ASIN=B07RW3XMSK&PREFIX=ns_6H0J4M8BKF6RQTH1SETY_38162_2_&WDG=baby_product_display_on_website&dpRequestId=6H0J4M8BKF6RQTH1SETY&from=product-details&storeID=baby-productsencodeURI(\'&originalURI=\' + window.location.pathname)","url":"/gp/pdp/pf/pricingFeedbackForm.html/ref=?ie=UTF8&%2AVersion%2A=1&%2Aentries%2A=0&ASIN=B07RW3XMSK&PREFIX=ns_6H0J4M8BKF6RQTH1SETY_38162_2_&WDG=baby_product_display_on_website&dpRequestId=6H0J4M8BKF6RQTH1SETY&from=product-details&storeID=baby-products","nsPrefix":"ns_6H0J4M8BKF6RQTH1SETY_38162_2_","path":"encodeURI(\'&originalURI=\' + window.location.pathname)","title":"Tell Us About a Lower Price"}); return { key:"pricing-fbW", method: function(){ return {"trigger":"ns_6H0J4M8BKF6RQTH1SETY_38162_1_hmd_pricing_feedback_trigger_product-details","destination":"/gp/pdp/pf/pricingFeedbackForm.html/ref=?ie=UTF8&%2AVersion%2A=1&%2Aentries%2A=0&ASIN=B07RW3XMSK&PREFIX=ns_6H0J4M8BKF6RQTH1SETY_38162_2_&WDG=baby_product_display_on_website&dpRequestId=6H0J4M8BKF6RQTH1SETY&from=product-details&storeID=baby-productsencodeURI(\'&originalURI=\' + window.location.pathname)","url":"/gp/pdp/pf/pricingFeedbackForm.html/ref=?ie=UTF8&%2AVersion%2A=1&%2Aentries%2A=0&ASIN=B07RW3XMSK&PREFIX=ns_6H0J4M8BKF6RQTH1SETY_38162_2_&WDG=baby_product_display_on_website&dpRequestId=6H0J4M8BKF6RQTH1SETY&from=product-details&storeID=baby-products","nsPrefix":"ns_6H0J4M8BKF6RQTH1SETY_38162_2_","path":"encodeURI(\'&originalURI=\' + window.location.pathname)","title":"Tell Us About a Lower Price"}; } } }); } }); Would you like to tell us about a lower price?']

a24 = ['Product Dimensions', '17.8 x 1.5 x 1.3 inches', 'Item Weight', '10.2 ounces', 'Shipping Weight', '10.4 ounces (View shipping rates and policies)', 'Manufacturer', 'Mikomer', 'ASIN', 'B076HNPWBH', 'Customer Reviews', '/* * Fix for UDP-1061. Average customer reviews has a small extra line on hover * https://omni-grok.amazon.com/xref/src/appgroup/websiteTemplates/retail/SoftlinesDetailPageAssets/udp-intl-lock/src/legacy.css?indexName=WebsiteTemplates#40 */ .noUnderline a:hover { text-decoration: none; }', '4.6 out of 5 stars 313 customer reviews P.when(\'A\', \'ready\').execute(function(A) { A.declarative(\'acrLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrLinkClickCount", (ue.count("acrLinkClickCount") || 0) + 1); } }); }); P.when(\'A\', \'cf\').execute(function(A) { A.declarative(\'acrStarsLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrStarsLinkWithPopoverClickCount", (ue.count("acrStarsLinkWithPopoverClickCount") || 0) + 1); } }); });', '', '4.6 out of 5 stars', 'Best Sellers Rank', '#8,847 in Home & Kitchen (See Top 100 in Home & Kitchen)', '#19 in Window Films']

a25 = ['Product Dimensions', '4.1 x 4.1 x 20.8 inches', 'Item Weight', '2.65 pounds', 'Shipping Weight', '2.65 pounds (View shipping rates and policies)', 'Domestic Shipping', 'Item can be shipped within U.S.', 'International Shipping', 'This item can be shipped to select countries outside of the U.S. Learn More', 'ASIN', 'B00IVZCLHQ', 'Item model number', '74968', 'Manufacturer recommended age', '36 months - 7 years', 'Best Sellers Rank', '#2,016 in Toys & Games (See Top 100 in Toys & Games)', "#1 in Kids' Folding Chairs", '', 'Customer Reviews', '/* * Fix for UDP-1061. Average customer reviews has a small extra line on hover * https://omni-grok.amazon.com/xref/src/appgroup/websiteTemplates/retail/SoftlinesDetailPageAssets/udp-intl-lock/src/legacy.css?indexName=WebsiteTemplates#40 */ .noUnderline a:hover { text-decoration: none; }', '4.0 out of 5 stars 115 customer reviews P.when(\'A\', \'ready\').execute(function(A) { A.declarative(\'acrLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrLinkClickCount", (ue.count("acrLinkClickCount") || 0) + 1); } }); }); P.when(\'A\', \'cf\').execute(function(A) { A.declarative(\'acrStarsLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrStarsLinkWithPopoverClickCount", (ue.count("acrStarsLinkWithPopoverClickCount") || 0) + 1); } }); });', '', '4.0 out of 5 stars']

a26 = ['Package Dimensions', '11.2 x 9.1 x 3 inches', 'Item Weight', '2.02 pounds', 'Shipping Weight', '2.02 pounds (View shipping rates and policies)', 'Manufacturer', 'Franco Manufacturing Company Inc', 'ASIN', 'B07PNYQDP3', 'Item model number', 'NA1048', 'Customer Reviews', '/* * Fix for UDP-1061. Average customer reviews has a small extra line on hover * https://omni-grok.amazon.com/xref/src/appgroup/websiteTemplates/retail/SoftlinesDetailPageAssets/udp-intl-lock/src/legacy.css?indexName=WebsiteTemplates#40 */ .noUnderline a:hover { text-decoration: none; }', '4.5 out of 5 stars 23 customer reviews P.when(\'A\', \'ready\').execute(function(A) { A.declarative(\'acrLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrLinkClickCount", (ue.count("acrLinkClickCount") || 0) + 1); } }); }); P.when(\'A\', \'cf\').execute(function(A) { A.declarative(\'acrStarsLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrStarsLinkWithPopoverClickCount", (ue.count("acrStarsLinkWithPopoverClickCount") || 0) + 1); } }); });', '', '4.5 out of 5 stars', 'Best Sellers Rank', '#8,983 in Home & Kitchen (See Top 100 in Home & Kitchen)', "#6 in Kids' Sheet & Pillowcase Sets"]

a27 = ['Package Dimensions', '14.5 x 12 x 5 inches', 'Item Weight', '2.49 pounds', 'Shipping Weight', '2.51 pounds (View shipping rates and policies)', 'Manufacturer', 'Youhao', 'ASIN', 'B07D7MYQHQ', 'Item model number', 'STR015070016', 'Customer Reviews', '/* * Fix for UDP-1061. Average customer reviews has a small extra line on hover * https://omni-grok.amazon.com/xref/src/appgroup/websiteTemplates/retail/SoftlinesDetailPageAssets/udp-intl-lock/src/legacy.css?indexName=WebsiteTemplates#40 */ .noUnderline a:hover { text-decoration: none; }', '4.3 out of 5 stars 133 customer reviews P.when(\'A\', \'ready\').execute(function(A) { A.declarative(\'acrLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrLinkClickCount", (ue.count("acrLinkClickCount") || 0) + 1); } }); }); P.when(\'A\', \'cf\').execute(function(A) { A.declarative(\'acrStarsLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrStarsLinkWithPopoverClickCount", (ue.count("acrStarsLinkWithPopoverClickCount") || 0) + 1); } }); });', '', '4.3 out of 5 stars', 'Best Sellers Rank', '#9,258 in Home & Kitchen (See Top 100 in Home & Kitchen)', "#9 in Kids' Blankets & Throws", '#35 in Bed Throws']

a28 = ['Product Dimensions', '50 x 24 x 0.2 inches', 'Item Weight', '13.6 ounces', 'Shipping Weight', '13.6 ounces (View shipping rates and policies)', 'Manufacturer', 'Franco Manufacturing Company Inc', 'ASIN', 'B07QHXLD4J', 'Item model number', 'HH4598', 'Customer Reviews', '/* * Fix for UDP-1061. Average customer reviews has a small extra line on hover * https://omni-grok.amazon.com/xref/src/appgroup/websiteTemplates/retail/SoftlinesDetailPageAssets/udp-intl-lock/src/legacy.css?indexName=WebsiteTemplates#40 */ .noUnderline a:hover { text-decoration: none; }', '4.0 out of 5 stars 6 customer reviews P.when(\'A\', \'ready\').execute(function(A) { A.declarative(\'acrLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrLinkClickCount", (ue.count("acrLinkClickCount") || 0) + 1); } }); }); P.when(\'A\', \'cf\').execute(function(A) { A.declarative(\'acrStarsLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrStarsLinkWithPopoverClickCount", (ue.count("acrStarsLinkWithPopoverClickCount") || 0) + 1); } }); });', '', '4.0 out of 5 stars', 'Best Sellers Rank', '#9,355 in Home & Kitchen (See Top 100 in Home & Kitchen)', "#5 in Kids' Bath Towels"]

a29 = ['Shipping Information', 'View shipping rates and policies', 'Manufacturer', 'LAGHCAT', 'ASIN', 'B07QTJF4HK', 'Customer Reviews', '/* * Fix for UDP-1061. Average customer reviews has a small extra line on hover * https://omni-grok.amazon.com/xref/src/appgroup/websiteTemplates/retail/SoftlinesDetailPageAssets/udp-intl-lock/src/legacy.css?indexName=WebsiteTemplates#40 */ .noUnderline a:hover { text-decoration: none; }', '3.9 out of 5 stars 41 customer reviews P.when(\'A\', \'ready\').execute(function(A) { A.declarative(\'acrLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrLinkClickCount", (ue.count("acrLinkClickCount") || 0) + 1); } }); }); P.when(\'A\', \'cf\').execute(function(A) { A.declarative(\'acrStarsLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrStarsLinkWithPopoverClickCount", (ue.count("acrStarsLinkWithPopoverClickCount") || 0) + 1); } }); });', '', '3.9 out of 5 stars', 'Best Sellers Rank', '#9,381 in Home & Kitchen (See Top 100 in Home & Kitchen)', "#2 in Kids' Throw Blankets"]

a30 = ['']

a31 = ['Product Dimensions: 26 x 22 x 19 inches ; 21.5 pounds', 'Shipping Weight: 29.6 pounds (View shipping rates and policies)', 'ASIN: B07HJR368C', 'Item model number: M42400T1', 'Average Customer Review: 4.6 out of 5 stars 19 customer reviews', 'Amazon Best Sellers Rank: #685 in Industrial & Scientific (See Top 100 in Industrial & Scientific)', '.zg_hrsr { margin: 0; padding: 0; list-style-type: none; } .zg_hrsr_item { margin: 0 0 0 10px; } .zg_hrsr_rank { display: inline-block; width: 80px; text-align: right; }', "#2 in\xa0Kids' Table & Chair Sets", 'Manufacturer’s warranty can be requested from customer service. Click here to make a request to customer service.', 'P.now("A","tellMeMoreLinkData").execute(function(A,tellMeMoreLinkData){ if(typeof tellMeMoreLinkData !== \'undefined\'){ A.state(\'lowerPricePopoverData\',{"trigger":"ns_93NHAG7QNJCNRVE09XKV_47251_1_hmd_pricing_feedback_trigger_product-detail","destination":"/gp/pdp/pf/pricingFeedbackForm.html/ref=zg_bsnr_3206325011_32_pfdpb?ie=UTF8&ASIN=B07HJR368C&PREFIX=ns_93NHAG7QNJCNRVE09XKV_47251_2_&WDG=biss_basic_display_on_website&dpRequestId=93NHAG7QNJCNRVE09XKV&from=product-detail&psc=1&refRID=XV98N7JZZMN0PCZ2EFAJ&storeID=industrialencodeURI(\'&originalURI=\' + window.location.pathname)","url":"/gp/pdp/pf/pricingFeedbackForm.html/ref=zg_bsnr_3206325011_32_pfdpb?ie=UTF8&ASIN=B07HJR368C&PREFIX=ns_93NHAG7QNJCNRVE09XKV_47251_2_&WDG=biss_basic_display_on_website&dpRequestId=93NHAG7QNJCNRVE09XKV&from=product-detail&psc=1&refRID=XV98N7JZZMN0PCZ2EFAJ&storeID=industrial","nsPrefix":"ns_93NHAG7QNJCNRVE09XKV_47251_2_","path":"encodeURI(\'&originalURI=\' + window.location.pathname)","title":"Tell Us About a Lower Price"}); return { key:"pricing-fbW", method: function(){ return {"trigger":"ns_93NHAG7QNJCNRVE09XKV_47251_1_hmd_pricing_feedback_trigger_product-detail","destination":"/gp/pdp/pf/pricingFeedbackForm.html/ref=zg_bsnr_3206325011_32_pfdpb?ie=UTF8&ASIN=B07HJR368C&PREFIX=ns_93NHAG7QNJCNRVE09XKV_47251_2_&WDG=biss_basic_display_on_website&dpRequestId=93NHAG7QNJCNRVE09XKV&from=product-detail&psc=1&refRID=XV98N7JZZMN0PCZ2EFAJ&storeID=industrialencodeURI(\'&originalURI=\' + window.location.pathname)","url":"/gp/pdp/pf/pricingFeedbackForm.html/ref=zg_bsnr_3206325011_32_pfdpb?ie=UTF8&ASIN=B07HJR368C&PREFIX=ns_93NHAG7QNJCNRVE09XKV_47251_2_&WDG=biss_basic_display_on_website&dpRequestId=93NHAG7QNJCNRVE09XKV&from=product-detail&psc=1&refRID=XV98N7JZZMN0PCZ2EFAJ&storeID=industrial","nsPrefix":"ns_93NHAG7QNJCNRVE09XKV_47251_2_","path":"encodeURI(\'&originalURI=\' + window.location.pathname)","title":"Tell Us About a Lower Price"}; } } } else{ P.when("A").register("tellMeMoreLinkData",function(A){ A.state(\'lowerPricePopoverData\',{"trigger":"ns_93NHAG7QNJCNRVE09XKV_47251_1_hmd_pricing_feedback_trigger_product-detail","destination":"/gp/pdp/pf/pricingFeedbackForm.html/ref=zg_bsnr_3206325011_32_pfdpb?ie=UTF8&ASIN=B07HJR368C&PREFIX=ns_93NHAG7QNJCNRVE09XKV_47251_2_&WDG=biss_basic_display_on_website&dpRequestId=93NHAG7QNJCNRVE09XKV&from=product-detail&psc=1&refRID=XV98N7JZZMN0PCZ2EFAJ&storeID=industrialencodeURI(\'&originalURI=\' + window.location.pathname)","url":"/gp/pdp/pf/pricingFeedbackForm.html/ref=zg_bsnr_3206325011_32_pfdpb?ie=UTF8&ASIN=B07HJR368C&PREFIX=ns_93NHAG7QNJCNRVE09XKV_47251_2_&WDG=biss_basic_display_on_website&dpRequestId=93NHAG7QNJCNRVE09XKV&from=product-detail&psc=1&refRID=XV98N7JZZMN0PCZ2EFAJ&storeID=industrial","nsPrefix":"ns_93NHAG7QNJCNRVE09XKV_47251_2_","path":"encodeURI(\'&originalURI=\' + window.location.pathname)","title":"Tell Us About a Lower Price"}); return { key:"pricing-fbW", method: function(){ return {"trigger":"ns_93NHAG7QNJCNRVE09XKV_47251_1_hmd_pricing_feedback_trigger_product-detail","destination":"/gp/pdp/pf/pricingFeedbackForm.html/ref=zg_bsnr_3206325011_32_pfdpb?ie=UTF8&ASIN=B07HJR368C&PREFIX=ns_93NHAG7QNJCNRVE09XKV_47251_2_&WDG=biss_basic_display_on_website&dpRequestId=93NHAG7QNJCNRVE09XKV&from=product-detail&psc=1&refRID=XV98N7JZZMN0PCZ2EFAJ&storeID=industrialencodeURI(\'&originalURI=\' + window.location.pathname)","url":"/gp/pdp/pf/pricingFeedbackForm.html/ref=zg_bsnr_3206325011_32_pfdpb?ie=UTF8&ASIN=B07HJR368C&PREFIX=ns_93NHAG7QNJCNRVE09XKV_47251_2_&WDG=biss_basic_display_on_website&dpRequestId=93NHAG7QNJCNRVE09XKV&from=product-detail&psc=1&refRID=XV98N7JZZMN0PCZ2EFAJ&storeID=industrial","nsPrefix":"ns_93NHAG7QNJCNRVE09XKV_47251_2_","path":"encodeURI(\'&originalURI=\' + window.location.pathname)","title":"Tell Us About a Lower Price"}; } } }); } }); Would you like to tell us about a lower price?']

a32 = ['Product Dimensions', '17 x 2 x 2 inches', 'Item Weight', '8.8 ounces', 'Shipping Weight', '8.8 ounces (View shipping rates and policies)', 'Manufacturer', 'Artviva', 'ASIN', 'B07CG2YCPC', 'Customer Reviews', '/* * Fix for UDP-1061. Average customer reviews has a small extra line on hover * https://omni-grok.amazon.com/xref/src/appgroup/websiteTemplates/retail/SoftlinesDetailPageAssets/udp-intl-lock/src/legacy.css?indexName=WebsiteTemplates#40 */ .noUnderline a:hover { text-decoration: none; }', '4.2 out of 5 stars 46 customer reviews P.when(\'A\', \'ready\').execute(function(A) { A.declarative(\'acrLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrLinkClickCount", (ue.count("acrLinkClickCount") || 0) + 1); } }); }); P.when(\'A\', \'cf\').execute(function(A) { A.declarative(\'acrStarsLink-click-metrics\', \'click\', { "allowLinkDefault" : true }, function(event){ if(window.ue) { ue.count("acrStarsLinkWithPopoverClickCount", (ue.count("acrStarsLinkWithPopoverClickCount") || 0) + 1); } }); });', '', '4.2 out of 5 stars', 'Best Sellers Rank', '#10,528 in Home & Kitchen (See Top 100 in Home & Kitchen)', '#22 in Window Films']

a33 = ['Product Dimensions', '2.5 x 2.5 x 3.8 inches', 'Item Weight', '3.52 ounces', 'Shipping Weight', '4.2 ounces (View shipping rates and policies)', 'ASIN', 'B07N5XG38L', 'Item model number', '38484', 'Manufacturer recommended age', '6 - 8 years', 'Best Sellers Rank', '#2,536 in Toys & Games (See Top 100 in Toys & Games)', "#357 in Kids' Home Store", '', 'Customer Reviews', '/* * Fix for UDP-1061. Average customer reviews has a small extra line on hover * https://omni-grok.amazon.com/xref/src/appgroup/websiteTemplates/retail/SoftlinesDetailPageAssets/udp-intl-lock/src/legacy.css?indexName=WebsiteTemplates#40 */ .noUnderline a:hover { text-decoration: none; }', 'Be the first to review this item', '', '0.0 out of 5 stars']

a34 = ['Size', '2 Pack', 'Number Of Pieces', '5']
#
# for i in a33:
#     print(len(i))


# s = 'Product Dimensions: 2.4 x 4.2 x 10.4 inches ; 1.4 pounds'
# print(len(s))
# print(s[20:])

#
# s = {'name': 'O-Cedar EasyWring Microfiber Spin Mop, Bucket Floor Cleaning System', 'price': '$29.98', 'ASIN': 'B00WSWGVZQ', 'BestSellersRank1': '#102 in Home & Kitchen ', 'BestSellersRank2': '1 in Household Floor Cleaners', 'ItemWeight': '5.2 pounds', 'Manufacturer': 'O-Cedar', 'PackageDimensions': '19.5 x 11.7 x 11.5 inches', 'commit': '7,022', 'icon': '4.3 ', 'name_url': 'https://www.amazon.com/Cedar-EasyWring-Microfiber-Bucket-Cleaning/dp/B00WSWGVZQ/ref=zg_bsnr_10802561_1?_encoding=UTF8&psc=1&refRID=S7RYJQE4EAXQFPF0ZDE7', 'upd': 'New (3) from $29.98 & FREE shipping'}
# print(s['name'])


# l = ['Amazon Bestsellers Rank:', '.zg_hrsr { margin: 0; padding: 0; list-style-type: none; } .zg_hrsr_item { margin: 0 0 0 10px; } .zg_hrsr_rank { display: inline-block; width: 80px; text-align: right; }', '#6 in\xa0Wireless Headphones', '#5 in\xa0Mobile Phone Bluetooth Headsets']
#
# print(l[2:])

l = "'PackageDimensions': '2 x 1 x 1 cm ; 118 g'"
print(l[20:])