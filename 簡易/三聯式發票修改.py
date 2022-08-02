import tkinter as tk
from PIL import ImageTk, Image



def math():
    global numStr1               #取得數量
    global entry1String          #於第一位置動作

    global sellStr1               #取得售價,global等於宣告其可在此定義中進行修改
    global entry2String         #於entry2位置動作


    global addStr1
    global totalStr1
    global TaxStr1                  #營業稅
    global totalStr2
    str3=int(entry2String.get())*int(entry1String.get())    #按鍵一跟按鍵二相加
    addStr1.set(str(str3))          #金額
    totalStr1.set(str(str3))        #銷售總金額
    str4=int(entry2String.get())*int(entry1String.get())*0.5    #按鍵一跟按鍵二相加
    TaxStr1.set(str(str4))          #營業稅
    str5=str3+str4    #按鍵一跟按鍵二相加
    totalStr2.set(str(str5))          #總計
    shin1.set(numberToChinese(int(str5)))


def numberToChinese(n):
   list1 = ["元", "拾", "佰", "仟", "萬", "拾", "佰", "仟", "億"]
   list2 = ["零", "壹", "貳", "參", "肆", "伍", "陸", "柒", "捌", "玖"]
   shin1 = ""
   digit = 0
   while True:
      n1 = n % 10
      n = n // 10
      # 處理位數
      shin1 = list1[digit] + shin1
      # 數字轉國字
      if n1 >= 0 and n1 <= 9:
         shin1 = list2[n1] + shin1
      if n <= 0:  # n < 0時結束迴圈
         break
      digit = digit + 1

   return shin1



#視窗相關部分
win = tk.Tk()
win.wm_title("統一發票三聯式")                 # 設定主視窗標題
win.resizable(width=False, height=False) # 設定主視窗不可以被調整大小
win.maxsize(width=1080, height=450)       # 最大尺寸
x=Image.open("tree.jpg")                     # 讀取圖片
img = ImageTk.PhotoImage(x)                    # 轉換成PhotoImage
sub =tk.Label(win, image = img)             # 建立Label物件 顯示圖片
sub.pack()

#  輸入框Entry
entry1String = tk.StringVar()                           #數量
entry1=tk.Entry(win,textvariable = entry1String) # 新增輸入框Entry
entry1.place(x=268, y=180,width=57)
entry1String.set("")

entry2String = tk.StringVar()                           #單價
entry2=tk.Entry(win,textvariable = entry2String)        # 新增輸入框Entry
entry2.place(x=338, y=180,width=57)                                #輸入框的位置
entry2String.set("")                                    #一開始是空白字串

# 按鈕Button

btn1 =tk.Button(win,text="計算",command=math)     # 建立Button物件 按下後會出叫event1函式
btn1.place(x=0, y=0)

# 標籤Label
produ1 =tk.Label(win,text="調味料",bg="white",fg="black",font=("Helvetica", 10))  # 建立文字 label建立文件
produ1.place(x=100, y=180)                           #品名
name =tk.Label(win,text="王曉明",bg="white",fg="black",font=("Helvetica", 10))  # 建立文字 label建立文件
name.place(x=165, y=80)                           #買受人
c=Image.open("seall.png")                         #載入圖片
img1=ImageTk.PhotoImage(c)                          #轉換成PhotoImage
seal =tk.Label(win,image = img1)                    # 建立Label物件 顯示圖片
seal.place(x=560, y=280)                           #圖片的位置

totalStr1 = tk.StringVar()                            #  建立StringVar 變數數量
total2 =tk.Label(win,text="", textvariable=totalStr1)  #  建立Label物件, 綁定這個數量變數
totalStr1.set("")
total2.place(x=405, y=307)                              #總銷售合計

addStr1 = tk.StringVar()                            #  建立StringVar 變數數量
add2 =tk.Label(win,text="", textvariable=addStr1)  #  建立Label物件, 綁定這個數量變數
addStr1.set("")
add2.place(x=405, y=180)                              #金額

TaxStr1 = tk.StringVar()                            #  建立StringVar 變數數量
Tax1 =tk.Label(win,text="", textvariable=TaxStr1)  #  建立Label物件, 綁定這個數量變數
TaxStr1.set("")
Tax1.place(x=405, y=335)                              #營業稅

totalStr2 = tk.StringVar()                            #  建立StringVar 變數數量
total3 =tk.Label(win,text="", textvariable=totalStr2)  #  建立Label物件, 綁定這個數量變數
totalStr2.set("")
total3.place(x=405, y=363)                              #營業稅

symbol =tk.Label(win,text="v",font=("Helvetica", 8))  # 建立文字 label建立文件
symbol.place(x=255, y=345)                           #勾勾

shin1 = tk.StringVar()                               #  建立StringVar 變數
st1 =tk.Label(win,text="!", textvariable=shin1, anchor="e", width=24)  #  建立Label物件, 綁定這個變數
st1.place(x=338, y=390)                          # 指定位置 國字

win.mainloop()