from bs4 import BeautifulSoup
import requests
from lxml import etree # for xpath selector
from fake_useragent import UserAgent
import pandas as pd
import numpy as np
from time import sleep
import datetime as dt

def stock(code):
    def stock_info(req):
        if req.status_code == 200:
            index_xpath = [1,2,3,4,5,7]
            value = []
            stock_name = ''
            long_short = ''
            soup = BeautifulSoup(req.content, 'lxml')
            soup_string = str(soup)
            selector = etree.HTML(soup_string)
            stock_name = selector.xpath('/html/body/div[1]/div/div/div/div/div[5]/div[1]/div[1]/div/div[1]/div/div[1]/h1')
            for i in index_xpath:
                value += selector.xpath('/html/body/div[1]/div/div/div/div/div[5]/div[1]/div[1]/div/div[3]/div/section[1]/div[2]/div[2]/div/ul/li[%d]/span[2]'%i)
            value = [float(value[idx].text) for idx, i in enumerate(value)]
            difference = round(value[0] - value[5], 2)
            daily_price = round(difference / value[5] * 100, 2)
            long_short = '漲' if value[0] >= value[5] else '跌'
            output = ('股名：%s\n最近：%s\n成交：%s\n開盤：%s\n最高：%s\n最低：%s\n均價：%s\n昨收：%s\n漲跌幅：%.2f%%\n漲跌：%.2f'
                        %(stock_name[0].text,long_short , value[0], value[1], value[2], value[3], value[4], value[5], daily_price, difference))
            return output
        else:
            return '(error)request not 200'


    url = ('https://tw.stock.yahoo.com/quote/%d'%code)
    ua = UserAgent()
    headers = {'User-Agent': ua.Firefox, 'Referer': url}
    req = requests.get(url, headers=headers)
    output = stock_info(req)
    return output
