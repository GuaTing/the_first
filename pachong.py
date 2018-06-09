import requests
# -*- coding: utf-8 -*-
"""
created on 2018/5/
author:Guo
target:获得时光网中电影的公司
finished on:2017/6/9
"""
# from pymongo import MongoClient
# conn = MongoClient('192.168.0.113', 27017)
# db = conn.mydb
# my_set = db.test_set
import sys
import urllib.parse
# reload(sys)
# sys.setdefaultencoding('utf-8')
from lxml import etree
from selenium import webdriver
# #中文轉url編碼
# # print(url)
# r= requests.get(url)
# print(r.content.decode("utf-8"))
#
import requests
def production_company(url):
    """
    获取制作公司
    :param url: 电影制作公司所在頁面地址
    :return:
    """
    r = requests.get(url)
    page_source = r.content.decode("utf-8")
    html = etree.HTML(page_source)
    p_company = {}
    for i in html.xpath("//div[@class='db_contout']/div[@class='db_cont ']/div[@class='details_cont']//dd/div[@class='clearfix']/div[@class='fl wp49'][1]/ul/li/a"):
        all_name = i.xpath("text()")
        all_url = i.xpath("@href")
        # print(e2)
        # print(e3)
        for p_name in all_name:
            for p_url in all_url:
                p_company[p_name] = p_url
    print(p_company)
    return p_company
def distribution_company(url):
    """
    获取发行公司
    :param url:电影发行公司所在頁面地址
    :return:
    """
    r = requests.get(url)
    page_source = r.content.decode("utf-8")
    html = etree.HTML(page_source)
    l_conpany = {}
    for i in html.xpath("//div[@class='db_contout']/div[@class='db_cont ']/div[@class='details_cont']//dd/div[@class='clearfix']/div[@class='fl wp49'][2]/ul/li/a"):
        all_name = i.xpath("text()")
        all_url = i.xpath("@href")
        for l_name in all_name:
            for l_url in all_url:
                l_conpany[l_name] = l_url
    print(l_conpany)
    return l_conpany

r = open("../2013.txt")
line = r.readlines()
final = {}
a = []
z = 0
names_list = []
movie_names = []
movie_ids = []
year = {}
year["year"] = "2013"
for names_line in line:
    names_line = names_line.replace('\n','\x01')
    movie_names.append(names_line.split('\x01')[0])
    movie_ids.append(names_line.split('\x01')[1])
    url0 = "http://search.mtime.com/search/?q="+urllib.parse.quote(names_line.split('\x01')[0])
    print(url0)
    driver = webdriver.PhantomJS(executable_path='../phantomjs')
    driver.get(url0)
    fans_info_data = driver.page_source
    html = etree.HTML(fans_info_data)
    names = names_line.split('\x01')[0]
    print(names+"\t2222")
    for i in html.xpath("//div[@class='main']/ul[@id='moreRegion']/li[@class='clickobj']/h3/a"):
        get_title = i.xpath("text()")

        for title in get_title:
            if "2013" in title:
                print(title+"\t3333")
                z += 1
                get_url = i.xpath("@href")
                print("get_url")
                print (get_url)
        #         a.append(e5)
                for url1 in get_url:
                    print(url1)
                    url = url1+'details.html'
                    # a = [names]
                    # print(a)
                    # z += 1
                    if names in names_list:
                        continue
                    else:
                        names_list.append(names)
                        with open('../film2013/'+names+'.txt',"a+") as f:
                            f.write("{"+'"_id"'+"="+str(movie_ids)+'\n'
                                +'"year"'+":"+"2013"+'\n'
                                +'"movie_name"'+"="+str(names)+'\n'
                                +'"p_company":'+str(production_company(url))+'\n'
                                +'"l_company":'+str(distribution_company(url))+'}'
                            )

# for movie_name in movie_names:
#     if movie_name not in names_list:
#         print(movie_name)
#         with open('../film2013/'+'NULL.txt',"a+") as f:
#             f.write(movie_name+'\n')
            # if "2007" not in n:
            #     break
                # print(e0)
    # print("z:"+str(z))
# for i in e0_list:
#         print(i)
# print(z)
# print(e0_list.__len__())

# url = 'http://movie.mtime.com/32446/details.html'
# name(url)
# print('制作公司:')
# production_company(url)
# print('发行公司:')
# distribution_company(url)