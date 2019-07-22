import os

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from pyquery import PyQuery as pq
import pymongo
import time
import text

# mongodb配置
MONGO_URL = 'localhost'
MONGO_DB = 'JD'
MONGO_TABLE = 'product'
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
browser.set_window_size(1400,1400)




def search(name):
    print("正在搜索")
    try:
        browser.get('https://www.jd.com/')

        # 输入框
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#key"))
        )
        # 搜索按钮
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#search > div > div.form > button > i")))

        input.clear()  # 清空搜索框
        input.send_keys(name)
        # 按钮事件
        submit.click()

        # 滚动条滚动
        # js = "window.scrollTo(300,1000);"
        # browser.execute_script(js)
        # time.sleep(3)
        #
        # js = "window.scrollTo(300,2000);"
        # browser.execute_script(js)
        # time.sleep(3)
        #
        # js = "window.scrollTo(300,3000);"
        # browser.execute_script(js)
        # time.sleep(3)
        #
        # js = "window.scrollTo(300,4000);"
        # browser.execute_script(js)
        # time.sleep(3)
        #
        # js = "window.scrollTo(300,5000);"
        # browser.execute_script(js)
        # time.sleep(3)
        #
        # js = "window.scrollTo(300,6000);"
        # browser.execute_script(js)
        # time.sleep(3)
        #
        # js = "window.scrollTo(300,7000);"
        # browser.execute_script(js)
        # time.sleep(3)
        #
        js = "window.scrollTo(300,8000);"
        browser.execute_script(js)
        time.sleep(3)

        # 隐式等待
        # browser.implicitly_wait(10)

        # 判断页面是否加载完成
        total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#J_bottomPage > span.p-skip > em:nth-child(1)")))

        get_products()
        # next_page()
        # return total.text

    except TimeoutException:
        return search(name)


# 翻页
def next_page(page_number):
    print("正在翻页",page_number)
    try:
        # 输入页码框
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#J_bottomPage > span.p-skip > input"))
        )
        # 确定按钮
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#J_bottomPage > span.p-skip > a")))
        # 清除内容
        input.clear()
        # 输入页码
        input.send_keys(page_number)
        submit.click()
        # 滚动条滚动
        # browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

        # time.sleep(3)
        # 判断是否跳到下一页
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#J_bottomPage > span.p-num > a.curr"), str(page_number)))
        # 滚动条滚动
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

        get_products()
    except TimeoutException:
        # 如果失败则重新请求
        next_page(page_number)



# 获取商品列表页面信息
def get_products():
    # 最外层的div包括所有的商品
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_searchWrap .m-list .gl-item')))
    # 获取网页源代码
    # html = browser.page_source

    # 解析网页代码
    # 声明pq对象
    doc = pq(browser.page_source,parser="html")
    items = doc('#J_searchWrap .m-list .gl-item').items()

    for item in items:
        #商品价格
        price = item.find("div.p-price > strong > i").text()
        #商品总评价数量
        commit = item.find("div.p-commit > strong").text()
        #商品名称
        name = item.find("div.p-name.p-name-type-2 > a > em").text()
        #商家名称
        shop = item.find("div.p-shop > span > a").text()
        # 是否自营
        goods_icons = item.find(".goods-icons").text()
        #商家url
        shop_url = "https:" + str(item.find(".J_im_icon a").attr('href'))
        #商品url
        good_url = item.find(".p-name a").attr('href')
        if good_url[0:5] != 'https':
            good_url = "https:" + good_url

        product = {
            # 'price': price,
            # 'commit': commit,
            'name': name,
            # 'shop': shop,
            # 'goods_icons': goods_icons,
            'shop_url': shop_url,
            'good_url': good_url,
        }

        # save_to_mongo(product)
        print(product)

        get_goods(product)


# 获取商品详情页信息
def get_goods(slt):
    print("进入商品详情页")
    time.sleep(2)
    browser.get(slt['good_url'])
    #隐式等待
    browser.implicitly_wait(5)

    doc = pq(browser.page_source, parser="html")
    #图片url
    # img_url = "https:" + doc('#spec-img').attr('src')
    #商品的详细信息
    # titles = doc('ul.parameter2.p-parameter-list').text()
    #商品的主体信息
    # ptable = doc('.Ptable-item').text()

    #加入大字典中
    # slt['img_url'] = img_url
    # slt['titles'] = titles
    # slt['ptable'] = ptable

    get_shop(slt)


# 获取商家信息
def get_shop(curr):
    print("进入商家页")
    time.sleep(2)
    browser.get(curr['shop_url'])
    # save_to_mongo(curr)
    browser.back()
    browser.back()


    # 判断目录是否存在
    # path = 'F:/shops/'
    # if not os.path.exists(os.path.split(path)[0]):
    #     # 目录不存在创建，makedirs可以创建多级目录
    #     os.makedirs(os.path.split(path)[0])
    # path = curr['name'] + '.html'
    # try:
    #     with open(path, 'wb') as f:
    #         f.write(browser.page_source)
    #         print('保存成功')
    # except Exception as e:
    #     print('保存失败', e)


    # 滚动条滚动
    # js = "window.scrollTo(300,1000);"
    # browser.execute_script(js)
    # time.sleep(1)


#存储mongodb
def save_to_mongo(result):
    try:
        if db['name'].update({"name": result['name'], "price": result['price']}, {"$set": dict(result)}, upsert=True,multi=True):
        # if db[MONGO_TABLE].insert_one(result):
            print("存储到MONGODB成功",result)
            pass
    except Exception:
        print("存储失败",result)



def main():
    l = ['苹果','香蕉','桃子']
    for name in l:
        search(name)
        # 提取100
        for page in range(2,4):
            next_page(page)
    # 关闭浏览器
    browser.quit()
if __name__ =="__main__":
    main()