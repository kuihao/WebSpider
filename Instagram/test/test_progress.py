'''
皆需要於 terminal 運作才看得出差異
'''

from time import sleep
temp = 0
total = 100
for n in range(100):
    temp += 1
    
    print(  '\r' + '[Progress]:[%s%s]%.2f%%;' % (
            '█' * int(temp*20/total), ' ' * (20-int(temp*20/total)),
            float(temp/total*100)), end='')
    
    
    # 最原始方法
    #percent = int(temp/total*100)
    #print(f'[{n+1}]', '*' * percent, end='\r') # end 填''或\r效果類似
    
    #sleep(0.01)


'''
from time import sleep
from tqdm import tqdm

for i in tqdm(range(100)):
    sleep(0.01)
'''