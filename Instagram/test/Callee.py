# 被導入、被呼叫的程式

# 不用寫成類別、物件也可以，直接制定函式。「參數接上等於某值」表示預設值，
# 若呼叫函式沒給參數初值，則會自動賦予預設值。此處預設值為 integer 123
def out(A=123):
    print(A)

print('Callee is running')

# if __name__ == '__main__': #(這裡面只有 Command Line 時會執行)
# __name__意義是「模組名稱」。如果該檔案是被引用，其值會是模組名稱；但若該檔案是(透過命令列)直接執行，其值會是 __main__