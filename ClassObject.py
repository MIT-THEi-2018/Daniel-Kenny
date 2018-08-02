import tkinter as tk
from tkinter import messagebox  # import this to fix messagebox error
import pickle
from PIL import Image, ImageTk

window = tk.Tk()
window.title('Prototype')
window.geometry('450x300')

# welcome image
canvas = tk.Canvas(window, height=200, width=500)
image_file = tk.PhotoImage(file='welcome.gif')
image = canvas.create_image(0,0, anchor='nw', image=image_file)
canvas.pack(side='top')

# user information
tk.Label(window, text='User name: ').place(x=50, y= 150)
tk.Label(window, text='Password: ').place(x=50, y= 190)

var_usr_name = tk.StringVar()
var_usr_name.set(' ')
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=160, y=150)
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=160, y=190)

def usr_login():
	tk.messagebox.showinfo(title='Welcome', message='Please enjoy the application')
	main_page()
    # usr_name = var_usr_name.get()
    # usr_pwd = var_usr_pwd.get()
    # try:
    #     with open('usrs_info.pickle', 'rb') as usr_file:
    #         usrs_info = pickle.load(usr_file)
    # except FileNotFoundError:
    #     with open('usrs_info.pickle', 'wb') as usr_file:
    #         usrs_info = {'admin': 'admin'}
    #         pickle.dump(usrs_info, usr_file)
    # if usr_name in usrs_info:
    #     if usr_pwd == usrs_info[usr_name]:
    #         tk.messagebox.showinfo(title='Welcome', message='How are you? ' + usr_name)
    #     else:
    #         tk.messagebox.showerror(message='Error, your password is wrong, try again.')
    # else:
    #     is_sign_up = tk.messagebox.askyesno('Welcome',
    #                            'You have not signed up yet. Sign up today?')
    #     if is_sign_up:
    #         usr_sign_up()

def main_page():
	main = tk.Toplevel(window)
 
	main.title("Prototype")
 
	main.geometry('300x500')
 
	# listb = Listbox(main)

	# region_list = ['Central and Western', 'Eastern','Southern']

	# for item in region_list:
	# 	listb.insert(0,item)
	# 	listb.pack()
	# 	listb.grid(column=0, row=0)
	l = main.Label(window, 
    text='OMG! this is TK!',    # 标签的文字
    bg='green',     # 背景颜色
    font=('Arial', 12),     # 字体和字体大小
    width=15, height=2  # 标签长宽
    )
	l.pack()    # 固定窗口位置



def usr_sign_up():
    def sign_to_Mofan_Python():

        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()
        with open('usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
        if np != npf:
            tk.messagebox.showerror('Error', 'Password and confirm password must be the same!')
        elif nn in exist_usr_info:
            tk.messagebox.showerror('Error', 'The user has already signed up!')
        else:
            exist_usr_info[nn] = np
            with open('usrs_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tk.messagebox.showinfo('Welcome', 'You have successfully signed up!')
            window_sign_up.destroy()
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x300')
    window_sign_up.title('Sign up window')

    new_name = tk.StringVar()
    new_name.set('')
    tk.Label(window_sign_up, text='User name: ').place(x=10, y= 10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=150, y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='Password: ').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=150, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='Confirm password: ').place(x=10, y= 90)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=150, y=90)

    new_live_region = tk.StringVar()
    tk.Label(window_sign_up, text='region: ').place(x=10, y= 130)
    entry_live_region = tk.Entry(window_sign_up, textvariable=new_name)
    entry_live_region.place(x=150, y=130)




    btn_comfirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_Mofan_Python)
    btn_comfirm_sign_up.place(x=150, y=170)

# login and sign up button
btn_login = tk.Button(window, text='Login', command=usr_login)
btn_login.place(x=170, y=230)
btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
btn_sign_up.place(x=270, y=230)


window.mainloop()