
n = 10   #int(input('輸入整數: '))
a = '*'    # a 是*號
b = ' '    # b 是空字串
c = int(n/2)   # c  是輸入n的一半 取整數
d = 0
h = int(n/2)    # h  是輸入n的一半 取整數

for i in range(1,n):    #for迴圈 從 1-n
    if i < int(n/2):    #如果 i 小於 輸入n的一半

        c-=1             #c 每次 -1
        print(b*c+a*i+a*(i-1))   #輸出 圖的上半部分 b*c+a*i  是左半部
                                 # a*(i-1)是右半部 第一個位置不輸出 所以i-1
    else:               # 跑一半畫完上半部之後 開始跑下一半
        c+=1
        h-=1
        d+=1
        print(c*b+a*(i-2*d)+a*(h-2))  #畫下半部 c*b+a*(i-2*d) 是左半部
                                      #a*(h-2)是右半部

#
