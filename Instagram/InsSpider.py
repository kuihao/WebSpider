'''
直接下載登入後首頁出現的圖片
'''
# [!!!] 從 InsSpider 的位置執行 AutoLogin.py 路徑會發生變化
from mylib import AutoLogin 
from bs4 import BeautifulSoup
import requests
import sys
import os

# --- 從首頁獲取圖片網址 ---

soup = BeautifulSoup(AutoLogin.browser.page_source,'lxml') # 抓取網頁原始碼

results = soup.find_all("div", class_="KL4Bh")
#print(results)

print("正在萃取網頁中的圖片網址...")
image_links = [result.img.get("src") for result in results]
#for index, link in enumerate(image_links):
#    index += 1
#    print(type(link))
#    print(f"[{index}] {link}")

print("開始下載圖片...")
for index, link in enumerate(image_links):
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

'''
# 獲取影片連結
url = 'https://www.instagram.com/p/CFHwyL6s9Gn/'
browser.get(url) 
soup = Soup(browser.page_source,"lxml")
soup.find_all(class_="_5wCQW")[0].video.get('src')
'''
