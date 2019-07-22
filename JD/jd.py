# -*- coding: utf-8 -*-



# import os
#
#
# def save(html, path):
#     '''
#     以文件形式保存数据
#     :param html: 要保存的数据
#     :param path: 要保存数据的路径
#     :return:
#     '''
#     # 判断目录是否存在
#     if not os.path.exists(os.path.split(path)[0]):
#         # 目录不存在创建，makedirs可以创建多级目录
#         os.makedirs(os.path.split(path)[0])
#     try:
#         # 保存数据到文件
#         with open(path, 'wb') as f:
#             f.write(html.encode('utf8'))
#         print('保存成功')
#     except Exception as e:
#         print('保存失败', e)
#
#
# if __name__ == "__main__":
#     html = '数据'  # 要保存的数据
#     path = 'F:/a/b/1.txt'  # 设置路径，也可设为相对路径
#     save(html, path)
#

  # page = response.url.split("/")[-1]
        # page = urllib.parse.unquote(page)
        # path = 'F:/goods/'
        # # 判断目录是否存在
        # if not os.path.exists(os.path.split(path)[0]):
        #     # 目录不存在创建，makedirs可以创建多级目录
        #     os.makedirs(os.path.split(path)[0])
        #
        # # for name in self.names:
        # #     filename = name + '.html'
        #     path = 'F:/goods/'
        #     path = path + page
        #     with open(path, 'wb') as f:
        #         # import pdb
        #         # pdb.set_trace()
        #         f.write(response.body)
        #     # self.log('保存文件: %s' % filename)
        #     f.close()

#
# b = 'https://ccc-x.jd.com/dsp/nc?ex'
# print(b[0:5] + '1')
# c = '//ccc-x.jd.com/dsp/nc?ex'
# print(c[0:5])
# f = b.replace('//', ',')
# f1 = c.replace('//', ',')
# print(f[0])
# print(f1[0])
#
# a = 'https:https://ccc-x.jd.com/dsp/nc?ex'

#
#
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# print(browser.page_source)#browser.page_source是获取网页的全部html
# browser.close()

#
# for i in range(1,100):
#     print("第{}页".format(i))





# https://search-x.jd.com/Search?&keyword=%E6%89%8B%E6%9C%BA&page=3&ad_ids=292%3A5
# https://search-x.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&page=2&ad_ids=291%3A33

#
# https://search-x.jd.com/Search?callback=jQuery6043004&area=12&enc=utf-8&keyword=%E6%89%8B%E6%9C%BA&adType=7&urlcid3=655&page=1&ad_ids=291%3A33
# https://search-x.jd.com/Search?callback=jQuery2410430&area=12&enc=utf-8&keyword=%E6%89%8B%E6%9C%BA&adType=7&urlcid3=655&page=1&ad_ids=292%3A5
#
# 2
# https://search-x.jd.com/Search?callback=jQuery1481131&area=12&enc=utf-8&keyword=%E6%89%8B%E6%9C%BA&adType=7&urlcid3=655&page=2&ad_ids=291%3A33
# https://search-x.jd.com/Search?callback=jQuery8970835&area=12&enc=utf-8&keyword=%E6%89%8B%E6%9C%BA&adType=7&urlcid3=655&page=2&ad_ids=292%3A5
#
# 3
# https://search-x.jd.com/Search?callback=jQuery3721191&area=12&enc=utf-8&keyword=%E6%89%8B%E6%9C%BA&adType=7&urlcid3=655&page=3&ad_ids=291%3A33
# https://search-x.jd.com/Search?&keyword=%E6%89%8B%E6%9C%BA&page=3&ad_ids=292%3A5