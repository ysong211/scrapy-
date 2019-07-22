
from scrapy.cmdline import execute


import sys
import os
# sys.path.append('F:\JD\jdgoods_spider')

print(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy","crawl","jdshop"])