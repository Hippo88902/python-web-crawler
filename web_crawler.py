import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By

# 設置目標網站的URL模板
base_url = 'url/{}'

# 使用Selenium開啟瀏覽器會話
driver = webdriver.Chrome()

# 設置登錄信息
username = 'username'
password = 'password'

for i in range(1,3074):
    url = base_url.format(i)
    
    # 打開網頁
    driver.get(url)
    
    # 找到帳號和密碼的輸入框，輸入相應信息
    username_field = driver.find_element(By.ID, 'id_username')
    password_field = driver.find_element(By.NAME, 'password')
    
    # 輸入用戶名和密碼
    username_field.send_keys(username)
    password_field.send_keys(password)
    
    # 模擬按下Enter鍵來提交表單
    password_field.send_keys(Keys.RETURN)
    
    # 等待一段時間，以確保登錄完成
    sleep(5)
    
    # 獲取已登錄的網頁內容
    logged_in_page_content = driver.page_source
    
    # 解析HTML網頁內容
    soup = BeautifulSoup(logged_in_page_content, 'html.parser')
    
    # 生成文件名，例如：output_1.txt, output_2.txt, ...
    output_filename = f'output_{i}.txt'
    
    # 將網頁內容保存到文件中
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write(str(soup))
    
    # 關閉瀏覽器
    driver.quit()
    
    # 使用Selenium重新開啟瀏覽器，以便下一個叠代循環
    driver = webdriver.Chrome()
    
# 關閉瀏覽器
driver.quit()