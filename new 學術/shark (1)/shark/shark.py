import tkinter as tk

x = 0   #管理捲動位置的變數
ani=0
def animation():
    global x,ani # x 以全域變數處理
   
    x = x +2  #背景速度 與 after()連動
    if x == 298:  #背景圖x(寬)的大小
        x = 0    #當背景圖到底時再回到原點
    canvas.delete("BG")  #暫時刪除影像
    canvas.create_image(x-149, 84, image=img_bg, tag="BG")  #繪製背景圖像(左側)
    canvas.create_image(x+149, 84, image=img_bg, tag="BG")  #繪製背景圖像(右側)
    #100(數字越大速度越慢)毫秒後再次執行這個函數。after()即時處理函數
    
    ani=(ani+1)%4
    canvas.create_image(250, 100, image=img_b[ani], tag="BG")
    root.after(2, animation)

#主角
'''ani=0
def mainer():
    global ani
    canvas.delete("B")
    canvas.create_image(450, 450, image=gif_b, tag="B")
    root.after(1, animation)
'''
root = tk.Tk()   # 建立 tkinter 視窗物件
root.title('SHARK')        # 設定標題
#root.iconbitmap('下載1.ico')  # 設定 icon ( 格式限定 .ico )
img_bg=tk.PhotoImage(file='shark2.png')

gif_b=tk.PhotoImage(file='未命名.png')

canvas = tk.Canvas(width=298, height=168)#建立視窗大小
# 如果是 Mac 使用下面這行，可以使用 gif 或 png
#root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='下載1.png'))
#img_bg=tk.Photoimage(file='下載1.png')
#canvas.create_image(150,84,image=img_bg)
canvas.pack()#將視窗大小canvas放入主元件中
img_b = [
    tk.PhotoImage(file="sui/sui1.png"),
    tk.PhotoImage(file="sui/sui2.png"),
    tk.PhotoImage(file="sui/sui3.png"),
    tk.PhotoImage(file="sui/sui4.png")
]
animation()
#mainer()
root.mainloop()  # 放在主迴圈中
'''import tkinter

x = 0
ani = 0
def animation():
    global x, ani
    x = x + 8
    if x == 480:
        x = 0
    canvas.delete("BG")
    canvas.create_image(x-240, 150, image=img_bg, tag="BG")
    canvas.create_image(x+240, 150, image=img_bg, tag="BG")
    ani = (ani+1)%8
   
    canvas.create_image(50, 200, image=img_dog[ani], tag="BG")
   
    root.after(150, animation)
   
root = tkinter.Tk()
root.title("動畫")
canvas = tkinter.Canvas(width=480, height=300)
canvas.pack()
     
img_bg = tkinter.PhotoImage(file="park.png")
img_dog = [
    tkinter.PhotoImage(file="redhat_run/run1.png"),
    tkinter.PhotoImage(file="redhat_run/run2.png"),
    tkinter.PhotoImage(file="redhat_run/run3.png"),
    tkinter.PhotoImage(file="redhat_run/run4.png"),
    tkinter.PhotoImage(file="redhat_run/run5.png"),
    tkinter.PhotoImage(file="redhat_run/run6.png"),
    tkinter.PhotoImage(file="redhat_run/run7.png"),
    tkinter.PhotoImage(file="redhat_run/run8.png")
]
animation()
root.mainloop()'''