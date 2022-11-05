from time import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.microsoft import EdgeChromiumDriverManager

browser = webdriver.Edge(EdgeChromiumDriverManager().install())

#get naver shopping page
browser.get("https://shopping.naver.com/home")
browser.implicitly_wait(10)

#search input click
search = browser.find_element_by_css_selector("input._searchInput_search_text_3CUDs")
search = browser.click()

#search keyward input
search.send_keys('아이폰 13')
search.send_keys(Keys.ENTER)

before_h = browser.execute_script("return window.scrollY")

#infinit scrolling
while True:
    browser.find_element_by_css_selector("body").send_keys(Keys.END)
    time.sleep(1)
    after_h = browser.execute_script("return window.scrollY")
    
    if after_h == before_h:
        break

#product imfo div tag
items = browser.find_element_by_css_selector(".basicList_info_area__TWvzp")

for item in items:
    name = item.find_element_by_css_selector(".basicList_link__JLQJf").text
    price = item.find_element_by_css_selector(".price_num__S2p_v").text
    print(price)
    
    