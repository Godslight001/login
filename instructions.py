
import sys

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

import instructions_support


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = data (root)
    instructions_support.init(root, top)
    root.mainloop()

w = None
def create_data(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = data (w)
    instructions_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_data():
    global w
    w.destroy()
    w = None

class data:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#ececec' # Closest X11 color: 'gray92' 
        font10 = "-family {Segoe UI} -size 16 -weight normal -slant "  \
            "roman -underline 1 -overstrike 0"
        font12 = "-family {Segoe UI} -size 24 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("600x450+367+127")
        top.title("WELCOME")
        top.configure(background="#d9d9d9")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=-0.033, rely=-0.089, relheight=1.202
                , relwidth=1.065)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(background="#ffffff")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=639)

        self.instructions = tk.Label(self.Frame1)
        instruct = open("instructions.txt","r",encoding="UTF8").read()
        self.instructions.place(relx=0.078, rely=0.259, height=111, width=544)
        self.instructions.configure(background="#ffffff")
        self.instructions.configure(disabledforeground="#a3a3a3")
        self.instructions.configure(foreground="#000000")
        self.instructions.configure(text=instruct)
        self.instructions.configure(width=544)

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.419, rely=0.166, height=36, width=114)
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font10)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''WELCOME''')

        self.startbttn = tk.Button(self.Frame1)
        self.startbttn.place(relx=0.344, rely=0.684, height=44, width=227)
        self.startbttn.configure(activebackground="#ececec")
        self.startbttn.configure(activeforeground="#000000")
        self.startbttn.configure(background="#ffffff")
        self.startbttn.configure(disabledforeground="#a3a3a3")
        self.startbttn.configure(font=font12)
        self.startbttn.configure(foreground="#000000")
        self.startbttn.configure(highlightbackground="#d9d9d9")
        self.startbttn.configure(highlightcolor="black")
        self.startbttn.configure(pady="0")
        self.startbttn.configure(text='''CONTINUE''')
        self.startbttn.configure(width=227)

if __name__ == '__main__':
    vp_start_gui()





