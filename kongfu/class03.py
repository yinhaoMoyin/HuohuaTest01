1.包 Commonlib文件Commonlib 类方法 Commonshare(持续更新中)
from selenium import webdriver
import time,unittest

class Commonshare(object):
    #初始化
   def __init__(self):
    #创建浏览器
    self.driver = webdriver.Chrome()
    #隐式等待
    self.driver.implicitly_wait(3)
    #浏览器最大化
    self.driver.maximize_window()
  def open_url(self,url):
    #请求指定站点
    self.driver.get(url)
    time.sleep(3)
  def locateElement(self,locate_type,value):
    el = None
    if locate_type == 'id':
    el = self.driver.find_element_by_id(value)
    elif locate_type == 'name':
    el = self.driver.find_element_by_name(value)
    elif locate_type == 'class':
        el = self.driver.find_element_by_class_name(value)
    elif locate_type == 'tag':
    el = self.driver.find_element_by_tag_name(value)
    elif locate_type == 'link':
    el = self.driver.find_element_by_link_text(value)
    elif locate_type == 'partial':
        el = self.driver.find_element_by_partial_link_text(value)
    elif locate_type == 'xpath':
        el = self.driver.find_element_by_xpath(value)
    elif locate_type == 'css':
        el = self.driver.find_element_by_css_selector(value)
     #定位到元素才返回元素
     if el is not None:
    return el
  # 直接对定位到的元素进行点击
 def click(self,locate_type,value):
    #调用LocateElement()
    el = self.locateElement(locate_type,value)
    #执行点击
    el.click()
 #直接对定位到的元素进行文本输入
 def input_data(self,locate_type,value,data):
    # 调用LocateElement()
    el = self.locateElement(locate_type, value)
     # 输入发送
    el.send_keys(data)
#获取定位到的元素中的文本内容<a>xxxx</a>
def get_text(self,locate_type,value):
    #调有locateElement()
     el = self.locateElement(locate_type,value)
    return el.text
# 获取定位到的元素中的标签属性
 def get_attr(self, locate_type,value,data):
    # 调有locateElement()
    el = self.locateElement(locate_type, value).get_attribute(data)
    return el
 def handle(self):
    #获取句柄，进入第二个句柄
    handle_list01 = self.driver.window_handles
    self.driver.switch_to.window(handle_list01[1])
    # 当前标签页，标题获取
    bt01 = '当前标题:', self.driver.title
    print(bt01)
  def screenshot(self):
    PicDir=time.strftime("%m_%d-%H:%M:%S",time.localtime())+"_huohua_dl_01.png"
    print(PicDir)
    #未加时间戳，和格式化
    self.driver.get_screenshot_as_file('/Users/panyinhao/PycharmProjects/untitled3/Testcase/snapshot02/%s'%PicDir)
   def close(self):
    self.driver.close()
    ##收尾清理方法
    #def __del__(self):
    # time.sleep(3)
    # self.driver.quit()

if __name__ == '__main__':
com = Commonshare()
com.open_url('https://www.baidu.com/')
# com.input_data('id','kw','selenium')
time.sleep(3)
d2 = com.get_attr('class','s_ipt','class')
print(d2)
# del com
