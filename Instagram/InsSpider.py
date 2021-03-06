# 程式呼叫時，檔案的相對路徑參考點是呼叫者 (此程式)，而非被呼叫者(副程式)
# # 先建立 SS.txt 檔案，裡面有兩行資料分別為帳號、密碼
Path_PrivateInfo = "SS.txt"
# # 指定 Chrome Web Driver 程式所在路徑 (隨Chrome版本更新，這檔案也要更新)
Path_WebDriver = "mylib/chromedriver.exe" 

# 從 mylib 資料夾中的 AutoLogin.py 引入 autologin 函式，
# 因為是間接引入，故實際上不會執行 AutoLogin.py
from mylib.AutoLogin import autologin
autologin(Path_PrivateInfo, Path_WebDriver)

print("InsSpider Finish.")