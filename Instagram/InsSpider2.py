
# 從 InsSpider 的位置執行 AutoLogin.py 路徑會發生變化

from mylib import AutoLogin 
# 引入 Beautiful Soup 模組
from bs4 import BeautifulSoup
import requests
import sys
import os
#import pandas as pd
#import tqdm # 進度條

# 嘗試進入珍藏頁面下載
url_album = '相簿或珍藏頁面'
AutoLogin.browser.get(url_album)
# 等待圖片載入網頁
AutoLogin.WebDriverWait(AutoLogin.browser, 1000).until(AutoLogin.EC.presence_of_element_located((AutoLogin.By.CLASS_NAME,
'KL4Bh')))
soup = BeautifulSoup(AutoLogin.browser.page_source,'lxml') # 抓取網頁原始碼
results = soup.find_all("div", {"class": "KL4Bh"})#, class_="KL4Bh"

'''
# 檢查是否有抓到東西
print(results)
for index, msg in enumerate(results):
    print(f"[{index+1}] {msg}")
'''
# 將萃取的圖片網址放進陣列
print("將萃取的圖片網址放進陣列")
image_links = [result.img.get("src") for result in results]
'''
# 檢視萃取到的圖片網址
for index, link in enumerate(image_links):
    #print(type(link))
    print(f"[{index+1}] {link}")
'''

# 下載圖片
print("準備下載圖片...")
#progress = tqdm(total=len(image_links)) # 進度條套件 :D
for index, link in enumerate(image_links):
    #progress.update(1)
    foldername = "ins_images"
    if not os.path.exists(f"{foldername}"):os.mkdir(f"{foldername}")  # 建立資料夾
    req_img = requests.get(link)  # 下載圖片

    with open(f"{foldername}\instagram_photo_{index+1}.jpg", "wb") as file:  # 開啟資料夾及命名圖片檔
        file.write(req_img.content)  # 寫入圖片的二進位碼

print("InsSpider Finish.")
# --- 關閉程式 ---

# # 關閉瀏覽器 ---
AutoLogin.browser.close()
# # 關閉所有 WebDriver程式
AutoLogin.browser.quit()
print("All Session has closed")
print("Ready to close py...")
# # 結束 Python
sys.exit()

