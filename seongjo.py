from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request
product_file_path = '/home/soohyeon/'
product_file_name = 'test.txt'


# def crawling(driver):
#     crawling_results=[]
#
#     crawling_results.append(driver.find_element_by_tag_name())


def make_request():

    product_file = open(product_file_path + product_file_name, 'r')
    food_id = list()
    food_city = list()
    food_category = list()
    food_small_category = list()
    food_name = list()
    food_call_num = list()
    food_date = list()
    food_location = list()
    food_picture_url = list()
    food_menu = list()

    for product_code in product_file.readlines():
        try:
            driver = webdriver.Chrome('/home/soohyeon/다운로드/chromedriver')

            url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=' + product_code

            driver.get(url)

            driver.implicitly_wait(1)
            # food_name.append(driver.find_element_by_css_selector("#place_main_ct > div > div > div.sc_box.default > div.ct_box_area > div.biz_name_area > a").text)
            test(driver,"#place_main_ct > div > div > div.sc_box.default > div.ct_box_area > div.biz_name_area > a",food_name)
            test(driver,"#place_main_ct > div > div > div.sc_box.default > div.ct_box_area > div.biz_name_area > span",food_small_category)
            test(driver,"#place_main_ct > div > div > div.sc_box.default > div.ct_box_area > div.bizinfo_area > div > div.list_item.list_item_biztel > div",food_call_num)
            test(driver,"#place_main_ct > div > div > div.sc_box.default > div.ct_box_area > div.bizinfo_area > div > div.list_item.list_item_biztime > div",food_date)
            test(driver,"#place_main_ct > div > div > div.sc_box.default > div.ct_box_area > div.bizinfo_area > div > div.list_item.list_item_menu > div",food_menu)
            location(driver,"#place_main_ct > div > div > div.sc_box.default > div.ct_box_area > div.bizinfo_area > div > div.list_item.list_item_address > div > ul > li:nth-child(1) > span"
                     ,"#place_main_ct > div > div > div.sc_box.default > div.ct_box_area > div.bizinfo_area > div > div.list_item.list_item_address > div > ul > li:nth-child(2) > span.addr",food_location)
            picture(driver,"#place_main_ct > div > div > div.sc_box.default > div.top_photo_area.type_v4 > div:nth-child(1) > a > img",food_picture_url)
            # print(driver.find_element_by_css_selector("#place_main_ct").text)

            # print(driver.find_element_by_css_selector("#place_main_ct > div > div > div.sc_box.default > div.ct_box_area > div.biz_name_area > a").text)

            # print(driver.find_element_by_css_selector("#place_main_ct > div > div > div.sc_box.default > div.ct_box_area > div.biz_name_area > span").text)
            # print(driver.find_element_by_css_selector("#place_main_ct > div > div > div.sc_box.default > div.ct_box_area > div.bizinfo_area > div > div.list_item.list_item_biztel > div").text)
            # print(driver.find_element_by_css_selector("#place_main_ct > div > div > div.sc_box.default > div.ct_box_area > div.bizinfo_area > div > div.list_item.list_item_address > div > ul > li:nth-child(1) > span").text
            #       + driver.find_element_by_css_selector("#place_main_ct > div > div > div.sc_box.default > div.ct_box_area > div.bizinfo_area > div > div.list_item.list_item_address > div > ul > li:nth-child(2) > span.addr").text)
            # print(driver.find_element_by_css_selector("#place_main_ct > div > div > div.sc_box.default > div.ct_box_area > div.bizinfo_area > div > div.list_item.list_item_menu > div").text)
            # url =driver.find_element_by_css_selector("#place_main_ct > div > div > div.sc_box.default > div.top_photo_area.type_v4 > div:nth-child(1) > a > img").text
            print(food_picture_url)
            print(food_location)
            driver.close()
        except NoSuchElementException:
            pass
    product_file.close()

def test(driver, selector, list):
    try:
        list.append(driver.find_element_by_css_selector(selector).text)
    except NoSuchElementException:
        list.append("null")
        pass
def location(driver,selector1,selector2,list):
    try:
        list.append(driver.find_element_by_css_selector(selector1).text + driver.find_element_by_css_selector(selector2).text)
    except NoSuchElementException:
        list.append("null")
        pass
def picture(driver,selector,list):
    try:
        url1 = driver.find_element_by_css_selector(selector)
        a =url1.get_attribute("src")
        list.append(a)
    except NoSuchElementException:
        list.append("null")
        pass
make_request()