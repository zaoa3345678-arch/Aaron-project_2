import tkinter as tk #Python

win = tk.Tk()
win.title("tkinter GUI")
win.geometry("400x200")
# win.minsize(width=400, height=200)
# win.maxsize(width=1024, height=768)
win.resizable(width=False, height=False)
win.config(background="skyblue")
win.iconbitmap(r"C:\Users\user\Desktop\Aaron\Project_1\doc.ico") #須加r才會讀取idk why

def say_hi():
    print('hello world')

def ok():
    t=en.get()
    lb.config(text=t)

en = tk.Entry()
en.pack()

btn2 = tk.Button(text='ENTER', command=ok)
btn2.pack()

# img = tk.PhotoImage(file=r"C:\Users\user\Desktop\Aaron\Project_1\button.png")
# btn = tk.Button()
# btn.config(image=img)

btn = tk.Button(text='CLICK ME')
btn.config(background='green')
btn.config(width=10, height=5)
btn.config(command=say_hi)
btn.pack()

lb = tk.Label(text='The text')
lb.config(background='skyblue', foreground='white')
lb.pack()

win.mainloop()