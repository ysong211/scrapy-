#
# import requests
# from scrapy.selector import Selector
# import pymysql
#
# conn = pymysql.connect(host="127.0.0.1", user="root", passwd = "123456", charset="utf-8", db="article_spider")
# cursor = conn.cursor()
# #爬取西刺的免费ip代理
# def crawl_ips():
#
#     headers = {"User-Agent":"Mozilla/5.0 (X11; CrOS i686 4319.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36"}
#     for i in range(3547):
#         re = requests.get("https://www.xicidaili.com/nn/{0}".format(i), headers = headers)
#         selector = Selector(text=re.text)
#         all_trs = selector.css("#ip_list tr")
#
#         ip_list = []
#         for tr in all_trs[1:]:
#             speed_str = tr.css(".bar::attr(title)").extract()[0]
#             if speed_str:
#                 speed = float(speed_str.split("秒")[0])
#             all_texts = tr.css("td::text").extract()
#
#
#             ip = all_texts[0]
#             port = all_texts[1]
#             proxy_type = all_texts[5]
#             ip_list.append((ip, port, proxy_type, speed))
#
#         for ip_info in ip_list:
#             cursor.execute(
#                 "insert proxy_ip(ip, port, speed, proxy_type) VALUES('{0}', '{1}',{2},'HTTP')".format(
#                     ip_info[0], ip_info[1], ip_info[3]
#                 )
#             )
#             conn.commit()
#
#
# #从数据库中获取ip
# class GetIp(object):
#     #从数据库中删除无效的ip
#     def delete_ip(self, ip, port):
#         delete_spl = """
#             delete from proxy_ip where ip='{0}'
#         """.format(ip)
#         cursor.execute(delete_spl)
#         conn.commit()
#         return True
#
#     def judge_ip(self, ip, port):
#         #判断ip是否可用
#         http_url = "http://www.baidu.com"
#         proxy_url = "https://{0}:{1}".format(ip,port)
#         try:
#             proxy_dict = {
#                 "http":proxy_url,
#             }
#             response = requests.get(http_url,proxies=proxy_dict)
#             return True
#         except Exception as e:
#             self.delete_ip(ip)
#             return False
#         else:
#             code = response.status_code
#             if code <= 200 and code < 300:
#                 print("ip")
#                 return True
#             else:
#                 print("invalib ")
#                 self.delete_ip(ip)
#
#
#     def get_random_ip(self):
#         #随机取出ip
#         spl = """
#             SELECT ip,port FROM proxy_ip ORDER BY RAND() LIMIT 1
#         """
#
#         result = cursor.execute(spl)
#
#         for ip_info in cursor.fetchall():
#             ip = ip_info[0]
#             port = ip_info[1]
#
#             judge_re = self.judge_ip(ip,port)
#             if judge_re:
#                 return "http://{0}:{1}".format(ip,port)
#             else:
#                 return self.get_random_ip()
#
#
#
# # print(crawl_ips())
# if __name__=="__main__":
#     get_ip = GetIp()
#     get_ip.get_random_ip()