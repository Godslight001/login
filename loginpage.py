import sys
import tkinter.messagebox

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import loginpage_support
from instructions import data

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Login (root)
    loginpage_support.init(root, top)
    root.mainloop()

w = None
def create_Login(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Login (w)
    loginpage_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Login():
    global w
    w.destroy()
    w = None
    
def new():
    global newroot
    newroot=data(root)

class Login:
    def cancelLogin(self):
        msg=tkinter.messagebox.askyesno("Login Page","Are you sure you want to cancel Login?");
        if (msg):
            exit()
    def Login(self):
        user=self.userEntry.get()
        passw=self.passEntry.get()
        
        if user=="" or passw=="":
            tkinter.messagebox.showerror("Error", "Fill all fields")
        elif user=="user" and passw=="12345":
            tkinter.messagebox.showinfo("Login Page","You have successfully logged in");
            root.after(500,new)
            self.Frame1.destroy()
        else:
            tkinter.messagebox.showwarning("Login Page","The username or password you entered is incorrect");

            
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#ececec' # Closest X11 color: 'gray92' 
        font10 = "-family {Courier New} -size 13 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font11 = "-family {Times New Roman} -size 36 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        font12 = "-family {Segoe UI Emoji} -size 13 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI Emoji} -size 13 -weight bold -slant"  \
            " roman -underline 0 -overstrike 0"

        top.geometry("521x292+444+171")
        top.title("| Login")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#000000")
        top.configure(highlightcolor="#000000")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=-0.134, rely=-0.034, relheight=1.079
                , relwidth=1.353)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(background="#ffffff")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=705)

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.326, rely=0.095, height=61, width=180)
        self.Label1.configure(activebackground="#ffffff")
        self.Label1.configure(activeforeground="#ffffff")
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''SIGN IN''')

        self.userEntry = tk.Entry(self.Frame1)
        self.userEntry.place(relx=0.411, rely=0.349,height=30, relwidth=0.275)
        self.userEntry.configure(background="#fcf2ef")
        self.userEntry.configure(disabledforeground="#a3a3a3")
        self.userEntry.configure(font=font10)
        self.userEntry.configure(foreground="#000000")
        self.userEntry.configure(highlightbackground="#d9d9d9")
        self.userEntry.configure(highlightcolor="black")
        self.userEntry.configure(insertbackground="black")
        self.userEntry.configure(selectbackground="#c4c4c4")
        self.userEntry.configure(selectforeground="black")

        self.passEntry = tk.Entry(self.Frame1)
        self.passEntry.place(relx=0.411, rely=0.508,height=30, relwidth=0.275)
        self.passEntry.configure(background="#fcf2ef")
        self.passEntry.configure(disabledforeground="#a3a3a3")
        self.passEntry.configure(font=font10)
        self.passEntry.configure(foreground="#000000")
        self.passEntry.configure(highlightbackground="#d9d9d9")
        self.passEntry.configure(highlightcolor="black")
        self.passEntry.configure(insertbackground="black")
        self.passEntry.configure(selectbackground="#c4c4c4")
        self.passEntry.configure(selectforeground="black")
        self.passEntry.configure(show="*")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.227, rely=0.349, height=29, width=123)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font12)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''USERNAME     |''')

        self.Label2_2 = tk.Label(self.Frame1)
        self.Label2_2.place(relx=0.227, rely=0.508, height=29, width=124)
        self.Label2_2.configure(activebackground="#f9f9f9")
        self.Label2_2.configure(activeforeground="black")
        self.Label2_2.configure(background="#ffffff")
        self.Label2_2.configure(disabledforeground="#a3a3a3")
        self.Label2_2.configure(font=font12)
        self.Label2_2.configure(foreground="#000000")
        self.Label2_2.configure(highlightbackground="#d9d9d9")
        self.Label2_2.configure(highlightcolor="black")
        self.Label2_2.configure(text='''PASSWORD     |''')

        self.loginbttn = tk.Button(self.Frame1)
        self.loginbttn.place(relx=0.227, rely=0.698, height=38, width=116)
        self.loginbttn.configure(activebackground="#ececec")
        self.loginbttn.configure(activeforeground="#000000")
        self.loginbttn.configure(background="#ffffff")
        self.loginbttn.configure(disabledforeground="#a3a3a3")
        self.loginbttn.configure(font=font9)
        self.loginbttn.configure(foreground="#000000")
        self.loginbttn.configure(highlightbackground="#d9d9d9")
        self.loginbttn.configure(highlightcolor="black")
        self.loginbttn.configure(pady="0")
        self.loginbttn.configure(text='''LOGIN''')
        self.loginbttn.configure(command=self.Login)

        self.cancelbttn = tk.Button(self.Frame1)
        self.cancelbttn.place(relx=0.596, rely=0.698, height=38, width=86)
        self.cancelbttn.configure(activebackground="#ececec")
        self.cancelbttn.configure(activeforeground="#000000")
        self.cancelbttn.configure(background="#ffffff")
        self.cancelbttn.configure(disabledforeground="#a3a3a3")
        self.cancelbttn.configure(font=font9)
        self.cancelbttn.configure(foreground="#000000")
        self.cancelbttn.configure(highlightbackground="#d9d9d9")
        self.cancelbttn.configure(highlightcolor="black")
        self.cancelbttn.configure(pady="0")
        self.cancelbttn.configure(text='''CANCEL''')
        self.cancelbttn.configure(command=self.cancelLogin)

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

if __name__ == '__main__':
    vp_start_gui()





