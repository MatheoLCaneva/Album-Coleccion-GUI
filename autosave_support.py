#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7.5
#  in conjunction with Tcl version 8.6
#    Aug 31, 2022 11:56:07 PM -03  platform: Windows NT
#    Sep 01, 2022 12:14:26 AM -03  platform: Windows NT
#    Sep 01, 2022 12:23:04 AM -03  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import autosave

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = autosave.Main(_top1)
    root.mainloop()

def cerrar(): 
    root.destroy()

def print(*args):
    print('autosave_support.print')
    for arg in args:
        print ('    another arg:', arg)
    sys.stdout.flush()

if __name__ == '__main__':
    autosave.start_up()





