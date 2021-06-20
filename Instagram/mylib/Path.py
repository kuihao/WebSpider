# (???待查證)好像是因為 VScode 使以 workplace 的角度來看待所有路徑，之後改CML時要debug
# 程式呼叫時，檔案的相對路徑參考點是呼叫者 (此程式)，而非被呼叫者(副程式)

# # 先建立 SS.txt 檔案，裡面有兩行資料分別為帳號、密碼
Path_PrivateInfo = "SS.txt" # 資安保險，只有使用時才輸入正確路徑
# # 指定 Chrome Web Driver 程式所在路徑 (隨Chrome版本更新，這檔案也要更新)
Path_WebDriver = "chromedriver.exe" # 資安保險，只有使用時才輸入正確路徑


'''
檢查檔案位置
'''
#with open('相對路徑','r') as fp: 
#     all_lines = fp.readlines()
#print(all_lines)