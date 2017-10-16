# -*- coding: utf-8 -*-

import lxml.html
from selenium import webdriver
import time
import logging
import os

logging.basicConfig(format='%(asctime)s %(message)s')

def my_nintendo():
    try:
        driver = webdriver.PhantomJS()
        driver.get("https://store.nintendo.co.jp/customize.html")
        root = lxml.html.fromstring(driver.page_source)
        text = root.find_class("stock")[0].text

        if text != "SOLD OUT":
            os.system("osascript -e 'display notification \"Come switch on my nintendo!!\"'")
        driver.close()
    except:
        logging.error("my nintendo error")
        time.sleep(300)


    return

if __name__ == '__main__':
    while True:
        my_nintendo()
        time.sleep(60)
