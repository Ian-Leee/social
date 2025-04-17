import tkinter as tk

root = tk.Tk()  #建立tkinter視窗物件
root.title('不好說～')  #設定標題
img_bg = tk.PhotoImage(file="shark2.png")  #載入背景
canvas = tk.Canvas(width=300, height=168)#建立視窗大小
canvas.create_image(150,84,image=img_bg) #在畫布上顯示圖像

canvas.pack()#將視窗大小canvas放入主元件中

root.mainloop()#放在主迴圈中