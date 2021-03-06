# 載入需要的套件
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import sys



# 如果是從 InsSpider 呼叫，引入路徑必須加上 mylib；直接執行 AutoLogin 則不用
if __name__ == 'mylib.AutoLogin':
    from mylib.Path import Path_PrivateInfo
    from mylib.Path import Path_WebDriver
else:
    from Path import Path_PrivateInfo
    from Path import Path_WebDriver

# --- 載入隱私資料 ---
File_AccInfo = open(Path_PrivateInfo, mode='r')
Data = ""
Data = File_AccInfo.read().splitlines()
File_AccInfo.close()

# --- 使用 Web Driver 開啟網頁 ----
# # 開啟瀏覽器視窗 (Chrome)
browser = webdriver.Chrome(Path_WebDriver)
# # 欲前往的地址
url = 'https://www.instagram.com/'  
# # 前往網址
browser.get(url) 

# --- 等待並檢查「帳密」的網頁元素生成 ---
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.NAME, 'username')))
# # 找到帳號輸入區塊，並變數命名為 username_input
username_input = browser.find_elements_by_name('username')[0]
# # 找到密碼輸入區塊，並變數命名為 password_input
password_input = browser.find_elements_by_name('password')[0]
# # 程式自動輸入帳密
print("Keying username and password...")
username_input.send_keys(Data[0])
password_input.send_keys(Data[1])


# --- 等待並檢查「登入」的網頁元素生成 ---
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH,
'//*[@id="loginForm"]/div/div[3]/button/div')))
# # 找到登入區塊，並變數命名為 login_click
login_click = browser.find_elements_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')[0]
# # 點擊登入鈕
login_click.click()

# --- 等待並檢查「儲存資料詢問」的網頁元素生成 ---
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')))
# --- 找到不儲存登入資料區塊，並變數命名為 store_click --- 
store_click = browser.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')[0]
# --- 程式自動點擊不儲存 ---
store_click.click()

# --- 等待並檢查「通知開啟詢問」的網頁元素生成 ---
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[2]')))
# ------ 找到通知開啟詢問區塊，並變數命名為 notification_click ------                                                                                                    
notification_click = browser.find_elements_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')[0]
# --- 程式自動點擊不開啟通知 ---
notification_click.click()


# 改寫成物件的話....
"""
class Class_AutoLogin:
    def __init__(self, Path_PrivateInfo, Path_WebDriver):
        self.Path_PrivateInfo = Path_PrivateInfo
        self.Path_WebDriver = Path_WebDriver

    def autologin(self):
        # --- 載入隱私資料 ---
        File_AccInfo = open(self.Path_PrivateInfo, mode='r')
        Data = ""
        Data = File_AccInfo.read().splitlines()
        File_AccInfo.close()

        # --- 使用 Web Driver 開啟網頁 ----
        # # 開啟瀏覽器視窗 (Chrome)
        browser = webdriver.Chrome(self.Path_WebDriver)
        # # 欲前往的地址
        url = 'https://www.instagram.com/'  
        # # 前往網址
        browser.get(url) 

        # --- 等待並檢查「帳密」的網頁元素生成 ---
        WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.NAME, 'username')))
        # # 找到帳號輸入區塊，並變數命名為 username_input
        username_input = browser.find_elements_by_name('username')[0]
        # # 找到密碼輸入區塊，並變數命名為 password_input
        password_input = browser.find_elements_by_name('password')[0]
        # # 程式自動輸入帳密
        print("Keying username and password...")
        username_input.send_keys(Data[0])
        password_input.send_keys(Data[1])


        # --- 等待並檢查「登入」的網頁元素生成 ---
        WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH,
        '//*[@id="loginForm"]/div/div[3]/button/div')))
        # # 找到登入區塊，並變數命名為 login_click
        login_click = browser.find_elements_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')[0]
        # # 點擊登入鈕
        login_click.click()

        # --- 等待並檢查「儲存資料詢問」的網頁元素生成 ---
        WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')))
        # --- 找到不儲存登入資料區塊，並變數命名為 store_click --- 
        store_click = browser.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')[0]
        # --- 程式自動點擊不儲存 ---
        store_click.click()

        # --- 等待並檢查「通知開啟詢問」的網頁元素生成 ---
        WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[2]')))
        # ------ 找到通知開啟詢問區塊，並變數命名為 notification_click ------                                                                                                    
        notification_click = browser.find_elements_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')[0]
        # --- 程式自動點擊不開啟通知 ---
        notification_click.click()
    def __del__(self):
        print('object closing...')
"""
# --- 關閉程式 ---
"""
# # 關閉瀏覽器 ---
browser.close()
# # 關閉所有 WebDriver程式
browser.quit()
print("All Session has closed")
print("Ready to close py...")
# # 結束 Python
sys.exit()
"""