import base64
from tkinter import *
from tkinter import messagebox

def main():

    def EncodeBase64():
        v1 = v.get()
        msg = v1.encode('utf-8')
        bs64 = base64.b64encode(msg)
        print(bs64)
        messagebox.showinfo("加密结果", " %s " %bs64)
        #break
        mainloop()

    def DecodeBase64():
        v2 = v.get()
        src = v2.encode('utf-8')
        debs = base64.b64decode(src)
        print(debs)
        messagebox.showinfo("解密结果", " %s " %debs)
        #break
        mainloop()
        
    top = Tk()
    top.title("Base64加密")
    top.geometry("800x400")
    
    Interface =Label(top)
    Interface.pack()
    Interface1 = Label(top, text="请输入需要加解密字符串")  # 创建背景图上的文本
    Interface1.place(relx=0.5, rely=0.3, anchor='center')
    
    v = StringVar()
    Label(top, text="字符输入处").place(relx=0.15, rely=0.4)
    e = Entry(top, textvariable=v)
    e.place(relx=0.3, rely=0.4, width=400)

    button1 = Button(top, text='加密', width=6, height=2, bg='#00FF7F', command=EncodeBase64)
    button1.place(relx=0.4, rely=0.7)
    button1 = Button(top, text='解密', width=6, height=2, bg='#00FF7F', command=DecodeBase64)
    button1.place(relx=0.5, rely=0.7)
    button2 = Button(top, text='退出', width=6, height=2, bg='#00FF7F', command=top.withdraw)
    button2.place(relx=0.6, rely=0.7)
    mainloop()

if __name__ == '__main__':
    main()
