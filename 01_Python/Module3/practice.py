# 終極密碼 讓使用者能夠重複猜數字，直到猜對為止
# 告訴使用者需要輸入的數字範圍 input()#請輸入1到100
# 超出範圍要顯示「超出範圍請重新輸入」
# 數字太大 要提示「請輸入更小的數字」
# 數字太小 要提示「請輸入更大的數字」
# 使用者猜對要回傳「恭喜中獎」

#升級版:

#1.用try except打包後，使用者輸入中文或其他文字可以重新輸入
#2.把 answer的數字改成random
#3.


import random
num = random.randint(1, 100)
cnt = 0



while True :
        try:
            data =  int(input("請輸入1到100:"))
        except ValueError: 
                print("請輸入數字")
                continue
        if  data > 100 or data <=0 :
                print("超出範圍請重新輸入")
                continue
        elif data < num:
                print("請輸入更大數字")
                continue
        elif data > num:
                print("請輸入更小數字")
                continue
        elif data == num:
                print("恭喜中獎")
                cnt +=1
                if cnt == 3:
                    print("已猜對三次，恭喜過關")
                    break
                else: # 還沒猜對三次=>重新設定答案讓使用者繼續猜
                    print(f"已猜對{cnt}次，進行下一輪")
                    num = random.randint(1, 100)
                    continue
                




