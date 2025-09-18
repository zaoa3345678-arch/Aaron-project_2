import tkinter as tk # python3 tkinter


win = tk.Tk() #建立主視窗
win.title("tkinter GUI") #主視窗標籤

#大小
win.geometry("400x200") #width * height
# win.minsize(width=400, height=200) #最小寬400，最小高為200，須輸入參數設定
# win.maxsize(width=1024, height=768) #最大寬1024，最大高為768，須輸入參數設定
win.resizable(False, False) #等價 win.resizable(0,0)

#icon
win.iconbitmap(r'C:\Users\user\Desktop\Aaron\Project_1\doc.ico') #須為.ico檔，放在相同的python資料夾即可

#background color
win.config(background="skyblue")

#transparent
win.attributes("-alpha", 0.314159) #0為不透明，1為透明

#on the top
win.attributes("-topmost", 1) #1為置頂，0為不置頂

win.mainloop() #常駐主視窗
