from tkinter import *
import tkinter as tk


import filemove
import Movefilesmain

def load_gui(self):

    self.sourcestr= StringVar()
    self.deststr=StringVar()

    self.lbl_sourcefolder = tk.Label(self.master, text="Choose Source Folder:")
    self.lbl_sourcefolder.grid(row=0, column=0, padx=(27,0), pady=(10,0))
    self.lbl_destfolder=tk.Label(self.master, text="Choose Destination Folder:")
    self.lbl_destfolder.grid(row=2, column=0, padx=(27,0), pady=(10,0))

    self.txt_sourcefolder= tk.Entry(self.master, textvariable=self.sourcestr)
    self.txt_sourcefolder.grid(row=1, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0))
    self.txt_destfolder= tk.Entry(self.master, textvariable=self.deststr)
    self.txt_destfolder.grid(row=3, column=0, rowspan=1,  columnspan=2, padx=(30,40), pady=(0,0))

    self.btn_move=tk.Button(self.master, width=12, height=2, text='Move', command=lambda:filemove.move_Files(self))
    self.btn_move.grid(row=8, column=1, padx=(25,0), pady=(45,10))
    self.btn_source=tk.Button(self.master, width=12, height=2, text='Source', command=lambda:filemove.source_ask_directory(self))
    self.btn_source.grid(row=1, column=3, padx=(25,0), pady=(45,10))
    self.btn_dest=tk.Button(self.master, width=12, height=2, text='Destination', command=lambda:filemove.dest_ask_directory(self))
    self.btn_dest.grid(row=3, column=3, padx=(25,0), pady=(45,10))


if __name__ == "__main__":
    pass
