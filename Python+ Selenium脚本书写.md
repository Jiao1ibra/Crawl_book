###### Python+ Selenium脚本书写

#### 一、安装模块和选择浏览器

1、模块安装

```python
pip install selenium
```

2、浏览器驱动安装

- 我使用的firefox浏览器，当然还可以选择chrome浏览器 	

2.1 下载 GeckoDriver驱动

- 下载地址：https://github.com/mozilla/geckodriver/releases

2.2 环境变量配置

- 将 geckodriver.exe文件拖到Python的Scripts目录下 
- 将 geckodriver.exe文件拖到浏览器的安装目录(C:\Program Files\Mozilla Firefox)下

##### 注意： 浏览器的版本 不能高于驱动的要求最高版本

3、实例

-  检查准备工作是否完善，简单进行下测试。使用selenium和firefox驱动打开指定url网页。

```
# 1-导入模块文件
from selenium import webdriver
# 2-初始化浏览器为chrome浏览器
driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
# 3-这里我们打开的是百度首页
driver.get('https://www.baidu.com/')
# 4-打印下网页标题
print(driver.title)
# 5-关闭浏览器
driver.quit()
```

 完成后，程序会在控制台输出：**百度一下，你就知道** 

#### 二、定位页面元素的八种方法

综述：

- id定位：find_element_by_id(' ')
- name定位：find_element_by_name(' ')
- class定位：find_element_by_class_name(' ')
- tag定位：find_element_by_tag_name(' ')
- link定位：find_element_by_link_text(' ')
- partial link定位：find_element_by_partial_link_text(' ')
- xpath定位：find_element_by_xpath(' ')
- CSS定位：find_element_by_css_selector(' ')
- By定位



1、利用ID定位元素

```
from selenium import webdriver
# 设置浏览器
driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
#设置浏览器大小：全屏
driver.maximize_window()
#打开百度首页
driver.get('https://www.baidu.com/')
#定位百度搜索输入框之前，先分析下它的html结构
#<input type="text" class="s_ipt nobg_s_fm_hover" name="wd" id="kw" maxlength="100" autocomplete="off">
#发现它的 id="kw" ，接下来我们就通过id进行定位
try:
    driver.find_element_by_id('kw').send_keys('哈哈')
    print('test post：id')
except Exception as e:
    print('test fail')

#输出内容：test post：id
```

2、利用name定位元素

```
from selenium import webdriver
driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
driver.maximize_window()

#打开百度首页
driver.get('https://www.baidu.com/')
#搜索框的html结构：<input type="text" class="s_ipt nobg_s_fm_hover" name="wd" id="kw" maxlength="100" autocomplete="off">
# 根据name属性定位
try:
    driver.find_element_by_name('wd').send_keys('哈哈')
    print('test post：name')
except Exception as e:
    print('test fail')

#输出内容：test post：name
```

3、利用class定位元素

```
from selenium import webdriver
driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
driver.maximize_window()

#打开百度首页
driver.get('https://www.baidu.com/')
#搜索框的html结构：<input type="text" class="s_ipt nobg_s_fm_hover" name="wd" id="kw" maxlength="100" autocomplete="off">
# 根据class_name属性定位
try:
    driver.find_element_by_class_name('s_ipt').send_keys('哈哈')
    print('test post：class_name')
except Exception as e:
    print('test fail')

#输出内容：test post：class_name
```

4、利用tag_name定位元素

```
from selenium import webdriver
driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
driver.maximize_window()

#打开百度首页
driver.get('https://www.baidu.com/')
#搜索框的html结构：<input type="text" class="s_ipt nobg_s_fm_hover" name="wd" id="kw" maxlength="100" autocomplete="off">
# 根据tag_name属性定位
try:
    driver.find_element_by_tag_name('form')
    print('test post：tag_name')
except Exception as e:
    print('test fail')

#输出内容：test post：tag_name
```

5、利用link_text定位元素

-  link_text：根据跳转链接上面的文字来定位元素。 

```
from selenium import webdriver
driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
driver.maximize_window()

#打开百度首页
driver.get('https://www.baidu.com/')
# 根据link_text属性定位元素“新闻”，然后点击按钮
try:
    driver.find_element_by_link_text('新闻').click()
    print('test post：tag_name')
except Exception as e:
    print('test fail')

#输出内容：test post：link_text
```

6、利用partial_link_text定位元素

-  和link_text定位元素差不多，partial_link_text是通过文字信息中的部分字段来定位元素。 

```
from selenium import webdriver
driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
driver.maximize_window()

#打开百度首页
driver.get('https://www.baidu.com/')
# 根据partial_link_text属性定位元素“新闻”，然后点击按钮
try:
    driver.find_element_by_partial_link_text('闻').click()
    print('test post：tag_name')
except Exception as e:
    print('test fail')

#输出内容：test post：partial_link_text
```

7、利用xpath定位元素

```
from selenium import webdriver
driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
driver.maximize_window()

#打开百度首页
driver.get('https://www.baidu.com/')
# 根据xpath定位元素
try:
    driver.find_element_by_xpath('//*[@id="kw"]').send_keys('哈哈')
    print('test post：xpath')
except Exception as e:
    print('test fail')

#输出内容：test post：xpath
```

