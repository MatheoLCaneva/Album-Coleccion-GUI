#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.5
#  in conjunction with Tcl version 8.6
#    Sep 01, 2022 12:22:24 AM -03  platform: Windows NT

from enum import auto
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_script = sys.argv[0]
_location = os.path.dirname(_script)

import autosave_support
import menuAgregar

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40' # X11 color: #666666
_ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
_ana2color = 'beige' # X11 color: #f5f5dc
_tabfg1 = 'black' 
_tabfg2 = 'black' 
_tabbg1 = 'grey75' 
_tabbg2 = 'grey89' 
_bgmode = 'light' 

_style_code_ran = 0
def _style_code():
    global _style_code_ran
    if _style_code_ran:
       return
    style = ttk.Style()
    if sys.platform == "win32":
       style.theme_use('winnative')
    style.configure('.',background=_bgcolor)
    style.configure('.',foreground=_fgcolor)
    style.configure('.',font='TkDefaultFont')
    style.map('.',background =
       [('selected', _compcolor), ('active',_ana2color)])
    if _bgmode == 'dark':
       style.map('.',foreground =
         [('selected', 'white'), ('active','white')])
    else:
       style.map('.',foreground =
         [('selected', 'black'), ('active','black')])
    _style_code_ran = 1



class Main:
      def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        self.root = Tkinter.tk() 
        top.geometry("651x553+656+215")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Toplevel 0")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.0, rely=0.0, height=62, width=654)
        self.Label1.configure(activebackground="#59ef52")
        self.Label1.configure(background="#529cef")
        self.Label1.configure(compound='center')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 20")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(justify='right')
        self.Label1.configure(text='''Colección Qatar 2022''')

        _style_code()
        self.TFrame1 = ttk.Frame(self.top)
        self.TFrame1.place(relx=0.015, rely=0.127, relheight=0.859
                , relwidth=0.974)
        self.TFrame1.configure(relief='groove')
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief="groove")

        self.btnAgregar = ttk.Button(self.TFrame1)
        self.btnAgregar.place(relx=0.3, rely=0.126, height=65, width=226)
        self.btnAgregar.configure(takefocus="")
        self.btnAgregar.configure(text='''Agregar Figurita''')
        self.btnAgregar.configure(compound='left')
        self.btnAgregar.configure(command=self.openAdd)

        self.btnChequear = ttk.Button(self.TFrame1)
        self.btnChequear.place(relx=0.3, rely=0.4, height=65, width=226)
        self.btnChequear.configure(takefocus="")
        self.btnChequear.configure(text='''Comprobar Figurita''')
        self.btnChequear.configure(compound='left')

      def openAdd(self):
         menuAgregar.start_up()


def start_up():
   autosave_support.main()

if __name__ == '__main__':
   root = autosave_support.main()



