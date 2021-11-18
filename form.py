# 備忘錄：按鈕繼續新增
import tkinter as tk
import tkinter.messagebox
import predict

window = tk.Tk()
window.title('window')
window.geometry("1280x720+800+600")
# command
##########################
def define_layout(obj, cols=1, rows=1):
    def method(trg, col, row):

        for c in range(cols):
            trg.columnconfigure(c, weight=1)
        for r in range(rows):
            trg.rowconfigure(r, weight=1)

    if type(obj) == list:
        [method(trg, cols, rows) for trg in obj]
    else:
        method(obj, cols, rows)

def validate(P):
    if str.isdigit(P) or P == '':
        return True
    else:
        return False


def output():
    msg = entry.get()
    if msg == '':
        tk.messagebox.showerror(title='WARNING', message = '不能輸出空白')
    else:
        msg = int(entry.get())
        stock_info.set(predict.stock(msg))
        #tk.messagebox.showinfo(title='WARNING', message = msg)

##########################
# creat divs in window
div_size = 100
output_size = div_size * 2
pad = 5
align_mode = 'nswe'
div1 = tk.Frame(window, width=output_size, height=output_size, bg='#135a94') # for output
div2 = tk.Frame(window, width=div_size, height=div_size, bg='#d6b220') # for output info
div3 = tk.Frame(window, width=div_size, height=div_size, bg='#0fa65a') # for input

div1.grid(column=0, row=0, padx=pad, pady=pad, rowspan=2, sticky=align_mode)
div2.grid(column=1, row=0, padx=pad, pady=pad, sticky=align_mode)
div3.grid(column=1, row=1, padx=pad, pady=pad, sticky=align_mode)

# objects in window
stock_info = tk.StringVar()
stock_info.set('個股預覽')
label_info = tk.Label(div2, textvariable=stock_info, bg='#d6b220', font=30)
label_info.grid(column=0, row=0, sticky=align_mode)


label_input = tk.Label(div3, text='請輸入股票編號', font=20)
label_input.grid(column=0, row=0, sticky=align_mode)

vcmd = (div3.register(validate), '%P')
entry = tk.Entry(div3, width=10, font=(30), validate='key',justify='center', validatecommand=vcmd)
entry.grid(column=0, row=1)

bt1 = tk.Button(div3,width = 20, text='OK', bg='#4287f5',activebackground='#143261',activeforeground='white', fg='white', font=(20), command=output)
bt1.grid(column=0, row=2)


define_layout(window, 2, 2)
define_layout(div1)
define_layout(div2, rows=1)
define_layout(div3, rows=3)

window.mainloop()