8、利用CSS定位页面元素

```
from selenium import webdriver
driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
driver.maximize_window()

#打开百度首页
driver.get('https://www.baidu.com/')
# 根据css_selector定位元素
try:
    driver.find_element_by_css_selector('#kw').send_keys('哈哈')
    print('test post：xpath')
except Exception as e:
    print('test fail')

#输出内容：test post：css_selector
```

9、By定位

- 除了使用上面的方法外，还可以利用find_element()方法，通过By来定位元素。
- 使用之前需要导入By类

```
#导入By类
from selenium.webdriver.common.by import By
```

-  那么上面的方法还可以改写为： 

```
driver.find_element(By.ID,'kw')
driver.find_element(By.NAME,'wd')
driver.find_element(By.CLASS_NAME,'s_ipt')
driver.find_element(By.TAG_NAME,'form')
driver.find_element(By.LINK_TEXT,'新闻')
driver.find_element(By.PARTIAL_LINK_TEXT,'闻')
driver.find_element(By.XPATH,'//*[@id="kw"]')
driver.find_element(By.CSS_SELECTOR,'#kw')
```

##### 另：定位元素中的子元素

- 下列实例为获取第一个class为sc-bZQynM的div中的第二个标签a的文本

```
div1=soup.select('div.sc-bZQynM')      #获取图书名  碰到class中有空格的 挑其中一个唯一的写就行
txt=div1[0].select('a')[1].get_text()
```

#### 三、设置浏览器大小、刷新页面、前进和后退

1、设置浏览器大小

- maximize_window()：设置浏览器大小为全屏
- set_window_size(500,500)：设置浏览器分辨率为：500×500

```
from selenium import webdriver
import time  

driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
driver.maximize_window()   #设置浏览器大小：全屏
driver.get('https://www.baidu.com')  
time.sleep(2)

driver.set_window_size(500,500)  # 分辨率 1280*800  
time.sleep(2)

driver.set_window_size(1024,768)  # 分辨率 1024*768  
time.sleep(2)
```

2、刷新浏览器页面

-  refresh()方法：刷新浏览器页面 

```
from selenium import webdriver
import time  

driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
driver.maximize_window()   #设置浏览器大小：全屏
driver.get('https://www.baidu.com')  
time.sleep(1)

try:
    driver.refresh()  #刷新页面
    print('刷新页面')
except Exception as e:
    print('test fail')

#输出内容：刷新页面
```

3、浏览器的后退和前进

- back()：后退
- forward()：前进

```
from selenium import webdriver
import time  

driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
driver.maximize_window()   #设置浏览器大小：全屏
driver.get('https://www.baidu.com')  

#点击打开百度新闻页面
driver.find_element_by_link_text('新闻').click()
time.sleep(2)

driver.back()  #后退：回到百度首页
time.sleep(2)

driver.forward()  #前进：前进到百度新闻页面
time.sleep(2)
```

#### 四、获取页面信息

1.获取页面title

- title：获取当前页面的标题显示的字段

```
from selenium import webdriver
import time  

driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
driver.get('https://www.baidu.com')  

#打印网页标题
print(driver.title)
#输出内容：百度一下，你就知道
```

2.获取页面URL

- current_url：获取当前页面的URL

```
from selenium import webdriver
import time  

driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
driver.get('https://www.baidu.com')  

#打印网页标题
print(driver.current_url)
#输出内容：https://www.baidu.com/
```

3.获取浏览器版本号

- capabilities['version'])：打印浏览器version的值

```
from selenium import webdriver
import time  

driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
driver.get('https://www.baidu.com')  

#打印网页标题
print(driver.capabilities['version'])
#输出内容：67.0.3396.87
```

4.获取元素尺寸

- size：返回元素的尺寸

```
from selenium import webdriver
import time  

driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
driver.get('https://www.baidu.com')  

#定位输入框
input_box = driver.find_element_by_id('kw')
#打印输入框尺寸
print(input_box.size)
#输出内容：{'height': 22, 'width': 500}
```

5.获取元素的文本

- text：返回元素的文本信息

```
from selenium import webdriver
import time  

driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
driver.get('https://www.baidu.com')  

#定位备案元素
recordcode = driver.find_element_by_id('jgwab')
#打印备案元素信息
print(recordcode.text)
#输出内容：京公网安备11000002000001号
```

6.获得属性值

- get_attribute('')方法
- get_attribute('href'):获取href属性值
- get_attribute('id'):获取id属性值

```
# coding=utf-8
import time
from selenium import webdriver


driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
driver.maximize_window()
driver.implicitly_wait(6)
driver.get("https://www.baidu.com")
time.sleep(1)

for link in driver.find_elements_by_xpath("//*[@href]"):
    print (link.get_attribute('href'))
driver.quit()
```

#### 彩蛋：

​		为了发扬可持续性发展战略 最好设置一定的等待时间

1、显性等待时间

```
import time#导入包
time.sleep(3)#设置时间间隔为3秒
```

2、隐式等待时间

-  就是在等待页面元素加载全部完成后才进行下一步操作 

```
wait1.until(lambda driver: driver.find_element_by_xpath("//div[@id='link-report']/span"))
```

Good Luck !