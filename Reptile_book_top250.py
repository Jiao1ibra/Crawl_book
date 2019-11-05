# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 09:53:10 2019

@author: 焦少
"""

import requests
import os
import pymysql
import pandas as pd
import random
from lxml import etree

MY_USER_AGENT = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    ]


IMG = []                   #所有图像
BOOK = []                  #所有图书 作者 出版社 价格简介。。。

def get_html(url):
    
    headers ={'User-Agent': random.choice(MY_USER_AGENT)}          #模拟多个UA 反爬虫
#    headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}    
                                        #F12 在network中 top250?start=0点开 中
    try:
        html = requests.get(url,headers = headers)
        html.encoding = html.apparent_encoding
        if html.status_code == 200 :    #HTTP状态码 200 表示网络请求成功
            print ("成功获取源代码")
#            print (html.text)
    except Exception as e:
        print ("获取源代码失败：%s" %e)
    
    return html.text

def parse_html(html):
    
    books = []
    imgurls = []
    html = etree.HTML(html)
    lis = html.xpath("//ul[@class='subject-list']/li")   #总共有个25个table 找相邻的div  一定要相邻的 
    for li in lis:
    
        imgurl = li.xpath(".//img/@src")[0]   # .//表示在li子目录下 获取src
        imgurls.append(imgurl)
        
        name = li.xpath(".//div[@class='info']/h2/a/text()")[0].strip() #找能专属表示name的标签 中间任何属性都不能省  
        total = ("".join(li.xpath(".//div[@class='pub']/text()"))).split('/')
        if (len(total) == 4):
            author = total[0]
            publish = total[-3]
            publication_time = total[-2]
            price = total[-1]
        elif(len(total) == 5):
            author = total[0] + "&&" + total[1]
            publish = total[-3]
            publication_time = total[-2]
            price = total[-1]
        elif(len(total) == 2):
            author = total[0]
            price = total[-1]
            publish = None
            publication_time = None
        elif(len(total) == 1):
            author = total[0]
            publish = None
            publication_time = None
            price = None
            
            
        if name.__contains__("?"):
            name = name.replace("?", "？")
        if name.__contains__(":"):
            name = name.replace(":", "：")
        if name.__contains__("/"):
            name = name.replace("/", " ")
            
            #在Windows系统中，文件名不允许使用的字符有： < > / \ | : " * ?（均为英文版，可替换成中文版）
        if (len(li.xpath(".//div[@class='star clearfix']/span[2]/text()")) != 0):
            rating_score = li.xpath(".//div[@class='star clearfix']/span[2]/text()")[0] #获取div下的第二个span中的内容
        else:
            rating_score = None
        rating_num = li.xpath(".//div[@class='star clearfix']/span[@class='pl']/text()")[0].split('(')[1]
        rating_num = rating_num.split(')')[0].strip()
        
        if(len(li.xpath(".//div[@class='info']/p/text()")) != 0):
            introduce = li.xpath(".//div[@class='info']/p/text()")[0]
        else:
            introduce  = None             #python 中 None为Null
        
        sql = "insert into book2(author,publish,publication_time,price,rating_score,rating_num,introduce,imgurl) values('%s','%s','%s','%s','%s','%s','%s','%s')" %(author,publish,publication_time,price,rating_score,rating_num,introduce,imgurl)
                #不论MySQL的表结构当中，某个字段为何种类型，如float，int,bit,datetime型, Python的SQL语句中都要用%s来表示格式，否则对于非字符串类型的字段，插入式可能会报错    
        try:
            cursor.execute(sql)    #解压sql命令
            conn.commit()           #执行sql命令
        
        except:
            conn.rollback()         #回滚
        book = {'name':name,'author':author,'publish':publish,'publication_time':publication_time,'price':price,'rating_score':rating_score,'rating_num':rating_num,'introduce':introduce}
                                        #book为字典
        books.append(book)            #列表中追加字典
    return books,imgurls
   
def downloadimg(url,book):
    
    if 'bookposter2' in os.listdir(r'C:\Users\Libra\.spyder-py3\training\recommended system'): #如果当前文件夹中也有bookposter 则跳过
        pass
    else:
        os.mkdir('bookposter2')           #创建文件夹bookposter
    os.chdir(r'C:\Users\Libra\.spyder-py3\training\recommended system\bookposter2')    #changedir 进入该文件夹
    
    img = requests.get(url).content      #获取下载链接
    with open(book['name'] + '.jpg','wb')as f:     #下载中
        print ('正在下载：%s' %url)
        f.write(img)
     
if __name__ == '__main__':
    
    conn = pymysql.Connect(host='localhost',user='root',password='990926',database='pymysql',port=3306,charset='utf8')
                        #连接上mysql服务器
    cursor = conn.cursor()      #获取操作游标
    
    for i in range(25):
        url = 'https://book.douban.com/tag/%E4%BA%92%E8%81%94%E7%BD%91?start='+ str(i*20) + '&type=T'
                                            #每一页的网站有规律性
        html = get_html(url)
#        books = parse_html(html)[0]
#        imgurls = parse_html(html)[1]
        parse_html(html)
        
#        BOOK.extend(books)
#        IMG.extend(imgurls)
        

#    for i in range(499):
#        downloadimg(IMG[i],BOOK[i])
#    os.chdir(r'C:\Users\Libra\.spyder-py3\training\recommended system')
#    bookdata = pd.DataFrame(BOOK)
#    bookdata.to_csv('book2.csv',encoding="utf_8_sig") 
#    print ("图书信息成功保存到本地")
    conn.close()            #关闭服务