from time import sleep
from selenium import webdriver

chrome = webdriver.Chrome()

chrome.get("https://www.bilibili.com/")

chrome.find_element_by_class_name("search-keyword").send_keys("鬼灭之刃")
sleep(5)
chrome.close()
