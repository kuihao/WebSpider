# 如何導入自己的程式？

# 可以直接導入 (import) 檔名，不用加附檔名.py
# 此方法相當於直接從這個程式要求 OS fork 一個副程式
# 意思是直接 import Callee，則 Callee 也會被執行起來
# 注意！Callee 的內部函式並未引入 Caller，需要用小數點算子來「指定」 Callee 執行內部函式
import Callee 
Callee.out()

# 也可以不執行 Callee，而是
# 單純從 Callee 檔案裡面引入特定的函式
# 相當於 Caller 本身新增了原本位在 Callee 內部的函式 
from Callee import out
out('lala')

# 以上兩個方法都會產生一個 __pycache__ 檔案